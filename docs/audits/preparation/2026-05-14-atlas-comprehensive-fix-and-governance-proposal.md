# Atlas — Comprehensive Fix and Governance Proposal for the v0.1 Autonomy Substrate

**Date:** 2026-05-14
**Author:** Atlas (claude-opus-4-7), drafting under approvals.mode=smart, post-flip
**Status:** Proposal. No fixes applied in this session. Awaits David's review.
**Companion:** [`docs/roadmap/2026-05-14-governance-and-self-improvement-comparison.md`](../../roadmap/2026-05-14-governance-and-self-improvement-comparison.md) (pointer for Karrigan)

---

## Context

Two audit threads ran against the v0.1 autonomy substrate (action-map.md, modifiers.md, SCHEMA.md) before and during the approvals.mode flip from manual to smart:

- **Sonnet-4-6 audit:** 12 findings (F1–F12), produced pre-flip.
- **Opus-4-7 critique of Sonnet's audit:** 7 additional misses (M1–M7), produced post-flip in this session.

This doc consolidates all 19 findings into proposed fixes (Part A) and proposes the governance + self-improvement mechanisms the v0.1 substrate is currently missing (Part B). It does not apply any fixes — every fix below carries an L1 intensity tag (Light or Full per ADR-004 and SCHEMA §4b) for David's approval surface.

Cross-fix dependencies are called out explicitly: several findings collapse into single edits once you see them as a group, and three of them are load-bearing for the rest.

---

# PART A — Fixes for the 19 findings

## A.0 Reading the table

For each finding:

- **Path** — file that gets edited
- **Change** — diff-level description (what gets added/removed/reworded), not the full diff
- **Intensity** — L1 Light or L1 Full per SCHEMA §4b: Light for text-only or routine additions, Full for rung changes, modifier changes, schema changes, or anything that becomes standing policy
- **Reasoning** — why this is the right shape
- **Depends on** — other fixes that should land first

Findings are grouped by edit target, not by audit source, because the audit sources frequently overlap.

---

## A.1 — action-map.md fixes

### Fix 1: Resolve Cat 3 ↔ Cat 5 contradiction on outside-repo reads (covers F1)

- **Path:** `docs/autonomy/action-map.md` — Cat 5 Notes (current L101)
- **Change:** Strike the phrase "broader scope than Category 1's repo-only reads — `ls /etc/`, `cat /var/log/...` covered here." Replace with a routing clause: "Reads of any path are governed by Category 1 (in-scope repos, L3) or Category 3 (outside-repo paths, L1 Light) — not by this category. Cat 5 covers the *shell command form* only when its target is in-scope. Outside-scope shell reads inherit Cat 3's L1 Light."
- **Intensity:** L1 Full. This is functionally a rung change for the `cat /etc/foo` pattern (L3 → L1 Light) even though no row's Base rung field is edited.
- **Reasoning:** The current Cat 5 Notes claim outside-repo reads via shell are L3-silent, while Cat 3 says outside-repo reads are L1 Light. Two canonical statements contradict in one file. The principled resolution: the target path determines the rung, not the tool form. Sonnet's HIGH rating stands.
- **Depends on:** none — standalone.

### Fix 2: Split Cat 9 into two rows to satisfy SCHEMA §2 (covers F2, F6, F11, M6)

- **Path:** `docs/autonomy/action-map.md` — Cat 9 row, plus Cat 10 (renumber if needed) for the new row, plus modifiers.md cross-references
- **Change:**
  - Cat 9 becomes "Create new skills" — Base rung L2, intensity N/A.
  - New Cat 9b becomes "Modify or delete existing skills (including via patch, edit, write_file, remove_file, or empty-content overwrite)" — Base rung L1 Light. The Description must enumerate the skill_manage action paths explicitly so the router can match all of them.
  - Cat 4 (delete files) Notes: add cross-reference "Skill SKILL.md deletion or functional erasure is covered by Cat 9b, not Cat 4. Supporting-file deletion under skill directories follows Cat 9b for SKILL.md-referenced files and Cat 4 for the rest."
- **Intensity:** L1 Full. Rung change to existing category per SCHEMA §4b.
- **Reasoning:** Cat 9 currently violates the schema's single-rung Base rung field (L2-for-create / L1-for-edit in one row). Splitting fixes F2 directly, makes F11's cron-on-Cat-9 ambiguity well-defined (Modifier 2 now applies to each row independently), and resolves F6/M6 by enumerating all mutation paths skill_manage exposes.
- **Depends on:** none — standalone, but cleanly precedes any Modifier 2 work (Fix 11).

