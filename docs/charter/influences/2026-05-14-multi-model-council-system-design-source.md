# Multi-Model Council Analysis on System Design Best Practices — Primary Source

**Captured:** 2026-05-14
**Source:** David Izzard, multi-model analysis (GPT-5.5 Thinking + Claude Opus 4.7 Thinking + Gemini 3.1 Pro Thinking) using the founder/operator framing prompt
**Status:** Primary source — do not paraphrase, do not summarize, do not edit
**Use:** Reference material for the 2026-05-14+ best-practices implementation audit. Compare against current DavidOS substrate (SOUL.md, action-map.md, modifiers.md, SCHEMA.md, ADRs) to identify what's already encoded, what's missing, what was lost in consolidation, and what's high-leverage to encode next.

**Related flag (per David):** Run this same multi-model council analysis for Karrigan's foundational principles — focus area: improving operator inputs (driving high-leverage UI improvements, prompt optimization, information triage, decision framing, time/energy management, organization, etc.).

---

## Original prompt

Respond like a founder/operator who has built scalable AI-native systems and companies. I want non-generic guidance for building highly efficient, productive, and compounding services or operating systems. Focus on leverage, architecture, operational design, automation strategy, information theory, bottleneck analysis, agent/workflow design, observability, evaluation, and organizational efficiency. Give me:

1. The core principles that matter most
2. The architecture pattern you would use for most AI-native systems
3. The highest leverage bottlenecks to diagnose first
4. The automation hierarchy: what to automate first, later, and never
5. The metrics that reveal whether the system is compounding
6. Common failure modes and how to avoid them
7. A practical checklist I can use before building any new system
8. A stronger version of this prompt for reuse

Avoid generic productivity advice. Be direct, opinionated, and operator-level.

---

## 1. Where Models Agree

| Finding | Evidence |
|---|---|
| Deterministic shell + probabilistic core (LLM inside a cage) ✓✓✓ | LLMs should reason; system owns state/permissions/routing/versioning. "Deterministic shell, probabilistic core". "Separation of cognition and execution". |
| Separate planner/executor/evaluator; avoid self-confirming loops ✓✓✓ | Role separation prevents self-validating automation. "Separate planner, executor, critic". Router-Actor-Critic pattern. |
| Evals are non-negotiable; define "good" before scaling ✓✓✓ | "No eval = no production" and rubric/factuality/diff checks. "Write the eval before the prompt". "Evals are your CI/CD". |
| Context quality (signal density) is a primary bottleneck ✓✓✓ | "Treat context as scarce…signal density". "Information density is the real KPI". "Context bloat (entropy) is the silent killer". |
| Risk/reversibility should dictate autonomy + approvals ✓✓✓ | Approval classes + risk taxonomy + gates. "Reversibility dictates autonomy". HITL thresholds and high-risk gating. |
| Observability + traces + replay are required for compounding ✓✓✓ | Need logs/traces/cost/latency/approval outcomes to improve. Structured traces + eval harness + budgets. Full DAG tracing + telemetry platforms. |

## 2. Where Models Disagree

| Topic | GPT-5.5 | Claude | Gemini | Why |
|---|---|---|---|---|
| Primary "first bottleneck" to diagnose | Decision latency + context assembly + rework | Eval coverage gap first | Context bloat + eval latency + HITL choke points | GPT-5.5 frames ops as queue/decision system; Claude frames reliability as eval substrate; Gemini frames performance/unit economics as context+eval runtime+HITL. |
| Default architecture emphasis | Governed event-driven OS with policy gate + memory steward + workflow runner | Router → specialist agents → tool layer → memory/eval substrate | Stateful Router-Actor-Critic DAG with explicit state machine backbone (e.g., Temporal) | All converge on layered systems, but differ on what is "the spine": policy/queue (GPT-5.5), specialist topology (Claude), workflow engine/state machine (Gemini). |
| What compounds most: tools vs workflows vs decision records | Workflow as durable unit; agents are replaceable | "Tools are the unit of leverage" | DAG + typed schemas + state transitions as core artifact | Different definitions of "asset": reusable workflow definitions (GPT-5.5), durable tools (Claude), hardened state transitions/contracts (Gemini). |
| Automation sequencing | Start with low-risk frequent tasks; then decision support; then supervised execution; then closed-loop optimization | Similar staging, but explicitly "automate the derivative, keep the integral human" | "Automate eval pipelines + state recovery early," delay dynamic tool selection/multi-agent negotiation | GPT/Claude prioritize business workflows; Gemini prioritizes infrastructure automation (schema validation/retries/evals) earlier to stabilize autonomy. |

