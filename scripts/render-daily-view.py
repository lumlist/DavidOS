#!/usr/bin/env python3
"""Daily Operating View v0 — DavidOS / iZZi AI Systems.

Renders a single static HTML page (and a markdown mirror) summarizing the
state of David's day, assembled from the local Paperclip API and the repo
file system. No external services. No persistent state. No caching.
Stdlib-only.

Outputs:
  docs/daily/today.html
  docs/daily/today.md

Constraints honored (per DAV-17 [APPROVAL: code-change] at 2026-05-10T05:31):
  - Only the three files above are written by this script.
  - Stdlib only.
  - No scheduling, no Langfuse, no Obsidian-MCP, no caching, no persistent state.
  - On API schema/network failure, repo-derived sections still render and a
    warning banner is shown at the top.

Designed per docs/atlas/davidos-operating-ui-v1-plan-revised.md §"Stage 2".
"""

from __future__ import annotations

import datetime as dt
import glob
import html
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Configuration (parameterized later when iZZi customer mode arrives)
# ---------------------------------------------------------------------------

PAPERCLIP_BASE = os.environ.get("PAPERCLIP_BASE", "http://127.0.0.1:3100/api")
COMPANY_ID = os.environ.get(
    "PAPERCLIP_COMPANY_ID",
    "d7e560c2-b978-4959-87e2-47e02c31d9d8",
)
ATLAS_AGENT_ID = os.environ.get(
    "PAPERCLIP_ATLAS_AGENT_ID",
    "dbf81a0c-9996-4834-849e-c24b7343c4e7",
)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
DAILY_DIR = DOCS_DIR / "daily"
WIKI_DIR = DOCS_DIR / "wiki"
RAW_DIR = DOCS_DIR / "raw"
ATLAS_RECS = DOCS_DIR / "atlas" / "recommendations-today.md"

OUT_HTML = DAILY_DIR / "today.html"
OUT_MD = DAILY_DIR / "today.md"

API_TIMEOUT = 5.0  # seconds per request
NOW = dt.datetime.now(dt.timezone.utc)


# ---------------------------------------------------------------------------
# Tag detection (per docs/atlas/comment-conventions-v0.md)
# ---------------------------------------------------------------------------

TAG_REQUEST = re.compile(r"^\s*\\?\[APPROVAL-REQUEST\]", re.IGNORECASE)
TAG_APPROVAL = re.compile(r"^\s*\\?\[APPROVAL:\s*([a-z0-9_-]+)\s*\]", re.IGNORECASE)
TAG_REJECT = re.compile(r"^\s*\\?\[REJECT\]", re.IGNORECASE)
TAG_BLOCKER = re.compile(r"^\s*\\?\[BLOCKER\]", re.IGNORECASE)
TAG_STATUS = re.compile(r"^\s*\\?\[STATUS\]", re.IGNORECASE)
TAG_DELIVERABLE = re.compile(r"^\s*\\?\[DELIVERABLE\]", re.IGNORECASE)
KIND_LINE = re.compile(r"^\s*kind:\s*([a-z0-9_-]+)", re.IGNORECASE | re.MULTILINE)


# ---------------------------------------------------------------------------
# API access (graceful degradation)
# ---------------------------------------------------------------------------


class ApiUnavailable(RuntimeError):
    """Raised when a Paperclip API call cannot be served. Caller decides
    whether to render the section as empty + add a banner."""


def _api_get(path: str) -> Any:
    url = PAPERCLIP_BASE.rstrip("/") + path
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        raise ApiUnavailable(f"GET {url}: {exc}") from exc


# ---------------------------------------------------------------------------
# Data fetchers
# ---------------------------------------------------------------------------


def fetch_issues() -> Tuple[List[Dict[str, Any]], Optional[str]]:
    try:
        items = _api_get(f"/companies/{COMPANY_ID}/issues")
        if not isinstance(items, list):
            raise ApiUnavailable(f"unexpected issues payload: {type(items).__name__}")
        return items, None
    except ApiUnavailable as exc:
        return [], str(exc)


def fetch_projects() -> Tuple[Dict[str, str], Optional[str]]:
    try:
        items = _api_get(f"/companies/{COMPANY_ID}/projects")
        if not isinstance(items, list):
            return {}, f"unexpected projects payload: {type(items).__name__}"
        return {p["id"]: p.get("name", p["id"]) for p in items if isinstance(p, dict) and "id" in p}, None
    except ApiUnavailable as exc:
        return {}, str(exc)


