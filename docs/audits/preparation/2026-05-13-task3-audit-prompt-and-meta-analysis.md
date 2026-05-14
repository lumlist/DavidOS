# Audit Preparation — Task 3: Audit Prompt and Meta-Analysis

**Produced by:** Claude Opus 4.7 (via Computer)
**Date:** 2026-05-13 evening CDT
**Status:** Preparation artifact for the 2026-05-13 structural audit. **The Audit Prompt section below is the load-bearing artifact — what gets given to charter-active Atlas (Sonnet-class) when the audit runs.**
**Purpose:** Convert the consolidated principles from Task 2 into a self-contained audit prompt that produces a substrate-level decision document.

**Inputs:**
- Task 1 output (reconstruction + critique)
- Task 2 output (consolidated principles, coverage matrix, tensions)
- `docs/sessions/2026-05-13-pickup-brief.md` (Path C tripwires, 5-step path)
- `docs/sessions/NEXT-SESSION-OPEN.md` (9 open structural questions)
- All foundation ADRs

**Output structure:** Four sections — (1) Audit Prompt (the load-bearing artifact, ready to copy-paste); (2) What This Audit Cannot Tell Us (acknowledged limits); (3) What Would Mean the Audit Prompt Itself Was Wrong (meta-failure signals); (4) Next 30 Minutes After Audit Output Lands (operator playbook).

**Decisions reflected in this artifact:**
- The audit will be run by charter-active Atlas (decided 2026-05-13 evening). Activation precedes audit. The bootstrap-circularity caveat in §2 applies if activation is deferred during audit execution.
- David let the audit propose resolutions to all four verification questions. These are encoded in §5 of the audit prompt as required output.

---

## 1. AUDIT PROMPT

The block below is self-contained. Copy-paste to the next Sonnet-class agent as-is.

