# Audit Preparation — Task 1: Reconstruction and Critique

**Produced by:** Claude Opus 4.7 (via Computer)
**Date:** 2026-05-13 evening CDT
**Status:** Preparation artifact for the 2026-05-13 structural audit.
**Purpose:** Reconstruct the structure of David's design-principles source (extracted from a binary `.one` file with partial order loss) and surface internal inconsistencies and conflicts with the existing DavidOS charter and ADRs.

**Inputs:**
- `docs/charter/davidos-design-principles-source-2026-05-13.md` (verbatim OneNote extraction)
- `docs/charter/outcomes-and-frustrations-2026-05-13.md` (charter primary source)
- The four foundation ADRs in `docs/decisions/`

**Output structure:** Two sections — (1) Reconstructed Principles, organized into PRINCIPLES / PATTERNS / RULES; (2) Critique, covering internal inconsistencies, things implied but not named, and conflicts with the existing DavidOS charter and ADRs.

**Decision on ambiguities:** David and Sonnet/Computer reviewed Task 1 on 2026-05-13 evening and decided to proceed to Task 2 without pre-resolving the 5 flagged ambiguity items. Per Task 2 framing, ambiguities can be resolved in consolidation or surfaced to the audit. See `docs/audits/preparation/2026-05-13-task2-consolidated-principles.md`.

---

## 1. RECONSTRUCTED PRINCIPLES

Method note. The source has ~33 OneNote page timestamps acting as section dividers. Most page titles (e.g. "Make Every workflow observable", "Design for trust gradients") appear once or twice immediately after a timestamp; bodies are then scattered. I grouped each fragment under the title whose semantic neighborhood it fits. Where two fragments could plausibly belong to two sections, I flag with [AMBIGUOUS]. I do not paraphrase; quoted lines are verbatim with line numbers from `davidos-design-principles-source-2026-05-13.md` (hereafter "source").

I distinguish the three kinds the task asks for. David's source itself does not label them — this categorization is mine, applied conservatively: a fragment that names a single conditional action is a RULE; a fragment that names a structural commitment with cascading implications is a PRINCIPLE; a fragment that names a reusable shape (layers, command-center, intensity tiers) is a PATTERN.

### A. PRINCIPLES (structural commitments)

#### P1 — Information architecture is the foundation

"The system is only as good as its information architecture" (source L32)

"Most AI-native systems fail because the builder focuses on agents, prompts, automations, or interfaces before defining the information model." (L28)

"If those primitives are weak, everything becomes chat history soup." (L29)

"A strong AI-native system has clear primitives:" (L30) — David then enumerates the primitives. Reconstructed list (drawn from scattered lines L23–L36):

- "Raw messages, documents, data, screenshots, calls, user actions" (L35)
- "Current status of projects, workflows, goals, tasks, constraints" (L33)
- "Durable knowledge the system should remember" (L24)
- "Outputs worth reusing: docs, code, SOPs, templates, datasets" (L23)
- "Rules for routing, automation, risk, cost, security, quality" (L25)
- "Evidence of whether outputs were good" (L27)
- "Human or system-generated corrections" (L36)
- "Explicit choices with rationale and tradeoffs" (L31)

The framing question: "What information enters the system, how is it classified, where does it live, who or what can act on it, and how does it improve future decisions?" (L26)

[AMBIGUOUS: L34 "The highest-leverage question is:" sits in this section but its body — "What would this look like if it operated 10x larger with 90% less human involvement" (L40, L43) — is duplicated under the Highest Leverage Question section below. The "highest-leverage question" phrase may have been authored twice with two different meanings, or strings placed the same line in two pages.]

#### P2 — The highest-leverage question

Title appears as both "The Highest Leverage Question" (L42) and "The Highest Leverage Questions" (L45). [AMBIGUOUS: singular vs plural — likely the same section retitled.]

Body, stated twice: "What would this look like if it operated 10x larger with 90% less human involvement" (L40, L43). The two statements are identical; the duplication is almost certainly extraction noise, not two distinct ideas.

#### P3 — Prefer workflows before autonomy

Title: "Prefer workflows before autonomy" (L68)

No body content appears under this exact title in the source. [AMBIGUOUS: section header without retrievable body — the body may be among the unattributed bottleneck/automation-hierarchy fragments. Closest semantic neighbors: "Agents should operate inside workflows. Workflows should improve over time." (L164); "Start with recommendations and drafts. Move to execution only when the workflow is stable, reversible, and measurable." (L365). These read like the missing body but cannot be confirmed without the .one file.]

#### P4 — Design for compounding assets

Title appears twice: L70, L73.

"Every run should improve one of these: dataset, prompt, SOP, evaluation rubric, customer profile, knowledge base, automation rule, product insight, or distribution channel." (L71)

"If usage does not make the system smarter or more valuable, it is not compounding." (L71, continued)

#### P5 — Exploit Parallelism

Title appears twice, both with David's spelling "Parallellism": L75, L77.

[AMBIGUOUS: title with no body in the extraction. No nearby orphan lines obviously belong here.]

#### P6 — Turn tacit expertise into operating code

Title appears twice: L79, L82.

"Capture how an expert thinks: their filters, thresholds, disqualifiers, escalation rules, taste, examples, and anti examples." (L80)

"The moat is not the prompt. The moat is encoded judgment plus proprietary context plus feedback data." (L80, continued)

