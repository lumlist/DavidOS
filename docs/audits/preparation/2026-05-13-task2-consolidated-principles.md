# Audit Preparation — Task 2: Consolidated Principles

**Produced by:** Claude Opus 4.7 (via Computer)
**Date:** 2026-05-13 evening CDT
**Status:** Preparation artifact for the 2026-05-13 structural audit.
**Purpose:** Consolidate David's ~18 reconstructed principles + 6 patterns into the highest-leverage set — the principles whose adoption shapes the most downstream architecture decisions. Each principle includes a falsifiable test, a charter-outcome coverage matrix, and surfaced tensions.

**Inputs:**
- Task 1 output (reconstruction + critique): `2026-05-13-task1-reconstruction-and-critique.md`
- `docs/charter/outcomes-and-frustrations-2026-05-13.md` (the 11-point charter outcome list)
- The four foundation ADRs

**Output structure:** Three sections — (1) Consolidated Principles ordered by leverage; (2) Coverage Matrix mapping principles × charter outcomes; (3) Gaps, Overlaps, and Tensions.

**Decision on verification questions:** David (2026-05-13 evening) decided "let the audit propose" resolutions to all four verification questions Opus surfaced at the end of Task 2 (P2/P3 merge, three uncovered outcomes, P3-vs-P7 tie-breaker, P5-vs-ADR-002 tension). These resolutions are part of the audit's required output, not preconditions for running the audit. See Task 3 preparation artifact for how this was encoded into the audit prompt.

---

## 1. CONSOLIDATED PRINCIPLES

**Count arrived at: 7.**

**Reasoning:** I started from the 18 reconstructed PRINCIPLES plus 6 PATTERNS. Pattern 1 (four-layer) and Pattern 2 (command-center / five subsystems) both decompose into "the system has named structural parts that don't bleed into each other" — they collapse into one principle (Principle 2 below). P10 (reusable assets) and P4 (compounding assets) are the same idea stated at workflow vs. system level — they collapse into Principle 4. P12 (build around bottlenecks) and P14 (the seven bottlenecks) are the same principle plus its instance list — they collapse into Principle 7. P9 (decision velocity), P2 (highest-leverage question), and the Pattern 6 pre-build checklist all support but do not stand alongside the seven that remain. Pattern 4 (compounding metrics) and Pattern 5 (failure modes) are tests of the principles below, not principles. P3, P5, P16, P18 had insufficient extracted body to elevate to principle status. Below 7, two principles would always collapse together (e.g., information architecture and curated memory both fail in the same failure mode); above 7, principles become rules-with-promotions. 7 is where each remaining principle is independently falsifiable.

Ordered by leverage (highest first):

### Principle 1 — Information architecture comes before agents

**STATEMENT:** "The system is only as good as its information architecture" (source L32); decide what enters, how it's classified, where it lives, who can act on it, and how it improves future decisions (L26) before building agents, prompts, automations, or interfaces.

