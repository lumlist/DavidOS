---
status: pending
requested_at: <YYYY-MM-DDTHH-MMZ>
kind: offline-work
source: Atlas
---

# <one-line title>

## what

(Concrete proposed action. Single sentence.)

## why

(Why this matters now. Link the originating Session Debrief or Parking Lot item: `from <path>:<line-or-section>`.)

## risk

(What could go wrong. Reversibility: reversible / partially-reversible / irreversible. If irreversible, justify why offline-execution rather than next-session-with-David is the right call.)

## expected_cost

(Token budget estimate, wall-clock estimate, any external-service spend. If `paid-service` cost is involved, this item must ALSO include a `[APPROVAL-REQUEST] kind: paid-service` cross-reference — offline-work alone does not authorize paid-service cost.)

## proposed_action

(Exact commands, scripts, or steps Atlas will run on approval. Write enough that David can audit without asking follow-ups.)

---

## Decision log (Atlas appends)

- `<YYYY-MM-DDTHH-MMZ>` requested by Atlas.
- (`<YYYY-MM-DDTHH-MMZ>` David replied `[APPROVAL: offline-work]` / `[REJECT]` / `[DEFER: <YYYY-MM-DD>]` — Atlas updates frontmatter `status:` accordingly.)
- (`<YYYY-MM-DDTHH-MMZ>` Atlas executed; result summary; pointer to artifact / wake / commit.)