#### P7 — Build a strong router before building more agents

Title appears twice: L84, L87.

"A strong router decides: what type of work is this, what context is required, what tool should handle it, what risk tier applies, what output format is needed, and what approval is required." (L85)

"Routing quality determines system quality." (L85, continued)

#### P8 — Measure leverage with a blunt formula

Title appears twice (L89, L93). L89 also runs the title together with a parenthetical: "Measure leverage with a blunt formula | If a system saves time once, its an automation, if it improves each time it runs, it is infrastructure".

Formula: "Leverage = business value created / human attention required" (L90–91, reconstructed from the two-line fragment).

Restated body: "If a system saves time once, it is automation. If it improves every time it runs, it is infrastructure." (L94). This is the same idea as L89, expressed twice with slightly different phrasing — apparent duplication noted.

#### P9 — Optimize for decision velocity, not task volume

Title: "Optimize for decision velocity, not task volume" (L96)

"A bad system helps you complete more tasks." (L95)

"A good system makes the right tasks obvious." (L100)

"A great system makes many decisions unnecessary because the right action is already encoded in the operating model." (L98)

"The most valuable systems compress the time between:" (L102) — followed by three items: "noticing something," (L101), "deciding what to do," (L97), "learning from the result." (L103).

#### P10 — Every workflow should produce reusable assets

Title: "Every workflow should produce reusable assets" (L104)

"If a workflow only produces the immediate output, it is labor." (L108)

"If it also produces a better prompt, checklist, dataset, routing rule, reusable template, SOP, evaluator, or automation, it is compounding." (L116)

"For every workflow, ask:" (L106) → "What should this create that makes the next similar workflow faster or better?" (L110)

"Compounding byproduct" examples (L111) — David lists exemplar byproducts scattered across L105–L117:

- "Reusable research protocol" (L105)
- "Persona-specific messaging library" (L107)
- "Regression test and diagnostic script" (L109)
- "Customer support reply" (L112)
- "Feature evaluation rubric" (L113)
- "Triage classifier and response template" (L115)
- "Market research memo" (L117)

[AMBIGUOUS: "Customer support reply" (L112) and "Market research memo" (L117) read as immediate outputs, not compounding byproducts; David may have intended these as examples of the immediate output paired with the compounding byproduct (e.g., "customer support reply" → "Triage classifier and response template"). The extraction order is not reliable enough to confirm the pairing.]

#### P11 — Use AI where ambiguity is high and software where repeatability is high

Title (L120). David then lists where each belongs:

- AI: "reasoning under uncertainty" (L118)
- Software: "Use deterministic software for:" (L122) → "repeatable business logic" (L121)

"This is one of the most important operating rules." (L119) — David flags this principle as one of his most important.

#### P12 — Build around bottlenecks, not features

Title (L129).

"The correct automation target is rarely the most annoying task. It is the constraint that limits the entire system." (L126)

"Typical bottlenecks:" (L130):

- "too much human review" (L131)
- "no feedback loop after execution" (L125)
- "inconsistent quality standards" (L127)

"Where does throughput, quality, or learning degrade?" (L124) — diagnostic prompt

[AMBIGUOUS: only three bottleneck examples are present in the L124–L131 cluster. The later "Highest-leverage bottlenecks to diagnose first" section (P14 below) enumerates seven; these may be the same list scrambled, or two distinct lists. I treat them as two distinct sections because P14 has its own explicit title.]

#### P13 — Design for trust gradients

Title (L140).

"Not all automation should have the same permission level." (L135)

"The mistake is either giving agents too much autonomy too early or keeping everything in manual review forever." (L133)

"Use graduated autonomy:" (L139) → ladder of actions, reconstructed (the ordering in the source is scrambled but the verbs progress in escalating autonomy):

- "Execute low-risk reversible actions" (L132)
- "Execute within predefined policy limits" (L136)
- "Execute and monitor outcomes" (L137)
- "Redesign its own workflow with approval" (L138)

"Most systems should live between L1 and L3 for a long time." (L141) — implies the ladder above is L1–L4. The L1–L4 labels themselves are not present in the extraction. [AMBIGUOUS: I have inferred the ladder ordering. David may have intended a different order.]

#### P14 — Highest-leverage bottlenecks to diagnose first

Title (L213). This is a meta-principle: David enumerates seven bottlenecks and, for each, gives symptoms and remedies. The seven (numbered by David himself):

- "Context retrieval bottleneck" (L199)
- "Decision bottleneck" (L271)
- "Evaluation bottleneck" (L236)
- "Handoff bottleneck" (L246)
- "Human review bottleneck" (L227)
- "Tool fragmentation bottleneck" (L255)
- "Prompt bottleneck" (L242)

Because lines for each bottleneck are interleaved, I cluster symptoms vs. remedies by best fit. Confidence in groupings is medium; the cluster boundaries are not fully recoverable from strings output.

**1. Context retrieval bottleneck (L199)** — symptoms cluster:
- "You paste screenshots, logs, or instructions repeatedly." (L206)
- "You repeatedly re-explain goals, preferences, project state, or prior decisions." (L233)
- "Agents or tools lose context between steps." (L238)
- "Context is not assembled before work starts." (L239)
- "Work restarts instead of continues." (L214)

High-leverage question: "What information does the system keep asking me for that it should already know?" (L237) [AMBIGUOUS: one of L195/L237/L263 is the "High-leverage question" stub (L195, L263) — both occurrences appear without a tagline body in their immediate cluster; L237 is the likely body for one of them.]