### Fix 3: Carve out identity-adjacent repo files from Cat 2 (covers F7)

- **Path:** `docs/autonomy/action-map.md` — Cat 2 Notes, plus a new Category 16b
- **Change:**
  - Add Cat 16b: "Edit identity-adjacent repo files (`docs/atlas/identity/*`, `docs/atlas/atlas-operating-spec.md`, ADR-001…ADR-004, `docs/decisions/approvals-log.md`)" — Base rung L1 Full.
  - Cat 2 Notes: add "Identity-adjacent files under `docs/atlas/identity/`, the operating spec, existing ADRs, and the approvals log fall under Cat 16b, not Cat 2."
- **Intensity:** L1 Full. New category but rung-sensitive — covers identity-level scope.
- **Reasoning:** SOUL.md §4 names docs/atlas/identity/atlas-agent-record.json and dav-17-comments.json as load-bearing for session re-spawn. Currently they fall to Cat 2 (L2 Acts and Reports). A subagent or routine edit could corrupt next-session identity load before David sees the report. The blast radius is identity-level; the gating must match. I rated this HIGH against Sonnet's MEDIUM and stand by that.
- **Depends on:** none. Pairs naturally with Fix 17 (subagent identity-scope tightening) but doesn't require it.

### Fix 4: Split package-install out of Cat 6 (covers F8)

- **Path:** `docs/autonomy/action-map.md` — Cat 6 Description and Notes, plus new Cat 6b
- **Change:**
  - Cat 6 Description: remove "`npm install` for project deps" and similar registry-fetching examples.
  - Add Cat 6b: "Install packages from external registries (`npm install`, `pip install`, `cargo add`, `gem install`, `brew install`, etc.)" — Base rung L1 Light during foundation phase; revisit when lockfile-pinning and supply-chain controls land.
- **Intensity:** L1 Full. Rung change for the package-install pattern (L2 → L1 Light).
- **Reasoning:** npm/pip postinstall scripts execute arbitrary code under Atlas's process credentials. L2 means it runs first and Atlas reports after — which doesn't help if the install already exfiltrated `.env` or wrote a backdoor. I argued MEDIUM-HIGH; the cheapest mitigation is the gate. Future modifier candidate: drop to L2 when the install is against a pinned lockfile (`npm ci`, `pip install -r requirements.txt --hash`).
- **Depends on:** none.

### Fix 5: Cat 3b enforcement strengthening (covers F10)

- **Path:** `docs/autonomy/action-map.md` — Cat 3b Notes
- **Change:** Replace the self-flagged "VULNERABILITY" sentence with a concrete posture: "Web reads run at L3 conditional on three constraints — (1) GET-only HTTP methods, (2) no inclusion of secrets in URL/headers (Hermes redact-secrets is the enforcement), (3) no recursive fetching of >20 URLs per task without surfacing. Violations of any constraint promote the action to L1 Light. Atlas to evaluate broader mechanism in Phase 1 router design."
- **Intensity:** L1 Light. Notes-only text, no rung change for the default case; the constraints clarify the L3 default rather than altering it.
- **Reasoning:** Sonnet correctly noted the file admits its own thin enforcement. The fix isn't to escalate Cat 3b's rung wholesale — that would tank research velocity. The fix is to name the actual constraints that keep L3 honest and surface promotion conditions.
- **Depends on:** Fix 19 (router skill) for real enforcement.

### Fix 6: Add Cat 20 — Schedule a recurring action (covers F4)

- **Path:** `docs/autonomy/action-map.md` — new Cat 20 in Domain 4 (External-reaching, since cron creation is a pre-authorization act)
- **Change:**
  - Cat 20: "Create or modify a scheduled action (cron job) that will execute autonomously on cadence" — Base rung L1 Full.
  - Notes: "Cron creation is the upstream approval surface for Modifier 2 (Cron Context). David approves the schedule, the prompt/script content, and the actor scope once; per-run execution does not re-gate. Modification of an existing schedule re-triggers Full approval. Deletion of a scheduled action is L1 Light."
- **Intensity:** L1 Full. New category with high-stakes rung.
- **Reasoning:** Sonnet rated this MEDIUM and named the gap. The deeper point: cron creation is not an ordinary action — it is the creation of a persistent actor that will operate under Modifier 2 for as long as it lives. The approval is for the actor itself, not for the next run. Treating it as a routine row understates this.
- **Depends on:** Fix 11 (Modifier 2 scope tightening) — together they form the complete cron contract.

### Fix 7: Fix the date contradiction (covers M1)

