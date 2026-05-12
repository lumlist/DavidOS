# ADR-004: Workspace-native approval mechanism

**Date:** 2026-05-11
**Status:** Accepted
**Deciders:** David Izzard

## Context

DavidOS's operating principles require approval gates for spending, external messages, production edits, account creation, legal/privacy conclusions, major business strategy, file deletion, and code commits unless explicitly authorized. The vision doc codifies this list. Atlas's personality charter references it.

Under Paperclip, approvals had a working mechanism: `[APPROVAL: <kind>]` comment tags inside issue threads. The tag signaled *this is an approval gate*, David's reply provided the decision, and the tagged comment plus reply became a durable audit trail searchable later. Two functions in one artifact: **signal** and **record**.

That mechanism died with Paperclip ([ADR-003](./ADR-003-paperclip-frozen-atlas-memo-library.md)). Today, approvals happen in free-flowing hermes-workspace chat. That works for ephemeral one-offs but fails for substantive decisions because there is no:

- Standardized way to mark a chat turn as *this is an approval request*
- Durable record of *what was approved, why, when, with what conditions*
- Way to find prior approvals later without scrolling chat logs

The Paperclip mechanism is also not directly portable. Tag conventions inside chat feel bureaucratic. Workspace doesn't ship a native approval primitive. And David's threshold for *how rigorous* an approval should be varies by project phase, risk, reversibility, and current system confidence — a static checklist would freeze a judgment that's intentionally evolving.

## Decision

Introduce a Workspace-native approval mechanism with four components:

1. **A structured approval-request format** Atlas uses in chat when proposing actions on the canonical "requires approval" list. Scales between two intensities (light vs full) based on stakes.

2. **A durable approvals log** at `docs/decisions/approvals-log.md` (append-only, dated). One line per approval with topic, intensity, decision, and link to the relevant session debrief or ADR.

3. **A hybrid escalation rule:** small approvals are captured in the session debrief and indexed in the approvals log. Large approvals (anything that becomes operating policy or carries reversibility cost) are escalated to a new ADR and also indexed.

4. **A default expiry on policy-level approvals.** Tactical one-offs do not expire. Policy approvals (anything that becomes a standing rule) carry a default 90-day review window unless marked permanent or assigned a different window.

## Rationale

**Why the structured format (Decision 2: Option C):**

- Free-form (current state) is failing — approvals get lost in chat scrollback.
- Tag conventions (`[APPROVAL NEEDED: spending]`) are parser-friendly but bureaucratic in a chat UI, and don't communicate the *substance* of the decision.
- A 4-line structure (**Action / Reason / Risk / Reversibility**) is the lightest discipline that captures what an approval actually needs to decide on. It scales — when the action is trivial the four lines collapse to a paragraph; when serious they expand.

**Why two intensities, not a fixed bar:**

David's threshold for approval rigor depends on project phase, risk, reversibility, and current system confidence. A static checklist freezes judgment that's intentionally evolving. Two intensities — Light and Full — let Atlas pick based on stakes without escalating every micro-decision into a meeting.

**Why hybrid storage (Decision 1: Option D):**

- ADR-for-everything (Option C) is overkill for tactical decisions.
- Chat-only (Option A) is the current failing state.
- Session-debriefs-only (Option B) loses the cross-session retrieval value.
- Hybrid matches the existing pattern: significant decisions become ADRs (already the convention), tactical decisions live in session debriefs, and the approvals log indexes both so retrieval is one file open instead of grep.

**Why a separate approvals log (Decision 4: Option B):**

A single append-only `docs/decisions/approvals-log.md` is cheap to maintain (one line per approval) and high-leverage for retrieval. Atlas reads it at session start to know what's been approved before re-asking. Without the log, "did we already approve X?" requires scrolling old sessions, which is friction that pushes toward re-approving things or skipping approval entirely.

**Why default 90-day expiry on policy approvals:**

Matches the re-evaluation discipline that's already in every ADR. Tactical approvals are point-in-time and don't expire (it would be silly to "renew" approval for a $50 expense from three months ago). Policy approvals — anything that becomes a standing rule — should be revisited so the system doesn't ossify around stale assumptions. 90 days is the default; any approval can be marked permanent or assigned a different window at the time of approval.

**Reversibility:** This ADR introduces a convention, not infrastructure. If the convention proves bureaucratic in practice, modifying or replacing it costs nothing more than editing this ADR and updating Atlas's personality charter.

## The mechanism in detail

### Canonical "requires approval" list (unchanged from vision doc)

Atlas does NOT take these actions without explicit approval:

- Spending money / creating accounts (paid services, subscriptions)
- Sending external messages (emails, DMs, posts)
- Editing production systems beyond DavidOS itself
- Applying database migrations
- Legal/privacy conclusions
- Major business strategy decisions
- Deleting files
- Committing or pushing code unless explicitly authorized in-session

Atlas MAY do these without approval:

- Drafting documents, summaries, analyses
- Proposing plans and identifying risks
- Reading and citing existing artifacts
- Asking clarifying questions

### Approval intensities

**Light approval** — appropriate when stakes are low, action is highly reversible, and David has high confidence in the proposed direction.

Format:
```
[APPROVAL — LIGHT]
Action: <one sentence>
Reason: <one sentence>
Risk / reversibility: <one sentence; how easy to undo if wrong>
Approve / modify / deny?
```

Example contexts: small expense (<$50) on an existing approved vendor, sending a routine drafted email already reviewed, deleting clearly obsolete files in a known-safe directory.

