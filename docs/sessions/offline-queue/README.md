# docs/sessions/offline-queue/

Pending-review work items Atlas has recommended Atlas (or another agent) execute while David is offline. Each item is a single file with a status header. David approves, rejects, or defers each item between sessions; Atlas executes only after status flips to `approved`.

Filename convention: `<YYYY-MM-DD>-<short-slug>.md` (e.g., `2026-05-12-cleanup-stale-output-files.md`).

Frontmatter (YAML):

```yaml
---
status: pending     # pending | approved | rejected | deferred
requested_at: 2026-05-12T14:32Z
kind: offline-work  # always 'offline-work' for this folder
source: Atlas       # Atlas | <agent-slug>
---
```

Body sections (in this order):

1. **what** — concrete proposed action.
2. **why** — link to the Session Debrief or Parking Lot item that motivated it.
3. **risk** — what could go wrong; reversibility.
4. **expected_cost** — token budget / wall-clock / external-service spend.
5. **proposed_action** — exact commands or steps Atlas will run on approval.

Approval flow:

- Atlas opens an `[APPROVAL-REQUEST] kind: offline-work` comment on the session-tracker issue, one per pending file. The comment summarizes what / why / risk / cost.
- David replies on the comment with `[APPROVAL: offline-work]`, `[REJECT]`, or `[DEFER: <YYYY-MM-DD>]`.
- Atlas updates the file's `status:` header to `approved` / `rejected` / `deferred` and re-records the decision date in the body. Atlas executes only items with `status: approved`.

Rules:

- Atlas does NOT execute the proposed action until status is `approved`. Pre-research within `safe-doc-edit` bounds is allowed (e.g., Atlas may scan the affected files and refine the cost estimate) but no destructive or out-of-scope action.
- Daily Operating View "Pending approvals" section auto-includes pending offline-queue items because each is already an `[APPROVAL-REQUEST]` with a `kind:`.
- Items with `status: deferred` are re-surfaced in the Daily Operating View on or after the deferred-until date.

Lifecycle reference: `docs/atlas/davidos-session-workflow-v0.md`.
