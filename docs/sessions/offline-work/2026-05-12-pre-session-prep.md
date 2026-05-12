# Pre-Session Prep — Offline Work Memo

**Date:** 2026-05-12 02:17 – 04:30 AM CDT
**Status:** Offline work. Pre-Atlas thinking. Not approved decisions. This memo is the primary pickup point for next official session.
**Purpose:** Capture tonight's framing work so the next session resumes precisely, with the pending direction decision held for fresh judgment.

---

## TL;DR for fresh-attention reading

Tonight's work surfaced that the original M6b plan (design an iZZi business planning workflow) needed multiple structural reframes. Each reframe sharpened the design. Late in the conversation, parallel research subagents returned findings that suggest a deeper structural pivot is warranted — but that decision deserved fresh judgment, so it was deferred to next session.

**The pending decision:** whether to (A) continue M6b as a project intake-to-handoff system, (B) pivot to substrate-first design that ships behavioral baselines for Atlas before any process work, or (C) hybrid. Research lightly favors B.

**Everything tonight is preserved.** No work is lost. Tomorrow's first decision is the direction; everything else cascades from it.

---

## What happened tonight

Started 2:17 AM with David's reframe of M6b: don't design the business planning workflow as a deliverable; design a process that produces good iZZi project decisions over time, with system-first / services-as-byproduct discipline. The system gets built and the business model emerges from it.

The conversation surfaced increasingly sharp framing through five exchanges:

1. **System-first reframe.** M6b shifts from "scope the consulting service" to "design the process by which projects move through DavidOS, of which consulting service emerges as a byproduct."

2. **Project taxonomy.** David surfaced that DavidOS will host both business-component and personal-system projects, with possible amend-mid-flight conversions. The process needs to handle both with type-specific overlays.

3. **Scope challenge.** David questioned whether the intake-to-handoff framing was the right area at all (vs. input-quality hardening, model selection, context engineering). The answer landed on reframing to a broader "intake-to-handoff system" that includes input quality as a first-class concern.

4. **Layer A/B/C distinction.** David clarified that "for a theoretical business, we would need a customer intake first." This surfaced three layers: A (David's project intake), B (iZZi customer onboarding), C (customer's project intake). Decision: stay in Layer A only; defer B/C explicitly with documented rationale.

5. **Registries, self-improvement, risk mitigation.** David pushed for portfolio awareness, additional registries, self-improvement, and current-best-practices research. Two research subagents spawned in parallel.

The research came back with findings that don't fully fit the framework we'd been building. That's where tonight stopped.

---

## What was decided tonight (held as pre-Atlas thinking, not approved decisions)

### Decision 1: Scope — Layer A only

