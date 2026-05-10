# docs/sessions/submitted/

Immutable archive of submitted session artifacts. Files here are written by `scripts/session.py {start,end}` (Stage 2.6+) and by Atlas (the Session Debrief) — never edited by hand after creation.

Filename convention: `<YYYY-MM-DDTHH-MM>-<kind>.md` where kind is one of:

- `session-start` — copy of David's Session Start Submission at the moment he ran `scripts/session.py start`. Contents: top-of-mind, decisions, questions, ideas, considerations.
- `session-end` — copy of David's optional Session End notes (may be empty). Indicates the session has been explicitly ended.
- `debrief` — Atlas's Session Debrief, produced ALWAYS in response to a `[SESSION END]` regardless of whether David provided notes. Eight-section schema per `docs/atlas/davidos-session-workflow-v0.md` §8.

Read access:

- Atlas reads all submitted files. The Session Debrief is durable Atlas-output (treated as memory). Session Start / End submissions become instructions only via the matching Atlas response (`[SESSION-START-RESPONSE]` / `[SESSION-DEBRIEF]`).
- David reads them via the Daily Operating View "Session history" surface (Stage 2.6+) or directly.

Rules:

- Files in this folder are immutable. Corrections are issued as a follow-up `[SESSION-START-CORRECTION]` / `[SESSION-END-CORRECTION]` comment on the session-tracker issue, not by editing the file.
- Atlas does not delete files here. Archival rules (e.g., quarterly compaction into `docs/archive/`) require `[APPROVAL: policy-change]`.

Lifecycle reference: `docs/atlas/davidos-session-workflow-v0.md`.