```
# DavidOS Structural Audit — 2026-05-13

You are conducting a structural audit of DavidOS at commit `441dd58` (or later if subsequent commits exist; if later, name the commit you are reading). You are operating as a Sonnet-class agent advising David Izzard.

This audit is the load-bearing event for the 2026-05-13 session. Its output replaces or confirms the existing 5-step path before any further substrate work proceeds. Do not begin activation work, do not edit SOUL.md, and do not modify substrate items until this audit completes.

================================================================
PART A — REQUIRED READING (read in this order, do not skip)
================================================================

Primary sources (do-not-paraphrase, primary-source charter docs):
  1. docs/charter/outcomes-and-frustrations-2026-05-13.md
     — 11 charter outcomes, 3 frustrations, 3 clarifying responses
  2. docs/charter/davidos-design-principles-source-2026-05-13.md
     — David's verbatim AI-native system design principles
     (NOTE: extracted via `strings` from a .one file; ordering is partially
      scrambled; treat as authoritative content, not authoritative structure)

Foundation decisions:
  3. docs/decisions/ADR-001-adopt-hermes-workspace.md
  4. docs/decisions/ADR-002-anthropic-oauth-over-api-key.md
  5. docs/decisions/ADR-003-paperclip-frozen-atlas-memo-library.md
  6. docs/decisions/ADR-004-workspace-native-approval-mechanism.md
  7. docs/decisions/approvals-log.md

Session state:
  8. docs/sessions/2026-05-13-pickup-brief.md  (especially Path C tripwires)
  9. docs/sessions/NEXT-SESSION-OPEN.md         (9 open structural questions)
 10. docs/sessions/2026-05-12-session-record.md (state of SOUL.md sections 1-5 vs 6-9)

Influences under consideration (not adopted; you decide):
 11. docs/charter/influences/2026-05-13-nate-herk-aios-course.md
     — Four C's order rule: Context → Connections → Capabilities → Cadence
 12. docs/charter/influences/2026-05-13-anthropic-agent-skills-video.md
     — Skill-first framing
 13. docs/charter/influences/2026-05-13-nate-herk-tech-stack-and-frameworks.md
     — Decision framework + "needle moved per hour"

Runtime reference (load if needed for activation-related findings):
 14. docs/reference/hermes-internals.md (read TL;DR, §2, §5, §8 at minimum)

If a file path above is missing in the repo at audit time, note it as a
finding rather than proceeding with assumptions about its content.

================================================================
PART B — EVALUATION FRAMEWORK
================================================================

You evaluate DavidOS state against SEVEN CONSOLIDATED PRINCIPLES derived
from David's design-principles source. Each principle includes a
FALSIFIABLE TEST you must apply against the current repo.

Architectural principles are load-bearing across all phases of DavidOS's
life. Operating principles are load-bearing for the current foundation-
building phase only. Evaluate each principle in its appropriate context.

  P1 [ARCHITECTURAL] Information architecture comes before agents
     Statement: "The system is only as good as its information
     architecture" (design-principles source L32). Decide what enters,
     how it's classified, where it lives, who can act on it, and how it
     improves future decisions (L26) before building agents, prompts,
     automations, or interfaces.
     Test: Does the repo contain a document that defines (a) canonical
     entity types (project, decision, approval, session, asset, etc.),
     (b) where each lives, and (c) which file is source of truth when
     they disagree? If no such document exists, P1 is violated.

  P2 [ARCHITECTURAL] Separate the system into named layers; no layer
     owns the strategy
     Statement: Input / Reasoning / Execution / Learning layers
     (source L47, L49), command-center architecture (L153). "Do not let
     the execution layer own the strategy. Do not let memory become an
     unfiltered dump. Do not let the interface become the system" (L60).
     Test: Pick any current DavidOS workflow (e.g., the approvals-log
     update flow from ADR-004). Name the file/component that is the
     Input layer, Reasoning layer, Execution layer, and Learning layer
     for that workflow. If any layer is absent or chat-resident, P2 is
     violated.

  P3 [ARCHITECTURAL] Build a strong router before building more agents
     Statement: "A strong router decides: what type of work is this,
     what context is required, what tool should handle it, what risk
     tier applies, what output format is needed, and what approval is
     required. Routing quality determines system quality" (L84–L85).
     Test: Is there a file, function, or documented decision procedure
     in DavidOS that, given an incoming request, emits (work type,
     required context, tool, risk tier, output format, approval
     requirement)? If classification is implicit in Atlas's prompt
     only, P3 is violated.

  P4 [ARCHITECTURAL] Every workflow produces a reusable asset; otherwise
     it's labor
     Statement: "If a workflow only produces the immediate output, it is
     labor" (L108). Compounding assets (L71): dataset, prompt, SOP,
     evaluation rubric, customer profile, knowledge base, automation
     rule, product insight, or distribution channel.
     Test: For the last three workflows in docs/sessions/submitted/
     and docs/decisions/approvals-log.md, name the specific reusable
     asset each added to a library. If you cannot name an asset for
     2-of-3, P4 is violated.

  P5 [ARCHITECTURAL] Without evaluation you have production volume, not
     compounding
     Statement: "Every important output should be evaluated against
     explicit criteria" (L155). "Without evaluation, you do not have
     compounding. You have production volume" (L168). Log inputs,
     outputs, model used, cost, latency, confidence, failure reason,
     human correction, business outcome (L64).
     Test: For any DavidOS workflow, can you produce (a) the evaluation
     rubric, (b) logged inputs/outputs/cost/latency/confidence for the
     last run, and (c) a comparison against a prior run or baseline?
     If no logging infrastructure exists, P5 is violated.

  P6 [ARCHITECTURAL] Graduate autonomy by risk; never fully automate
     values, taste, or irreversible bets
     Statement: "Not all automation should have the same permission
     level" (L135). Graduated autonomy (L139). "If action is
     irreversible, costly, or security-sensitive, pause for approval"
     (L208). "Never fully automate: values, taste, irreversible bets,
     and accountability" (L279).
     Test: For each item in ADR-004's canonical "requires approval" list
     (ADR-004 L66–L75), is there a documented risk tier and the
     corresponding autonomy rung the system uses? If only the two-
     intensity (Light/Full) gating exists with no risk tiers and no
     autonomy ladder, P6 is partially satisfied — name which half.

  P7 [OPERATING] Build around the binding bottleneck, not the most
     annoying feature
     Statement: "The correct automation target is rarely the most
     annoying task. It is the constraint that limits the entire system"
     (L126). Seven candidate bottlenecks (L213): context retrieval,
     decision, evaluation, handoff, human review, tool fragmentation,
     prompt.
     Test: Is there a current document in DavidOS that names which of
     the seven bottlenecks is binding right now, with evidence, and
     which is being worked on next? If not, P7 is violated.

SUCCESS CRITERIA: the 11 charter outcomes (read O1–O11 from
docs/charter/outcomes-and-frustrations-2026-05-13.md L13–L23). A passing
audit shows DavidOS state advancing those outcomes; a failing audit
shows misalignment with citation.

COVERAGE CONTEXT (from prior consolidation work — treat as input, not
gospel; you may contest):
  - O2 (well-architected) is served by 5 of 7 principles (P1, P2, P3,
    P5, P6) — known over-specification.
  - O7 (inventiveness), O8 (monetization awareness), O11 (no bullshit)
    are served by 0 or 1 principle — known under-coverage.
  - O4 served by 2 (P1, P3). O5 served by 3 (P5, P6, P7). O9 served
    by 2 (P3, P6).

KNOWN TENSIONS between principles (treat as input):
  T1: P3 (router-first / prerequisite ordering) vs. P7 (bottleneck-first
      / demand-driven ordering). Activates when the diagnosed binding
      bottleneck is downstream of routing.
  T2: P4 (every workflow produces an asset) vs. P7 (build around the
      bottleneck). Activates when the binding bottleneck is latency
      and asset-production overhead slows the workflow.
  T3: P5 (evaluate, including cost) vs. ADR-002 (deliberate cost-blindness
      via Anthropic OAuth flat subscription). Cost component of P5's
      required logging is structurally prevented by the accepted ADR.
  T4: P6 (4-rung autonomy ladder) vs. ADR-004 (2-intensity Light/Full
      format). ADR-004 is a subset of P6, not yet a faithful
      implementation.

================================================================
PART C — REQUIRED OUTPUT
================================================================

Save your audit to docs/audits/2026-05-13-structural-audit.md with these
EXACT top-level sections in this order. Do not add other top-level
sections; nest additional structure beneath these.

§1. EXECUTIVE FINDING (≤ 200 words)
    One-paragraph summary: does the substrate-first plan still hold,
    does it need resequencing, or are there structural problems that
    block further substrate work? Then a single sentence naming the
    highest-leverage thing to build next.

§2. PRINCIPLE-BY-PRINCIPLE EVALUATION
    For each of P1–P7, in order: state the principle, run its
    falsifiable test against the current repo with file:line citations,
    return one of {SATISFIED, PARTIALLY SATISFIED, VIOLATED, UNTESTABLE
    AT THIS COMMIT} and the evidence. If UNTESTABLE, state what would
    make it testable. No verdicts without citation.

§3. CHARTER-OUTCOME ALIGNMENT
    For each of O1–O11: name the current DavidOS state that advances
    or fails it, with citation. Explicitly assess whether the
    operational-discipline bias in the principle set (5 principles
    serving O2; 0 or 1 serving O7/O8/O11) is appropriate for David's
    current phase (foundation now → first revenue soon → portfolio
    later, per outcomes-and-frustrations-2026-05-13.md L55), or
    indicates the principle set is over-fit to one outcome at the
    expense of others. Return one of {APPROPRIATE FOR PHASE,
    OVER-FIT — REBALANCE NEEDED, UNDER-FIT — ADD COVERAGE} with reasoning.

§4. ANSWERS TO THE 9 OPEN STRUCTURAL QUESTIONS
    Quote each question from docs/sessions/NEXT-SESSION-OPEN.md and
    provide an explicit recommendation. Mark each as
    {RECOMMEND ADOPT, RECOMMEND REJECT, RECOMMEND DEFER WITH TRIGGER}.
    For each ADOPT recommendation, name the artifact (ADR number, file
    path, substrate item) that operationalizes it. Q7 (Four C's order
    rule) is the highest-impact; treat its answer as load-bearing for
    §6 below.

§5. RESOLUTIONS TO THE FOUR VERIFICATION QUESTIONS
    For each of (a)–(d) below, propose a resolution with reasoning. Do
    not defer; the operator has decided you must propose. If you
    cannot decide, state precisely what evidence would decide it.

    (a) Should P2 (named layers) and P3 (strong router) merge into one
        architectural principle, or remain separate? Both fail in the
        "monolithic agent" mode. The case for merging is real. The
        case for separating is that a layered system without a router
        still routes (implicitly) and a router without layered
        subsystems still routes (to one execution surface).
    (b) Are the three uncovered charter outcomes (O7 inventiveness,
        O8 monetization-awareness, O11 doesn't-bullshit-me) intentional
        omissions that should remain unaddressed by the principle set,
        or gaps requiring new principles? If gaps, name the new
        principle(s) and where they would slot into P1–P7.
    (c) Is there a tacit tie-breaker between P3 (router-first /
        prerequisite ordering) and P7 (bottleneck-first / demand-driven
        ordering)? If yes, name it (e.g. "prerequisites trump bottlenecks
        when not yet built; bottlenecks trump prerequisites once
        prerequisites exist"). If no tie-breaker exists, propose one
        and justify.
    (d) Resolve the P5-vs-ADR-002 tension by one of: {REVISE ADR-002
        to re-enable per-call cost observability, SOFTEN P5's cost
        requirement, ACCEPT BOTH and document the contradiction in the
        approvals log, OR a fourth path you propose explicitly}.

§6. SUBSTRATE-FIRST PLAN VERDICT
    State whether the 5-step path in docs/sessions/NEXT-SESSION-OPEN.md
    L67–L73 still holds, needs resequencing, or needs replacement.
    Resolve the P3-vs-P7 tension (T1) by stating which principle takes
    precedence under current conditions, with reasoning grounded in
    the §2 verdicts. If the Four C's order rule from
    docs/charter/influences/2026-05-13-nate-herk-aios-course.md is
    adopted, restate the path under that rule. Produce a numbered
    sequence with duration estimates. If the path needs resequencing,
    explicitly name what moves, what stays, and what's added or removed.

§7. SOUL.MD ACTIVATION VERDICT
    SOUL.md sections 1–5 were reviewed on 2026-05-12 (see
    docs/sessions/2026-05-12-session-record.md). Sections 6–9 remain
    unreviewed. Decide one of:
      {ACTIVATE AS-IS (after operator finishes 6–9 in normal pass),
       ACTIVATE THEN ITERATE (post-activation revision is acceptable),
       REVISE BEFORE ACTIVATION (specific revisions required first),
       DEFER ACTIVATION (with specific unblocker named)}.
    Then explicitly: which of the 7 consolidated principles, and which
    of the 3 uncovered outcomes (O7, O8, O11), require explicit
    representation in SOUL.md before activation, and where in SOUL.md
    they would land (which section). If none, say so explicitly.

§8. HIGHEST-LEVERAGE NEXT BUILD
    One sentence: the single highest-leverage artifact to build next
    after this audit lands. Must follow from §6 and §2 verdicts. Must
    be specific enough that the operator can begin work without
    further clarification.

§9. STRUCTURAL FINDINGS (overflow)
    Anything you found that doesn't fit in §1–§8. Includes: file paths
    referenced in this prompt that don't exist in the repo; assumptions
    you had to make because evidence was missing; principle-vs-ADR
    contradictions beyond T3 and T4; risks the operator should know
    about before acting on this audit.

================================================================
PART D — CITATION DISCIPLINE
================================================================

Every claim about current DavidOS state must cite a specific file and
line number (or `glob` result, or `ls -la` listing). Claims without
citations are FLAGGED AS ASSUMPTIONS TO VERIFY and listed in §9.

Acceptable citation forms:
  - `docs/decisions/ADR-004-workspace-native-approval-mechanism.md L66–L75`
  - `glob '**/skills/**' returned 0 results`
  - `ls docs/audits/ → directory does not exist`

Unacceptable:
  - "Looking at the repo, it seems..."
  - "The ADRs imply..."
  - Quoting content without file:line.

If you need to read a file not in PART A's required reading list, read
it and cite from it. Do not synthesize from titles or assumed contents.

================================================================
PART E — FAILED AUDIT CONDITIONS
================================================================

A failed audit returns coherent output that is nevertheless not
actionable. You must self-detect and abort if any of these fire.
On abort, write only §1 and §9 to the audit file, mark the file
status as "AUDIT ABORTED — escalate to Opus tripwire," and stop.

Path C tripwires (from docs/sessions/2026-05-13-pickup-brief.md L141–L146,
inherited):
  F1: You cannot quote the canary string `ATLAS-CHARTER-7734-ACTIVE`
      when asked (only applies post-activation; if pre-activation,
      skip this tripwire).
  F2: Your audit ignores or contradicts the 11-point outcome list
      without naming why.
  F3: Your audit recommends actions that violate approval discipline
      (e.g., autonomous tool adoption, unilateral ADR creation, code
      pushed without explicit approval).
  F4: Your audit reads as generic "AI system best practices" without
      specific references to DavidOS file paths, ADR numbers, or
      charter outcomes.

Additional tripwires derived from the consolidated principles:
  F5: Any §2 verdict lacks a file:line citation.
  F6: §6 resolves the P3-vs-P7 tension without naming which principle
      takes precedence and why.
  F7: §7 recommends activation but §2 returned VIOLATED on three or
      more architectural principles (P1–P6) AND those violations
      bear on Atlas's intended responsibilities. Activation under
      that condition compounds drift; defer instead.
  F8: §4 returns DEFER on five or more of the 9 structural questions.
      Deferring the majority means the audit has not done its job —
      surface this as a structural finding (§9) and abort.
  F9: Your principle-by-principle evaluation produces only verdicts
      and no specific recommended actions in §6 or §8.
  F10: You generated more open questions than you closed (count
       questions added to §9 vs. questions answered in §4 — if added
       ≥ closed, abort).

If a tripwire fires, the audit failure itself is a useful regression-
suite test case. Do not retry. Escalate per pickup-brief Path C.

================================================================
PART F — SCOPE BOUNDS
================================================================

This audit is scoped to produce a SUBSTRATE-LEVEL DECISION, not an
implementation. You are not authorized to:
  - Edit SOUL.md (recommend only)
  - Edit ADRs (recommend only; ADR-005+ creation is a separate approved
    action, not an audit output)
  - Push code or activate Atlas
  - Adopt influence notes (the influence notes remain "under
    consideration" until ADR-005+ is approved; you recommend, operator
    approves)
  - Conduct work beyond §1–§9 above
  - Spawn subagents (this is a single-pass synthesis; if you find the
    work irreducibly requires a subagent, surface that as a §9 finding
    and stop)
  - Read or modify any repo other than DavidOS (per repo-scope
    principle, NEXT-SESSION-OPEN.md L84)

Time bound: produce §1–§9 within a single bounded synthesis pass. If
during the pass you discover that producing §1–§9 to the citation
standard in PART D would require materially more time than a single
session can absorb (operationalized as: you find yourself wanting to
read more than 8 additional files beyond PART A's required list, OR
you find yourself recommending more than 3 new ADRs in §4), STOP, write
§1 and §9 only, mark "AUDIT SCOPE EXCEEDED — recommend operator split,"
and explain in §9 what split you'd recommend. This is a STRUCTURAL
FINDING, not a failure.

================================================================
PART G — STARTING CONDITIONS
================================================================

When you begin:
  - You have read access to the DavidOS repo. Assume it is at the
    commit named in the audit file header.
  - You do not yet have Atlas charter-active. If post-activation, F1
    (canary) is a hard test. If pre-activation, skip F1.
  - You may issue read-only shell commands (ls, grep, glob, cat) to
    verify file:line claims. You may not issue write commands.
  - The operator (David) is not at the keyboard during your synthesis
    pass. Save the audit; he reads after.

Begin with PART A. Output only the audit file at
docs/audits/2026-05-13-structural-audit.md. Do not narrate your reading
or planning — the audit file is the artifact.

END OF AUDIT PROMPT.
```