## 3. Unique Discoveries

| Model | Unique Finding | Why It Matters |
|---|---|---|
| Claude Opus 4.7 Thinking | Memory split: episodic/semantic/procedural substrate | Helps you design "what sticks" vs "what replays" vs "what trains behavior." |
| Gemini 3.1 Pro Thinking | Idempotency-by-default as a first-class principle | Prevents duplicate side-effects under retries — critical once agents touch real systems. |
| GPT-5.5 Thinking | Queue discipline as the OS (tasks w/ SLA, dependencies, risk) | Without queue semantics, AI just accelerates chaos and approval thrash. |

## 4. Comprehensive Analysis

### High-Confidence Findings

All three models converge on the only architecture that scales in the real world: LLMs must be boxed into deterministic systems that own state, permissions, routing, versioning, and rollback. The practical implication is blunt: if your "agent" can directly interpret an ambiguous instruction and mutate production state, you don't have an AI-native system — you have a liability with a demo.

They also agree you should split roles to avoid self-approval (planner/executor/critic/governor/memory steward). GPT-5.5 explicitly calls out the self-confirming automation trap — one agent deciding, executing, and judging its own work. Claude reinforces the same separation as an anti-pattern against "orchestrator-as-god-object." Gemini bakes it into the Router-Actor-Critic DAG and insists the critic (or deterministic checks) validate outputs before downstream effects. Operationally: you're building a control loop, not an employee simulation.

The third strong consensus: evals are the compounding engine. Claude's "write the eval before the prompt" is the cleanest operator filter: if you can't test it, you don't understand it well enough to automate. GPT-5.5 goes further: "No eval = no production," with schema checks, diff checks, factuality gates, and accept/reject logging. Gemini frames evals as CI/CD and warns against "vibe-based" prompting, plus highlights eval latency as a scaling killer. The net: your competitive advantage is not model choice; it's measurement + iteration velocity.

Finally, all models treat context as an information theory problem: maximize signal density, minimize entropy, and aggressively control what enters the prompt. If you get this right, smaller/cheaper models often outperform bigger ones because the system is feeding them clean, scoped decision payloads.

### Areas of Divergence

The main divergence is where to start diagnosing bottlenecks. GPT-5.5 starts from the founder constraint: decision latency, rework, approvals, and tool friction. Claude starts from the production constraint: eval coverage — if you can't measure correctness, nothing else matters. Gemini starts from the scaling constraint: context bloat, eval runtime, and HITL choke points — because those dominate cost and throughput once volume rises. These aren't contradictions; they're different "first cuts" depending on what's currently breaking: business cadence (GPT-5.5), reliability/quality (Claude), or unit economics/throughput (Gemini).

They also differ on the "primary compounding asset." GPT-5.5 argues the durable abstraction is the workflow (agents are interchangeable workers). Claude argues durable leverage is tools (prompts churn; tools compound). Gemini argues durable leverage is the state machine + typed contracts (schemas + idempotent transitions make everything debuggable and safe). In practice, you want all three, but sequencing matters: start with contracts + workflow skeleton, then invest in tools where there's repeated friction, and finally productize the workflow library as your internal "capability catalog."

### Unique Insights Worth Noting

Claude's episodic/semantic/procedural memory split is a useful mental model for governance: episodic traces are for replay/debug, semantic is for retrieval, procedural is for "how we do things here." Gemini's idempotency emphasis is the difference between "works in a sandbox" and "safe under retries and partial failures," especially once you have tool tail latency and cascading retries. GPT-5.5's queue-discipline framing is the operator reality: if your system can't say what's blocked, what's high-risk, what needs approval, and what recurs, it will amplify noise into burnout.

### Recommendations

Build a governed workflow engine where every run produces: (1) an artifact, (2) a trace, (3) an eval result, and (4) a candidate improvement (memory/policy/workflow/tool) that must pass a gate before becoming canonical. Start with Level-1/2 autonomy (draft + sandbox), enforce idempotency, instrument everything, and only then graduate workflows to supervised execution and selective auto-execution based on reversibility + eval pass thresholds.

---

## (1) Core principles that matter most (operator version)