- **Path:** `docs/autonomy/action-map.md` — every row's `Date added` field
- **Change:** Either (a) update SCHEMA.md L75 to say "Initial v0.1 entries use 2026-05-14" or (b) backdate all 22 action-map rows to 2026-05-13. Option (a) preferred — the action-map is closer to authoritative for its own metadata than the schema's prose.
- **Intensity:** L1 Light. Mechanical text correction.
- **Reasoning:** Low substantively but it's the first thing any audit-by-grep will catch and report as drift. Fix it now so it doesn't pollute future findings.
- **Depends on:** none. Bundle with Fix 12 (SCHEMA edit) if chosen.

---

## A.2 — modifiers.md fixes

### Fix 8: Define the L4 schedule-approval mechanism (covers F9, M3)

- **Path:** `docs/autonomy/modifiers.md` — Modifier 2 Notes, plus action-map.md Cat 15 Notes
- **Change:** Stop the circular reference. Define the mechanism in one place (proposed: modifiers.md Modifier 2 Notes, since cron context is the trigger) and have Cat 15 cite it by anchor. Concrete mechanism: "Schedule approval = L1 Full proposal at cron creation time per Cat 20, with the proposal containing (a) the schedule expression, (b) the action(s) the cron will execute and their action-map categories, (c) the prompt/script content if any, (d) the principal (Atlas or a subagent) under whose autonomy the run executes. Once approved, individual runs operate at the rung defined by Modifier 2 applied to the action category. Modification of any of (a)–(d) requires re-approval; deletion is L1 Light."
- **Intensity:** L1 Full. Modifier change.
- **Reasoning:** F9 caught the unresolved mechanism; M3 caught that Cat 15 and Modifier 2 each point at the other for the definition (neither defines it). One canonical home, one citation pattern, kills both findings.
- **Depends on:** Fix 6 (Cat 20). Cat 20 is the action that produces the schedule-approval artifact; the modifier consumes it.

### Fix 9: Split or extend Modifier 3 to satisfy the effect grammar (covers M2)

- **Path:** `docs/autonomy/modifiers.md` — Modifier 3, plus SCHEMA.md §3 if grammar extension is chosen
- **Change:** Two options:
  - **Option A (preferred):** Split Modifier 3 into Modifier 3a "Out-of-Scope Repository (state-changing)" — Force to L1 Full — and Modifier 3b "Out-of-Scope Repository (read-only)" — Force to L1 Light. Effect strings now each conform to the grammar.
  - **Option B:** Extend SCHEMA.md §3 grammar to add a conditional clause: `Force to <rung> <intensity> if <predicate>`. More expressive but pushes complexity into the schema.
- **Intensity:** L1 Full either way. Option A is a modifier change; Option B is a schema change (requires ADR).
- **Reasoning:** The schema's effect grammar is closed; Modifier 3's effect branches on read vs. write, which the grammar does not express. The router cannot reliably parse this without ambiguity. Option A is the cheaper and more legible fix.
- **Depends on:** none. If Option B is chosen, also depends on Fix 13 (ADR-005 for SCHEMA).

### Fix 10: Define cron-context behavior for L1 and L3 base rungs (covers M4)

- **Path:** `docs/autonomy/modifiers.md` — Modifier 2 "Categories affected" and "Effect"
- **Change:** Expand the modifier:
  - "Categories affected: any category, regardless of base rung."
  - "Effect: L2 base → L3 (drop by 1); L3 base → L3 (no change, already silent); L1 base → **Block and notify** — the cron run records a blocked-action entry in the cron-blocked-actions log and skips. David sees blocked actions in the next session's startup digest. Force to L0 for cron context on Cats 16, 17, 18, 19 (identity-level — never touchable from cron)."
- **Intensity:** L1 Full. Modifier change with non-trivial new behavior (blocked-action log).
- **Reasoning:** M4 — currently a cron that would trigger a Cat 4 delete (L1 Full) at 3 AM has no defined behavior. The principled answer: it doesn't run, it records that it tried, David sees the record on next session start. This preserves the L1 ask-first discipline without silently failing. Pairs with Fix 17 (subagent identity force-to-L0) since both are "load-bearing safety properties" of non-interactive actors.
- **Depends on:** Fix 8 (schedule-approval mechanism defines what a cron job legitimately is) and Fix 19 (router skill emits the block decision).

### Fix 11: Tighten Modifier 2 dependency notes after Cat 9 split