**Decision:** Tonight's design work focuses on David's project intake-to-handoff system. Layer B (iZZi customer onboarding) and Layer C (customer's own project intake) are explicitly deferred.

**Rationale:**
- Layer B can't be designed well without Layer A being battle-tested. Customer-facing onboarding has to be backed by a real system, not an aspiration.
- Layer B has the most variability and the most learning required. Designing it now would over-fit to current assumptions about target customer, sales motion, pricing, and service shape — all of which mature from doing the work.
- The "build it for yourself, then commercialize" arc is one of the most reliable founder patterns. The founder is the highest-quality early customer.

**Downstream costs of this deferral (real but accepted):**
- Possible rework on Layer A data structures when Layer C bolts on. Mitigated by including implicit "owner" field in project records.
- Possible rework on agent governance for multi-tenancy. Mitigated by "designed for one tenant, structured for many" principle.
- Can't show prospects a polished onboarding funnel until later. Acceptable — early consulting customers will be sold on David's outcomes, not on a polished funnel.

### Decision 2: Project taxonomy — two categories with conversion mechanic

**Decision:** Two project types:
- Business-component (intends monetization or business value)
- Personal-system (no monetization intent)

Projects can convert between types mid-flight via two triggers:
- David declares (unilateral)
- Atlas proposes at checkpoint review (David approves)

**Rationale:**
- Three categories ("business-latent") was considered and rejected — it captures "we might monetize later" which is true of almost everything; adds noise.
- The conversion mechanic handles latent business potential without needing a third category.
- Portfolio-wide awareness applies at all times: the system considers the whole project portfolio, not just the project currently being intaken or worked on.

### Decision 3: Project lifecycle — different shape per type

**Decision:** Two lifecycle shapes:

**Personal-system project:**
```
Idea → Build → Use
```
No GTM phase, no checkpoints around business decisions.

**Business-component project:**
```
Idea → Planning → Build → Checkpoints → GTM evaluation
```
Lifecycle ends at GTM-decision (Shape B per the alignment question). Launch/operate are separate downstream processes. "The asset exists and is being used" is the strongest GTM signal, not a separate phase.

**Conversion mechanic:** If a personal-system project converts to business-component mid-build, the system retroactively injects the planning/checkpoint structure and surfaces what wasn't decided.

### Decision 4: Fork vocabulary — five concepts with reconciliation patterns

**Decision:** Five fork-related concepts, each with a defined reconciliation pattern:

1. **Fork** — one-way decision, expensive to reverse. Reconciliation: Full ADR-004 approval, often promoted to an ADR.
2. **Soft fork** — directional commitment that constrains future options but doesn't close them. Reconciliation: disclosure + Light approval. David can upgrade to full fork if intuition says so.
3. **Reversible** — everything else. Made freely; no approval required.
4. **Compound fork** — accumulation of related soft forks / reversible decisions that together become a fork. Reconciliation: full fork treatment applied retroactively to the cumulative path. Atlas's job to surface.
5. **Time-pressured fork** — decision that would be soft fork or reversible if there were time, but compressed timeline upgrades severity. Reconciliation: full fork with explicit time-pressure annotation; follow-up to revisit if circumstances allow.

**World-class properties this design targets:**
1. Identification is reliable (system actively names forks; Atlas's responsibility)
2. Reconciliation is proportional (no over-policing or under-policing)
3. Reconciliation is durable (decisions are retrievable; reasoning preserved)

### Decision 5: Multi-tenancy principle — "designed for one tenant, structured for many"

**Decision:** All substrate (registries, agent definitions, observation files) designed with implicit per-tenant scoping even though only one tenant (David) exists today.

**Application:**
- Registries get a `tenant_id` field (or YAML frontmatter equivalent) on every entry. Today it's always "david."
- Agent governance scoped to one operator today, but designed with option for multi-tenancy.
- Atlas observations register per-tenant (no cross-tenant aggregation by default).
- Self-improvement loops are per-tenant; one user's pattern recommendations don't bleed into another's.

**Rationale:** The cost of designing single-tenant in a multi-tenant-compatible way is near zero today. The cost of retrofitting multi-tenancy onto a single-tenant design is high. Decided to pay the small upfront cost.

### Decision 6: Self-improvement is a system tenet, not a section

**Decision:** Self-improvement gets elevated to foundational principle status alongside multi-tenancy. It's not narrowly scoped to risk mitigation (David's correction). It applies across:
- Quality (which artifacts produced strong outcomes)
- Efficiency (wasted steps, redundant context, faster paths)
- Calibration (confidence-vs-accuracy patterns)
- Pattern recognition (what kinds of decisions recur)
- Capability growth (what skills the system lacks)
- Aesthetic refinement (voice, format, level of detail)
- Risk mitigation (one application of self-improvement, not its parent)

**Vocabulary note:** Use "system tenet" or "foundational principle" — not "tenant" — to avoid collision with multi-tenancy terminology.

### Decision 7: Specialized lead agents — Business-Model Lead as clonable template

**Decision:** Two-layer agent model:

**Layer 1 (universal):** Atlas remains the project orchestrator across all projects, business or personal.

**Layer 2 (dimension-specific):** Specialized lead agents for dimensions that need deep attention. **Business-Model Lead is the first** Layer 2 dimension. Designed as a clonable template — other dimensions (Technical, Customer, Financial, Legal) inherit the shape when their dimensions need attention.

**Status:** Rough shape sketched, not full charter. Atlas designs the full charter next session (high-leverage Opus task).

---

## What the research returned

Two research subagents ran in parallel late in the session. Outputs saved to:
- `docs/atlas/research/registries-research-report.md` (529 lines)
- `docs/atlas/research/best-practices-research-report.md` (564 lines)

### Registry research — headline findings

**Hypothesis was 7 registries. Research refined to 8.**

Confirmed:
- Project Registry (exists, needs refresh — stale post-migration)
- Approvals Log (exists, strongest current design)
- Atlas Observations (proposed, validated)
- Customer-Zero Patterns (exists, correct shape)

Refined or added:
- **Decisions / Open Questions Register** — replaces proposed "Forks Register" as more foundational. Fork-type tracking folds in as a `fork_type` field. FamilyAI's `docs/product/08-decision-log.md` is the template (D-NNN format with Status, Decision Gate, Who Decides, Alternatives, Risks Accepted).
- **Agent Roles / Capabilities Register** — new, flagged as the repo's biggest single gap. Eight empty agent role stubs in `david-ai-workspace-v0.md`; the repo audit explicitly calls this out.
- **Tool Registry** — new (this overlaps with the best-practices research; see below).
- **Risks Register** — confirmed as proposed.

Hermes substrate concepts worth borrowing directly:
1. `MEMORY.md` / `USER.md` split (behavioral vs. factual)
2. Curator freshness signals (`last_run_at`, lifecycle states)
3. Context compressor handoff prefix ("reference only, not active instruction")
4. Skills lifecycle states for Customer-Zero Patterns
5. Insights engine categories for structured observations
6. Profiles isolation architecture as the multi-tenancy model

External patterns worth borrowing:
- Cursor Memory Bank's mandatory-read-list concept → `docs/atlas/session-start-substrate.md` manifest
- Google ADK's four-layer context stack (session / user / app / agent-memory)

Critical multi-tenancy finding: every registry entry needs a `source` field recording which session or agent created it. Cheap now, painful to retrofit.

### Best-practices research — headline findings

**The biggest gap in DavidOS is the absence of behavioral baselines for Atlas.** Without a regression suite, drift and reward hacking are invisible. Recommended: a **Charter Regression Suite** (10-20 canonical prompt/response pairs + LLM-as-judge) as the highest-ROI next action.

Top-3 ADRs recommended by the research:
1. **Charter Regression Suite ADR** — behavioral baselines for Atlas. Single afternoon to build, protects against drift / charter overshoot / specification gaming.
2. **Tool Registry ADR** — explicit "tool access contract" per capability with periodic tightening review. Tool/permission creep is structurally underestimated.
3. **Atlas Runbook** — respawn guide + behavioral contract + capability inventory in plain language a second operator could act on. AI succession problem is real (60-80% reconstruction cost when undocumented).

Other key findings:
- Self-improvement loops have demonstrated gains BUT the degeneration risk is also real (agent writes increasingly elaborate instructions to itself over time). Mitigation: never autonomous self-modification of the charter; always operator approval gate.
- Anthropic's published agent safety guidance (August 2025) explicitly endorses the patterns DavidOS already uses (approval gates, read-only defaults, allowlisting).
- Three un-named failure modes worth tracking: prompt injection via external data, MCP supply chain, agent termination failure.

### Where the two reports converge

- Both identify Agent Roles as critical missing substrate
- Both elevate Tool Registry to ADR-worthy
- Both emphasize multi-tenancy as a now-or-never design discipline
- Both validate the existing approval/ADR infrastructure as strong
- Both suggest the substrate work is more foundational than the process design

### Where they diverge (or where I need to reconcile)

- Registry research focuses on operating substrate (what Atlas reads)
- Best-practices research focuses on behavioral substrate (what Atlas IS verified to do)
- These are complementary, not contradictory. Both are needed.

---

## The deferred decision: A vs. B vs. C

**Question:** Given the research findings, how do we proceed?

### Option A: Continue M6b as planned
Finish the intake-to-handoff brief as scoped tonight. Atlas reviews. Best-practices findings fold into the brief's risk-mitigation section. Charter Regression Suite becomes an ADR-005 candidate that follows from the brief.

**Pro:** Uses tonight's framing work directly. No reframing cost.
**Con:** Designs process layer on weak Atlas foundation. Research suggests behavioral baselines should come first.

### Option B: Pivot to substrate-first
Tonight's framing becomes input to a NEW brief on "substrate Atlas needs to support any downstream system." Substrate items: charter regression, tool registry, registries (the 8 from research), observations loop, agent roles register. M6b moves to the session *after* substrate ships.

**Pro:** Matches what research surfaced as foundational. Substrate generalizes to iZZi customer-zero better than process-only. Stronger foundation for everything downstream.
**Con:** Tonight's framing work serves a different scope. Doesn't waste it but reframes it.

### Option C: Hybrid
One large brief covering both: intake-to-handoff system AS the framework, with substrate work as Phase 1 that must ship before any project flows through the framework.

**Pro:** Captures full shape with correct sequencing. Doesn't pivot scope.
**Con:** Bigger brief. Higher cognitive load on Atlas's review. May lose precision by combining two concerns.

### My (Computer's) recommendation: Option B
Reasoning:
- Research isn't ambiguous — both reports independently surface substrate gaps as more foundational
- Process design without behavioral baselines is unverifiable
- M6b doesn't go away; it gets stronger sitting on real substrate
- Substrate is also customer-zero generalizable — possibly more so than process design

But this is a structural decision and deserves fresh judgment.

---

## What's preserved and where

All artifacts in `/home/user/workspace/m6b-brief/` and `/home/user/workspace/m6b-research/` plus this memo. Committed to DavidOS at `docs/atlas/research/` (research reports) and `docs/sessions/offline-work/2026-05-12-pre-session-prep.md` (this memo).

Specifically:
- `docs/atlas/research/registries-research-report.md` — full registry research output
- `docs/atlas/research/best-practices-research-report.md` — full best-practices research output
- `docs/sessions/offline-work/2026-05-12-pre-session-prep.md` — this memo (the primary pickup point)
- `docs/sessions/NEXT-SESSION-OPEN.md` — updated to point here

Conversation transcript with full reasoning available in the session that produced this memo (Perplexity Computer history).

---

## Tomorrow's opening sequence

**Step 1 — Read this memo first.** Especially the "deferred decision" section.

**Step 2 — Make the A/B/C decision.** Or modify the options. This is the structural choice that shapes everything downstream.

**Step 3 — Optionally: routine ops first if context-loading helps.**
- Pull latest from GitHub (`git pull origin main`)
- Hermes update (`9a63b5f → e855825`) — routine, can do before substantive work
- Atlas charter update for ADR-004 — small paste-and-run

**Step 4 — Execute the chosen direction.**
- If A: continue drafting the intake-to-handoff brief with research findings folded in
- If B: draft the substrate brief (this is a new artifact, but tonight's framing decisions still apply to it)
- If C: draft the unified brief

**Step 5 — Atlas reviews under Opus.** Whatever's drafted, Atlas pressure-tests structurally. This is the explicit Opus budget moment.

---

## Open Atlas questions surfaced tonight (regardless of A/B/C direction)

These questions persist across options:

1. Should the "Agent Roles / Capabilities Register" use the existing `docs/workspace/agents/<name>.agent.json` pattern as the record format, or a different shape?
2. What's the right cadence for periodic Atlas Observations review? Monthly vs. quarterly vs. triggered-by-volume?
3. Should the Decisions / Open Questions Register live at `docs/decisions/open-questions.md` (sibling to approvals-log) or at the project level (per-project decision log following FamilyAI's pattern)?
4. Where does the Charter Regression Suite live? `docs/atlas/regression/`?
5. The 5-fork-concept vocabulary — does Atlas agree that "compound fork" and "time-pressured fork" earn their keep, or are they over-engineering?
6. Project-portfolio review cadence — what triggers it (volume? time? checkpoint)? Who initiates?
7. The Business-Model Lead Layer 2 agent — what's the activation rule? Always-on for business-component projects? Only at GTM evaluation phase? Per-checkpoint?

---

## What this memo does NOT do

- Make any approved decisions. Everything is pre-Atlas thinking.
- Commit to A, B, or C. That's tomorrow's first decision.
- Draft the actual substrate or framework. That's after the direction is chosen.

---

## Final note on tonight's process

This offline-work session validated the "AI-assisted research before commitment" pattern. The research surfaced a structural pivot we wouldn't have caught without it. The cost was ~2 hours of structured conversation + 20 minutes of parallel research. The output is significantly stronger than what would have shipped without it.

Worth codifying this pattern. Candidate addition for `docs/atlas/customer-zero-patterns.md` next session: "offline structured-conversation + parallel-research pattern" as a project-shaping technique.

---

*End of memo. Pickup point for next session: read TL;DR, make A/B/C decision, proceed.*