- **Deterministic spine, probabilistic edges.** Code owns state + side effects; LLMs own reasoning.
- **Evals-first.** If you can't test "good," you can't automate it.
- **Context is a budget.** Optimize signal density; aggressively exclude noise.
- **Separate judgment from execution.** Planner/executor/critic/governor/memory steward.
- **Reversibility drives autonomy.** Two-way door = automate; one-way door = gate.
- **Compounding or it doesn't ship.** Every run must improve future runs (evals, artifacts, tools, policies).

## (2) Architecture pattern I'd use for most AI-native systems

A stateful, event-driven workflow DAG: Intake → Router/Policy → Context Builder → Specialist Steps (planner/actor) → Evaluator/Critic → Action Gate → Tool Executor → Observability → Memory/learning curator.

Make workflows the unit of ownership; enforce typed I/O; run everything through gates.

## (3) Highest leverage bottlenecks to diagnose first

- Eval coverage + eval latency (can you measure + iterate fast?).
- Context assembly cost / entropy (how often you re-brief; how much junk you pass).
- Rework rate (accept/edit/rewrite/discard by workflow).
- HITL placement + approval load (are humans reviewing too late?).
- Tool tail risk (P95/P99 failures/latency causing retry cascades).
- Decision logging quality ("why" captured, not just "what").

## (4) Automation hierarchy (first / later / never)

- **Automate first:** bounded, repetitive, low-risk + infrastructure that stabilizes everything (schema validation, retries, eval runners, routing, extraction).
- **Automate later:** decision support + drafting with explicit rubrics + approval gates.
- **Automate cautiously:** supervised execution (customer-facing or write actions) with reversibility + confidence thresholds.
- **Never fully automate:** accountability domains — strategy, irreversible commitments, sensitive comms, security/financial actions without hard gates.

## (5) Metrics that reveal compounding

- Cost per accepted outcome (not per run).
- Autonomy rate / autonomous resolution rate (end-to-end without HITL).
- Human correction + rework loop count trending down per workflow.
- Decision cycle time (signal→decision→action→feedback) trending down.
- Memory hit rate + memory precision (useful retrieved / retrieved).
- Eval pass rate on frozen golden set trending up.
- Data flywheel velocity: failures → labeled cases → new evals → improved routing/prompt/tool.

## (6) Common failure modes + how to avoid

- **God agent / god prompt** → decompose into typed steps; enforce schemas.
- **No eval layer** → treat evals as CI/CD, ship only behind gates.
- **Memory poisoning** → curated writes + promotion rules; aggressive forgetting.
- **Context obesity** → retrieval + summarization + strict context budgets.
- **Agent sprawl** → no agent without contract, owner, eval, kill switch.
- **Infinite loops / runaway cost** → max-depth, budgets, fallbacks, circuit breakers.
- **Over-broad tool permissions** → least privilege + dry-run + audit + rollback.

## (7) Practical pre-build checklist (use before any new system)

- **Purpose:** what bottleneck, what decision/action, what "done"?
- **Examples:** ≥20–50 real I/O examples collected.
- **Contracts:** strict input/output schemas + state transitions defined.
- **Evals:** runnable rubric + golden set + failure mining plan.
- **Risk:** reversibility classes + approval gates mapped.
- **Idempotency:** retries won't duplicate side effects.
- **Observability:** traces, costs, prompts, tool calls, replay, versioning.
- **Autonomy level:** start L1/L2; criteria to graduate to L3/L4.
- **Kill switch:** token/time/tool-call budgets; disable path.
- **Compounding loop:** what gets better after every run (eval/memory/workflow/tool)?

## (8) Stronger prompt for reuse

> Act as a founder/operator who has built scalable AI-native workflow systems in production. I'm building [system] to achieve [throughput/latency/cost] under constraints [team/budget/risk]. Assume LLMs are stochastic; I want a deterministic control plane.
>
> Deliver:
> - Non-negotiable principles (compounding, information density, evals-first, reversibility/autonomy).
> - Reference architecture diagram (intake → router/policy → context builder → planner/actor → critic/evals → gate → tools → logs → memory curator), including state model + idempotency strategy.
> - Bottleneck diagnosis order with the exact measurements to take first week.
> - Automation roadmap (now/next/later/never) tied to risk classes + rollback.
> - Compounding metrics with target trajectories.
> - Failure modes + counter-patterns (agent sprawl, memory poisoning, eval theater, context obesity).
> - Pre-build checklist + "do-not-build-unless" filter.
>
> Style: direct, opinionated, production-grade; include schemas, gates, and budgets.