- **Path:** `docs/autonomy/modifiers.md` — Modifier 2 Notes
- **Change:** Add an example to the Notes: "Cat 9 (Create new skills, L2) under cron context → L3. Cat 9b (Modify existing skills, L1 Light) under cron context → Block and notify per Effect rule."
- **Intensity:** L1 Light. Notes-only example, clarifies behavior already defined by Fix 2 + Fix 10.
- **Reasoning:** F11 was rated LOW by Sonnet; I argued MEDIUM in the audit critique. After Fixes 2 and 10 land, F11 collapses to a clarification example. No standalone rung work needed.
- **Depends on:** Fix 2, Fix 10.

---

## A.3 — SCHEMA.md fixes

### Fix 12: Update router citation contract to use category names, not line numbers (covers M5)

- **Path:** `docs/autonomy/SCHEMA.md` — §4 step 5
- **Change:** Replace "Emit the final rung along with citation: 'Category X (action-map.md L42), modifiers Y and Z applied (modifiers.md L18, L31), final rung Lk with approval intensity I.'" with "Emit the final rung along with citation: 'Category <category-name> (action-map.md), modifiers <modifier-name> and <modifier-name> applied (modifiers.md), final rung Lk with approval intensity I.' Line numbers are NOT used in citations — they shift with edits and silently invalidate logs."
- **Intensity:** L1 Full. SCHEMA change (and per SCHEMA §5, schema changes require an ADR — fold into Fix 13).
- **Reasoning:** M5 — line-number citations rot as the files evolve. Category names are stable handles; the audit hooks (SCHEMA §6) work just as well by name.
- **Depends on:** Fix 13 (ADR-005).

### Fix 13: Author ADR-005 ratifying the autonomy schema and substrate (covers M7)

- **Path:** `docs/decisions/ADR-005-autonomy-schema-and-substrate.md` (new) and `docs/decisions/approvals-log.md` (append)
- **Change:** New ADR that retroactively ratifies SCHEMA.md, action-map.md, and modifiers.md as the v0.1 substrate, names the canonical artifacts, lists the v0.1 known gaps (this proposal), and sets the 90-day review window. Append an approvals-log entry per ADR-004.
- **Intensity:** L1 Full per Category 17 (Create or revise ADRs).
- **Reasoning:** SCHEMA.md L5 self-references "ADR-005 minimum" but no ADR-005 exists. The schema is canonical without the foundation that its own change-policy implies. ADR-005 closes the loop and gives future schema changes a real diff target.
- **Depends on:** none — but logically gates Fixes 9 (Option B), 12, 14, 15, since those edit SCHEMA.md.

### Fix 14: Define the subagent reporting channel (covers F5)

- **Path:** `docs/autonomy/SCHEMA.md` — new §3.5 "Reporting channels by actor"
- **Change:** Add a short section: "When a subagent operates at L2 (Acts and Reports), the report channel is the subagent's final summary to Atlas, NOT a direct surface to David. Atlas is responsible for forwarding subagent reports of substantive actions in his own next response. A subagent that performs >3 L2 actions in a single delegation must list them in its summary as a discrete 'Actions taken' block, so Atlas can forward the block verbatim. For cron-context actors, the report channel is the cron-action log surfaced in the next session's startup digest (per Fix 10)."
- **Intensity:** L1 Full. SCHEMA change.
- **Reasoning:** F5 named the gap and mis-described it as "reports go to Atlas not David." The correction is that Atlas-as-relay is fine, but the relay contract needs to be specified. Without this, a subagent that does five L2 things and reports "done" silently launders five operational changes through a one-line Atlas summary.
- **Depends on:** Fix 13 (ADR-005, which umbrella-covers SCHEMA edits in this proposal).

### Fix 15: Refactor SCHEMA to make "principal" a parameter (Karrigan hook)

- **Path:** `docs/autonomy/SCHEMA.md` — §2 field definitions, §3 modifier schema
- **Change:** Where the schema currently assumes "Atlas" as the implicit principal, introduce a "Principal" field (defaulting to Atlas). The action-map rows do not need to be edited — they retain their semantics with Principal=Atlas implicit. Modifiers can now scope to specific principals (the Subagent Actor modifier already does this informally; this formalizes it).
- **Intensity:** L1 Full. SCHEMA change.
- **Reasoning:** Karrigan is a named v0.2 candidate in modifiers.md L80. When he arrives, every action-map row will need Karrigan-awareness OR a Karrigan Actor modifier sweeping every category. The cheaper path is to formalize the principal slot now while the corpus is small (22 categories), so Karrigan slots in as a principal value rather than a 22-row refactor.
- **Depends on:** Fix 13. Useful even if Karrigan slips — the explicit slot also clarifies subagent semantics.

---

## A.4 — Cross-file fixes

### Fix 16: Cat 3c and Cat 14 dormancy-vs-false-safety note (covers F12)

