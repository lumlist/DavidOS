# Future Conversation Flags

**Status:** Roadmap document for substantive design conversations David wants to have post-activation, captured during autonomy map population on 2026-05-14. These are not implementation specs — they are flagged topics that should not be lost between sessions.

**How to use:** When opening a substrate or post-audit work session, scan this file for any flag that aligns with the current work. Address the flag explicitly or note it as still pending.

---

## Flag 1: Memory observability and impact analysis (UI-level)

**Surfaced:** 2026-05-14, during autonomy map Category 8 review
**Context:** David asked whether a future UI could analyze and observe how memories are impacting the system

### The question

How can David see, in a future DavidOS UI, the impact of memory entries on Atlas's behavior over time? Specifically:

- Which memory entries are being referenced most often?
- Which memory entries are stale (never referenced)?
- Where has a memory entry shaped a recommendation — and was the recommendation better or worse for it?
- Can David spot memory entries that are biasing Atlas in ways he didn't intend?

### Why this matters

P5 (without evaluation you have production volume, not compounding) and P15 from David's design principles source (memory must be curated, not accumulated) both imply memory needs to be observable. Hermes's `memory_char_limit: 2200` is a curation discipline mechanism, but it doesn't surface *which* entries are paying off.

Memory observability is a self-improvement mechanism — the system improves how it curates by seeing which entries earn their place.

### What this requires

- Per-session logging of which memory entries were loaded and referenced (some of this already exists in Hermes session history)
- Cross-session aggregation of memory-entry citations
- A UI affordance for browsing memory entries with usage stats and impact assessment
- Potentially: Atlas-assisted "memory triage" — pruning suggestions based on observed usage

### When to address

After Phase 1 substrate lands (so there's enough Atlas operation to observe). Most likely Phase 2 or Phase 3 work. Not blocking on activation.

---

## Flag 2: Skill quality and external-skill discovery

**Surfaced:** 2026-05-14, during autonomy map Category 9 review
**Context:** David flagged that beyond Atlas creating skills, the system should ensure it implements the highest-leverage skills available, including skills built outside DavidOS or default in the Hermes architecture

### The question

How does DavidOS ensure that the skills Atlas operates with are the highest-leverage skills available, not just the skills Atlas happened to create? Three sub-questions:

- **Discovery:** Are there high-leverage skills built by others (in the Hermes ecosystem, in adjacent communities, in open-source repos) that DavidOS should adopt?
- **Assessment:** For skills already in DavidOS, how does Atlas evaluate whether each skill is performing well and how it might be improved?
- **Default skills:** The 26 default Hermes skills are present in Atlas's profile. Which are being used? Which are dead weight? Which should be customized for DavidOS purposes?

### Why this matters

P4 (every workflow produces a reusable asset) only delivers compounding if the assets are good. A workflow library that accumulates mediocre skills without quality discipline ends up with mediocre output. The principle requires both creation *and* curation.

This also intersects with the Karrigan intent (`2026-05-14-karrigan-intent-capture.md`) — Karrigan's stated functions include "conduct research/experiments to always be aware of the best tactics and strategies for operators and the tools/UI I'm engaging with." External skill discovery is one of those research areas.

### What this requires

- An external-skill awareness mechanism — Atlas or Karrigan periodically reviews what's available in adjacent ecosystems and proposes adoptions
- A skill-quality assessment loop — periodic review of installed skills against an evaluation rubric (which `davidos-evaluation` from Phase 1 may operationalize)
- A skill-improvement mechanism — Atlas proposes refinements to existing skills based on observed usage and failures

### When to address

This is likely Karrigan's territory more than Atlas's, given Karrigan's research-oriented role. Post-audit, after Karrigan's design begins. The skill-quality assessment piece (internal) might land earlier if `davidos-evaluation` includes it.

---

## Flag 3: Orchestration and infrastructure-level alternatives

**Surfaced:** 2026-05-14, during autonomy map Category 10 review
**Context:** David flagged that orchestration techniques themselves should be subject to the same continuous-improvement discipline — DavidOS should be assessing its own orchestration approach, borrowing from others, or changing infrastructure if warranted. Specifically named **Roo Code** as an alternative worth considering.

### The question

How does DavidOS ensure that the orchestration patterns it uses (subagent spawning, delegation hierarchy, multi-agent coordination, workflow orchestration) are the highest-leverage patterns available, not just the patterns we adopted at the time of setup?

- **Current orchestration:** Hermes provides subagent spawning, depth/concurrency limits, profile-based actors. Is this the right primitive set?
- **Alternative infrastructures:** Roo Code is one named alternative. There may be others (LangGraph, AutoGen, CrewAI, custom approaches). Which would serve David's goals better?
- **Borrowing:** Even within the Hermes substrate, are there orchestration techniques from other agent systems worth porting in?
- **Triggering infrastructure changes:** If a fundamentally better orchestration approach exists, what's the threshold for switching? (Recall the 20% productivity dip rule from the Nate Herk tech stack influence note — switching costs are real.)

### Why this matters

The substrate-first plan and ADR-001 committed to Hermes as the daily-driver runtime. That commitment was made with the information available at the time. It's tool-agnostic per SOUL.md Section 5 (P-tool-agnostic), but tool-agnostic doesn't mean "never reconsider" — it means "the choice is justified, and reconsideration is permitted with cause."

P7 (build around the binding bottleneck) implies the orchestration question should be revisited if orchestration becomes the binding constraint. Right now it's not — the binding constraint is substrate (autonomy, router, evaluation). But once Phase 1 lands and Karrigan exists, the bottleneck may shift.

### What this requires

- A periodic orchestration review (likely Karrigan's research function once he's built)
- Explicit criteria for "when to consider an infrastructure switch" — what evidence would cross the 20% dip rule
- Migration path scoping if a switch is warranted — DavidOS's repo-as-asset structure was designed exactly so the substrate survives a runtime change
- Specific evaluation of Roo Code and other named alternatives once Karrigan is operating

### When to address

Post-Karrigan. Karrigan's research function is the natural home for this kind of continuous-comparison work. Until then, the answer is "Hermes is fine, revisit when there's evidence to consider an alternative."

---

## How these three flags relate to each other

All three are **continuous-improvement mechanisms** for parts of DavidOS that are currently snapshot-in-time: memory at the entry level, skills at the workflow level, orchestration at the infrastructure level. They're variations of the same pattern — "the system should be aware of what's working and what's not, and propose improvements grounded in observation."

This pattern intersects strongly with the consolidated principle P5 (without evaluation you have production volume, not compounding) and with the future Karrigan agent's role.

**Suggestion for future design:** Consider whether all three flags should resolve into a single substrate item — a `davidos-self-improvement` skill or pattern that handles memory observability, skill quality assessment, and orchestration review on a recurring cadence. If they have enough in common to share infrastructure, building one mechanism is cheaper than building three.

---

## How to add new flags

When a future-conversation flag emerges in any session:

1. Append a new section to this file with the same structure (Flag N + headers)
2. Date it
3. Capture the original context (what was being discussed when the flag was raised)
4. State the question, why it matters, what it requires, and when to address
5. Commit so it's durable

Do not let flags accumulate in conversation only. They get lost between sessions.
