#!/usr/bin/env python3
"""
scripts/session.py — DavidOS Session Workflow CLI

Subcommands:
  start   Copy session-start-draft to submitted/, post [SESSION START] on tracker issue,
          reset draft to blank template.
  end     Copy session-end-draft to submitted/, post [SESSION END] on tracker issue,
          reset draft to blank template.
  status  Print current session state (is a session active? last start/end timestamps).

Usage:
  python scripts/session.py start
  python scripts/session.py end
  python scripts/session.py status

Configuration:
  Reads scripts/session-config.json for Paperclip API details and tracker issue ID.
  Repo root is inferred from the script's own location (one level up from scripts/).

Design constraints (Stage 2.6):
  - Standard library only (no third-party dependencies).
  - No localhost server, no hosted UI, no scheduling, no new agents.
  - Does NOT update the Daily Operating View renderer (Stage 2.7 gate).
  - Does NOT run smoke tests automatically — David runs the first test.

Source: DAV-17 Stage 2.6 [APPROVAL: code-change] at 2026-05-10T23:33:12Z.
Spec:   docs/atlas/davidos-session-workflow-v0.md
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_PATH = SCRIPT_DIR / "session-config.json"
DRAFTS_DIR = REPO_ROOT / "docs" / "sessions" / "drafts"
SUBMITTED_DIR = REPO_ROOT / "docs" / "sessions" / "submitted"
TEMPLATES_DIR = REPO_ROOT / "docs" / "atlas" / "templates"

SESSION_START_DRAFT = DRAFTS_DIR / "session-start-draft.md"
SESSION_END_DRAFT = DRAFTS_DIR / "session-end-draft.md"
SESSION_START_TEMPLATE = TEMPLATES_DIR / "session-start-template.md"
SESSION_END_TEMPLATE = TEMPLATES_DIR / "session-end-notes-template.md"

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_config():
    if not CONFIG_PATH.exists():
        die(f"Config not found: {CONFIG_PATH}")
    with open(CONFIG_PATH) as f:
        return json.load(f)

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)

def now_iso():
    """Return current UTC time as ISO 8601 string."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def timestamp_slug():
    """Return a filesystem-safe timestamp: YYYY-MM-DDTHH-MM."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M")

def paperclip_post_comment(api_base, issue_id, body):
    """Post a comment to a Paperclip issue via the REST API. Returns the comment dict."""
    url = f"{api_base}/issues/{issue_id}/comments"
    payload = json.dumps({"body": body}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        die(f"Paperclip API error {e.code} on POST {url}: {body_text[:500]}")
    except Exception as e:
        die(f"Paperclip API request failed: {e}")

def paperclip_get_comments(api_base, issue_id):
    """Fetch all comments for a Paperclip issue."""
    url = f"{api_base}/issues/{issue_id}/comments"
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        die(f"Failed to fetch comments for issue {issue_id}: {e}")

def reset_draft(draft_path, template_path, label):
    """Reset a draft file to its blank template state."""
    if not template_path.exists():
        print(f"  WARNING: Template not found at {template_path}, leaving {label} draft intact.", file=sys.stderr)
        return
    content = template_path.read_text(encoding="utf-8")
    draft_path.write_text(content, encoding="utf-8")
    print(f"  Reset {label} draft to blank template.")

def read_draft(draft_path, label):
    """Read draft content. Returns (content_str, is_empty_bool).

    "Empty" means David hasn't written anything beyond the template scaffolding.
    We only inspect content after the first '---' separator (the intro paragraph
    above '---' is template boilerplate, not user content). After that separator,
    any non-blank, non-heading, non-parenthetical line is considered substantive.
    """
    if not draft_path.exists():
        return "", True
    content = draft_path.read_text(encoding="utf-8").strip()
    lines = content.splitlines()
    # Find the first '---' separator and look only at what follows
    try:
        sep_idx = next(i for i, l in enumerate(lines) if l.strip() == "---")
        body_lines = lines[sep_idx + 1:]
    except StopIteration:
        body_lines = lines  # no separator found — inspect everything

    substantive = [
        l for l in body_lines
        if l.strip()
        and not l.strip().startswith("#")
        and not l.strip().startswith("---")
        and not (l.strip().startswith("(") and l.strip().endswith(")"))
    ]
    is_empty = len(substantive) == 0
    return content, is_empty

# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_start(cfg):
    """
    Session Start:
    1. Read session-start-draft.md. Validate it has at least some content.
    2. Copy to submitted/<ts>-session-start.md.
    3. Post [SESSION START] comment on tracker issue.
    4. Reset session-start-draft.md to blank template.
    """
    api_base = cfg["paperclipApiBase"]
    issue_id = cfg["sessionTrackerIssueId"]
    tracker_id = cfg.get("sessionTrackerIdentifier", issue_id)

    content, is_empty = read_draft(SESSION_START_DRAFT, "session-start")

    if is_empty:
        print(
            "session-start-draft.md appears empty (no substantive content beyond headings).\n"
            f"Fill it in at: {SESSION_START_DRAFT}\n"
            "Then re-run: python scripts/session.py start"
        )
        sys.exit(1)

    ts = timestamp_slug()
    iso = now_iso()

    # Archive
    SUBMITTED_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = SUBMITTED_DIR / f"{ts}-session-start.md"
    archive_path.write_text(content, encoding="utf-8")
    print(f"  Archived session-start submission to: {archive_path.relative_to(REPO_ROOT)}")

    # Post Paperclip comment
    comment_body = (
        f"[SESSION START] {iso}\n\n"
        f"David's session-start submission (archived to `{archive_path.relative_to(REPO_ROOT)}`):\n\n"
        "---\n\n"
        + content
    )
    comment = paperclip_post_comment(api_base, issue_id, comment_body)
    comment_id = comment.get("id", "?")
    print(f"  Posted [SESSION START] comment on {tracker_id} (comment id: {comment_id})")

    # Reset draft
    reset_draft(SESSION_START_DRAFT, SESSION_START_TEMPLATE, "session-start")

    print(f"\nSession started at {iso}.")
    print(f"Atlas will respond on {tracker_id} at next heartbeat with a [SESSION-START-RESPONSE].")


def cmd_end(cfg):
    """
    Session End:
    1. Read session-end-draft.md (optional — empty is valid).
    2. Copy to submitted/<ts>-session-end.md (even if empty).
    3. Post [SESSION END] comment on tracker issue.
    4. Reset session-end-draft.md to blank template.
    """
    api_base = cfg["paperclipApiBase"]
    issue_id = cfg["sessionTrackerIssueId"]
    tracker_id = cfg.get("sessionTrackerIdentifier", issue_id)

    content, is_empty = read_draft(SESSION_END_DRAFT, "session-end")
    iso = now_iso()
    ts = timestamp_slug()

    # Archive (even if empty — the file is the timestamp record)
    SUBMITTED_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = SUBMITTED_DIR / f"{ts}-session-end.md"
    archive_path.write_text(content if content else "(no notes)", encoding="utf-8")
    print(f"  Archived session-end submission to: {archive_path.relative_to(REPO_ROOT)}")

    # Post Paperclip comment
    if is_empty:
        notes_section = "(David did not provide optional notes — this is valid.)"
    else:
        notes_section = (
            "David's optional notes (archived to "
            f"`{archive_path.relative_to(REPO_ROOT)}`):\n\n"
            "---\n\n"
            + content
        )

    comment_body = (
        f"[SESSION END] {iso}\n\n"
        + notes_section
    )
    comment = paperclip_post_comment(api_base, issue_id, comment_body)
    comment_id = comment.get("id", "?")
    print(f"  Posted [SESSION END] comment on {tracker_id} (comment id: {comment_id})")

    # Reset draft
    reset_draft(SESSION_END_DRAFT, SESSION_END_TEMPLATE, "session-end")

    print(f"\nSession ended at {iso}.")
    print(f"Atlas will produce a [SESSION-DEBRIEF] on {tracker_id} at next heartbeat.")


def cmd_status(cfg):
    """
    Status:
    Print whether a session is currently active (last event was [SESSION START] vs [SESSION END]),
    and the timestamps of the most recent start and end.
    """
    api_base = cfg["paperclipApiBase"]
    issue_id = cfg["sessionTrackerIssueId"]
    tracker_id = cfg.get("sessionTrackerIdentifier", issue_id)

    comments = paperclip_get_comments(api_base, issue_id)
    # Sort by createdAt
    comments.sort(key=lambda c: c.get("createdAt", ""))

    last_start = None
    last_end = None
    for c in comments:
        body = c.get("body", "")
        created = c.get("createdAt", "?")
        if body.startswith("[SESSION START]"):
            last_start = created
        elif body.startswith("[SESSION END]"):
            last_end = created

    print(f"Session tracker: {tracker_id} ({issue_id})")
    print(f"  Last [SESSION START]: {last_start or '(none)'}")
    print(f"  Last [SESSION END]:   {last_end or '(none)'}")

    if last_start is None and last_end is None:
        print("\nState: No sessions recorded yet.")
    elif last_start and (last_end is None or last_start > last_end):
        print(f"\nState: SESSION ACTIVE (started {last_start})")
    elif last_end and (last_start is None or last_end >= last_start):
        print(f"\nState: No active session (last ended {last_end})")

    # Draft state
    _, start_empty = read_draft(SESSION_START_DRAFT, "session-start")
    _, end_empty = read_draft(SESSION_END_DRAFT, "session-end")
    print(f"\n  session-start-draft.md: {'(blank template)' if start_empty else 'HAS CONTENT — ready to run: python scripts/session.py start'}")
    print(f"  session-end-draft.md:   {'(blank template)' if end_empty else 'HAS CONTENT — can be submitted with: python scripts/session.py end'}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

USAGE = """\
Usage: python scripts/session.py <subcommand>

Subcommands:
  start   Submit session-start-draft.md and begin a new working session.
  end     Submit session-end-draft.md (optional notes) and close the session.
  status  Show current session state (active? last start/end timestamps).

Workflow:
  1. Fill in docs/sessions/drafts/session-start-draft.md
  2. Run: python scripts/session.py start
  3. [Work with Atlas. Fill in session-end-draft.md anytime (optional).]
  4. Run: python scripts/session.py end
  5. Atlas produces a Session Debrief at next heartbeat.

Config: scripts/session-config.json (Paperclip API, tracker issue ID)
Spec:   docs/atlas/davidos-session-workflow-v0.md
"""

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(USAGE)
        sys.exit(0)

    subcommand = sys.argv[1]
    if subcommand not in ("start", "end", "status"):
        print(f"ERROR: Unknown subcommand '{subcommand}'\n", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        sys.exit(1)

    cfg = load_config()

    if subcommand == "start":
        cmd_start(cfg)
    elif subcommand == "end":
        cmd_end(cfg)
    elif subcommand == "status":
        cmd_status(cfg)


if __name__ == "__main__":
    main()