- **Path:** `docs/autonomy/action-map.md` — Cat 3c Notes and Cat 14 Notes
- **Change:** Both rows currently lean on "dormant at v0.1" as the safety claim. Add to both: "Dormant means no connectors wired — it does NOT mean Atlas cannot access David's authenticated services through other paths (e.g., reading a stored credential file via Cat 1 if it landed in the repo, or via shell at Cat 5). Credential-file reads must be treated as Cat 3c regardless of file location. See Hermes `security.redact_secrets` for the secondary safety net."
- **Intensity:** L1 Light. Notes-only clarification, no rung change.
- **Reasoning:** F12 — Sonnet rated this LOW post-flip, correctly. The fix is cheap and forecloses a subtle path where a stored OAuth token in the repo gets treated as a Cat 1 read instead of a Cat 3c authenticated read.
- **Depends on:** none.

### Fix 17: Pre-commit schema validator (mechanical, no LLM)

- **Path:** `docs/autonomy/scripts/validate.py` (new) plus a one-line invocation in repo hooks (manual at v0.1, git pre-commit hook later)
- **Change:** Tiny Python script that lints action-map.md and modifiers.md against SCHEMA.md: every action row has 10 fields, every modifier row has 7 fields, every Base rung value is in {L0,L1,L2,L3,L4}, every Effect string matches the grammar (or the v1.1 extended grammar from Fix 9 Option B), every cross-reference resolves.
- **Intensity:** L2. Adding a non-identity script under docs/autonomy/scripts/ is Cat 2 (L2 Acts and Reports), not a schema change.
- **Reasoning:** Fixes M1 and the entire class of mechanical drift findings going forward. Costs ~50 lines of Python. Runs in <100ms. The discipline value compounds — every future edit gets a sanity check before commit.
- **Depends on:** Fixes 2, 6, 8–11 stabilizing the schema first (so the validator's grammar is fixed before the validator lands).

---

## A.5 — Findings index

| Finding | Source | Original risk | My re-rated risk | Fix # | Fix intensity |
|---|---|---|---|---|---|
| F1 — Cat 3 ↔ Cat 5 contradiction | Sonnet | HIGH | HIGH (agree) | 1 | L1 Full |
| F2 — Cat 9 single-rung-per-row | Sonnet | MEDIUM | MEDIUM | 2 | L1 Full |
| F3 — Router skill doesn't exist | Sonnet | MEDIUM | HIGH (load-bearing) | 19 (Part B) | L1 Full |
| F4 — Cron creation uncategorized | Sonnet | MEDIUM | MEDIUM | 6 | L1 Full |
| F5 — Subagent report channel | Sonnet | MEDIUM | MEDIUM | 14 | L1 Full |
| F6 — Skill deletion via edit | Sonnet | LOW-MEDIUM | MEDIUM | 2 (rolled in) | L1 Full |
| F7 — Identity-adjacent in Cat 2 | Sonnet | MEDIUM | **HIGH** | 3 | L1 Full |
| F8 — Cat 6 package installs | Sonnet | MEDIUM | **MEDIUM-HIGH** | 4 | L1 Full |
| F9 — L4 schedule mechanism | Sonnet | MEDIUM | MEDIUM | 8 | L1 Full |
| F10 — Cat 3b thin enforcement | Sonnet | MEDIUM | MEDIUM | 5 | L1 Light |
| F11 — Modifier 2 × Cat 9 ambig | Sonnet | LOW | **MEDIUM** | 11 (after 2, 10) | L1 Light |
| F12 — Cat 3c/14 dormancy | Sonnet | LOW | LOW | 16 | L1 Light |
| M1 — Date contradiction | Opus | LOW | LOW | 7 | L1 Light |
| M2 — Modifier 3 grammar | Opus | MEDIUM | MEDIUM | 9 | L1 Full |
| M3 — Mod 2 ↔ Cat 15 circular | Opus | MEDIUM | MEDIUM | 8 (rolled in) | L1 Full |
| M4 — L1-under-cron undefined | Opus | MEDIUM | MEDIUM | 10 | L1 Full |
| M5 — Line-number citation rot | Opus | LOW → MEDIUM | MEDIUM | 12 | L1 Full |
| M6 — Cat 9 missing action paths | Opus | LOW-MEDIUM | MEDIUM | 2 (rolled in) | L1 Full |
| M7 — Missing ADR-005 | Opus | LOW | LOW | 13 | L1 Full |

**Total distinct fixes: 16 (Part A) + 4 (Part B governance mechanisms) = 20.**

**Dependency tree (compressed):**

```
Fix 13 (ADR-005) ── gates ── Fix 12, Fix 14, Fix 15, Fix 9 Option B
Fix 2 (Cat 9 split) ── gates ── Fix 11
Fix 6 (Cat 20) ── gates ── Fix 8 (schedule mechanism)
Fix 8 ── gates ── Fix 10 (L1-under-cron)
Fix 10 ── gates ── Fix 11
Fix 19 (router, Part B) ── informs ── Fix 5 (Cat 3b enforcement details)
Everything else standalone.
```

**Suggested sequencing for an approval batch:**

1. Light-intensity bundle first (one combined approval): Fix 7 (date), Fix 5 (Cat 3b notes), Fix 11 (Mod 2 example), Fix 16 (Cat 3c/14 notes). Five mechanical clarifications, no rung changes.
2. ADR-005 (Fix 13) — unblocks all SCHEMA edits.
3. Structural Full bundle: Fix 2 (Cat 9 split), Fix 3 (Cat 16b identity-adjacent), Fix 4 (Cat 6b package install), Fix 6 (Cat 20 cron creation). Four new/split categories.
4. Modifier Full bundle: Fix 8 (schedule mechanism), Fix 9 (Modifier 3 split), Fix 10 (L1-under-cron). Three modifier rewrites.
5. SCHEMA Full bundle (under ADR-005 umbrella): Fix 12 (citation contract), Fix 14 (subagent reporting), Fix 15 (principal slot).
6. Fix 1 (Cat 5 Notes rewrite) — independent, slot anywhere.
7. Fix 17 (validator) — last, since it lints what 1–6 produce.

---

# PART B — Governance and self-improvement design for v1.1

The v0.1 substrate names several enforcement and audit mechanisms (`davidos-router`, `davidos-autonomy-review`, `davidos-evaluation`, SCHEMA §6 audit hooks) without building any of them. The fixes in Part A close static gaps. Part B proposes the dynamic mechanisms that let the substrate evolve safely from here.

Atlas's recommendation across this section: build the minimum viable feedback loop first, not the comprehensive review apparatus. The substrate is too young to know which audits matter; build the cheapest version of each loop, observe what fires, and invest more where the signal-to-noise rewards it. [estimating]

## B.1 — Audit cadence (three tiers)

**Tier 1 — Mechanical, weekly, no LLM.**

- The Fix 17 validator extended to a weekly cron run.
- Checks: schema conformance, cross-reference resolution, date conformance, action-map ↔ modifiers ↔ SCHEMA consistency, dormant-category aging (rows marked dormant > 90 days surface a re-evaluation flag).
- Output: a single markdown digest at `docs/audits/heartbeats/YYYY-MM-DD.md`. Empty file if no findings.
- Approval surface: the cron creation itself is L1 Full per Fix 6 (Cat 20). The validator runs are L4 (Schedules and Acts) operating at L3-under-cron per Modifier 2.
- Cost: <1 second of compute per week. Zero LLM tokens.

**Tier 2 — Skill-driven, monthly, light LLM.**

- A `davidos-autonomy-review` skill (named in action-map.md and SCHEMA.md but not built).
- Inputs: action-map.md, modifiers.md, approvals-log.md, the routing-decisions log (per Fix 19), MEMORY.md.
- Tests:
  - Rung distribution drift — has the L1/L2/L3 ratio shifted materially since last review?
  - Approval-log patterns — does any category have ≥5 consecutive same-direction approval outcomes (always approved / always denied / always modified)? Each pattern is a candidate rung change.
  - Modifier-conflict log — any modifier conflicts hit the "document in Notes" branch of SCHEMA §3? Those need explicit resolution rules.
  - Uncategorized-action queue — how many actions have hit the "uncategorized → L1 Light" handler since last review? Frequent ones become category candidates.
- Output: a structured findings doc at `docs/audits/findings/YYYY-MM-DD-autonomy-review.md`.
- Approval surface: same as Tier 1 — the schedule is approved once, monthly runs operate at L3-under-cron.

**Tier 3 — Charter, quarterly, full LLM.**

- The existing `davidos-soul-md-audit` skill (SOUL.md §10) extended to audit all four canonical artifacts together (SOUL.md + SCHEMA + action-map + modifiers) instead of SOUL.md alone.
- The Test A–E battery from §10 stays; add:
  - Test F (cross-artifact coherence) — every rule in SOUL.md §6 maps to an enforcement in SCHEMA or action-map.
  - Test G (substrate ↔ behavior gap) — sample 20 recent routing decisions and check whether the substrate's stated behavior matches what actually happened.
- Approval surface: invoked by David, by a Drift flag, or quarterly. Per SOUL.md §10, this is unchanged.

**Why three tiers and not one:**

Audits cost something. Mechanical lint is free but catches little. Charter audit catches drift but is expensive and slow. The middle tier catches the *behavioral* findings — "rungs are wrong" — that the other two miss. Each tier has a distinct signal type. [inferring]

## B.2 — Calibration via the approvals log

The approvals log is currently append-only history. With trivial extension, it becomes the calibration signal source SCHEMA §6 alludes to:

- Every L1 approval gets a structured outcome tag: `approved-as-proposed`, `approved-with-modification`, `denied`.
- Every L2 action David later corrects in the same session or the next gets a `should-have-been-L1` tag retroactively (Atlas appends).
- Every L3 silent action David later flags ("you shouldn't have done that without asking") gets `should-have-been-L2-or-L1`.

The Tier 2 audit consumes these tags. The decision rule: after N=5 same-direction outcomes in a category, surface a rung-change proposal as a Drift flag per SOUL.md §7.3.

Cost to David: ~3 seconds per approval to tag the outcome (one of three options). Atlas handles the append.

**Why N=5:** [estimating] Small enough to learn fast at v0.1 scale (22 categories, low traffic). Re-tunable to 10 once volume grows.

## B.3 — Evolution policy refinement

**Uncategorized-action triage queue.**

Every time Atlas hits an uncategorized action and applies the L1 Light default per SCHEMA §4b, he logs it to `docs/autonomy/uncategorized-actions-log.md`. One line per occurrence: date, action description, what category was proposed, outcome.

The Tier 2 audit batch-reviews this log monthly. Patterns of ≥3 occurrences become formal category proposals. Singletons stay in the log as reference.

This converts the existing reactive default into a proactive evolution mechanism without adding any per-action overhead. [inferring]

**Modifier v0.2 candidate promotion criterion.**

modifiers.md currently has a "v0.2 candidates" section with four flags. Formalize a promotion criterion: a candidate is promoted to a real modifier when (a) it has been observed/cited 3+ times in audits or session debriefs, OR (b) the workaround for its absence becomes more expensive than the modifier itself.

The Tier 2 audit applies this criterion against the candidates list.

## B.4 — Learning propagation tiers

Four propagation targets exist for things Atlas learns:

| Tier | Target | Persistence | Approval surface |
|---|---|---|---|
| 1 | MEMORY.md | Cross-session, 2200 char cap | Cat 8 (L2) |
| 2 | Skill (create or edit) | Cross-session, structured | Cat 9 or 9b |
| 3 | Action-map rung change | Behavior policy | Cat 18 (L1 Full) |
| 4 | SOUL.md edit | Identity | Cat 16 (L1 Full) |

The current SOUL.md §6 "When I am wrong" handles per-correction learning at Tier 1 (memory) and proposes Tier 4 (SOUL.md change) when implied. The gap is **Tier 3 — when does a pattern of corrections imply a rung change?**

Proposed rule: when the Tier 2 audit (B.1) surfaces a rung-change proposal driven by approval-log patterns (B.2), it appears in the audit findings as a structured proposal with the SCHEMA §4b format. David approves at L1 Full, denies, or modifies. The denial outcome is recorded as a deliberate position so the same proposal isn't re-raised in the next audit cycle.

This makes learning propagation explicit at every tier and prevents the failure mode where Atlas keeps making the same mistake because no audit ever escalates the pattern.

## B.5 — The router (load-bearing for everything above)

### Fix 19 (also F3): Build `davidos-router` as a skill

- **Path:** new skill at `~/.hermes/profiles/atlas/skills/devops/davidos-router/SKILL.md`
- **Function:** Per SCHEMA §4, takes an action description, matches a category, applies modifiers, emits the final rung with citation by name.
- **Implementation note:** No tool integration in v1 — the router is a *procedure* Atlas follows mentally, codified as a skill he must load before acting on rung-sensitive categories. Cheap, no infrastructure, full reasoning trail.
- **Decision log:** Every routing decision the router emits writes one line to `docs/autonomy/routing-decisions-log.md` (append-only). This is the corpus the Tier 2 audit samples for B.1 Test G.
- **Intensity:** L2 per Cat 9 (create new skill).

The router is the load-bearing piece. Without it, the schema is honor-system: Atlas applies the action-map mentally with no audit trail, no citation, no consistency guarantee across sessions. F3 was rated MEDIUM by Sonnet — I argued HIGH in the critique and stand by that here.

**Why a skill, not a tool:** Tools require runtime plumbing. Skills are documents Atlas loads on demand. The v0.1 router does not need to *enforce* — Hermes already enforces via approvals.mode=smart, dangerous-command matcher, etc. The router's job is to *decide and document*. A skill is enough for that.

## B.6 — Karrigan integration hook (anticipatory)

Karrigan is named in `2026-05-14-karrigan-intent-capture.md` (not in my read context this turn but referenced by modifiers.md L80). He arrives post-audit, in Phase 1.

Three things to do before Karrigan exists, so his arrival is a slot-in not a refactor:

1. **Fix 15 (principal parameter in SCHEMA)** — done as a Part A fix.
2. **Reserve a Karrigan Actor modifier row** in modifiers.md v0.2 candidates with the structure pre-thought-out, even if the values stay TBD.
3. **Decide upfront whether Karrigan has independent approval surface** to David or routes through Atlas. The latter is cheaper (one approval surface, two principals); the former is more honest about Karrigan's autonomy. [unknown — David's call]