**Full approval** — appropriate when stakes are high, action is hard to reverse, money or external visibility is meaningful, or system confidence is unsettled.

Format:
```
[APPROVAL — FULL]
Action: <what will happen>
Reason: <why this is the right call>
Risk: <what could go wrong, with rough likelihood>
Reversibility: <how to undo, and what residual cost remains>
Alternatives considered: <what else was on the table and why rejected>
Confidence: <high / medium / low, with brief basis>
Approve / modify / deny?
```

Example contexts: spending in a new category, sending external messages to real people (vendors, customers, advisors), production edits, applying a database migration, anything that becomes operating policy.

### How Atlas picks intensity

Atlas defaults to Light when:
- Action is on the requires-approval list but cost/reversibility/visibility are all low
- David has expressed high confidence in this category recently
- The action is repeating a previously-approved pattern

Atlas defaults to Full when:
- Action involves money in a new category, or above a previously-approved ceiling
- Action is externally visible (real people, public surfaces, production systems)
- Reversibility is low or residual cost of mistake is meaningful
- The action would become standing policy if approved
- David has not previously approved this kind of action

David can override either direction at any time:
- *"Treat this as full approval"* — Atlas re-issues in Full format
- *"Skip the format, just do it"* — Atlas proceeds and logs as Light approval with notation that format was waived

### Storage and retrieval

**Every approval gets one line in `docs/decisions/approvals-log.md`** at the end of the session in which it was approved.

Line format:
```
| Date | Intensity | Topic | Decision | Expires | Link |
|------|-----------|-------|----------|---------|------|
| 2026-05-11 | Full | Adopt hermes-workspace as daily driver | Approved | Permanent | [ADR-001](./ADR-001-adopt-hermes-workspace.md) |
| 2026-05-11 | Light | Archive Paperclip-era files | Approved | n/a (tactical) | [Session debrief](../sessions/submitted/2026-05-11-evening.md) |
```

**Light approvals:** captured in the relevant session debrief (`docs/sessions/submitted/`). The debrief's approvals section lists what was approved. The log links to the debrief.

**Full approvals on policy-level decisions:** escalate to a new ADR. The log links to the ADR.

**Full approvals on tactical decisions:** captured in the session debrief like Light approvals but with the Full format preserved in the debrief.

### Expiry

| Approval type | Default expiry |
|---|---|
| Tactical (one-off action) | None — point-in-time |
| Policy (becomes standing rule) | 90 days from approval date |
| Marked permanent at time of approval | None |
| Marked with specific window at approval | As stated |

Atlas reads the approvals log at session start. If a policy approval is approaching expiry (within 14 days) or expired, Atlas surfaces it as part of session start.

## Consequences

**New things that need to exist:**

- `docs/decisions/approvals-log.md` (created in this commit, initially seeded with the three ADR-001/002/003 approvals retroactively).
- Updated Atlas personality charter — add an "Approval discipline" section pointing at this ADR and instructing the format. Will land in a follow-up commit so the personality reflects the ADR.

**New behaviors expected of Atlas:**

- Atlas uses the structured format whenever an action on the canonical list is proposed.
- Atlas picks intensity per the heuristics above and accepts David's overrides.
- Atlas reads the approvals log at session start and surfaces approaching/expired policy approvals.
- Atlas appends approval entries to the log as part of session-end debrief, alongside the customer-zero observations already in his charter.

**New behaviors expected of David:**

- David's approval responses should match the format Atlas used (one-word for Light is fine; substantive engagement for Full). Approvals outside this discipline still count but are noted in the log as such.
- David can revoke a prior approval at any time by adding a new log entry. Revocations are also logged.

**Things that become obsolete:**

- Free-form approval-by-implication ("just do it") still works but is logged as such, with a note that the bypass was explicit. Frequent bypasses are a signal the format is wrong, not that the discipline is wrong — the ADR should be revised.

**Cross-customer (iZZi customer-zero) implication:**

Approval mechanism is the kind of thing every future iZZi customer will want. The two-intensity format and the centralized approvals log are designed to generalize — strip out the David-specific defaults and they're a reusable template. This ADR's structure (canonical list + intensity + log + expiry) is the durable pattern.

## Re-evaluation triggers

- Two or more approvals get lost or skipped in a single week → format is too heavy, simplify
- Atlas regularly mis-picks intensity (Full when Light suffices, or vice versa) → heuristics need tuning
- The approvals log exceeds ~50 entries and retrieval becomes painful → switch to a structured data format or index by topic
- Workspace ships a native approval primitive that obsoletes the chat-based convention → migrate
- A second iZZi customer onboards and the format proves un-generalizable → rework with both contexts in mind

Default review window: **2026-08-11** (90 days). Sooner if any trigger fires.

## Related

- [ADR-001](./ADR-001-adopt-hermes-workspace.md) — Adopt hermes-workspace
- [ADR-002](./ADR-002-anthropic-oauth-over-api-key.md) — Anthropic OAuth
- [ADR-003](./ADR-003-paperclip-frozen-atlas-memo-library.md) — Atlas as memo library
- [`docs/decisions/approvals-log.md`](./approvals-log.md) — durable approvals index (created with this ADR)
- [`docs/atlas/identity/README.md`](../atlas/identity/README.md) — Atlas's re-spawn procedure (next revision will reference this ADR)
- Vision doc [`david-ai-workspace-v0.md`](../../david-ai-workspace-v0.md) — canonical requires-approval list