Remedies: "Maintain current operating context per project." (L218); "Create project state files." (L264); "Separate workspace from system of record." (L221); "Use agents to sync, summarize, and reconcile state." (L225).

**2. Decision bottleneck (L271)** — symptoms:
- "Work stalls because every next step requires human judgment." (L258)
- "You spend time deciding what to do rather than doing it." (L243)
- "The system gives options but not recommendations." (L241)
- "No default operating principles." (L240)
- "No decision policy." (L267)
- "No risk tolerance model." (L268)
- "No escalation rules." (L266)

Remedies: "Define decision rights." (L265); "Encode reversible vs irreversible action policies." (L249); "Use confidence thresholds." (L209).

**3. Evaluation bottleneck (L236)** — symptoms:
- "Lots of outputs, unclear quality." (L228)
- "No comparison against prior output." (L253)
- "No regression tests." (L252)
- "No feedback capture." (L234)
- "Same mistakes recur." (L245)
- "You do not know which agents, prompts, or workflows work best." (L222)
- "No automatic prompt improvement." (L216)

High-leverage question: "How do we know this output was good besides vibes?" (L230)

Remedies: "Add output rubrics." (L200); "Track error categories." (L250); "Run periodic workflow audits." (L247); "Compare first draft vs final accepted draft." (L197).

**4. Handoff bottleneck (L246)** — symptoms:
- "No standardized handoff packet." (L224)
- "No workflow checkpointing." (L256)

