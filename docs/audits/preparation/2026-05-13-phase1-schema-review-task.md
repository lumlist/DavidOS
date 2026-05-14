# Phase 1 Task: Autonomy Map Schema Design Review

**Status:** Phase 1 task addendum for charter-active Atlas. To be executed after the structural audit (per `2026-05-13-task3-audit-prompt-and-meta-analysis.md`, revised per Tasks 4 and 5) completes.

**Purpose:** The audit evaluates whether the populated autonomy map satisfies P6. It does not evaluate whether the schema design choices (5 rungs, action-category primary key, 10-field schema with audit metadata, action-map-with-modifiers structure) are the best choices for satisfying P6. This task adds explicit schema-design evaluation as a separate post-audit work item.

**Trigger:** David, 2026-05-13 evening, explicitly requested that Atlas give feedback on the schema choices in addition to verifying the populated map.

---

## Task statement (for Atlas)

You have just completed the 2026-05-13 structural audit (saved at `docs/audits/2026-05-13-structural-audit.md`). Your audit verdict on P6 evaluated whether the populated autonomy map satisfies the principle's falsifiable test. This task is different: evaluate whether the **schema design choices** made on 2026-05-13 are the best choices for satisfying P6 and the other consolidated principles, or whether different choices would serve the principles better.

**Read in this order:**

1. `docs/audits/preparation/2026-05-13-autonomy-map-design-decisions.md` — the three structural decisions (5 rungs, action-category primary key, 10-field schema) and the principle-grounded reasoning for each.
2. `docs/autonomy/SCHEMA.md` — the canonical definition of rungs and fields.
3. `docs/autonomy/action-map.md` — the populated v0.1 action map (~15–25 categories).
4. `docs/autonomy/modifiers.md` — the v0.1 modifier rules.
5. `docs/autonomy/README.md` — orientation document.

**Then evaluate each of the three structural decisions:**

### Evaluation 1: Five rungs vs alternatives

Confirm or contest the decision to use five rungs (L0 Forbidden, L1 Asks First, L2 Acts and Reports, L3 Acts Silently, L4 Schedules and Acts) versus David's original four-rung sketch in his design-principles source. Cite specifically.

Possible verdicts:
- **CONFIRM** — five rungs are the right cut. Reasoning grounded in operational distinctions and principle satisfaction.
- **CONTEST** — different rung count or different rung definitions would serve the principles better. Propose alternative with reasoning.
- **EXTEND** — five rungs are right but additional rungs are needed. Propose additions.

### Evaluation 2: Action-category primary key vs alternatives

Confirm or contest the decision to map autonomy to action categories with actor/context as modifiers, versus per-agent maps or one-unified-map-with-agent-column structures. Cite specifically against P1, P3, P4, P6.

Possible verdicts:
- **CONFIRM** — action-category-with-modifiers is the principle-aligned structure for DavidOS specifically.
- **CONTEST** — different primary key (per-agent, per-process, or hybrid) would serve the principles better in DavidOS's actual evolution path. Propose alternative with reasoning.
- **EXTEND** — action-category primary key is right but the modifier system is insufficient. Propose extensions.

### Evaluation 3: 10-field schema with audit metadata

Confirm or contest the decision to include audit metadata fields (Date added, Added by, Review trigger, Last reviewed) in the v0.1 schema versus deferring to v0.2. Evaluate whether the "on observed drift" default review trigger is appropriate or whether a different default would be better.

Possible verdicts:
- **CONFIRM** — 10-field schema with "on observed drift" default is right for v0.1.
- **CONTEST** — fewer fields or different defaults would serve the system better. Propose alternative with reasoning.
- **EXTEND** — 10 fields are right but additional fields are needed. Propose additions.

### Evaluation 4: Schema gaps deferred to v0.2

The design-decisions document explicitly defers three things to v0.2: time-of-day conditions, cross-category dependencies, and confidence-threshold conditional rungs. Evaluate whether any of these should be addressed sooner than v0.2.

Possible verdicts:
- **DEFERRAL APPROPRIATE** — v0.2 is the right time for each of the three.
- **PROMOTE ONE OR MORE** — specify which deferred items should be addressed sooner and why.

### Output

Save your evaluation to `docs/audits/2026-05-13-autonomy-map-schema-review.md` with these sections:

- §1. Evaluation 1 verdict (rungs)
- §2. Evaluation 2 verdict (primary key)
- §3. Evaluation 3 verdict (schema fields and defaults)
- §4. Evaluation 4 verdict (v0.2 deferrals)
- §5. Recommendations — concrete changes you propose, if any, with the specific edit to make and to which file
- §6. What you would want David to verify before acting on your recommendations

If your verdict on every evaluation is CONFIRM with no recommended changes, say so explicitly in one paragraph and stop. Do not invent disagreements.

---

## Constraints

- Cite specific lines of `2026-05-13-autonomy-map-design-decisions.md` and the relevant principle files when contesting any decision.
- "I would have made the same choice for the same reason" is a valid CONFIRM answer. Do not invent alternative reasoning to seem rigorous.
- This evaluation does not authorize editing the autonomy map. It produces recommendations; David approves any changes via ADR-004 Full intensity (autonomy map edits are identity-level per Section 6 of SOUL.md).
- Bound the scope: this is a single-pass evaluation, not an open-ended exploration. If you find yourself wanting to redesign the autonomy system from scratch, surface that as a structural finding in §5 and stop.

---

## Why this task exists

The audit's principle-by-principle evaluation tests whether DavidOS state satisfies the principles. It does not surface "here's why I would have done it differently" feedback on schema choices that satisfy the principles via one path when alternative paths would also have satisfied them.

For autonomy map specifically, David explicitly wanted Atlas's feedback on the structural choices (not just verification of the populated map). This task provides that feedback as a focused single-pass evaluation, scoped to the three decisions documented on 2026-05-13.

If Atlas's evaluation surfaces material disagreements with the design decisions, David approves changes via ADR-004 Full intensity. If Atlas confirms the decisions, the schema is validated by independent post-activation review.
