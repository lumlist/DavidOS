# Pickup Brief — Wednesday, 2026-05-13

**Status:** Authoritative pickup document for tomorrow's session.
**Created:** 2026-05-13 ~5:00 AM CDT by Sonnet at end of 2026-05-12 evening session.
**For:** David, and whichever agent picks up the session.
**Purpose:** Provide a clear, durable answer to "what are we doing tomorrow, why, and how do we know it worked." Read this before any other action.

---

## TL;DR (read this first)

1. **Tonight discovered the foundation we thought we had wasn't actually there.** Atlas was never charter-active. The Opus review of Substrate Brief v1 was never saved. The activation work we planned for tonight got deferred.
2. **Tonight produced new foundation-level material** that needs to be processed before activation can responsibly proceed: a verbatim charter (your 11 outcomes + 3 frustrations), three influence notes from YouTube videos, an authoritative Hermes runtime reference, and 9 open structural questions.
3. **Tomorrow opens with a structural audit, not activation work.** The audit decides whether the substrate-first plan still holds, or whether it needs to be resequenced (the Four C's order rule is the highest-impact open question).
4. **Recommended approach: Path C** — charter-active Atlas conducts the audit; Opus invoked only as a second-pass reviewer if the audit fails a "charter-active quality" test. Paths A (Opus tonight/upfront) and B (Atlas alone, no Opus tripwire) remain visible for tomorrow's explicit decision.
5. **Faith restoration is the goal of tomorrow's first 30 minutes**, not a deliverable to be assumed. You should be able to read this brief, then the audit output, and feel "yes, we're on the right path" — or call it explicitly if you don't.

---

## Where we actually are (honest state)

### What's in DavidOS as of commit `441dd58` (pre-pickup-brief commit)

- **Charter primary source:** [`docs/charter/outcomes-and-frustrations-2026-05-13.md`](../charter/outcomes-and-frustrations-2026-05-13.md) — your 11-point outcome list, 3 frustrations, 3 clarifying responses, all verbatim. Marked do-not-paraphrase. This is the first primary-source charter document for DavidOS.
- **Three influence notes (under consideration, not adopted):**
  - [Anthropic Agent Skills](../charter/influences/2026-05-13-anthropic-agent-skills-video.md) — skills as the core implementation unit
  - [Nate Herk AIOS Course (Four C's)](../charter/influences/2026-05-13-nate-herk-aios-course.md) — the architecture and build order, Context → Connections → Capabilities → Cadence
  - [Nate Herk Tech Stack + Frameworks](../charter/influences/2026-05-13-nate-herk-tech-stack-and-frameworks.md) — the operating discipline and decision rule
- **Hermes runtime reference:** [`docs/reference/hermes-internals.md`](../reference/hermes-internals.md) — 578-line authoritative reference produced by a research subagent tonight. Cross-validated against actual VPS state.
- **Tonight's session record:** [`docs/sessions/2026-05-12-session-record.md`](./2026-05-12-session-record.md) — chronological narrative, decisions made, uncomfortable discoveries, drift indicators.
- **Approvals log:** [`docs/decisions/approvals-log.md`](../decisions/approvals-log.md) — appended 6 entries from tonight, 41 total entries.
- **Four foundation ADRs:** [`ADR-001`](../decisions/ADR-001-adopt-hermes-workspace.md) (Hermes daily driver), [`ADR-002`](../decisions/ADR-002-anthropic-oauth-over-api-key.md) (auth + model policy), [`ADR-003`](../decisions/ADR-003-paperclip-frozen-atlas-memo-library.md) (Paperclip frozen, Atlas as memo library), [`ADR-004`](../decisions/ADR-004-workspace-native-approval-mechanism.md) (approval mechanism).

### What's deliberately NOT in DavidOS yet

- **SOUL.md draft v0.2** — paused mid-review in ephemeral workspace. Sections 1-5 reviewed (with revisions: UUID cut, "David's outcomes first" merged with customer-zero as #1 principle, vocabulary discipline stripped, Stop-At-Strength stripped, repo-scope principle added). Sections 6-8 (Boundaries, Voice, Verification) not yet reviewed. Status-of-this-document section at bottom acknowledging v1 nature. Held out of git deliberately; the finished version commits next session after activation.
- **Substrate Brief v1** — in VPS working clone at `~/projects/personal-ai-workspace/docs/substrate-brief-v1.md` (213 lines, hash `0940d0f6fcb9bfbb`), but not yet pushed to the GitHub remote. Will be reviewed and revised by charter-active Atlas in tomorrow's work, then committed as v1.1.
- **No DavidOS skills exist yet.** The repo has `docs/`, but no `skills/` folder. Influence notes 1 and 2 both recommend skills as the core implementation unit; not yet adopted.

### What's open in NEXT-SESSION-OPEN.md (9 structural questions)

1. Which of the 11 charter outcomes belong in SOUL.md vs Charter Regression Suite vs Substrate Brief?
2. Does the 5-step path need reordering to serve phase priorities (foundation now → first-revenue soon → portfolio later)?
3. Should a Phase State / Operating Mode substrate item exist so Atlas knows which phase he's advising in?
4. Is milestone tracking a missing substrate item or covered by Decisions Register + Session-Start Manifest?
5. Is zero-setup session resumption sufficiently addressed by Session-Start Manifest, or its own item?
6. Adopt skill-first framing (Video 1) as ADR-005?
7. **(Highest impact)** Adopt Four C's order rule (Video 2) — does it resequence the 5-step path?
8. Adopt Nate Herk's decision framework (Video 3) for evaluating new tools as a formal pattern?
9. Reframe milestone tracking as "needle moved per hour" rather than tasks completed?

### The infrastructure state (VPS)

- Atlas profile exists at `~/.hermes/profiles/atlas/` but `SOUL.md` is the default generic Hermes text, not the Atlas charter
- `~/.local/bin/atlas` wrapper does not exist
- Gateway, dashboard, and pnpm dev processes likely still running with empty `HERMES_HOME` from tonight's session (will need to be stopped cleanly before activation)
- Activation is roughly 60-90 minutes once we decide to do it — see [`hermes-internals.md`](../reference/hermes-internals.md) Sections 2, 5, 8

---

## Tomorrow's plan in plain language

### Phase 1 (first ~30 minutes): Faith check

Read this brief. Read the charter file. Skim the three influence notes' TL;DRs. Skim the session record.

**End state of Phase 1:** You either say "yes, this is the right path forward" or "no, something is off, let's reassess." If the latter, do not proceed to Phase 2 — stop and discuss.

### Phase 2 (next ~60-90 minutes): Structural audit

Conduct an audit of all DavidOS work to date against the charter file. The audit's purpose is to answer the 9 open structural questions and either confirm the 5-step path, resequence it, or replace it.

**Recommended approach: Path C** (see section below). Charter-active Atlas conducts the audit; Opus invoked only as a second-pass reviewer if the audit fails a quality test.

**End state of Phase 2:** A written audit output saved to `docs/audits/2026-05-13-structural-audit.md` covering: what's coherent in DavidOS, what contradicts, what's missing, what the 5-step path should look like after the audit, recommended adoption decisions on the three influence notes.

### Phase 3 (after audit): Execute on audit findings

Depending on what the audit produces, this is one of:

- **If audit confirms current plan:** Complete SOUL.md draft sections 6-8, write to VPS, activate Atlas, run canary check. This is Step 1 of the original 5-step path.
- **If audit resequences the plan (e.g., Four C's adopted):** New Step 1 becomes "capture operational context" — onboarding interview against David to capture what he sells, what's selling, quarterly priorities, his tools, his work buckets. Output: `docs/context/about-david.md`, `docs/context/priorities-2026-Q2.md`, `docs/context/buckets.md`. Activation may be deferred until Context layer is more complete.
- **If audit surfaces unresolved structural problems:** Pause, document the problems, return to operator (David) for direction. Don't push forward through uncertainty.

**End state of Phase 3:** Either Atlas is charter-active and verified, or there's a clear written reason why activation is being deferred and what unblocks it.

### Phase 4 (only if Phases 1-3 complete cleanly): Move into substrate work

Per the original 5-step path or its audit-revised version. Begin shipping the first substrate items.

---

## The three approaches to the audit (Paths A, B, C)

You've been considering how to conduct the audit. Three options, all defensible:

### Path A — Opus conducts the audit upfront

**What it is:** Switch to Opus 4.7 at session start. Have it read the conversation thread (including this one), every file in DavidOS, the influence notes, the charter, the SOUL.md draft, and produce an audit + strategic recommendations.

**Pros:**
- Frontier-model judgment on synthesis-heavy work where Sonnet vs Opus has the biggest gap
- Independent observer view, unanchored to charter constraints
- Fastest path to "objective external read" of the work

**Cons:**
- Real money — Opus is roughly 5x Sonnet cost for comparable work; audit-style work is token-heavy
- Opus has no charter loaded, so its recommendations are unconstrained — may suggest things charter-active Atlas wouldn't (e.g., autonomy-heavy patterns David's charter explicitly rejects)
- Removes the most valuable first task charter-active Atlas could do
- If we Opus-audit before Atlas exists, future Atlas review of the Opus audit is biased by the Opus framing (same bias issue we already flagged in the Substrate Brief context)

### Path B — Charter-active Atlas conducts the audit alone

**What it is:** Complete SOUL.md sections 6-8, activate Atlas, then have him conduct the audit operating under the charter. No Opus involvement.

**Pros:**
- Audit is anchored to David's actual outcomes via SOUL.md
- Cheapest option (Sonnet-class per ADR-002)
- The audit *is* the first real test of whether charter-active Atlas adds value
- Aligned with the within-task model selection pattern already approved

**Cons:**
- Sonnet vs Opus is a real capability gap on cross-document synthesis
- No external check — charter Atlas may have blind spots baked into his constraints
- If Atlas's audit is low-quality, we won't know until after spending the session on it

### Path C — Atlas first, Opus as tripwire (RECOMMENDED)

**What it is:** Charter-active Atlas conducts the audit. **Built-in tripwire:** if Atlas's output on the 9 structural questions reads as Sonnet-role-playing-Atlas rather than charter-active-Atlas reasoning, stop, invoke Opus as second-pass reviewer, and treat the failed audit itself as the first charter-regression test case.

**Pros:**
- Best of both: charter-anchored by default, Opus available for the high-judgment moments where it's actually needed
- Aligned with the within-task model selection pattern already approved (Sonnet default, Opus for synthesis components)
- The tripwire creates an explicit quality test for charter-active Atlas
- A failed audit produces useful information (regression suite test case) rather than wasted spend

**Cons:**
- Requires defining "charter-active quality" clearly enough to recognize failure
- Slightly more orchestration complexity than Paths A or B

**Tripwire definition (proposed):** Atlas's audit fails the charter-active test if any of:
- He cannot quote the canary string `ATLAS-CHARTER-7734-ACTIVE` when asked
- His audit ignores or contradicts the 11-point outcome list without naming why
- His audit recommends actions that violate approval discipline (e.g., autonomous tool adoption)
- His audit reads as generic "AI system best practices" without specific references to DavidOS file paths, ADR numbers, or charter outcomes

If any trigger fires, halt the audit, document the failure, and invoke Opus as second-pass reviewer.

---

## How to tell if tomorrow worked

Specific success and failure criteria, so faith can be restored or its absence can be named cleanly:

### Tomorrow's session SUCCEEDED if:

1. ✅ Phase 1 faith check passes — you read the materials and the path makes sense
2. ✅ Audit output exists at `docs/audits/2026-05-13-structural-audit.md` with explicit answers to each of the 9 structural questions
3. ✅ At least one of: (a) Atlas is verified charter-active via canary check, OR (b) there's a clear written reason why activation was deferred and what unblocks it
4. ✅ The audit identifies what needs to ship next (revised Step 1 or confirmed Step 1)
5. ✅ All work is committed to GitHub in focused commits with clear messages

### Tomorrow's session FAILED if:

1. ❌ More than 90 minutes pass without an audit output existing
2. ❌ The 9 structural questions are still unanswered at end of session
3. ❌ The session generates more open questions than it closes
4. ❌ Activation is attempted before audit is complete (this is the drift pattern from tonight)
5. ❌ Any of the four Path C tripwires fires and is ignored rather than escalated

### Tomorrow's session is AMBIGUOUS if:

- ⚠ Atlas activation works but the audit quality is uncertain
- ⚠ Audit completes but Phase 4 substrate work doesn't begin
- ⚠ You finish the session feeling "okay" but not "confident"

**Treat ambiguous as failure for purposes of next-day planning.** If you can't honestly say "yes, this is on the right path" at session end, write down what would make it a yes, and start the next session from there.

---

## Pre-flight checklist (read before starting tomorrow)

In order:

1. ☐ This brief: `docs/sessions/2026-05-13-pickup-brief.md`
2. ☐ Charter primary source: `docs/charter/outcomes-and-frustrations-2026-05-13.md`
3. ☐ Session record from tonight: `docs/sessions/2026-05-12-session-record.md`
4. ☐ Skim TL;DRs of three influence notes (don't read fully unless needed):
   - `docs/charter/influences/2026-05-13-anthropic-agent-skills-video.md`
   - `docs/charter/influences/2026-05-13-nate-herk-aios-course.md`
   - `docs/charter/influences/2026-05-13-nate-herk-tech-stack-and-frameworks.md`
5. ☐ Skim NEXT-SESSION-OPEN: `docs/sessions/NEXT-SESSION-OPEN.md`
6. ☐ Confirm `git pull` on VPS to get all of this onto the working clone

### Then decide:

- ☐ Is Phase 1 faith check passing? (Yes → Phase 2; No → reassess)
- ☐ Which audit path? (A, B, or C — recommended C)
- ☐ Who's at the table for tomorrow's audit? (Sonnet/Atlas alone, Opus alone, or Sonnet/Atlas with Opus on standby)

---

## What I am specifically NOT doing in this brief

- **Not telling you the audit's conclusions.** That's tomorrow's audit's job, not this brief's job. This brief sets up the audit; it doesn't preempt it.
- **Not picking adoption decisions on the three influences.** Those are audit outputs. This brief surfaces them as open questions.
- **Not committing the SOUL.md draft to git.** Still held in ephemeral workspace per tonight's decision. Finished version commits after activation.
- **Not running the audit tonight.** End session after this brief and presentation commit. Resume in ~10 hours.

---

## One last note (from operator to David)

Tonight you said the goal of tomorrow is **architectural confidence** — being able to read this and feel "yes, we're moving in the right direction."

The honest answer is that I (Sonnet) can't restore that confidence by writing more documents. What restores it is:

1. **Sleeping on it.** Reading this brief tomorrow with rested judgment will tell you more than reading it now would.
2. **Doing the audit.** The 9 structural questions are not abstract — they have concrete answers, and getting those answers concretely is what closes the uncertainty loop.
3. **Watching charter-active Atlas operate.** If he can produce a real audit that respects the charter, that's the strongest possible signal that the foundation is sound. If he can't, the failure itself is information — it tells you what to fix next.

Tonight's work is preparing the audit. Tomorrow's work is conducting it. Neither alone solves the confidence question. Both together should.

End of brief.
