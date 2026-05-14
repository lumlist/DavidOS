# Audit Preparation — Task 5: SOUL.md Text Integration Pass

**Produced by:** Claude Opus 4.7 (via Computer)
**Date:** 2026-05-13 evening CDT
**Status:** Preparation artifact for the 2026-05-13 structural audit.
**Purpose:** Close the visibility gap on the SOUL.md draft text and confirm or revise Task 4 recommendations against the actual approved state of Sections 1–9.

**Trigger:** After Task 4 landed, David and Sonnet identified that Opus had been judging Sections 1–5 blind — he had only the session record's description of what those sections contained, not the actual draft text. Operator provided the missing context (on-disk text + Section 5 delta from 2026-05-12 walkthrough + Section 6 self-reference catch from Sonnet's review of Task 4) and asked Opus to update only the deltas.

**Decisions reflected in this artifact:**
- David accepted the two-layer split between SOUL.md (operating stance, 6 principles) and AGENTS.md (architectural, 7 consolidated principles), with reconciliation as Phase 1 work post-activation.
- The autonomy-map / Section-6 co-dependency identified by Opus in Task 5 (4) resulted in a revised Phase 0 sequence (P0.1a → P0.1b → P0.1c → P0.1d → P0.2 → P0.3).

---

## Opus's note on visibility

I do not have visibility into the actual SOUL.md draft text — the user message says "given (a) the actual SOUL.md draft text above" but the text above describes Section 5's principle list, not the full draft. I'll work from what is described: 6 approved Section 5 principles, plus the Section 6 forward-reference catch from Sonnet's review. If the user intended to paste fuller draft text and it was lost, flag for me and I'll re-evaluate.

**Operator note (Sonnet/Computer):** The full SOUL.md v0.2 text was prepared by Sonnet but not pasted into the Opus message. Opus worked from the Section 5 delta description plus the Section 6 catch and still produced sound output. Sonnet's review of Task 5 concluded the full text round-trip was not necessary — Opus's Section 5 mapping was correct from the description, and Sections 6/7/8/9 content was not in dispute. Task 5 stands as authoritative.

---

## (1) Task 4 (4) and (5) recommendations — what stands, what changes

### Task 4 (4) — Sections 1–5 revisit: stands with one specific change.

My Task 4 (4) said "no revisit needed for activation, two small additions post-activation" and named the post-activation additions as (i) AGENTS.md auto-load note in Section 4 and (ii) "principle reconciliation in Section 5." I also wrote: "If David's Section 5 currently lists principles other than the 7 consolidated ones from task 2, flag this before activation but do not block on it."

The new information confirms the conditional triggered — Section 5 has 6 principles, not the 7 consolidated ones, with different language and groupings. My recommendation stands. The reconciliation is post-activation work; it does not block activation. The conditional in Task 4 (4) was written precisely for this case.

### One specific change to Task 4 (4): I underestimated Section 5's coverage of the seven consolidated principles. Mapping the approved Section 5 against the seven:

| Approved Section 5 principle | Maps to consolidated principle |
|---|---|
| David's outcomes come first | Frames all seven; not a 1:1 map |
| Tool-agnostic | No direct principle map (cross-cutting) |
| Anti-overengineering | Partial P7 (build around bottleneck, not features) |
| Cost-aware | Partial P5 (cost as part of observability) |
| Approval-disciplined | P6 (graduated autonomy) |
| Repo scope | No direct principle map (operational boundary) |
| Each session starts fresh | Partial P1 (information architecture — explicit context per session) |

Section 5 covers P5, P6, P7 partially and does not name P1 (information architecture), P2 (named layers), P3 (router), or P4 (reusable assets). That's a real gap, not just a translation difference.

**Updated recommendation:** Post-activation reconciliation is a Phase 1 task with a specific shape — extend Section 5 to either name the missing four principles or explicitly reference the consolidated set as the architectural principles (with Section 5 retained as the operating stance layer). Not a blocker.

### Task 4 (5) — Sections 7–9 rework: stands without revision.

The delta only affected Section 5. Section 7 light edits (epistemic honesty clause, inventive-commercial lens clause), Section 8 stand-as-drafted, Section 9 unknown — all unchanged by this delta.

---

## (2) Section 6 self-reference catch — confirm

**Confirm.** Sonnet's catch is correct. Task 4 (3) Section 6 text says "the canonical list... lives at `docs/decisions/atlas-autonomy-map.md` (to be authored as the first post-activation artifact)" while Task 4 (7) Phase 0 puts authoring at step P0.2, pre-activation. The phasing in (7) is correct; the Section 6 text is the inconsistency.

The phasing is right because Section 6's autonomy logic references the map operationally — Atlas needs to consult it during his first post-activation session, so it must exist when he activates. Authoring it pre-activation is the prerequisite, not post-activation work.

### Revised Section 6 fragment (replaces the "Autonomy by category" subsection):

```
### Autonomy by category (the configured map)

Atlas's autonomy is set by configuration, not by chat habit. Per P6,
the canonical list of action categories with their autonomy rung
lives at docs/decisions/atlas-autonomy-map.md. The v0.1 map is
authored by David pre-activation as the initial category-to-rung
table; I extend it post-activation as new action categories emerge,
proposing each extension as a Full approval item.

When I encounter an action category not on the map, I treat it as
advisory by default and surface the gap rather than assume a rung.

Hermes configuration that enforces this:
- approvals.mode: smart
- skills.guard_agent_created: true
- checkpoints.enabled: true (max_snapshots: 20)
- terminal.backend: local (sensitive paths still gated)
```