Remedies: "Every agent handoff should include:" (L254) → "next recommended action" (L261). [AMBIGUOUS: David's handoff-packet contents are clearly truncated. Only "next recommended action" is recoverable as a handoff-packet element. Other elements may be among orphan lines L171–L185.]

**5. Human review bottleneck (L227)** — symptoms:
- "You are still approving everything." (L215)
- "The AI produces drafts, but you remain the integration layer." (L257)

High-leverage question: "What percentage of human reviews materially change the output?" (L231)

Remedies: "Identify low-risk reversible actions." (L220); "Let the system execute those." (L223); "Keep high-impact actions gated." (L201); "If review rarely changes the result, automate more." (L229); "Track where review changes outcomes." (L219).

**6. Tool fragmentation bottleneck (L255)** — symptoms:
- "Work is spread across chat, docs, Notion, GitHub, Slack, email, dashboards, and local files." (L244)
- "No single system knows what is true." (L270)
- "No canonical source of state." (L269)
- "Tools are integrated cosmetically, not operationally." (L212)
- "The system does not have durable, queryable memory." (L211)

Remedies: "Define source-of-truth hierarchy." (L203); "Do not let every tool become a memory layer." (L226).

**7. Prompt bottleneck (L242)** — symptoms:
- "The operator has to be a prompt engineer every time." (L202)
- "The operator should not have to remember the best way to ask." (L262)
- "No workflow-specific templates." (L232)

Remedies: "Build a prompt router." (L248); "Convert recurring prompts into reusable workflows." (L235); "Save examples of excellent outputs." (L210); "Store prompts that produced high-quality outputs." (L259).

[AMBIGUOUS: cluster boundaries between #2 Decision, #5 Human review, and #6 Tool fragmentation overlap. Several lines (e.g. L204 "No automation tiers." / L205 "No clear distinction between low-risk and high-risk actions.") could belong to either #2 or #5.]

#### P15 — Memory must be curated, not accumulated

Title (L142).

"The worst AI systems remember everything and understand nothing." (L144)

Curation test: "Will this materially improve future decisions or execution?" (L143) → "If not, it is noise." (L145)

"Memory should be structured into:" (L148) — David's memory-type list, reconstructed from scattered orphan lines (medium confidence):

- "durable user preferences" (L159)
- "current constraints" (L163)
- "relevant project state" (L184)
- "applicable policies" (L178)
- "Prompts, checklists, templates" (L146)
- "examples of good outputs" (L182)

"Every durable memory should answer:" (L149): "What decision was made?" (L166), "What rule should be updated?" (L160), "What artifact should be saved?" (L181), "What should be easier next time?" (L191), "whether memory should be updated" (L193).

"It is context compression." (L157)

[AMBIGUOUS: L146 "Prompts, checklists, templates" plausibly belongs to either P15 (memory types) or P10 (reusable assets).]

#### P16 — Standardize decision interfaces

Title (L39).

[AMBIGUOUS: title with no clearly attributable body. The lines best matching this concept are P7's router enumeration (L85), the "minimum viable context" enumeration under P19 (L161, L177), and the handoff packet under P14 #4. David may have intended "decision interfaces" as the umbrella that contains the router, the handoff packet, and the approval format — but this is inference, not extraction.]

#### P17 — Use AI / Use software (operating rule emphasis)

Already captured under P11. David explicitly flags it: "This is one of the most important operating rules." (L119) — I record the emphasis here so it isn't lost.

#### P18 — Build Evaluation Systems Early

Title (L485, isolated at end of extraction).

[AMBIGUOUS: title appears as a trailing fragment with no attached body. The body is almost certainly distributed across the Evaluation bottleneck cluster (#3 in P14) and the "Failure mode 4: No evaluation loop" cluster in the Failure Modes section below. I do not invent a body.]

### B. PATTERNS (reusable design shapes)

#### Pattern 1 — Four-layer architecture (Input / Reasoning / Execution / Learning)

Title (with typo): "Separate the system into 4 layers: Input, Reasoning, Execution. Learning" (L47). Restated: "Separate the system into layers: Input, Reasoning, Execution. Learning" (L49). Both versions of the title appear; the periods before "Learning" are likely extraction noise from strings.

Motivation: "Most people build one giant agent that tries to do everything. That creates brittle, opaque systems." (L50)

"System: Use this architecture:" (L53)

Layer responsibilities:

- "Input layer: capture demand, data, context, intent" (L58)
- "Reasoning layer: classify, plan, decide, recommend" (L61) — also "Diagnose, reason, plan, evaluate tradeoffs" (L55)
- "Execution layer: take action through tools, APIs, workflows" (L52) — also "Use tools, APIs, scripts, browsers, email, calendar, code" (L51)
- "Learning layer: evaluate outcomes, update rules, improve prompts, improve routing" (L54)

Cross-cutting layers (orphan lines reading as additional layers):

- "Score quality, risk, completion, confidence" (L48) — evaluation cross-cut
- "Help the operator make decisions quickly" (L57) — operator-interface cross-cut
- "Preserve durable knowledge and state" (L59) — memory cross-cut

Anti-patterns: "Do not let the execution layer own the strategy. Do not let memory become an unfiltered dump. Do not let the interface become the system." (L60)

#### Pattern 2 — Command-center architecture / Reference architecture / Five essential subsystems

Titles (likely the same section under three names): "The architecture pattern I would use for most AI-native systems" (L150), "Reference architecture" (L154), "The five essential subsystems" (L194).

"Not a chatbot. Not a pile of automations. Not a monolithic agent." (L151)

"I would use a command-center architecture with specialized agents, durable memory, workflow orchestration, evaluation, and human control points." (L153)

The five subsystems, with letters David assigned:

- A. Intake / classification — "The intake layer should classify every request before work begins." (L192) [AMBIGUOUS: David labels B/C/D/E but A is implicit; intake is the most likely A based on the surrounding text.]
- B. Context assembly system (L169)
- C. Workflow orchestration system (L167)
- D. Evaluation system (L170)
- E. Memory and learning system (L174)

Intake classifier (under A): "whether this is a new workflow or existing workflow" (L175), "whether web or internal files are needed" (L173), "whether human approval is required" (L171). "This prevents the system from treating every request like generic chat." (L187). "This alone dramatically improves AI system reliability." (L196).

Context assembly (under B): "Before an agent acts, it should assemble the minimum viable context:" (L177). "Give the agent the smallest context package that preserves decision quality." (L161). Components include "applicable policies" (L178), "relevant project state" (L184), "current constraints" (L163), "durable user preferences" (L159), "examples of good outputs" (L182).

Workflow orchestration (under C): "Agents should operate inside workflows. Workflows should improve over time." (L164). "Do not let every agent improvise the process." (L183). Each workflow specifies "by which agent/tool," (L190), "with what evaluation criteria." (L158), "with what approval gates," (L186), "with what retry logic," (L189).

Evaluation (under D): "Every important output should be evaluated against explicit criteria." (L155). Evaluation criteria scattered: "audience fit, clarity, persuasion, compliance" (L165), "source quality, freshness, contradiction handling" (L172), "clear thesis, evidence, tradeoffs, next actions" (L176), "reliability, reversibility, observability, cost" (L179), "passes tests, low complexity, secure, maintainable" (L180), "context use, correctness, actionability, risk handling" (L185). "Without evaluation, you do not have compounding. You have production volume." (L168).

Memory and learning (under E): "After each meaningful workflow, the system should ask:" (L156) → "What decision was made?" (L166), "What rule should be updated?" (L160), "What artifact should be saved?" (L181), "What should be easier next time?" (L191). "This is where the system compounds." (L162). "Store decisions separately from notes." (L198).

[AMBIGUOUS: "The five essential subsystems" (L194) might be a separate section from "Reference architecture" (L154); I have merged them because they share the same A–E enumeration vocabulary and no other subsystem list appears.]

#### Pattern 3 — Automation hierarchy: first / later / never

Title: "Automation hierarchy: what to automate first, later, and never" (L299).

**Automate first: context, routing, formatting, and low-risk execution** (L277)

"These are the highest ROI because they reduce friction without creating much risk." (L310)

"These are leverage multipliers because they reduce cognitive switching." (L286)

Examples (scattered): "lead prioritization" (L289), "handoff packet generation" (L290), "meeting/document summarization" (L292), "project state updates" (L295), "duplicate detection" (L298), "recurring workflow setup" (L300), "customer support triage" (L302), "customer segmentation" (L303), "market research synthesis" (L305), "low-risk notifications" (L278).

**Automate second: judgment-assisted workflows** (L273) — heading.

David then says: "Here the AI should recommend, draft, rank, and explain." (L275); "The human should approve, refine, or reject." (L284); "AI can generate options and surface tradeoffs." (L281); "The operator owns judgment." (L287); "These require evaluation, not blind execution." (L297).

"Automate with review:" (L307) — likely the same list, restated.

Examples: "sales messaging personalization" (L301), "financial modeling assumptions" (L291).

**Automate later: actions with external consequences** (L315)

"Do this only after the system has policies, logs, approval gates, and rollback paths." (L311)

Examples: "outbound sales at scale" (L312), "changing production code" (L294), "access/permission changes" (L282), "financial transactions" (L280), "customer-facing decisions" (L285).

**Never fully automate: values, taste, irreversible bets, and accountability** (L279)

"Do not fully automate:" (L306)

"A strong system makes judgment easier, not absent." (L313)

Examples: "security-critical approvals" (L274), "legal/compliance pre-checks" (L276), "major hiring/firing decisions" (L288), "founder conviction decisions" (L304), "brand-defining creative direction" (L308), "relationship-sensitive communication" (L309), "company positioning" (L314), "final product taste" (L283), "large financial commitments" (L296), "agent workflow modifications" (L272).

[AMBIGUOUS: "agent workflow modifications" (L272) sits at the top of the cluster — could be a "never" example or a heading fragment for the whole section.]

#### Pattern 4 — Compounding metrics

Title: "Metrics that reveal whether the system is compounding" (L338). Section also titled "Core compounding metrics" (L342) and "My favorite operator metric" (L337) and "Another useful metric" (L354). Possibly four micro-sections collapsed into one extraction page.

Framing: "Most people measure activity. That is a trap." (L324); "You want metrics that show whether future work is becoming easier, faster, better, and less dependent on the operator." (L351); "If you create 20 outputs and 0 reusable assets, you are using AI as labor." (L326); "If you create 20 outputs and 8 reusable assets, you are building a system." (L331).

Named metrics (definitions verbatim):

- "Compounding ratio = reusable assets created / one-time outputs created" (L343)
- "Operator lift = percentage of workflow completed before human intervention" (L340) — David calls this "My favorite operator metric" (L337). Targets: "For early systems, 20 to 40 percent is good." (L344); "For mature internal systems, 60 to 80 percent is possible." (L330); "For external-facing high-risk systems, the safe number may be lower." (L334).
- "Decision latency = time from new information arriving to recommended action" (L325) — "Great operating systems reduce decision latency dramatically." (L353)
- "Context tax = minutes spent re-explaining known information per workflow" (L321) — "This should trend toward zero." (L345). David calls this "Another useful metric" (L354). [AMBIGUOUS: "Another useful metric" may instead refer to Context tax or Decision latency — both follow the "favorite metric" label in the extraction.]
- "Time to useful first draft" (L322)
- "Cycle time per workflow" (L350)
- "Marginal cost per output" (L347)
- "Human correction rate" (L318)
- "Error recurrence rate" (L320)
- "Approval bypass rate" (L349) — "This is a brutal but powerful metric." (L348)
- "Decision trace completeness" (L329)

Diagnostic questions (David's checklist for whether the system is compounding):

- "Is the system learning from mistakes?" (L328)
- "Is memory paying off?" (L319)
- "Is the system reducing ambiguity?" (L332)
- "Are low-risk actions trusted?" (L333)
- "Are outputs getting better?" (L335)
- "Is throughput increasing?" (L336)
- "Is context assembly improving?" (L339)
- "Can you understand why actions happened?" (L341)
- "Are workflows producing durable quality?" (L346)
- "Are workflows producing reusable leverage?" (L317)
- "How much work moved from manual to system-managed?" (L316)
- "Is scale becoming cheaper?" (L323)
- "Are one-off tasks becoming systems?" (L352)

#### Pattern 5 — Common failure modes (10)

Title: "Common failure modes and how to avoid them" (L420). David numbers them 1–10:

1. **Building agents before workflows** (L359) — "A clever agent demo is not a business system." (L357); "Agents are not the architecture. They are workers inside the architecture." (L414); avoid by — [AMBIGUOUS: no explicit "avoid by" line attached].

2. **Treating memory as storage** (L369) — "Saving everything is not intelligence." (L388); "Each memory should have a purpose." (L363); "Avoid by using memory types:" (L358).

3. **No source of truth** (L399) — "If project status lives in five places, the system will hallucinate state." (L417); "AI can summarize across tools, but it needs canonical state." (L403); "Avoid by regularly asking:" (L376) → "source of truth for tasks" (L373), "source of truth for metrics" (L372), "source of truth for documents" (L397), "source of truth for decisions" (L404), "source of truth for memory" (L389).

4. **No evaluation loop** (L367) — "Without evaluation, you will not know whether changes improve the system." (L385); "Avoid by creating rubrics for recurring outputs and requiring the system to compare:" (L356) → "expected output vs actual output" (L402), "first draft vs accepted draft" (L412), "failed attempt vs successful attempt" (L368), "old workflow vs new workflow" (L409).

5. **Over-automation too early** (L381) — "The fastest way to destroy trust is to let an immature system take consequential actions." (L371); "Start with recommendations and drafts. Move to execution only when the workflow is stable, reversible, and measurable." (L365); "Avoid by using autonomy levels." (L408).

6. **Under-automation forever** (L391) — "The opposite failure is using AI as a smart assistant forever." (L360); "If the human approves 90 percent of a category unchanged, that category should probably move to higher autonomy." (L416); avoid by — "Which approvals are ceremonial?" (L419) [AMBIGUOUS: this question is the closest "avoid by" anchor].

7. **Too much tool complexity** (L405) — "More tools does not mean more leverage." (L374); "Avoid by forcing every tool to justify its role:" (L370) → "Does it improve quality?" (L413), "Does it execute actions?" (L415), "Does it reduce cognitive load?" (L396), "Does it improve visibility?" (L383), "Does it reduce cost or cycle time?" (L393); "If an AI feature does not do one of those, it is probably theater." (L378); "If not, it is interface clutter." (L394).

8. **No observability** (L410) — "You cannot improve what you cannot see." (L379); "For serious systems, every important workflow should have traceability." (L395).

9. **Confusing novelty with leverage** (L386) — "Leverage comes from:" (L411) → "improving feedback loops" (L366), "shrinking cycle time" (L364), "increasing decision quality" (L382), "creating reusable assets" (L392), "reducing repeated human effort" (L380), "improving output consistency" (L377), "opening new revenue capacity" (L355).

10. **No economic model** (L406) — "AI-native systems should not just feel efficient. They should change the operating economics." (L361); "For services and companies, every system should eventually tie to economics." (L362); avoid by asking — "Does this create proprietary data?" (L384), "Does this improve speed to market?" (L387), "Does this reduce churn?" (L398), "Does this increase revenue capacity?" (L390), "Does this increase throughput per employee?" (L400), "Does this reduce cost to serve?" (L401), "Does this create a defensible workflow advantage?" (L407), "Does this improve gross margin?" (L418).

#### Pattern 6 — Pre-build checklist (sections A–I)

Title: "Practical checklist before building any new system" (L460). "Use this before building anything." (L426).

"If you cannot answer these, you are not ready to build. You are ready to prototype." (L477).

Sections (David labels A–I; A is implicit by position):

**A. Define the problem** [AMBIGUOUS: David labels B–I but not A; A is reconstructed by elimination from these lines]: "What exact workflow or decision is this system improving?" (L484); "Who is the operator or user?" (L436); "What painful bottleneck exists today?" (L473); "What does success look like?" (L483).

**B. Define the information model (L443):** "What inputs does the system need?" (L451); "What state must it maintain?" (L478); "What decisions must it record?" (L449); "What should be remembered?" (L474); "What should be forgotten?" (L427).

**C. Define the workflow (L463):** "What are the steps from intake to output?" (L457); "Which steps require reasoning?" (L481); "Which steps require deterministic software?" (L453); "Which steps require human approval?" (L476); "Which steps are reversible?" (L479); "Which steps are risky?" (L434).

**D. Define the agent/tool design (L425):** "Does this need one agent or multiple specialized agents?" (L467); "What tools does each agent need?" (L444); "What context does each agent receive?" (L454); "What format should each agent return?" (L468); "How are handoffs handled?" (L445); "What should each agent not be allowed to do?" (L459).

**E. Define the evaluation model (L465):** "What makes a good output?" (L441); "What makes a bad output?" (L480); "How will quality be scored?" (L438); "How will human edits be captured?" (L461); "What are the top failure cases?" (L435).

**F. Define observability (L456):** "What should be logged?" (L448); "What dashboard or review cadence is needed?" (L439); "Can you trace why a decision was made?" (L446); "Can you compare workflow performance over time?" (L462).

**G. Define automation boundaries (L437):** "What can be fully automated now?" (L482); "What should be drafted for review?" (L432); "What requires approval?" (L469); "What should never be automated?" (L428); "What confidence threshold is required for each action type?" (L429); "What is the fallback path when the system is uncertain?" (L471).

**H. Define compounding mechanism (L440):** "How does the system get better after each run?" (L452); "What reusable asset does this workflow create?" (L450); "What outputs should become reusable assets?" (L466); "What gets added to the prompt library?" (L447); "What gets added to the workflow library?" (L464); "What gets added to the evaluation library?" (L470); "What gets added to memory?" (L475); "How will the system learn from failures?" (L431); "What proprietary advantage could accumulate?" (L472); "What context does it need?" (L455) [AMBIGUOUS: L455 fits B or D better than H — possibly mis-grouped here by strings].

**I. Define economic value (L424):** "What revenue does this unlock?" (L442); "What cost does this remove?" (L433); "What throughput does this increase?" (L458); "What risk does this reduce?" (L430); "What metrics matter?" (L422); "What should become faster, cheaper, better, or more scalable?" (L421).

### C. RULES (single behavioral instructions)

David sprinkles explicit conditional rules throughout. I extract them as discrete RULEs distinct from the surrounding PRINCIPLES.

**Approval / autonomy rules:**
- R1. "If action is low-cost, reversible, and confidence > 80%, execute or recommend direct execution." (L217)
- R2. "If action is medium-risk, produce recommendation with rationale." (L260)
- R3. "If action is irreversible, costly, or security-sensitive, pause for approval." (L208)
- R4. "If review rarely changes the result, automate more." (L229)
- R5. "If the human approves 90 percent of a category unchanged, that category should probably move to higher autonomy." (L416)

**Memory rules:**
- R6. Curation test: "Will this materially improve future decisions or execution? If not, it is noise." (L143, L145)
- R7. "Store decisions separately from notes." (L198)
- R8. "Do not let every tool become a memory layer." (L226)

**Observability / evaluation rules:**
- R9. "Log inputs, outputs, model used, cost, latency, confidence, failure reason, human correction, and final business outcome. Without observability, you do not have a system. You have magic that will eventually break." (L64) — under section title "Make Every workflow observable" (L63, L66).
- R10. "Every important output should be evaluated against explicit criteria." (L155)
- R11. "Without evaluation, you do not have compounding. You have production volume." (L168)

**Architectural anti-rules ("do nots"):**
- R12. "Do not let the execution layer own the strategy." (L60a)
- R13. "Do not let memory become an unfiltered dump." (L60b)
- R14. "Do not let the interface become the system." (L60c)
- R15. "Do not let every agent improvise the process." (L183)

**Sequencing rules:**
- R16. "Start with recommendations and drafts. Move to execution only when the workflow is stable, reversible, and measurable." (L365)
- R17. "Most systems should live between L1 and L3 for a long time." (L141)

[AMBIGUOUS: R12–R14 are extracted from a single line in the source (L60); I split them because each "Do not…" is a distinct behavioral rule.]

---

## 2. CRITIQUE

### Internal inconsistencies inside the design-principles source

**I-1. Two definitions of "the highest-leverage question."** Source L34 introduces "The highest-leverage question is:" inside the information-architecture section, then L26 supplies its body: the five-part information-flow question. Sections L42/L45 use the same phrase ("The Highest Leverage Question(s)") as a section title whose body is the unrelated "10x larger with 90% less human involvement" prompt (L40, L43). Either David has two different "highest-leverage" questions and the same label is overloaded, or one is mislabeled. The principle "the highest-leverage question is X" cannot be true of two different X's; this needs to be resolved before the consolidation step.

**I-2. The graduated-autonomy ladder vs. "Most systems should live between L1 and L3."** P13 (source L132–L141) names four execution behaviors but the L1/L2/L3/L4 labels never appear in the extraction. L141 ("Most systems should live between L1 and L3") presumes a labeled ladder. Either the labels were lost in strings extraction or the ladder ordering is intuited rather than canonical. Without the labels, "between L1 and L3" is not actionable.

**I-3. Three bottleneck lists overlap.** P12 ("Build around bottlenecks, not features") lists three typical bottlenecks (L125, L127, L131). P14 ("Highest-leverage bottlenecks to diagnose first") lists seven numbered bottlenecks. Failure mode 7 ("Too much tool complexity," L405) overlaps with P14 #6 "Tool fragmentation." David has not stated whether these are nested (the seven include the three) or parallel taxonomies.

**I-4. Compounding-asset list vs. memory-types list overlap.** "Prompts, checklists, templates" (L146) appears in the memory section. "Every run should improve one of these: dataset, prompt, SOP, evaluation rubric, customer profile, knowledge base, automation rule, product insight, or distribution channel" (L71) lists prompts as a compounding asset. The same artifact ("prompt") is simultaneously a memory entry and a compounding output. That may be intentional — a prompt is both — but David does not say so, and if memory and compounding-assets are the same set the two principles collapse into one.

**I-5. Confidence threshold inconsistency.** R1 (L217) specifies a numeric threshold ("confidence > 80%"). R3 (L208) and R2 (L260) use qualitative thresholds ("irreversible, costly, or security-sensitive" / "medium-risk"). The system cannot route off "> 80%" if no other rule emits a numeric confidence. Either every rule needs a numeric confidence, or R1's "80%" is illustrative and should be reworded.

**I-6. "Build Evaluation Systems Early" floats at the tail with no body.** L485 introduces a titled principle that has no attached content in the extraction. It is either a duplicate of P14 #3 / Failure mode 4, or a separate intended section whose body did not survive extraction. Listed but not resolvable.

**I-7. Section P5 "Exploit Parallelism" is title-only.** L75/L77 give the title twice (with the typo "Parallellism") and nothing else. This is the single largest content gap in the source.

### Things the material implies but does not name

**M-1. No explicit risk taxonomy.** P7 router output includes "what risk tier applies" (L85). P13 ("trust gradients") implies risk tiers. R1–R3 imply at least three tiers (low/medium/high). The automation hierarchy (Pattern 3) implies a fourth ("never"). But the source never defines what makes an action "low," "medium," or "high" risk, or how the router computes the tier. Without that, P7, P13, R1–R3, and Pattern 3 cannot be operationalized.

**M-2. No mechanism for "encoded judgment."** P6 says "the moat is encoded judgment plus proprietary context plus feedback data" (L80). The source does not name how judgment gets encoded — prompt? rubric? decision tree? eval set? a rules file? This is the most strategically loaded line in the document and the most under-specified.

**M-3. No definition of "operating model."** P9 ("Optimize for decision velocity") relies on the phrase "the right action is already encoded in the operating model" (L98). "Operating model" is never defined. It could mean: the workflow library, the router, the rules in memory, or the union of all of the above.

**M-4. No explicit revocation or expiry on memory entries.** Memory rules (R6–R8) cover what to admit. The source is silent on when memory entries become stale or wrong, and on how the system corrects them. (Contrast with ADR-004's explicit 90-day expiry on policy approvals.)

**M-5. No author / owner concept for compounding assets.** P10 enumerates "byproducts" (prompts, rubrics, templates, etc.) but does not say who owns versioning, who approves a new addition to the prompt library, or how conflicts between two prompts for the same task are resolved.

### Conflicts with the existing DavidOS charter and ADRs

**C-1. R1's numeric confidence threshold vs. ADR-004's intensity heuristics.** Source L217 says: "If action is low-cost, reversible, and confidence > 80%, execute or recommend direct execution." ADR-004-workspace-native-approval-mechanism.md L117–L127 specifies qualitative heuristics for picking Light vs. Full approval ("stakes are low, action is highly reversible, David has high confidence", "money in a new category", etc.) with no numeric confidence threshold anywhere. ADR-004 also does not include "execute directly without approval" as an option for actions on the canonical list (ADR-004 L66–L75): every canonical-list action requires some approval (Light or Full). R1 says execute directly when confidence > 80%; ADR-004 says you still need at least a Light approval. These are in direct tension if a canonical-list action also happens to clear R1's threshold.

**C-2. P3 ("Prefer workflows before autonomy") vs. current DavidOS stack.** Source L68 names the principle but ADR-001-adopt-hermes-workspace.md L19 commits to hermes-workspace as the daily-driver UI, and ADR-003-paperclip-frozen-atlas-memo-library.md L20 freezes the only system (Paperclip) that previously embodied "workflow before autonomy" via its [APPROVAL: <kind>] workflow tags. ADR-004 L13 explicitly notes: "Today, approvals happen in free-flowing hermes-workspace chat. That works for ephemeral one-offs but fails for substantive decisions…" — i.e., the current stack is closer to "autonomy-in-chat" than to "workflow-before-autonomy." There is no contradiction in the ADRs themselves; the conflict is that the new principles document codifies a discipline the current stack does not yet enforce.

**C-3. P14 #6 "Tool fragmentation bottleneck" vs. current DavidOS reality.** Source L244 names the symptom: "Work is spread across chat, docs, Notion, GitHub, Slack, email, dashboards, and local files." outcomes-and-frustrations-2026-05-13.md Frustration 3 (L41) corroborates: "i sometimes have a hard time conceptualizing what i'm building and staying organized during this process". The current DavidOS surface area already spans GitHub (this repo), hermes-workspace chat (ADR-001), the approvals log markdown file (ADR-004 L27), session debrief files (ADR-004 L142), and Atlas archive JSON files (ADR-003 L21). The principles say "Define source-of-truth hierarchy" (L203); no ADR or charter document yet does. This is a real gap, not just a conflict.

**C-4. Observability rule R9 vs. current ADRs.** Source L64 mandates logging "inputs, outputs, model used, cost, latency, confidence, failure reason, human correction, and final business outcome." No ADR specifies any logging mechanism. ADR-002 L9 notes that OpenRouter did surface per-call costs and that this was useful ("OpenRouter Logs showed every recent gateway-routed call going through Amazon Bedrock"), but the decision to switch to Anthropic OAuth (ADR-002 L18) removes that visibility deliberately ("Cost certainty. Subscription is flat; no anxiety about runaway sessions" — L22). Under R9 the system should be logging cost per call. Under ADR-002 the system has deliberately chosen a billing path that does not expose per-call cost. These are in direct tension on the "cost" component of R9's required log fields. Latency, confidence, failure reason, and human correction are also not currently logged anywhere in the repo (no docs/observability/ directory exists; glob of **/*log*.md returns only approvals-log.md).

**C-5. P15 ("Memory must be curated, not accumulated") vs. ADR-003 Atlas archive.** Source L144: "The worst AI systems remember everything and understand nothing." ADR-003 L21 commits 44 DAV-17 comments and the full Atlas agent record to docs/atlas/identity/, treated as a "memo library you re-spawn." That is closer to "accumulate and re-feed selectively" than to "curate." ADR-003 L22 is explicit that the archive is re-fed on demand, which is curation-at-retrieval rather than curation-at-write. P15 does not specify which side of the curate/accumulate line applies — both readings are defensible. Flag, not a hard conflict.

**C-6. P11 ("Use AI where ambiguity is high and software where repeatability is high") vs. ADR-004's approval format.** ADR-004 specifies a 4-line (Light) or 7-line (Full) structured format that Atlas types into chat. The act of typing the structured format into a chat UI on every approval is a deterministic, highly repeatable task — exactly the kind of task P11 says should be software, not AI. ADR-004 has Atlas (an AI) do it. This is minor and arguably defensible (the AI is composing the content, not just rendering the template), but P11 read strictly would prefer a UI affordance over AI-generated boilerplate. Worth flagging.

**C-7. Outcome list alignment — no conflict found.** I compared the 11-point outcome list in outcomes-and-frustrations-2026-05-13.md L13–L23 against the reconstructed principles. Every outcome has at least one principle that supports it (e.g., "Actively self improves" → P4, P10, Pattern 4; "Loops me in on the decisions that matter" → P13, R1–R3; "Doesn't bullshit me" → R9, R10, Failure mode 8). No outcome contradicts any principle. No principle contradicts any outcome.

---

## What was wanted verified before Task 2

Per Task 1's closing paragraph, the largest open questions before consolidation were: (a) whether the "highest-leverage question" in P2 is genuinely two different questions or a single overloaded label (inconsistency I-1); (b) whether the bottleneck taxonomies in P12 and P14 are nested or parallel (I-3); (c) the canonical content of the four-rung autonomy ladder in P13 (I-2); (d) whether R1's numeric ">80% confidence" threshold is canonical or illustrative (C-1); (e) whether "Exploit Parallelism" (P5) and "Build Evaluation Systems Early" (P18) are real sections with lost bodies, or stub titles never filled in.

**David and Sonnet decision (2026-05-13 evening):** Proceed to Task 2 without pre-resolving. Ambiguities can be resolved in consolidation or surfaced to the audit. See Task 2 preparation artifact.