---

## 2. WHAT THIS AUDIT CANNOT TELL US

**Whether the principles themselves are right.** The audit evaluates DavidOS against the 7 consolidated principles. If the consolidation was wrong — if there should be 5 principles or 9, if P4 and P10 should not have merged, if "Inventiveness" and "No bullshit" should have been principles in their own right — the audit cannot surface that error structurally because the principles are its frame. The §3 over-fit test partially addresses this, but a coherent audit can return "APPROPRIATE FOR PHASE" and still be operating from the wrong principle set.

**Whether SOUL.md sections 6–9 are sound.** Section 7 forces a verdict on activation, but the audit reads SOUL.md only via the 2026-05-12 session record (sections 1–5 reviewed; 6–9 not). The audit cannot evaluate sections 6–9 directly because they are held in ephemeral workspace and not in the repo (per pickup-brief L36). Section 7's verdict is therefore "activate or defer given sections 1–5 plus principle requirements," not "sections 6–9 are sufficient."

**Whether Atlas charter-active produces qualitatively better output.** The Path C premise is that charter-active Atlas conducts the audit. If activation is deferred per the audit's own §7 verdict, the audit is being conducted by Sonnet-without-charter — exactly the configuration that ran every prior "Atlas" session and which the pickup-brief identifies as suspect. The audit cannot self-test for that condition pre-activation. F1 catches it only post-activation.