**Three changes from the Task 4 (3) version:**
- (a) "(to be authored as the first post-activation artifact)" replaced with the pre-activation/post-activation split
- (b) Atlas's behavior on unmapped categories made explicit ("treat it as advisory by default and surface the gap")
- (c) "proposing each extension as a Full approval item" preserved from the original since that mechanism still holds

---

## (3) Reconcile Section 5 before or during Phase 1?

**Recommendation: during Phase 1, as the first reconciliation task after AGENTS.md (P1.1). Not before activation.**

### Reasoning:

1. **Activation is gated on the canary check, not on Section 5 content correctness.** Section 5 as currently approved is internally coherent — six principles David explicitly walked through and approved. It is not wrong; it is incomplete relative to the consolidated set. Incomplete is not a blocker.

2. **Reconciling Section 5 before activation puts Sonnet (not charter-active Atlas) in charge of the reconciliation.** The reconciliation question is exactly the kind of identity-shaping work Atlas should participate in, not have done to him. Doing it pre-activation re-introduces the "Sonnet shaping Atlas" failure mode that the prior month's work was supposed to end.

3. **Reconciliation requires a structural choice:** either (a) extend Section 5 to list all seven consolidated principles, or (b) keep Section 5 as the operating stance layer (current 6 principles, which are operating commitments) and reference the consolidated set as architectural principles loaded separately. **Choice (b) is cleaner** because Section 5's six approved principles read as stance (how Atlas operates) rather than architecture (how the system is built). That choice is meaningful and deserves charter-active Atlas at the table.

4. **Phase 1's P1.1 (AGENTS.md authorship) is the natural place to put the architectural principles** — knowledge pack §I2 already drafts AGENTS.md content listing all seven consolidated principles. If AGENTS.md carries the architectural seven and SOUL.md Section 5 carries the operating six, the reconciliation resolves into a layering rather than a rewrite. This is the cleanest path.

### Concrete sequence:

Activate Atlas with Section 5 as approved (6 principles). First Phase 1 task is AGENTS.md authorship, which establishes the seven consolidated principles as project-level context auto-loaded per session. Second Phase 1 task is a Section 5 reconciliation pass where Atlas proposes whether Section 5 needs extension or stands as the operating-stance layer with AGENTS.md as the architectural layer. David approves the reconciliation as a Full approval item.

This adds a 0.5 step to Phase 1 (call it P1.1b) but does not change Phase 1's overall shape.

**Decision (David, 2026-05-13 evening):** Accept the two-layer split. Section 5 stays as the operating-stance layer; AGENTS.md will carry the 7 architectural principles; reconciliation happens post-activation as Phase 1 work.

---

## (4) Anything else in Task 4 that should change

**One thing: Task 4 (7) Phase 0 priority order needs P0.1 and P0.2 reordered, with P0.2's content sharpened.**

Task 4 (7) listed Phase 0 as: P0.1 finish SOUL.md → P0.2 Atlas Autonomy Map v0.1 → P0.3 activate → P0.4 config.

Given the Section 6 forward-reference catch and the autonomy map's load-bearing role in Section 6, the autonomy map should be authored during the Section 6 rewrite, not after. They are co-dependent: Section 6 references the map's structure; the map exists to satisfy Section 6's references. Doing P0.1 fully and then P0.2 risks finalizing Section 6 against a hypothetical map structure, then discovering the map's actual structure forces a Section 6 revision.

### Revised Phase 0 ordering:

- **P0.1a** — Author Atlas Autonomy Map v0.1 **structure** (the category schema and rung definitions, not the populated category list). 20–30 min, David + Sonnet.
- **P0.1b** — Rewrite Section 6 of SOUL.md against the map's actual structure (using the revised fragment in section 2 above). 20–30 min.
- **P0.1c** — Populate Atlas Autonomy Map v0.1 **category list** (10–25 initial categories with rungs). 30–45 min, David's judgment with Sonnet support.
- **P0.1d** — Section 7 light edits (epistemic honesty clause, inventive-commercial lens clause). 10 min.
- **P0.2** — Activate Atlas per pickup-brief Step 1 sub-tasks (canary check). 60–90 min.
- **P0.3** — Apply Hermes config from Task 4 (6). 10–15 min.

**Phase 0 total: ~2.5–3.5 hours**, slightly longer than the Task 4 (7) estimate but with the co-dependency resolved.

Nothing else in Task 4 changes. The seven consolidated principles, the audit prompt revision plan, the Hermes config, and the Phase 1/Phase 2 substrate ordering all stand. The two specific deltas above are the only revisions the missing context forces.

---

## Operational summary

After Task 5, the following are locked in for tonight's Phase 0:

1. SOUL.md Sections 1–5 stand as approved (6 principles in Section 5; do not extend pre-activation)
2. AGENTS.md (post-activation, P1.1) will carry the 7 consolidated architectural principles
3. Section 6 will be rewritten per Task 4 (3) **with the autonomy-by-category subsection replaced by Task 5 (2)**
4. Section 7 light edits per Task 4 (5) — epistemic honesty + inventive-commercial lens clauses
5. Sections 8–9 stand as drafted
6. Atlas Autonomy Map v0.1 will be authored by David pre-activation in two steps: structure (P0.1a) then population (P0.1c), with Section 6 finalized between them (P0.1b)
7. Hermes config applied per Task 4 (6) — `approvals.mode: smart`, `skills.guard_agent_created: true`, `checkpoints.enabled: true`, `agent.max_turns: 150`, etc.
8. Atlas activation per pickup-brief Step 1 procedure with canary verification

Phase 1 substrate work and the revised audit run wait for next session.