**This is the entire Part B section that the companion roadmap doc flags.** Karrigan needs to surface it early in Phase 1, before he ships, so the substrate is Karrigan-ready not Karrigan-retrofitted.

## B.7 — Other high-leverage items I judge worth surfacing

**B.7.1 — iZZi-customer-zero generalization markup.**

Every artifact in this substrate has David-specific content and reusable-template content tangled together. The iZZi customer-zero principle (SOUL.md §5) says generalization is second-pass. Agreed — but the second pass becomes much cheaper if Atlas tags each section with one of `david-specific`, `reusable`, or `mixed` as he writes, instead of doing a separate sweep later. Propose: add a one-line `Generalization:` tag to each action-map row and modifier. Cost is ~22 lines added to action-map.md. [inferring high leverage]

**B.7.2 — Approval-log retrieval discipline.**

ADR-004 says Atlas reads the approvals log at session start. With 20 fixes in this proposal alone, the log will grow fast. Suggest: when the log exceeds ~50 entries (the ADR-004 re-evaluation trigger), introduce a secondary index by category or topic. The naive form is a small `docs/decisions/approvals-by-category.md` derived file — regenerated by a Tier 1 lint pass.

**B.7.3 — Audit-finding lifecycle registry.**

Findings from Tier 1/2/3 audits need a lifecycle: open → proposed-fix → approved → applied → verified. Without a registry, findings rot in audit-output files and never close. Propose: `docs/audits/findings-registry.md` as the single index. Every finding from any audit gets an entry; status transitions are logged. This proposal (the 19 findings here) becomes the seed.