def fetch_comments(issue_id: str) -> List[Dict[str, Any]]:
    try:
        cs = _api_get(f"/issues/{issue_id}/comments")
        if isinstance(cs, list):
            return sorted(cs, key=lambda c: c.get("createdAt", ""))
    except ApiUnavailable:
        pass
    return []


def fetch_documents(issue_id: str) -> List[Dict[str, Any]]:
    try:
        ds = _api_get(f"/issues/{issue_id}/documents")
        if isinstance(ds, list):
            return ds
    except ApiUnavailable:
        pass
    return []


# ---------------------------------------------------------------------------
# Section computations
# ---------------------------------------------------------------------------


def _split_daily_note(path: pathlib.Path) -> Dict[str, List[str]]:
    """Parse a daily note. Returns {section_title: [bullet_lines]}."""
    if not path.exists():
        return {}
    sections: Dict[str, List[str]] = {}
    current: Optional[str] = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^##\s+(.*?)\s*$", line)
        if m:
            current = m.group(1).strip()
            sections.setdefault(current, [])
            continue
        if current is None:
            continue
        stripped = line.strip()
        if stripped.startswith("- ") and len(stripped) > 2:
            sections[current].append(stripped[2:].strip())
        elif stripped.startswith("-") and len(stripped) == 1:
            # empty bullet from template — skip
            continue
    return sections


def section_top_of_mind(today_note: pathlib.Path) -> Tuple[List[str], List[str]]:
    secs = _split_daily_note(today_note)
    return secs.get("Top of mind", []), secs.get("Decisions I want made today", [])


def _is_open(issue: Dict[str, Any]) -> bool:
    return issue.get("status") in ("todo", "in_progress", "backlog", "blocked")


def _last_activity(issue: Dict[str, Any]) -> str:
    return issue.get("lastActivityAt") or issue.get("updatedAt") or issue.get("createdAt") or ""


def _label_names(issue: Dict[str, Any]) -> List[str]:
    labels = issue.get("labels") or []
    out: List[str] = []
    for lab in labels:
        if isinstance(lab, dict):
            name = lab.get("name") or lab.get("slug") or lab.get("id")
            if name:
                out.append(str(name))
        elif isinstance(lab, str):
            out.append(lab)
    return out


