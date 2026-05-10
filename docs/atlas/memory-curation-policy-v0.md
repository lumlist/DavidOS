# Memory Curation Policy — v0

**Status:** Draft. Promote to durable on David's `[APPROVAL: policy-change]`.
**Companion:** the per-folder READMEs under `docs/{raw,wiki,output,archive,daily}/` describe purpose and write permission for each folder. This file describes the cross-cutting rules.

## 1. Repo as source of truth

`/home/hermes/projects/personal-ai-workspace/docs/` is the single source of truth for prose memory in DavidOS / iZZi AI Systems. Git is the audit log.

Forbidden:
- Storing prose memory in Paperclip DB fields (use `output/` and attach as a Paperclip document; the document's body is also persisted in Paperclip DB but the canonical copy lives in the repo).
- Storing prose memory only in Obsidian vault metadata (e.g., plugin-specific frontmatter that's not portable to plain markdown).
- Storing prose memory only in agent context windows (every durable insight must land in a file).

## 2. Folder layout

```
docs/
  raw/      # transcripts, screenshots, agent-output dumps, scratch — agents write freely
  wiki/     # cleaned, durable concepts and reference knowledge — approval to enter
  output/   # final memos, decision records, deliverables — agents write per-issue
  archive/  # superseded material — read-only after entry
  daily/    # daily notes (template-driven) — David writes; Atlas appends [ATLAS-NOTE]
  atlas/    # Atlas's operating spec, runs, skills, policies — Atlas writes, versioned
  sessions/ # Session workflow artifacts — see §3 sessions/-specific rules
  context/  # project-context files (preserved as-is, used by various tools)
```

`docs/atlas/` exists today and is unchanged. The five Stage 1 folders (`raw/`, `wiki/`, `output/`, `archive/`, `daily/`) are introduced in the Stage 1 bundle. `docs/sessions/` is introduced in the Stage 2.5 bundle. `docs/context/` is preserved as-is.

## 3. Write permission and promotion paths

| Folder | Agents may write directly? | Promotion path | Edit existing? |
|---|---|---|---|
| `raw/` | Yes | Promote to `wiki/` via `[PROMOTION-REQUEST]` → `[APPROVAL: wiki-promotion]` | Free (it's raw) |
| `output/` | Yes (only producing a deliverable for an issue) | Auto-archive 90 days after issue close | New version files (`-v1`); never overwrite |
| `wiki/` | No | Files arrive via approved promotion | `[APPROVAL: wiki-edit]` per edit |
| `archive/` | No | Auto from `output/`, or `[APPROVAL: archive-promotion]` from `wiki/` | Read-only |
| `daily/` | David writes; Atlas appends `[ATLAS-NOTE]` | Auto-archive 90 days | David edits in place; Atlas appends only |
| `atlas/` | Atlas writes (see §4) | n/a — this is Atlas's self-knowledge | Versioned by filename suffix; no overwrites without `[APPROVAL: policy-change]` |
| `sessions/drafts/` | David writes; Atlas writes Atlas-section of `parking-lot.md` only; other agents write their own subsection of `parking-lot.md` only | n/a — drafts are inert, not promoted | David edits in place; Atlas does NOT touch session-{start,end}-draft files during normal operation |
| `sessions/submitted/` | Atlas writes Session Debriefs; `scripts/session.py` (Stage 2.6+) writes session-start / session-end snapshots | n/a — immutable archive | Read-only after creation; corrections via follow-up `[SESSION-*-CORRECTION]` comment, not file edit |
| `sessions/offline-queue/` | Atlas creates pending items; Atlas updates `status:` header on David's reply | Approved items stay in folder until execution complete; then move to `docs/output/<originating-issue>/` or `docs/archive/sessions-offline-queue/` per item kind | Atlas updates `status:` and decision-log on David's reply; body is otherwise immutable |

### 3.1 `docs/sessions/`-specific rules

These rules are cross-cutting and apply on top of the per-folder rows above. Source of truth for the lifecycle and templates: `docs/atlas/davidos-session-workflow-v0.md`.

1. **Drafts are inert.** Atlas does NOT read `docs/sessions/drafts/session-start-draft.md` or `docs/sessions/drafts/session-end-draft.md` during heartbeat operation. Draft contents become instructions only when David runs `scripts/session.py {start,end}` (Stage 2.6+) and the script atomically copies the draft into `docs/sessions/submitted/` and posts the matching `[SESSION START]` / `[SESSION END]` comment.
2. **Atlas always produces the Session Debrief.** On every `[SESSION END]`, regardless of whether David provided notes, Atlas writes a Session Debrief to `docs/sessions/submitted/<timestamp>-debrief.md` and posts `[SESSION-DEBRIEF]` on the session-tracker issue. The Debrief follows the eight-section schema in `davidos-session-workflow-v0.md` §8.
3. **Submitted is immutable.** Files under `docs/sessions/submitted/` are not edited after creation. Corrections go in a follow-up `[SESSION-START-CORRECTION]` / `[SESSION-END-CORRECTION]` / `[SESSION-DEBRIEF-CORRECTION]` comment on the session-tracker issue.
4. **Parking Lot is observation, not direction.** `docs/sessions/drafts/parking-lot.md` has three labeled sections (`## David` / `## Atlas` / `## Other agents` with one H3 subsection per agent slug). Each entry: `- <YYYY-MM-DD HH:MM> | <category> | <text>`. Categories: `idea` | `question` | `concern` | `consideration` | `observation`. Atlas may surface high-value items in the Daily Operating View "Atlas recommendations" section and in the Session Debrief's `## Promotion candidates` section, but acts on none without explicit `[APPROVAL: <kind>]`.
5. **Agent-submitted items are suggestions only.** Items added to the Atlas section or Other-agents subsections of the Parking Lot are NOT durable memory, NOT active work, NOT skills, NOT automations, and NOT agent instructions. They become any of those only via David's explicit `[APPROVAL: <kind>]` on a corresponding promotion or approval-request.
6. **Offline-queue items are pending until approved.** Atlas reads pending items and may pre-research within `safe-doc-edit` bounds. Atlas does NOT execute the proposed action until the file's `status:` header is `approved`. Each pending item generates one `[APPROVAL-REQUEST] kind: offline-work` comment on the session-tracker issue.
7. **Cross-source segregation.** Atlas does not move items between Parking Lot sections. If an entry's source needs re-attribution, the original line stays and a corrective note is appended in the same source's section. Filtering "mine only" is supported by the file structure (David reads only `## David`); the Daily Operating View renderer (Stage 2.6+) will offer a per-source filter so all four views (David / Atlas / Other agents / All) are one click apart.


## 4. The `atlas/` folder is special

`docs/atlas/` is Atlas's self-knowledge: operating spec, run logs, skills, policies, conventions. It's the system's record of how it works. Rules:

- Atlas may write new files under `atlas/runs/` freely (pre-approved `safe-doc-edit`).
- Atlas may add new files under `atlas/` (root level, including new policy drafts) freely as drafts; they only become durable on `[APPROVAL: policy-change]`.
- Existing policy files under `atlas/` (named `*-policy-v*.md` or `*-spec-v*.md` or `*-conventions-v*.md`) are versioned by filename suffix. Substantive edits require `[APPROVAL: policy-change]` and produce a new file (e.g., `comment-conventions-v0.md` → `comment-conventions-v1.md`); no in-place overwrite.
- Typo fixes and pure-formatting changes to existing policy files are allowed under `safe-self-improvement` (per `approval-policy-v0.md` §5.2) with `[STATUS]` disclosure.

## 5. Freshness signals

The Daily Operating View (Stage 3) surfaces:

| Signal | Threshold | Source |
|---|---|---|
| Stale `wiki/` | unedited 60+ days | git log on file |
| Curation debt | `raw/` files unpromoted 14+ days | git log + folder listing |
| Auto-archive eligible | `output/` files where the originating issue closed 90+ days ago | Paperclip API + folder listing |
| Active `wiki/` hubs | top 10 most-linked files | grep across `docs/` for `[[...]]` and `](file)` references |

These signals are informational. They surface the work; they do not auto-execute (except auto-archive, which is deterministic and reversible via git).

## 6. Obsidian as view layer (deferred to Stage 2)

When Obsidian-MCP is approved and installed (separate `[APPROVAL: install]`), the Obsidian vault IS the `docs/` folder — same files, viewed differently. No syncing step. David's edit gestures (rename, link, refactor) write to the same files; git is the audit log.

Vector DB / semantic search over the vault is deferred until corpus exceeds ~50K notes (DAV-15 §11).

## 7. Self-amendment

Edits to this file require `[APPROVAL: policy-change]`.

End of file.