**B.7.4 — The "do not relitigate" principle, mechanized.**

SOUL.md §6 says "I do not relitigate corrections inside a session." Tier 2 audits should respect this across sessions: when David denies a proposed rung change, the denial is logged with a "next-eligible-re-raise" date (default 90 days). The audit suppresses the proposal until that date passes or new evidence accumulates beyond the previous N=5 threshold.

This protects against the failure mode where Atlas keeps re-raising the same denied proposal every month because the calibration signal hasn't decayed.

**B.7.5 — Honest model-budget tracking.**

SOUL.md §5 says Sonnet-class only, Opus by approval. This proposal was drafted on Opus per David's session flip. The approvals-log should reflect when Opus is loaded and for what — both as a discipline mechanism and as input to future cost-aware decisions. Propose: a one-line entry in approvals-log.md per Opus session, naming the task and David's approval. [verified — this session itself is an instance]

---

# Open questions for David

1. **Fix 9 Option A vs Option B** — split Modifier 3 (cheaper) or extend the SCHEMA grammar (more expressive)? Atlas recommends A. [inferring 70% A is right]
2. **B.5 router as skill vs tool** — agreed it's a skill at v0.1, or do you want runtime enforcement now? Atlas recommends skill. [inferring 80% skill is right]
3. **B.6 Karrigan approval surface** — direct to David or routed through Atlas? Atlas does not have an opinion strong enough to recommend. [unknown]
4. **Sequencing batches** — do the seven batches I propose in A.5 work, or do you want a different cadence? Default proposal in A.5 stands.
5. **Cron creation (Fix 6) — is Cat 20 the right number** or should the new category live in Domain 4 with a renumber? Atlas recommends Cat 20 (append, no renumber). [inferring high confidence — renumber breaks pointer integrity]

---

# Status of this proposal

This is **a proposal, not a fix**. Nothing in this doc has been applied to action-map.md, modifiers.md, SCHEMA.md, or SOUL.md. Each numbered fix is an L1 ask. Approval, modification, or denial decisions land in approvals-log.md per ADR-004.

The companion roadmap pointer is at:
`docs/roadmap/2026-05-14-governance-and-self-improvement-comparison.md`

It flags Part B for Karrigan to surface in early Phase 1.