def section_pending_approvals(
    issues: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """For each open issue, scan comments and find unmatched [APPROVAL-REQUEST]s."""
    pending: List[Dict[str, Any]] = []
    for issue in issues:
        if not _is_open(issue):
            continue
        comments = fetch_comments(issue["id"])
        # Walk forward; track open requests by kind. Pair on first matching approval/reject.
        open_by_kind: Dict[str, List[Dict[str, Any]]] = {}
        for c in comments:
            body = c.get("body") or ""
            first_line = body.lstrip().splitlines()[0] if body.strip() else ""
            if TAG_REQUEST.match(first_line):
                kind_m = KIND_LINE.search(body)
                kind = kind_m.group(1).lower() if kind_m else "unknown"
                open_by_kind.setdefault(kind, []).append(
                    {
                        "issue": issue,
                        "comment": c,
                        "kind": kind,
                    }
                )
                continue
            m_appr = TAG_APPROVAL.match(first_line)
            if m_appr:
                kind = m_appr.group(1).lower()
                # match most recent open of same kind, OR the first open if no match
                queue = open_by_kind.get(kind)
                if queue:
                    queue.pop(0)
                else:
                    # An [APPROVAL: bundle] satisfies all currently-open requests
                    # in the bundle's bundle_kinds set. Heuristic v0: if kind ==
                    # 'bundle' clear the closest pending request regardless.
                    if kind == "bundle":
                        for k_list in open_by_kind.values():
                            if k_list:
                                k_list.pop(0)
                                break
                continue
            if TAG_REJECT.match(first_line):
                # close the most recently opened request, regardless of kind
                for k_list in open_by_kind.values():
                    if k_list:
                        k_list.pop(0)
                        break
        for k_list in open_by_kind.values():
            pending.extend(k_list)
    pending.sort(key=lambda p: p["comment"].get("createdAt", ""))
    return pending


def section_open_decisions(issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [i for i in issues if _is_open(i) and "decision-needed" in _label_names(i)]


def _next_action(issue: Dict[str, Any], comments: List[Dict[str, Any]]) -> str:
    if not comments:
        if issue.get("description"):
            return "fresh issue — read description"
        return "no activity yet"
    last = comments[-1]
    body = last.get("body") or ""
    first_line = body.lstrip().splitlines()[0] if body.strip() else ""
    if TAG_REQUEST.match(first_line):
        return "needs David approval"
    if TAG_BLOCKER.match(first_line):
        snippet = body.replace("\n", " ")[:80]
        return f"blocked: {snippet}"
    if TAG_STATUS.match(first_line):
        snippet = body.replace("\n", " ")[8:88]
        return f"last status: {snippet.strip()}"
    if TAG_DELIVERABLE.match(first_line):
        return "deliverable shipped — awaiting closure"
    return body.replace("\n", " ")[:80]


def section_active_issues(
    issues: List[Dict[str, Any]],
    projects: Dict[str, str],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for issue in issues:
        if not _is_open(issue):
            continue
        comments = fetch_comments(issue["id"])
        rows.append(
            {
                "identifier": issue.get("identifier", ""),
                "title": issue.get("title", ""),
                "project": projects.get(issue.get("projectId") or "", "(none)"),
                "status": issue.get("status", ""),
                "priority": issue.get("priority", ""),
                "assignee": "Atlas" if issue.get("assigneeAgentId") == ATLAS_AGENT_ID else (issue.get("assigneeUserId") or issue.get("assigneeAgentId") or "(unassigned)"),
                "last_activity": _last_activity(issue),
                "next_action": _next_action(issue, comments),
                "id": issue.get("id"),
            }
        )
    # sort: blocked first, then in_progress, then todo; within each by priority then last_activity desc
    status_order = {"blocked": 0, "in_progress": 1, "todo": 2, "backlog": 3}
    priority_order = {"urgent": 0, "high": 1, "medium": 2, "low": 3}
    rows.sort(
        key=lambda r: (
            status_order.get(r["status"], 99),
            priority_order.get(r["priority"], 99),
            -_iso_seconds(r["last_activity"]),
        )
    )
    return rows


def _iso_seconds(iso: str) -> int:
    if not iso:
        return 0
    try:
        return int(dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())
    except ValueError:
        return 0


def section_recent_deliverables(
    issues: List[Dict[str, Any]],
    limit: int = 10,
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for issue in issues:
        for d in fetch_documents(issue["id"]):
            rows.append(
                {
                    "issue_identifier": issue.get("identifier", ""),
                    "issue_id": issue.get("id"),
                    "key": d.get("key", ""),
                    "title": d.get("title", ""),
                    "createdAt": d.get("createdAt", ""),
                    "size": len(d.get("body") or ""),
                }
            )
    rows.sort(key=lambda r: r["createdAt"], reverse=True)
    return rows[:limit]


def section_system_health(issues: List[Dict[str, Any]]) -> Dict[str, Any]:
    cutoff_24h = NOW - dt.timedelta(hours=24)
    runs_24h = 0
    loop_detected = False
    for issue in issues:
        comments = fetch_comments(issue["id"])
        for c in comments:
            try:
                ts = dt.datetime.fromisoformat((c.get("createdAt") or "").replace("Z", "+00:00"))
            except ValueError:
                continue
            if ts >= cutoff_24h:
                # Heartbeat session resume comments are a proxy for runs
                if "↻ Resumed session" in (c.get("body") or "") or TAG_STATUS.match((c.get("body") or "").lstrip().splitlines()[0] if c.get("body") else ""):
                    runs_24h += 1
        # Loop detection v0: if the issue has been completed/cancelled and is now reopened, flag.
        # Without a full revisions API we approximate: if the issue is open AND has any [DELIVERABLE] tag in past comments AND was updated within the last hour after a deliverable, flag.
        had_deliverable = any(TAG_DELIVERABLE.match((c.get("body") or "").lstrip().splitlines()[0]) for c in comments if c.get("body"))
        if had_deliverable and _is_open(issue):
            # Cheap heuristic only — flag if the issue had a deliverable AND remains open with comments arriving after it
            try:
                first_deliverable_idx = next(
                    i for i, c in enumerate(comments)
                    if TAG_DELIVERABLE.match(((c.get("body") or "").lstrip().splitlines() or [""])[0])
                )
                tail = comments[first_deliverable_idx + 1 :]
                # Loop is suspected if there's been an auto "↻ Resumed session" after the deliverable
                if any("↻ Resumed session" in (c.get("body") or "") for c in tail):
                    loop_detected = True
            except StopIteration:
                pass
    return {
        "runs_24h": runs_24h,
        "cost_24h_usd": None,  # Langfuse placeholder
        "heartbeat_loop": loop_detected,
    }


def section_memory_freshness() -> Dict[str, List[Tuple[str, int]]]:
    out: Dict[str, List[Tuple[str, int]]] = {
        "stale_wiki": [],
        "raw_curation_debt": [],
        "wiki_hubs": [],
    }
    if WIKI_DIR.exists():
        for p in sorted(WIKI_DIR.rglob("*.md")):
            if p.name == "README.md":
                continue
            mtime = dt.datetime.fromtimestamp(p.stat().st_mtime, tz=dt.timezone.utc)
            age_days = (NOW - mtime).days
            if age_days >= 60:
                out["stale_wiki"].append((str(p.relative_to(REPO_ROOT)), age_days))
    if RAW_DIR.exists():
        for p in sorted(RAW_DIR.rglob("*.md")):
            if p.name == "README.md":
                continue
            mtime = dt.datetime.fromtimestamp(p.stat().st_mtime, tz=dt.timezone.utc)
            age_days = (NOW - mtime).days
            if age_days >= 14:
                out["raw_curation_debt"].append((str(p.relative_to(REPO_ROOT)), age_days))
    # wiki hubs: count inbound links across docs/{wiki,output}
    if WIKI_DIR.exists():
        link_counts: Dict[str, int] = {}
        link_pat = re.compile(r"\[\[([^\]]+?)\]\]|\]\(([^)]+\.md)\)")
        scan_dirs = [WIKI_DIR, DOCS_DIR / "output"]
        wiki_basenames = {p.stem for p in WIKI_DIR.rglob("*.md") if p.name != "README.md"}
        for d in scan_dirs:
            if not d.exists():
                continue
            for p in d.rglob("*.md"):
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                for m in link_pat.finditer(text):
                    target = (m.group(1) or m.group(2) or "").strip()
                    if not target:
                        continue
                    base = pathlib.Path(target).stem
                    if base in wiki_basenames:
                        link_counts[base] = link_counts.get(base, 0) + 1
        out["wiki_hubs"] = sorted(link_counts.items(), key=lambda kv: -kv[1])[:10]
    return out


def section_recommendations() -> str:
    if ATLAS_RECS.exists():
        return ATLAS_RECS.read_text(encoding="utf-8", errors="replace").strip()
    return ""


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def _h(s: Any) -> str:
    return html.escape(str(s) if s is not None else "")


def _issue_url(issue_id: str) -> str:
    return f"http://127.0.0.1:3100/issues/{issue_id}"


def _fmt_iso(iso: str) -> str:
    if not iso:
        return ""
    try:
        d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return iso
    delta = NOW - d
    secs = int(delta.total_seconds())
    if secs < 0:
        return iso
    if secs < 60:
        return f"{secs}s ago"
    if secs < 3600:
        return f"{secs // 60}m ago"
    if secs < 86400:
        return f"{secs // 3600}h ago"
    return f"{secs // 86400}d ago"


def render_html(ctx: Dict[str, Any]) -> str:
    css = """
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
           max-width: 1100px; margin: 2rem auto; padding: 0 1.5rem; color: #1d1d1f; line-height: 1.45; }
    h1 { font-size: 1.6rem; margin: 0 0 0.25rem; }
    h2 { font-size: 1.15rem; border-bottom: 1px solid #e5e5e7; padding-bottom: 0.25rem; margin-top: 2rem; }
    .meta { color: #6e6e73; font-size: 0.85rem; margin-bottom: 1.5rem; }
    .banner { background: #fff7e6; border-left: 4px solid #f5a623; padding: 0.75rem 1rem; margin: 1rem 0; }
    .banner.error { background: #ffeaea; border-left-color: #d0021b; }
    table { border-collapse: collapse; width: 100%; font-size: 0.9rem; }
    th, td { text-align: left; padding: 0.4rem 0.5rem; border-bottom: 1px solid #f0f0f2; vertical-align: top; }
    th { color: #6e6e73; font-weight: 500; }
    .pri-high, .pri-urgent { color: #d0021b; font-weight: 600; }
    .pri-medium { color: #b97400; }
    .pri-low { color: #6e6e73; }
    .status-blocked { color: #d0021b; }
    .status-in_progress { color: #0070c0; }
    .status-todo { color: #6e6e73; }
    .placeholder { color: #b0b0b5; font-style: italic; }
    ul { padding-left: 1.25rem; }
    li { margin: 0.15rem 0; }
    code { background: #f5f5f7; padding: 0 0.25rem; border-radius: 3px; font-size: 0.85rem; }
    a { color: #0070c0; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .num { font-size: 1.6rem; font-weight: 600; }
    .num-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
    .num-cell { padding: 0.75rem 1rem; background: #f7f7fa; border-radius: 6px; }
    .num-label { color: #6e6e73; font-size: 0.8rem; }
    .ok { color: #2e7d32; }
    .warn { color: #d0021b; font-weight: 600; }
    """

    parts: List[str] = []
    parts.append("<!doctype html>")
    parts.append('<html lang="en"><head><meta charset="utf-8"><title>Daily Operating View — DavidOS</title>')
    parts.append(f"<style>{css}</style></head><body>")
    parts.append(f"<h1>Daily Operating View — DavidOS / iZZi AI Systems</h1>")
    parts.append(
        f'<div class="meta">Generated {_h(NOW.strftime("%Y-%m-%d %H:%M UTC"))} · '
        f'commit {_h(ctx.get("git_sha", "?")[:8])} · '
        f'<code>scripts/render-daily-view.py</code></div>'
    )

    # Banners
    if ctx.get("api_warning"):
        parts.append(
            f'<div class="banner error">Paperclip API issue: {_h(ctx["api_warning"])}. '
            "Repo-derived sections render normally; Paperclip-derived sections may be empty.</div>"
        )

    # 1. Top of mind
    parts.append("<h2>1. Top of mind</h2>")
    if ctx["top_of_mind"]:
        parts.append("<ul>")
        for item in ctx["top_of_mind"]:
            parts.append(f"<li>{_h(item)}</li>")
        parts.append("</ul>")
    else:
        parts.append(
            f'<div class="placeholder">No daily note for today. '
            f"Create <code>docs/daily/{NOW.strftime('%Y-%m-%d')}.md</code> from "
            "<code>docs/atlas/templates/daily-note.md</code>.</div>"
        )

    # 2. Decisions I want made today
    parts.append("<h2>2. Decisions I want made today</h2>")
    if ctx["decisions_today"]:
        parts.append("<ul>")
        for item in ctx["decisions_today"]:
            parts.append(f"<li>{_h(item)}</li>")
        parts.append("</ul>")
    else:
        parts.append('<div class="placeholder">(none)</div>')

    # 3. Pending approvals
    parts.append("<h2>3. Pending approvals</h2>")
    if ctx["pending_approvals"]:
        parts.append('<table><tr><th>Issue</th><th>Kind</th><th>Asked</th><th>What</th></tr>')
        for p in ctx["pending_approvals"]:
            issue = p["issue"]
            comment = p["comment"]
            body = comment.get("body") or ""
            what_m = re.search(r"^\s*what:\s*(.+?)\s*$", body, re.MULTILINE | re.IGNORECASE)
            what = what_m.group(1).strip() if what_m else body.replace("\n", " ")[:120]
            parts.append(
                f"<tr>"
                f'<td><a href="{_h(_issue_url(issue["id"]))}">{_h(issue.get("identifier",""))}</a></td>'
                f"<td><code>{_h(p['kind'])}</code></td>"
                f"<td>{_h(_fmt_iso(comment.get('createdAt','')))}</td>"
                f"<td>{_h(what[:140])}</td>"
                f"</tr>"
            )
        parts.append("</table>")
    else:
        parts.append('<div class="placeholder">(none — David is up to date on approvals)</div>')

    # 4. Open decisions
    parts.append("<h2>4. Open decisions</h2>")
    if ctx["open_decisions"]:
        parts.append('<table><tr><th>Issue</th><th>Status</th><th>Last activity</th><th>Title</th></tr>')
        for issue in ctx["open_decisions"]:
            parts.append(
                f"<tr>"
                f'<td><a href="{_h(_issue_url(issue["id"]))}">{_h(issue.get("identifier",""))}</a></td>'
                f'<td class="status-{_h(issue.get("status",""))}">{_h(issue.get("status",""))}</td>'
                f"<td>{_h(_fmt_iso(_last_activity(issue)))}</td>"
                f"<td>{_h(issue.get('title',''))}</td>"
                f"</tr>"
            )
        parts.append("</table>")
    else:
        parts.append('<div class="placeholder">(none labeled <code>decision-needed</code>)</div>')

    # 5. Active issues
    parts.append("<h2>5. Active issues</h2>")
    if ctx["active_issues"]:
        parts.append(
            '<table><tr><th>Issue</th><th>Project</th><th>Assignee</th><th>Status</th>'
            '<th>Pri</th><th>Last activity</th><th>Next action</th></tr>'
        )
        for r in ctx["active_issues"]:
            parts.append(
                f"<tr>"
                f'<td><a href="{_h(_issue_url(r["id"]))}">{_h(r["identifier"])}</a> '
                f'<span title="{_h(r["title"])}">{_h(r["title"][:40])}</span></td>'
                f"<td>{_h(r['project'])}</td>"
                f"<td>{_h(r['assignee'])}</td>"
                f'<td class="status-{_h(r["status"])}">{_h(r["status"])}</td>'
                f'<td class="pri-{_h(r["priority"])}">{_h(r["priority"])}</td>'
                f"<td>{_h(_fmt_iso(r['last_activity']))}</td>"
                f"<td>{_h(r['next_action'])}</td>"
                f"</tr>"
            )
        parts.append("</table>")
    else:
        parts.append('<div class="placeholder">(no open issues — all clear)</div>')

    # 6. Recent deliverables
    parts.append("<h2>6. Recent deliverables</h2>")
    if ctx["recent_deliverables"]:
        parts.append('<table><tr><th>When</th><th>Issue</th><th>Doc key</th><th>Title</th><th>Size</th></tr>')
        for d in ctx["recent_deliverables"]:
            parts.append(
                f"<tr>"
                f"<td>{_h(_fmt_iso(d['createdAt']))}</td>"
                f'<td><a href="{_h(_issue_url(d["issue_id"]))}">{_h(d["issue_identifier"])}</a></td>'
                f"<td><code>{_h(d['key'])}</code></td>"
                f"<td>{_h(d['title'])}</td>"
                f"<td>{d['size']:,} chars</td>"
                f"</tr>"
            )
        parts.append("</table>")
    else:
        parts.append('<div class="placeholder">(none)</div>')

    # 7. System health
    parts.append("<h2>7. System health</h2>")
    sh = ctx["system_health"]
    cost_text = "<span class='placeholder'>placeholder — Langfuse not yet installed (DAV-17 Stage 4)</span>"
    loop_text = (
        '<span class="warn">⚠ heartbeat-loop suspected</span>'
        if sh.get("heartbeat_loop")
        else '<span class="ok">✓ no loop detected</span>'
    )
    parts.append(
        '<div class="num-grid">'
        f'<div class="num-cell"><div class="num">{sh["runs_24h"]}</div>'
        '<div class="num-label">agent runs / status posts in last 24h</div></div>'
        f'<div class="num-cell"><div class="num">—</div>'
        f'<div class="num-label">total cost / 24h<br>{cost_text}</div></div>'
        f'<div class="num-cell"><div class="num">{loop_text}</div>'
        '<div class="num-label">heartbeat-loop indicator</div></div>'
        '</div>'
    )

    # 8. Memory freshness
    parts.append("<h2>8. Memory freshness</h2>")
    mf = ctx["memory_freshness"]
    if mf["stale_wiki"]:
        parts.append("<p><strong>Stale wiki/ (60+ days unedited):</strong></p><ul>")
        for path, age in mf["stale_wiki"][:20]:
            parts.append(f"<li><code>{_h(path)}</code> — {age}d old</li>")
        parts.append("</ul>")
    else:
        parts.append('<p><strong>Stale wiki/:</strong> <span class="placeholder">none</span></p>')
    if mf["raw_curation_debt"]:
        parts.append("<p><strong>Curation debt — raw/ files unpromoted 14+ days:</strong></p><ul>")
        for path, age in mf["raw_curation_debt"][:20]:
            parts.append(f"<li><code>{_h(path)}</code> — {age}d old</li>")
        parts.append("</ul>")
    else:
        parts.append('<p><strong>Curation debt:</strong> <span class="placeholder">none</span></p>')
    if mf["wiki_hubs"]:
        parts.append("<p><strong>Top wiki/ hubs by inbound link count:</strong></p><ul>")
        for name, n in mf["wiki_hubs"]:
            parts.append(f"<li><code>{_h(name)}</code> — {n} inbound links</li>")
        parts.append("</ul>")
    else:
        parts.append('<p><strong>Wiki hubs:</strong> <span class="placeholder">no wiki/ content yet</span></p>')

    # 9. Atlas recommendations
    parts.append("<h2>9. Atlas recommendations</h2>")
    if ctx["recommendations"]:
        # Render as <pre> for v0 — not parsing markdown in stdlib
        parts.append(f"<pre>{_h(ctx['recommendations'])}</pre>")
    else:
        parts.append(
            f'<div class="placeholder">(none — Atlas writes to <code>docs/atlas/recommendations-today.md</code>'
            ' when surfacing non-urgent suggestions)</div>'
        )

    parts.append("</body></html>")
    return "\n".join(parts)


def render_md(ctx: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append(f"# Daily Operating View — DavidOS / iZZi AI Systems")
    lines.append("")
    lines.append(
        f"Generated {NOW.strftime('%Y-%m-%d %H:%M UTC')} · commit "
        f"`{ctx.get('git_sha','?')[:8]}` · `scripts/render-daily-view.py`"
    )
    lines.append("")
    if ctx.get("api_warning"):
        lines.append(f"> ⚠ Paperclip API issue: {ctx['api_warning']}. Repo-derived sections render normally; Paperclip-derived sections may be empty.")
        lines.append("")

    def hdr(n: int, title: str) -> None:
        lines.append("")
        lines.append(f"## {n}. {title}")
        lines.append("")

    hdr(1, "Top of mind")
    if ctx["top_of_mind"]:
        for item in ctx["top_of_mind"]:
            lines.append(f"- {item}")
    else:
        lines.append(f"_No daily note for today. Create `docs/daily/{NOW.strftime('%Y-%m-%d')}.md` from `docs/atlas/templates/daily-note.md`._")

    hdr(2, "Decisions I want made today")
    if ctx["decisions_today"]:
        for item in ctx["decisions_today"]:
            lines.append(f"- {item}")
    else:
        lines.append("_(none)_")

    hdr(3, "Pending approvals")
    if ctx["pending_approvals"]:
        lines.append("| Issue | Kind | Asked | What |")
        lines.append("|---|---|---|---|")
        for p in ctx["pending_approvals"]:
            issue = p["issue"]
            comment = p["comment"]
            body = comment.get("body") or ""
            what_m = re.search(r"^\s*what:\s*(.+?)\s*$", body, re.MULTILINE | re.IGNORECASE)
            what = what_m.group(1).strip() if what_m else body.replace("\n", " ")[:120]
            ident = issue.get("identifier", "")
            lines.append(
                f"| [{ident}]({_issue_url(issue['id'])}) | `{p['kind']}` | "
                f"{_fmt_iso(comment.get('createdAt',''))} | {what[:140].replace('|','\\|')} |"
            )
    else:
        lines.append("_(none — David is up to date on approvals)_")

    hdr(4, "Open decisions")
    if ctx["open_decisions"]:
        lines.append("| Issue | Status | Last activity | Title |")
        lines.append("|---|---|---|---|")
        for issue in ctx["open_decisions"]:
            lines.append(
                f"| [{issue.get('identifier','')}]({_issue_url(issue['id'])}) | "
                f"{issue.get('status','')} | {_fmt_iso(_last_activity(issue))} | "
                f"{issue.get('title','').replace('|','\\|')} |"
            )
    else:
        lines.append("_(none labeled `decision-needed`)_")

    hdr(5, "Active issues")
    if ctx["active_issues"]:
        lines.append("| Issue | Project | Assignee | Status | Pri | Last act | Next action |")
        lines.append("|---|---|---|---|---|---|---|")
        for r in ctx["active_issues"]:
            lines.append(
                f"| [{r['identifier']}]({_issue_url(r['id'])}) | {r['project']} | "
                f"{r['assignee']} | {r['status']} | {r['priority']} | "
                f"{_fmt_iso(r['last_activity'])} | {r['next_action'][:80].replace('|','\\|')} |"
            )
    else:
        lines.append("_(no open issues — all clear)_")

    hdr(6, "Recent deliverables")
    if ctx["recent_deliverables"]:
        lines.append("| When | Issue | Doc | Title | Size |")
        lines.append("|---|---|---|---|---|")
        for d in ctx["recent_deliverables"]:
            lines.append(
                f"| {_fmt_iso(d['createdAt'])} | "
                f"[{d['issue_identifier']}]({_issue_url(d['issue_id'])}) | "
                f"`{d['key']}` | {d['title'].replace('|','\\|')} | {d['size']:,} chars |"
            )
    else:
        lines.append("_(none)_")

    hdr(7, "System health")
    sh = ctx["system_health"]
    lines.append(f"- agent runs / status posts in last 24h: **{sh['runs_24h']}**")
    lines.append(f"- total cost / 24h: _placeholder — Langfuse not yet installed (DAV-17 Stage 4)_")
    lines.append(f"- heartbeat-loop indicator: {'⚠ **suspected**' if sh.get('heartbeat_loop') else '✓ no loop detected'}")

    hdr(8, "Memory freshness")
    mf = ctx["memory_freshness"]
    lines.append("**Stale wiki/ (60+ days unedited):**")
    if mf["stale_wiki"]:
        for path, age in mf["stale_wiki"][:20]:
            lines.append(f"- `{path}` — {age}d old")
    else:
        lines.append("- _none_")
    lines.append("")
    lines.append("**Curation debt — raw/ files unpromoted 14+ days:**")
    if mf["raw_curation_debt"]:
        for path, age in mf["raw_curation_debt"][:20]:
            lines.append(f"- `{path}` — {age}d old")
    else:
        lines.append("- _none_")
    lines.append("")
    lines.append("**Top wiki/ hubs by inbound link count:**")
    if mf["wiki_hubs"]:
        for name, n in mf["wiki_hubs"]:
            lines.append(f"- `{name}` — {n} inbound links")
    else:
        lines.append("- _no wiki/ content yet_")

    hdr(9, "Atlas recommendations")
    if ctx["recommendations"]:
        lines.append(ctx["recommendations"])
    else:
        lines.append("_(none — Atlas writes to `docs/atlas/recommendations-today.md` when surfacing non-urgent suggestions)_")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def _git_sha() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=2,
        )
        return out.stdout.strip() if out.returncode == 0 else "?"
    except Exception:
        return "?"


def main() -> int:
    DAILY_DIR.mkdir(parents=True, exist_ok=True)

    issues, api_warning = fetch_issues()
    projects, proj_warning = fetch_projects()
    if proj_warning and not api_warning:
        api_warning = proj_warning

    today_note = DAILY_DIR / f"{NOW.strftime('%Y-%m-%d')}.md"
    top_of_mind, decisions_today = section_top_of_mind(today_note)

    pending = section_pending_approvals(issues) if issues else []
    open_decisions = section_open_decisions(issues) if issues else []
    active = section_active_issues(issues, projects) if issues else []
    recent = section_recent_deliverables(issues) if issues else []
    sh = section_system_health(issues) if issues else {"runs_24h": 0, "cost_24h_usd": None, "heartbeat_loop": False}
    mf = section_memory_freshness()
    recs = section_recommendations()

    ctx = {
        "api_warning": api_warning,
        "git_sha": _git_sha(),
        "top_of_mind": top_of_mind,
        "decisions_today": decisions_today,
        "pending_approvals": pending,
        "open_decisions": open_decisions,
        "active_issues": active,
        "recent_deliverables": recent,
        "system_health": sh,
        "memory_freshness": mf,
        "recommendations": recs,
    }

    OUT_HTML.write_text(render_html(ctx), encoding="utf-8")
    OUT_MD.write_text(render_md(ctx), encoding="utf-8")

    summary = {
        "wrote_html": str(OUT_HTML.relative_to(REPO_ROOT)),
        "wrote_md": str(OUT_MD.relative_to(REPO_ROOT)),
        "api_warning": api_warning,
        "counts": {
            "active_issues": len(active),
            "pending_approvals": len(pending),
            "open_decisions": len(open_decisions),
            "recent_deliverables": len(recent),
            "stale_wiki": len(mf["stale_wiki"]),
            "raw_curation_debt": len(mf["raw_curation_debt"]),
            "wiki_hubs": len(mf["wiki_hubs"]),
            "top_of_mind_items": len(top_of_mind),
            "decisions_today_items": len(decisions_today),
            "runs_24h": sh["runs_24h"],
            "heartbeat_loop": sh["heartbeat_loop"],
        },
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