**WHY IT'S LOAD-BEARING:** Without it, "everything becomes chat history soup" (L29). Every other principle below presupposes that the system has primitives to operate on: a router (P7) can't route without classified inputs; memory (P15) can't be curated without a schema; evaluation (Pattern 5 FM4) can't compare expected vs. actual without a canonical output type; the source-of-truth hierarchy (P14 #6) can't exist if there is no information model to anchor it. Failure mode: tools integrated cosmetically not operationally (L212), project status lives in five places (L417), the operator re-explains state every session (L233) — exactly Frustration 3 in the charter.

**ONE CONCRETE TEST:** Does the DavidOS repo contain a document that defines (a) the canonical entity types (project, decision, approval, session, asset, etc.), (b) where each lives, and (c) which file is the source of truth when they disagree? As of this commit, `docs/decisions/approvals-log.md` (ADR-004 L27) and `docs/sessions/submitted/` (ADR-004 L142) and `docs/atlas/identity/` (ADR-003 L21) all exist independently with no parent document declaring their relationship. DavidOS currently violates Principle 1.

**TYPE:** Architectural.

### Principle 2 — Separate the system into named layers; no layer owns the strategy

**STATEMENT:** "Separate the system into layers: Input, Reasoning, Execution, Learning" (L47/L49); use a "command-center architecture with specialized agents, durable memory, workflow orchestration, evaluation, and human control points" (L153); and "do not let the execution layer own the strategy. Do not let memory become an unfiltered dump. Do not let the interface become the system" (L60).

**WHY IT'S LOAD-BEARING:** This is the single principle that prevents the "one giant agent that tries to do everything" failure (L50), which is also Failure Mode 1 (L359, "Building agents before workflows"). Without named layers, the router (Principle 3) has nowhere to sit; the evaluator (Principle 5) has nothing to attach to; trust gradients (Principle 6) have no execution surface to gate. Without the three anti-rules, the layers exist on paper but collapse in practice (chat becomes the interface becomes the system). I merged the four-layer model and the command-center / five-subsystems model because they fail together: a system with layers but no subsystems is still "magic that will eventually break" (L64), and a system with subsystems but no layered separation has nowhere to put cross-cutting concerns like observability.

**ONE CONCRETE TEST:** Pick any current DavidOS workflow (e.g., the approvals-log update flow from ADR-004). Can you point to the file or component that is the Input layer, the Reasoning layer, the Execution layer, and the Learning layer for that workflow? As of this commit, the approval flow lives entirely in chat (input), is decided by Atlas in chat (reasoning), is executed by Atlas writing to `approvals-log.md` (execution), and has no Learning layer at all (no mechanism reads the log back to update Atlas's heuristics). DavidOS currently violates Principle 2 — the Learning layer is absent.

**TYPE:** Architectural.

### Principle 3 — Build a strong router before building more agents

**STATEMENT:** "A strong router decides: what type of work is this, what context is required, what tool should handle it, what risk tier applies, what output format is needed, and what approval is required. Routing quality determines system quality." (L84–L85)

**WHY IT'S LOAD-BEARING:** The router is the single component every other principle hands work to. Without it: trust gradients (Principle 6) can't be applied because nothing computes the risk tier; context assembly (Principle 1's downstream) can't run because nothing decides what context is required; the approval mechanism in ADR-004 (which depends on Atlas classifying actions against the canonical list, ADR-004 L66) is performed implicitly by Atlas's general reasoning rather than a dedicated router, which is why approvals "get lost in chat scrollback" (ADR-004 L37). Adding more agents before a router multiplies the routing problem instead of solving it (P14 #4 "Handoff bottleneck," L246).

**ONE CONCRETE TEST:** Is there a file, function, or documented decision procedure in DavidOS that, given an incoming request, emits (work type, required context, tool, risk tier, output format, approval requirement)? As of this commit, no such artifact exists; classification is implicit in Atlas's prompt and chat reasoning. DavidOS currently violates Principle 3.

**TYPE:** Architectural.

### Principle 4 — Every workflow produces a reusable asset; otherwise it's labor

**STATEMENT:** "If a workflow only produces the immediate output, it is labor" (L108). "Every run should improve one of these: dataset, prompt, SOP, evaluation rubric, customer profile, knowledge base, automation rule, product insight, or distribution channel" (L71). The leverage formula: "If a system saves time once, it is automation. If it improves every time it runs, it is infrastructure" (L94).

**WHY IT'S LOAD-BEARING:** This is the principle that makes DavidOS compound rather than just function. Without it, you can satisfy Principles 1–3 and 5–7 and still have a system that produces 20 outputs and 0 reusable assets — exactly the "labor" pattern David explicitly names as the failure (L326). It is the single principle that converts the 11-point charter outcome "Actively self improves" into something operational. Merged P4 (compounding assets) and P10 (every workflow produces reusable assets) — they fail in the same condition (a workflow that ships its immediate output and writes nothing back to a library) and cannot be violated independently.

**ONE CONCRETE TEST:** Pick the last three completed DavidOS workflows (most recent three entries in `docs/sessions/submitted/` and `docs/decisions/approvals-log.md`). For each, name the specific reusable asset that workflow added to a library (prompt library, workflow library, evaluation library, memory). If you cannot name an asset for 2-of-3, the principle is being violated. Likely violated currently — the four ADRs themselves are reusable assets (ADRs are a workflow library), but no prompt library, evaluation library, or routing-rule library exists in the repo as of this commit.

**TYPE:** Architectural.

### Principle 5 — Without evaluation you have production volume, not compounding

**STATEMENT:** "Every important output should be evaluated against explicit criteria" (L155). "Without evaluation, you do not have compounding. You have production volume" (L168). "You cannot improve what you cannot see" (L379) — log "inputs, outputs, model used, cost, latency, confidence, failure reason, human correction, and final business outcome" (L64). "Build Evaluation Systems Early" (L485).

**WHY IT'S LOAD-BEARING:** Principle 4 (reusable assets) without Principle 5 (evaluation) silently degrades — the system keeps adding to its libraries but has no way to know whether the additions are improving outputs. Principle 6 (trust gradients) cannot promote actions to higher autonomy without an evaluation signal showing "the human approves 90 percent of a category unchanged" (L416). Principle 7 (find the bottleneck) cannot identify the evaluation bottleneck without evaluation existing. This is the only principle that closes the Learning layer in Principle 2. I merged "evaluation" and "observability" because evaluation requires observability as its substrate, and a system with one but not the other produces no learning signal in either case.

**ONE CONCRETE TEST:** For any DavidOS workflow, can you produce (a) the evaluation rubric, (b) the logged inputs/outputs/cost/latency/confidence for the last run, and (c) a comparison against a prior run or expected baseline? As of this commit, no logging infrastructure exists, and ADR-002 (L18, L22) deliberately chose Anthropic OAuth specifically because it does not surface per-call cost — directly preventing the "cost" component of R9. DavidOS currently violates Principle 5, with a deliberate ADR-002 trade-off contributing to the violation.

**TYPE:** Architectural.

### Principle 6 — Graduate autonomy by risk; never fully automate values, taste, or irreversible bets

**STATEMENT:** "Not all automation should have the same permission level" (L135). "Use graduated autonomy" (L139) escalating from "execute low-risk reversible actions" (L132) up through "redesign its own workflow with approval" (L138). "If action is irreversible, costly, or security-sensitive, pause for approval" (L208). "Never fully automate: values, taste, irreversible bets, and accountability" (L279). "A strong system makes judgment easier, not absent" (L313).

**WHY IT'S LOAD-BEARING:** This is the principle that turns the router's risk-tier output (Principle 3) into actual behavior. Without it, the system swings between two failure modes David names explicitly: "giving agents too much autonomy too early or keeping everything in manual review forever" (L133) — Failure Modes 5 and 6 in his own list. It is also the principle that protects the operator from the system at scale (charter outcome "Loops me in on the decisions that matter"). I merged P13 (trust gradients), the L1–L4 autonomy ladder, the automation hierarchy (first/later/never), and R1–R3 (the conditional rules) because they share the same load-bearing claim — "permission scales with risk" — and a system that violates one violates all.

**ONE CONCRETE TEST:** Take ADR-004's canonical "requires approval" list (L66–L75). For each item, is there a documented risk tier and the corresponding autonomy rung the system uses? ADR-004 has two intensities (Light/Full, L86, L99) but no risk tiers and no autonomy ladder; the L1–L4 rungs from L141 are not encoded anywhere. DavidOS partially satisfies Principle 6 — the canonical "requires approval" list (ADR-004 L66–L75) and the Light/Full distinction satisfy the gating half; the graduated-autonomy ladder is unrealized.

**TYPE:** Architectural.

### Principle 7 — Build around the binding bottleneck, not the most annoying feature

**STATEMENT:** "The correct automation target is rarely the most annoying task. It is the constraint that limits the entire system" (L126). "Build around bottlenecks, not features" (L129). David's seven candidate bottlenecks to diagnose first (L213): context retrieval, decision, evaluation, handoff, human review, tool fragmentation, prompt.

**WHY IT'S LOAD-BEARING:** This is the only principle in the set that governs sequencing — what to build next. Without it, David builds whatever is most visible (UI work, new agents, novel features — exactly Frustration 3's "this leads me to want to work on the UI or constantly reanalyze my priorities", charter L41) rather than what unblocks the system. It also protects against Failure Mode 9 "Confusing novelty with leverage" (L386). This is the operating principle that determines which of the architectural principles (1–6) gets attention this week. I merged P12 (build around bottlenecks) and P14 (the seven bottlenecks) because the seven are instances of the one; a list without the principle is just a checklist, and a principle without the candidate list is unactionable.

**ONE CONCRETE TEST:** Is there a current document in DavidOS that names which of the seven bottlenecks is binding right now, with evidence, and which is being worked on next? The repo's ADRs sequence decisions but do not name the binding bottleneck. As of this commit, no such document exists. DavidOS currently violates Principle 7 — explaining why progress feels diffuse (Frustration 3).

**TYPE:** Operating.

---

## 2. COVERAGE MATRIX

Charter outcomes from `outcomes-and-frustrations-2026-05-13.md` L13–L23:

- **O1** — Aligned with my goals always
- **O2** — Applies the optimal decision framework (well-architected: security, cost-optimized, reliable)
- **O3** — Actively self improves
- **O4** — Always stays current on information where it needs to be
- **O5** — Predicts problems and actively avoids them
- **O6** — Easy for me to use
- **O7** — Is inventive to help me achieve my goals
- **O8** — Always considers if and how I could make money from what I'm building
- **O9** — Loops me in on the decisions that matter
- **O10** — Evolves with me
- **O11** — Doesn't bullshit me

| Principle | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 | O9 | O10 | O11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **P1** Information architecture before agents |   | X |   | X |   | X |   |   |   | X |   |
| **P2** Named layers; no layer owns strategy |   | X |   |   |   |   |   |   |   |   |   |
| **P3** Strong router before more agents | X | X |   | X |   | X |   |   | X |   |   |
| **P4** Every workflow produces reusable assets |   |   | X |   |   |   |   |   |   | X |   |
| **P5** Evaluation; otherwise production volume |   | X | X |   | X |   |   |   |   |   | X |
| **P6** Graduate autonomy by risk |   | X |   |   | X |   |   |   | X |   |   |
| **P7** Build around the binding bottleneck | X |   |   |   | X |   |   |   |   | X |   |

**Outcome coverage counts:**
- O1: 2 principles (P3, P7)
- O2: 5 principles (P1, P2, P3, P5, P6) — **OVER-SPECIFIED**
- O3: 2 principles (P4, P5)
- O4: 2 principles (P1, P3)
- O5: 3 principles (P5, P6, P7)
- O6: 2 principles (P1, P3)
- O7: 0 principles — **UNCOVERED GAP**
- O8: 0 principles — **UNCOVERED GAP**
- O9: 2 principles (P3, P6)
- O10: 3 principles (P1, P4, P7)
- O11: 1 principle (P5) — **UNDER-COVERED**

---

## 3. GAPS, OVERLAPS, AND TENSIONS

### Gaps (charter outcomes with no principle serving them)

**O7 "Is inventive to help me achieve my goals"** — Zero principles serve this. David's principles are entirely about operational discipline (architecture, evaluation, risk gating). None describe how the system should generate novel suggestions, surface non-obvious moves, or propose options David didn't ask for. The principles document specifies how to execute well; the charter asks for inventiveness. This is the largest unaddressed gap.

**O8 "Always considers if and how I could make money"** — Zero principles serve this directly. The closest is Failure Mode 10 ("No economic model," L406) and Principle 4's reusable-asset list (which includes "distribution channel" and "product insight," L71), but no principle says "every workflow proposes a monetization angle" or "every output is evaluated against revenue potential." Given Frustration 2 (charter L37 — "i dont know where i should start where i can quickly begin making money") this is a notable gap.

**O11 "Doesn't bullshit me"** — Only P5 (evaluation/observability) serves this, and only obliquely (you can detect bullshit if you measure outputs). No principle codifies epistemic honesty: surfacing confidence, refusing to invent when uncertain, distinguishing "I don't know" from "the answer is." This is a critical gap given how much of David's frustration with AI tools comes from this category.

### Overlaps (outcomes served by 4 or more principles)

**O2 (optimal decision framework / well-architected) — served by P1, P2, P3, P5, P6 = 5 principles.** This is over-specified. David's principles are heavily weighted toward "the system makes good architectural decisions," which is partially redundant — five principles each contributing to the same charter outcome means consolidation pressure either on the principles or on the outcome (O2 itself bundles three sub-outcomes: security, cost, reliability).

No other outcome reaches 4.

### Tensions (principle pairs that pull against each other)

**T1: P3 (strong router first) vs. P7 (build around the binding bottleneck).** If the current binding bottleneck is not "routing" but, say, "evaluation" (P14 #3) or "tool fragmentation" (P14 #6), P7 says work on that bottleneck next. P3 says routing is the prerequisite for everything else and should come first. **Condition:** when the diagnosed binding bottleneck is downstream of routing. **Tradeoff:** prerequisite ordering (P3) vs. demand-driven ordering (P7). Resolution would require a tie-breaker rule David has not stated.

**T2: P4 (every workflow produces an asset) vs. P7 (build around the bottleneck).** P4 says every workflow contributes a reusable byproduct; P7 says focus on the binding constraint. If the binding bottleneck is decision latency (charter L325) and adding asset-production overhead to each workflow slows the workflow down, P4 makes the bottleneck worse. **Condition:** when the binding bottleneck is throughput/latency rather than learning. **Tradeoff:** long-term compounding (P4) vs. short-term unblock (P7).

**T3: P5 (evaluate everything important) vs. ADR-002 deliberate cost-blindness.** Not a tension between two principles, but worth surfacing: P5 requires logging cost per workflow (source L64); ADR-002 L18, L22 chose a billing path that hides per-call cost. Under P5 strict, ADR-002 is currently in violation. The tension is between Principle 5 and an existing accepted ADR — flagged because it has to be resolved before task 3's audit prompt can include a cost-observability check without being immediately self-defeating.

**T4: P6 (graduate autonomy by risk) vs. ADR-004 (two-intensity approval format).** P6 implies a four-rung autonomy ladder (source L132–L141); ADR-004 L86, L99 implements two intensities (Light/Full). Two intensities are a subset of the four-rung ladder, not a contradiction — but they are not yet a faithful implementation of P6. **Condition:** when David wants to operate at rung 3 ("execute and monitor outcomes," L137) without requiring approval. ADR-004 does not currently allow that. **Tradeoff:** full P6 fidelity (4 rungs) vs. ADR-004's bias toward gate-everything-on-the-canonical-list discipline.

**T5: P1 (information architecture first) vs. P7 (build around the bottleneck) — at the meta-level.** If P1 is itself the binding bottleneck right now (the test in Principle 1 shows DavidOS violates it), P7 and P1 agree. If a downstream bottleneck (say, prompt library) is binding, P7 says address it; P1 says you can't address it well without the information model first. Same shape as the P3/P7 tension. Resolution: P1 and P3 are both prerequisites in David's framing; P7 governs sequencing among non-prerequisites. David has not stated this explicitly.

---

## What was wanted verified before Task 3

Per Task 2's closing paragraph, four open verification questions before audit-prompt design:

(a) Whether 7 is the right cut — specifically whether P2 (named layers) and P3 (strong router) should collapse into one architectural principle.

(b) Whether the three gaps (O7 inventiveness, O8 monetization, O11 no-bullshit) are intentional omissions in David's source material or extraction losses.

(c) Whether the P3-vs-P7 sequencing tension has a tie-breaker David already holds tacitly.

(d) Whether the P5-vs-ADR-002 tension is one David wants resolved by revising ADR-002, softening P5, or some other path.

**David decision (2026-05-13 evening):** Let the audit propose resolutions to all four. These were encoded into the Task 3 audit prompt as §5 required output. See `2026-05-13-task3-audit-prompt-and-meta-analysis.md`.
