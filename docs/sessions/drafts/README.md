# docs/sessions/drafts/

Working drafts for the active session. Inert by default — Atlas does NOT read these files during heartbeat operation. They become instructions only when David runs `scripts/session.py {start,end}` (Stage 2.6+) and the script atomically copies the draft into `../submitted/` and posts the matching `[SESSION START]` / `[SESSION END]` comment.

Files in this folder:

- `session-start-draft.md` — David fills before running `scripts/session.py start`. Reset to blank template after submission.
- `session-end-draft.md` — David optionally fills during the session for ideas / observations / questions. Empty is valid; David is NOT required to write a debrief — Atlas produces it.
- `parking-lot.md` — rolling Parking Lot with three labeled sections (`## David` / `## Atlas` / `## Other agents`). May be appended at any time by David, Atlas, or other agents. Each entry includes a source field. Items here are observations only — not active work, not durable memory, not instructions.

Rules (locked into `docs/atlas/approval-policy-v0.md`):

- Drafts are inert. Atlas never reads `session-start-draft.md` or `session-end-draft.md` during normal operation. Heartbeats do not poll draft files.
- Parking Lot is observation, not direction. Atlas may surface items as routing candidates in the Daily Operating View; never acts on them without explicit `[APPROVAL: <kind>]`.
- Agent-submitted Parking Lot items are *suggestions only*. They are not durable memory, active work, skills, automations, or agent instructions until David approves promotion.

Lifecycle reference: `docs/atlas/davidos-session-workflow-v0.md`.