**Operational context (David's actual work).** The Four C's question (Q7 / influence note 11) hinges on whether DavidOS has captured operational context — what David sells, what's selling, current 7 buckets. Per the Nate Herk note (2026-05-13-nate-herk-aios-course.md L118), operational context "almost" doesn't exist in DavidOS. The audit can recommend onboarding-interview substrate but cannot conduct it; that requires David at the keyboard.

**Whether the principle set is over-fit to David's stated preferences vs. his actual behavior.** All seven principles were extracted from David's verbatim source. Whether his behavior in sessions matches his principles (e.g., he says "build around bottlenecks" but spends time on UI per Frustration 3) is not testable by document inspection.

**Cost of running the audit itself.** Per ADR-002, per-call cost is structurally hidden. The audit cannot report its own credit consumption — a meta-instance of T3.

---

## 3. WHAT WOULD MEAN THE AUDIT PROMPT ITSELF WAS WRONG

The audit prompt is wrong, not just the audit's output, if any of these signals appear:

**The output is coherent and well-cited but recommends something David's charter explicitly rejects.** E.g., §8 recommends "build an autonomous routine that runs daily without approval" — a direct violation of ADR-004 and outcome O9. Coherent output that contradicts the charter means the prompt failed to bind the auditor to the charter, not that the auditor failed.

**Three independent audit runs (or the Opus tripwire pass) converge on substantially different §6 or §8 conclusions.** Quality criterion (c) requires substantial similarity across runs. Divergence means the prompt under-constrains the decision space — likely too many degrees of freedom in §5 or §6.

**The auditor returns §1–§9 in form but every §2 verdict is "PARTIALLY SATISFIED" or "UNTESTABLE."** This is the prompt asking falsifiable tests of a system that cannot answer them yet. If most tests are untestable, the prompt was written against the wrong evaluation surface — DavidOS is too early-stage to evaluate against these principles, and what was needed was a gap inventory, not a principle audit.

**§4 returns DEFER on five or more of the 9 questions despite F8.** If F8 fires, the audit aborts. The prompt being wrong looks like: F8 almost fires (4 deferrals) and the auditor produces coherent-looking output that doesn't actually decide anything. This pattern is harder to catch than an abort.

**The auditor satisfies every Path D citation but the citations point exclusively to ADRs and charter docs, never to running code, infrastructure, or VPS state.** That would mean the audit evaluated DavidOS-the-documentation, not DavidOS-the-system. The prompt's required reading is heavily document-weighted; if the system audit is what's needed, this prompt is the wrong tool.

**§5(b) resolves the three uncovered outcomes (O7/O8/O11) by adding three new principles that bring the total to 10.** That would mean the consolidation step was wrong (too aggressive) and the audit caught it — but it would also mean the audit prompt is now operating on principles that were just invented, which is a different audit than the one commissioned. Treat as a signal to redo task 2 before acting on this audit's §6 verdict.

**The auditor cites the design-principles source by line number for verbatim quotes but never reconciles its scrambled structure.** The prompt warns the source is strings-extracted and structure is partially unrecoverable. If the auditor treats the source as ordered, the prompt failed to enforce the caveat — and the §2 verdicts may rest on misattributed groupings from task 1's reconstruction.

---

## 4. NEXT 30 MINUTES AFTER AUDIT OUTPUT LANDS

**Minutes 0–5: Read §1 and §8 only.** Executive finding plus highest-leverage next build. This is the faith-check moment from pickup-brief Phase 1. Either the path makes sense or it doesn't. If §1 reports AUDIT ABORTED or AUDIT SCOPE EXCEEDED, jump to the Opus tripwire conversation and stop the rest of this 30-minute plan.

**Minutes 5–10: Check the tripwires.** Scan §9 for any F1–F10 trigger that the auditor self-detected but did not abort on (these can leak — the auditor may have softened a finding rather than fail the run). Also confirm: did §7 recommend ACTIVATE while §2 returned VIOLATED on three or more of P1–P6? If yes, F7 should have fired; if it didn't, the tripwire was bypassed and the audit needs second-pass review before acting.

**Minutes 10–18: Read §6 (substrate plan verdict) and §4 (Q7 Four C's answer).** These two together decide whether the next session is "finish SOUL.md sections 6–9 and activate" or "capture operational context first." Resolve the P3-vs-P7 tension as the audit proposed it; flag if the proposal feels wrong rather than acting on autopilot.

**Minutes 18–25: Read §5 (verification questions a–d).** Specifically: does the resolution to (d) require revising ADR-002, and if so, is that an audit recommendation that needs an explicit Full approval per ADR-004 L66–L75 before action? Most likely answer: yes — ADR revision is policy-level and needs Full approval. Queue it for approval, do not act on it as an audit byproduct.

**Minutes 25–30: Commit decisions.** Write a Light approval entry to `docs/decisions/approvals-log.md` for each audit recommendation accepted (§4 ADOPT items, §6 verdict, §8 next build). Open a draft for any ADR-005+ the audit triggered (Four C's adoption, skill-first adoption, principle additions for O7/O8/O11) but do not create the ADR file yet — that's the next session's first work item. End of 30 minutes: you know what's next, the decision is logged, and the next session opens with a single explicit task rather than a structural unknown.

---

## How this artifact is used

This file is preparation, not implementation. The audit itself runs separately and produces its output at `docs/audits/2026-05-13-structural-audit.md`. The §2-§4 sections of this file (limits, meta-failures, operator playbook) are the operator's reference when reading that audit output — particularly §3, which lists the signals that mean the audit prompt itself was wrong, not just the audit output.

When the audit lands:
1. Operator reads audit per §4's 30-minute playbook above
2. If any §3 signal fires, the prompt itself gets revised and the audit is re-run (or escalated to Opus per Path C)
3. Otherwise, the audit's §6 / §8 verdicts become the basis for the next work block

The principles, coverage matrix, and tensions from Task 2 are referenced explicitly in the audit prompt (Parts B and the COVERAGE CONTEXT block). If those need revision based on audit findings, that's a Task 2 revision, not a Task 3 patch.
