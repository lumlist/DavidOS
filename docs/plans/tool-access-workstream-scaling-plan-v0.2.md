---
artifact_type: plan
plan_id: tool-access-workstream-scaling
version: 0.2
created_at: 2026-05-27
updated_at: 2026-05-27
author: atlas
status: draft
schema_version: 0.1
supersedes: v0.1 (in-chat only, never written)
---

# DavidOS Tool-Access / Workstream-Scaling Plan v0.2

Status: DRAFT — approved in-chat for write. Scope: covers v1 (through FastDraft #2 and the run-up to #3). Anything beyond is named as deferred.

Note on path notation: in this document, a leading slash on paths like `/fastdraft/<id>/...` is **conceptual shorthand for the FastDraft artifact root**, not an absolute filesystem path. In implementation, repo-relative paths are written as `fastdraft/<id>/...` (no leading slash). All FastDraft artifact paths resolve relative to the active workspace root.

---

## Section 1 — v1 Execution: Three Lanes

v1 is not five orchestrated pipelines. v1 is three human-paced lanes that produce the artifacts the five-pipeline map describes. No queues, no dispatchers, no scheduled services.

**Lane v1-A — One FastDraft workflow**
- Active build: FastDraft #2 (med spa).
- Shape: sequential, gated, Atlas + David + worker agents (research, build) invoked as needed.
- Exactly one primary FastDraft build runs at a time. Light category scouting (≤2–3 categories) allowed in parallel; no second build.
- Next build = #3, triggered only by explicit David call after #2 teaches something.

**Lane v1-B — One knowledge-accretion process**
- Every FastDraft emits: Research Brief, Fact Pack (JSON-with-schema), Source Log (with completeness labels), Spatial Blueprint (JSON-with-schema), Build Log, Review Log (including Skill-Promotion Candidates and What-Failed sections), Pattern Card updates.
- Storage: Second Brain for canonical patterns/registry; project-local repo for project-specific artifacts. Executable Claude Code skill location resolves via Ari Repo Layout Note (G3.0).
- Pattern Curator + Reviewer are ROLES Atlas + David play, not separate agent identities (v1).
- Skill promotion: N=2 successful real uses → v0.1 eligibility, not "locked." Skills are living. Promoting one variant does NOT close the category.

**Lane v1-C — One David/customer loop**
- Pipeline 5 stays David-heavy by design. Nothing new built here in v1.
- No autonomous outbound. Spend/Auth/Data/Customer-facing gates remain Full.

---

## Section 2 — Five-Pipeline Conceptual Map

Status: **VOCABULARY + RESPONSIBILITY MAP. Not execution primitives.** Do not build queues/services from this section.

### Pipeline 1 — Lead + Fact

- Owner: Atlas (Research Coordinator role, v1; not personified).
- Supporting: research worker agent, retrieval adapters, Second Brain.

Research architecture (five roles):
- **R1 Intent Owner** — David sets strategic intent; Atlas drafts Research Brief.
- **R2 Source Retriever** — pluggable adapters (manual web, Perplexity manual, Tavily/Exa/Brave APIs deferred, Google Places manual/public-structured-source use only — API/Auth deferred). Adapter choice logged per retrieval.
- **R3 Fact Extractor** — LLM agent with strict extraction prompt + Fact Pack schema. Never invents.
- **R4 Fact Verifier** — separate pass, re-reads source vs. claim. Marks [verified|partial|contradicted|unverifiable].
- **R5 Fact Store** — Second Brain canonical + project-local snapshots. Raw source snapshots retained.

Source-completeness label on every raw source: `transcript-available | metadata-only | visual-only | source-inaccessible | needs-manual-transcript-extraction`. Default to `needs-manual-transcript-extraction` when unclear. Extractor refuses non-transcript-available without logged override. Forward-only labeling for v1.

Source Log row schema (one JSONL line per source):
- `source_id`, `url`, `retrieved_at`, `adapter`, `source_completeness`, `override_reason` (null unless override), `source_snapshot_path` (null unless retained), `linked_claims` (array of claim_ids).
- Adapter enum: `manual-web | perplexity-manual | tavily | exa | brave | direct-fetch | google-places-manual | other:<name>`.

**Data scope (v1):** FastDraft #2 uses public-source / public-web facts only.

- **Included** (no Data gate required): the target business's public website, public Google profile / manual listings, public social pages accessible without login, public directories, and publicly visible brand/assets.
- **Excluded unless a Data gate is explicitly approved in advance:** private data, login-walled content, paid/API/auth-based sources, customer-derived data, and any other non-public data.

Perplexity API, Tavily, Exa, Brave, Google Places API, and any structured-source API requiring auth all remain deferred behind G1.3 + Auth/Data gates.

Perplexity status: ONE adapter, manual use now. API adoption deferred behind Spend/Auth/Data gates + ≥5 real jobs of evidence.

**Gates:**
- G1.0 Light — Research Brief approved.
- G1.1 Light — candidate shortlist.
- G1.2 Light by default — Fact Pack handoff with verifier complete; **escalates to Full** if any load-bearing claim is `[contradicted]` or `[unverifiable]`, OR unverifiable-rate exceeds **15%** across all claims (v1 threshold, revisit after first real numbers).
- G1.3 Full — paid research API adoption (Perplexity, Tavily, Exa, Brave, Google Places API, etc.).
- G1.4 Full — Fact Store schema change once it has real data.

"Load-bearing" = any claim the Spatial Blueprint or build will reference. Marked in `facts.json` with `load_bearing: true`.

### Pipeline 2 — WOW Inspiration + Pattern

- Owner: Pattern Curator ROLE (Atlas + David, v1; no separate agent).
- Artifacts: Pattern Cards, Skill Registry/Index (Second Brain), Promotion Proposals.
- Seed source: `vault/04-presets/fast-draft-wow-pattern-menu.md` is the seed material for future Pattern Cards. The menu document is NOT immediately superseded — it remains source material until individual Pattern Cards are authored and approved.

Risk classes: `Approved | Candidate-Risky | Retired`.
- Candidate-Risky = internal experiments OK, blocked from customer-facing lead viewport / primary service explanation until proven.

Standing risk-class assignments:
- Sticky Narrative Anchor = Candidate-Risky.
- Premium Service Showroom = first promotion candidate after FastDraft #2 unless disproved.

**N=2 definition.** "Successful real use" of a pattern means BOTH:
- (a) the pattern shipped under G3.3 Full WITHOUT override (no bespoke layout reinvention applied to make it work), AND
- (b) David did not reject it as weakening owner-belief in the Review Log.

Owner-belief check: Review Log carries David-authored line — either `owner-belief: preserved` or `owner-belief: weakened: <reason>`. A pattern that received "weakened" cannot count toward N=2 regardless of other metrics. N=2 requires two qualifying ships across two different FastDrafts; one FastDraft cannot self-promote.

**Gates:**
- G2.1 Light — new Pattern Card.
- G2.2 Full — promotion to v0.1 skill (N=2 + David quality check).
- G2.3 Full — risk-class change.
- G2.4 Light — alternate variant within existing category.

### Pipeline 3 — Prototype Build

- Owner: Build agent (Claude Code with file-write + browser preview).
- Supporting: Ari (skill-loading, repo scaffolding), v8.2 reference folder READ-ONLY.

Default stack: vanilla HTML/CSS/minimal JS. Libraries (GSAP etc.) allowed with justification line in Build Log. Host repo being Vite/React does not change FastDraft default — FastDraft prototype output stays vanilla even when the host repo uses a framework.

Override surface (liberal): typography, spacing, palette, imagery, motion, content-density. NOT open-ended layout reinvention.

**Hard rules (no gate — agents refuse):**
- No Candidate-Risky patterns in lead viewport or primary service explanation.
- No writes into v8.2.
- No layout reinvention inside a skill.
- No absolute machine paths (e.g., `C:\Users\...`, `/Users/...`, `/home/...`) in HTML/CSS/JS/asset references. Workspace-relative paths only. Applies to `src`, `href`, `url()`, `import`, `fetch`, asset references, build configs.

Iteration loop shape (between G3.2 and G3.3): render → screenshot → vision/Gemini critique → revise → re-screenshot. Critique is INSIDE the iteration loop, not a separate gate.

**Gates:**
- G3.0 Light — Ari Repo Layout Note approved (first-class artifact before G3.1).
- G3.1 Light — Spatial Blueprint.
- G3.2 Light — first rendered draft.
- G3.3 Full — declared complete.

### Pipeline 4 — Review + Learning

- Owner: Reviewer ROLE (Atlas + David, v1; reviewer agent separate from build agent when both are agentic).
- Artifact: Review Log per FastDraft, with mandatory **Skill-Promotion Candidates** section AND mandatory **What Failed or Felt Off** section AND mandatory **Owner-Belief: preserved | weakened** line.
- Gates: G4.1 Light (Review Log draft), G4.2 Full (promotion candidate advancement → feeds G2.2).

### Pipeline 5 — Customer/Service Workflow

- Owner: David. Atlas drafts, preps, tracks.
- Hard rule: no agent sends anything on David's behalf. Ever.
- Gates: G5.1 Full (outbound), G5.2 Full (pricing/scope external), G5.3 Light (internal prep pack), G5.4 Full (post-engagement learnings filed back to Pipelines 1/2/4).

---

## Section 3 — Cross-Cutting Principles

### 3.1 Tool/Service Adoption Principle

Prefer existing high-quality tools/services when they reduce complexity, improve reliability, or integrate cleanly. Build custom only when: workflow is unique enough no off-the-shelf fits; privacy/control requires it; off-the-shelf creates more friction than it removes.

Default order: existing-in-stack → third-party with clean integration → lightweight glue → custom build.

Evidence requirement (hard for Spend/Auth/Data/Customer-facing; guidance for Light internal-only):
- one sentence: problem the tool solves the current stack doesn't
- one sentence: which existing option was ruled out and why
- one sentence: exit cost

Approval gates: Spend Full, Auth Full, Data Exposure Full, Customer-facing Integration Full, Light internal-only no-auth-no-cost = Light.

Applies especially to: research automation, CRM, mobile interface, memory/context management, WOW pattern workflows.

### 3.2 Single Control-Plane Principle (ADR-006 candidate, pending)

At any point there is exactly ONE control plane — one entity that routes work, owns gates, decides what runs next. In v1 and foreseeable future: Atlas. Every other agent/tool/service operates as worker, advisor, or passive ledger — never parallel orchestrator.

Enforcement: no tool gets gate authority; no tool gets routing authority; no tool gets autonomous write authority into governance state; orchestration-shaped proposals (words: dispatch/schedule/route/trigger/coordinate) trigger structural drift flag + David decision.

Status: to be drafted as ADR-006 in a separate proposal turn. Not folded into SOUL.md until ADR ratifies.

### 3.3 Atlas COI Disclosure Rule

Any time Atlas evaluates something that affects Atlas's own scope, authority, or role, Atlas opens with COI disclosure + names what evidence would change Atlas's view. Placement decision deferred: lives in this plan for now; later folded into SOUL.md §7 or an ADR depending on how it wears.

### 3.4 Self-Evaluation Triggers (replaces "96% memory" framing)

- Content-shape: (1) contradiction, (2) stale assumption suspected, (3) fuzzy recall, (4) cross-agent divergence.
- Event-shape: (5) major plan finalization, (6) memory write pending, (7) long session (~60+ turns / multi-workstream), (8) user correction, (9) cross-pipeline handoff.
- Capacity-shape (demoted): (10) memory near cap, (11) context window pressure.

Interrupt rules:
- Immediate interrupt: 1, 4, 5, 6, 8.
- Batched at natural breakpoints: 2, 3, 7, 9, 10, 11.

Atlas can observe: visible contradictions, citation vs. assertion, memory store sizes, user corrections in current session, turn count, imminent memory tool calls.

Atlas cannot observe: truth of old memory entries, concurrent-agent state, contents of past sessions not surfaced by session_search, on-disk repo drift since earlier session read, true context-window semantic utilization, intent shift since David wrote a doc.

David approval required: any memory write (Light min, Full for long-standing/USER PROFILE); load-bearing "still true" assumption on stale trigger; cross-agent divergence resolved in Atlas's favor before acting; compression/drop affecting downstream plan David hasn't seen.

Session close: self-eval pass folds into existing close checklist, no separate ritual.

### 3.5 Source-Completeness Labels

See §2 Pipeline 1.

### 3.6 Skill Specification Template (deferred)

A lightweight Skill Specification Template v0.1 will be drafted before the first N=2 promotion candidate emerges. Template work does NOT block FastDraft #2.

---

## Section 4 — AutoResearch as Constrained Optimization

Status: future optimization layer, not current default workflow. Plugs into specific places where preconditions hold.

**Five hard preconditions** (all required):
- P1 one editable file
- P2 locked evaluator
- P3 one scalar metric
- P4 time + token + dollar budget caps
- P5 keep/revert protocol (git commit on improvement, reset on regression)

**Failure-mode rules** (from transcript):
- Subjective "better" → blocks AutoResearch. Brand design, UX, pricing, "premium feel" stay human/Gemini/Atlas reviewed.
- Slow loop (eval > a few minutes/iter) → wrong shape; redesign or don't run.

**Pipeline fit:**
- Pipeline 1 strongest fit (fact extraction)
- Pipeline 2 poor (subjective)
- Pipeline 3 partial, late-stage, objective metrics only (load time, a11y, contrast, layout overlap, service visibility, responsive breakage)
- Pipeline 4 partial, v2+ (rubric scoring)
- Pipeline 5 no fit

**Isolation standing rules:**
- Loops never run in active/shared workspace.
- Required isolation: dedicated git-backed sandbox via clone, worktree, or feature branch with NO unrelated in-flight work.
- `git reset --hard` permitted ONLY inside isolated loop workspace, never in active workspaces.
- v1 loops run interactively only (David ~1hr kill range). No background daemon, no service, no scheduled cron.

**Workspace implication:** The active candidate workspace `izzi-revenue-dashboard` is NOT git-backed and stays non-git for FastDraft #2. Therefore AutoResearch cannot run from that workspace. The mini fact-extraction benchmark gets its own separate git-backed workspace, established as a later follow-up (see §7).

**First concrete application — mini fact-extraction benchmark:**
- 6 businesses (3 med spas + 3 scouting categories).
- Ground truth: services, hours, contact info, brand colors, logo presence/URL, source URLs.
- Atlas drafts ground truth with completeness labels; David spot-checks med spas; scouting drafts by Atlas/Ari, customer-facing later requires David review.
- Editable: extractor prompt + Fact Pack schema variants. Locked: scoring evaluator (F1 against ground truth). Metric: F1 on fixed test split. Budget: hard caps (e.g., ≤30 iters OR ≤$X OR ≤2h).
- Workspace: separate git-backed workspace, established as follow-up after FastDraft #2.

**Autonomy guardrails (v1):**
- No unattended overnight loops. David within ~1hr kill range. Hard token/time/dollar caps. Loosen after 1–2 clean runs.
- Output written to sandboxed location; promotion to production = separate gated step.

**Gates:**
- G-AR.0 Light by default; Full when paid tools, customer/customer-like private data, or substantial manual effort.
- G-AR.1 Full — first loop authorization. Loop Spec MUST include: `editable_file_path`, `evaluator_file_path`, `metric_definition`, `budget` (tokens/wall-clock/dollars), `worktree_path` OR `sandbox_path` (absolute), `rollback_method` (e.g., `git reset --hard <baseline_sha>` | branch deletion | clone discard), `budget_enforcement_method`, `kill_switch`, `expected_iterations`.
- G-AR.2 Light — subsequent loop runs in same loop.
- G-AR.3 Full — adopting any variant produced by loop into production.

Standing rule: every new metric/pipeline for AutoResearch requires its own G-AR.0 + G-AR.1, even if a prior loop succeeded in adjacent area.

---

## Section 5 — FastDraft #2 Artifact Conventions + Execution Playbook

### 5.0 Artifact Conventions

Canonical FastDraft layout (governed FastDrafts live here; legacy/free-form prototypes remain under `prototypes/`). The leading slash below is conceptual shorthand for the artifact root; in implementation, all paths are workspace-relative (no leading slash):

```
fastdraft/<id>/
  brief/         — Research Brief (brief.md + frontmatter)
  sources/       — Source Log (sources.jsonl) + raw snapshots under sources/raw/
  facts/         — Fact Pack (facts.json schema-validated) + verifier-report.md
  blueprint/     — Spatial Blueprint (blueprint.json schema-validated) + blueprint-notes.md
  build/         — prototype source (HTML/CSS/JS/assets) + build-log.md
  proofs/        — desktop-latest.png, mobile-latest.png + archive/<timestamp>-{desktop,mobile,desktop-above-fold,mobile-above-fold}.png
  review/        — review-log.md (Skill-Promotion Candidates + What-Failed + Owner-Belief line)
```

Legacy/reference convention preserved: `prototypes/<prototype-name>/index.html` + existing screenshots + `source-prompt.md`. v8.2 lives at `prototypes/premium-outdoor-living-v8-2-service-showroom/` and stays read-only reference.

**Screenshot tooling** (Q-T = C): existing `scripts/screenshot-prototype.ts` behavior is preserved for legacy/current prototypes. A separate FastDraft proof screenshot path is added alongside it, writing to `fastdraft/<id>/proofs/{latest,archive}`. Consolidation deferred until the new path proves out.

Minimal frontmatter on every `.md` artifact:
```yaml
---
fastdraft_id: <id>
artifact_type: brief|sources|facts|blueprint|build_log|review
created_at: <ISO8601>
updated_at: <ISO8601>
author: atlas|david|ari|<agent>
status: draft|review|approved|superseded
schema_version: 0.1
---
```

**v8.2 read-only enforcement** (staged):
- v1 immediate: agent instruction + plan hard refusal (no writes into `prototypes/premium-outdoor-living-v8-2-service-showroom/`).
- Ari Repo Layout Note (G3.0) proposes mechanical enforcement options (e.g., `.claude/settings.json` deny-write, OS-level deny-write ACL).
- No mechanical enforcement applied until Ari proposes exact content and David approves it.

### 5.0a FastDraft #2 Operator Context Pack (prerequisite)

Required before G1.0 and G3.0 execution. The Operator Context Pack is the v1 context spine that consolidates currently fragmented context across Atlas, Ari/Codex, Gemini, Claude Code, NotebookLM, Ruflo advisory, and Perplexity.

Proposed target file: `docs/plans/fastdraft-2/operator-context-pack.md` (separate G0.1 Light gate cycle).

**Contents** (single packet, versioned):
- Roles for this run (who plays which role: Atlas, Ari/Codex, Claude Code, Gemini, David).
- Gates catalog applicable to this run (§6 subset).
- Artifact paths and conventions (`fastdraft/<id>/` layout + frontmatter).
- Current plan reference (this document, version pinned).
- Source-completeness rules + Source Log row schema.
- **Data scope reminder:** public-source/public-web facts only unless Data gate explicitly approved. Inclusive/exclusive definition per §2 Pipeline 1 Data scope.
- Google/Gemini role definition for this run (vision/critique adapter, not orchestrator).
- Claude Code constraints (scoped file paths, write permissions, hard refusals).
- Ruflo status (advisory only, sandboxed, not integrated — see Appendix A).
- Open decisions list (items unresolved at run start; see §7).

**Repo Layout fields:** the Operator Context Pack may launch with Repo Layout fields (target directory, skill location, write permissions, v8.2 enforcement mechanism, screenshot tooling path, local server / browser verification path) marked `pending G3.0`. After the Ari Repo Layout Note is approved at G3.0, the Operator Context Pack is updated (status: `updated`, version bumped) with concrete values. G1.0 may proceed against a Context Pack with `pending G3.0` fields; G3.1 may not.

**Distribution:**
- Atlas reads it from Second Brain / VPS clone.
- Ari/Codex uses it locally as run reference.
- Claude Code receives scoped file paths + relevant context excerpts (not the whole packet).
- Gemini receives the pasted/uploaded packet for vision/critique passes.
- NotebookLM/Perplexity outputs fold back into the Source Log / Research Brief, not the Context Pack itself.

**Integration discipline:** Full direct agent integrations (cross-agent APIs, shared state stores, automated context sync) are DEFERRED. The Operator Context Pack is the v1 context spine. It is a document, not a service. It is hand-distributed, not auto-synced.

**Gate:** G0.1 Light — Operator Context Pack approved before G1.0 and G3.0 can pass. (Atlas drafts, David approves.)

### 5.1 Execution Playbook

Shape: sequential, gated, human-paced. No new infra spun up. Workspace = existing `izzi-revenue-dashboard` (non-git).

1. **Step 0a** — Atlas drafts FastDraft #2 Operator Context Pack. G0.1 Light approval. (Repo Layout fields may be `pending G3.0` at this point.)
2. **Step 0b** — Ari produces Repo Layout Note (proposed path: `<izzi-revenue-dashboard>/REPO-LAYOUT-NOTE.md`) covering target directory, skill location, write permissions, v8.2 read-only mechanism proposals, screenshot tooling path, local server / browser verification path. G3.0 Light approval. Operator Context Pack updated with concrete values after approval.
3. **Step 1** — Target selection. David picks med spa from shortlist (Atlas drafts shortlist).
4. **Step 2** — Research Brief (G1.0 Light).
5. **Step 3** — Agent-attempts-with-gates retrieval. At least 2 adapters (Perplexity manual + direct site browse + ideally one manual/public structured source like Google Places manual). Source-completeness labels on every entry. Default to `needs-manual-transcript-extraction` when unclear. **Public-source / public-web data only** (target's public website, public Google profile/manual listings, public social pages, public directories, publicly visible brand/assets) unless a Data gate is explicitly approved in advance.
6. **Step 4** — Extractor pass → Verifier pass → Fact Pack draft.
7. **Step 5** — Fact Pack handoff (G1.2 Light by default; escalates to Full if any load-bearing claim contradicted/unverifiable OR unverifiable-rate exceeds 15%).
8. **Step 6** — Pattern shortlist (3–5 candidates, likely incl. Premium Service Showroom). Sticky Narrative Anchor NOT in lead viewport / primary service explanation.
9. **Step 7** — Spatial Blueprint JSON-with-schema (G3.1 Light). Schema minimal — only fields #2 needs.
10. **Step 8** — Build in `fastdraft/<id>/build/` within `izzi-revenue-dashboard` workspace. Vanilla stack default; library justification in Build Log if used. Workspace-relative paths only.
11. **Step 9** — First rendered draft (G3.2 Light) → iteration loop (render → screenshot → vision/Gemini critique → revise → re-screenshot).
12. **Step 10** — Completion (G3.3 Full).
13. **Step 11** — Review Log filed within 48h (G4.1 Light). Includes Skill-Promotion Candidates section, What-Failed section, Owner-Belief line.
14. **Step 12** — David reviews promotion candidates. G2.2 Full only if promoting (probably not from #2 alone; N=2 likely triggered by #3).
15. **Step 13** — Pipeline 5: if shown externally, all outreach is David's (Atlas preps under G5.3 Light, outbound under G5.1 Full). If internal-only, only G5.4 Full to capture learnings.
16. **Step 14** — Decide whether to establish separate git-backed workspace for mini fact-extraction benchmark next (separate plan turn).
17. **Step 15** — #3 starts only on explicit David call.

---

## Section 6 — Gates Catalog (consolidated)

- Pre-run: **G0.1 L** (Operator Context Pack)
- Pipeline 1: **G1.0 L**, **G1.1 L**, **G1.2 L** (escalates to F on contradiction/unverifiable or >15% unverifiable-rate), **G1.3 F**, **G1.4 F**
- Pipeline 2: **G2.1 L**, **G2.2 F**, **G2.3 F**, **G2.4 L**
- Pipeline 3: **G3.0 L** (Repo Layout Note), **G3.1 L**, **G3.2 L**, **G3.3 F**
- Pipeline 4: **G4.1 L**, **G4.2 F**
- Pipeline 5: **G5.1 F**, **G5.2 F**, **G5.3 L**, **G5.4 F**
- AutoResearch: **G-AR.0 L** (F under paid/private/substantial-effort conditions), **G-AR.1 F**, **G-AR.2 L**, **G-AR.3 F**
- Tool adoption: Spend F, Auth F, Data Exposure F, Customer-facing Integration F, Light internal-only L

**Hard refusals (no gate — agents refuse):**
- Writes into v8.2.
- Candidate-Risky in lead viewport / primary service explanation.
- Autonomous outbound to any external party.
- Layout reinvention inside a skill (override surface limits stand).
- AutoResearch loop without all 5 preconditions.
- Orchestration role for any tool other than Atlas.
- Absolute machine paths in HTML/CSS/JS/assets — workspace-relative only.
- Ingestion of non-public/customer-derived data without an approved Data gate.

---

## Section 7 — Open Items / Deferrals / Follow-Ups

**Open items / deferrals:**
- Q3 Claude Code skill location — resolves via Ari Repo Layout Note (G3.0).
- Reviewer agent personification — deferred; Atlas + David v1.
- Spatial Blueprint schema authority — likely Second Brain; confirm during FastDraft #2.
- Pattern Curator personification — deferred; role only v1.
- External vs. internal use of FastDraft #2 — affects Pipeline 5 weight; David decides at Step 13.
- Perplexity / Tavily / Exa / Brave / Google Places API adoption — deferred behind G1.3 + Spend/Auth/Data gates + ≥5 real jobs evidence.
- CRM tool selection — deferred; revisit when research workflow has enough volume to define entity/relationship needs.
- Fact Store sidecar (relational) — deferred; revisit alongside CRM decision.
- Ruflo pilot — deferred to post-FastDraft #3 retrospective; see Appendix A.
- ADR-006 (Single Control-Plane Principle) — to be drafted as separate proposal turn.
- COI rule placement — lives in §3.3 of this plan; SOUL.md/ADR decision deferred.
- Tools Under Consideration list move to Second Brain — pending Gate O / write authority.
- Skill Specification Template v0.1 — deferred until before first N=2 promotion candidate; does not block #2.
- Screenshot tooling consolidation — deferred until new `fastdraft/proofs/` path proves out alongside legacy script.
- v8.2 mechanical enforcement — pending Ari Repo Layout Note proposal + David approval.
- Second Brain pointer/summary to this plan — deferred; avoid duplicating the full plan into Second Brain. A short pointer may be added later.

**Open follow-ups to revisit during this session:**
1. **Active workspace constraint:** Option A (existing non-git `izzi-revenue-dashboard`) is chosen for FastDraft #2. Decide later whether to (i) create a git-backed FastDraft workspace for FastDraft #3 onward, OR (ii) establish a separate git-backed benchmark workspace only, OR (iii) leave both decisions until #2 ships and we know more.
2. **Agent context fragmentation:** solve v1 with FastDraft #2 Operator Context Pack. Deeper integrations (cross-agent APIs, shared state stores, automated context sync) deferred. Revisit only if Context Pack hand-distribution proves too lossy across #2 and #3.

**Proposed future write targets** (each requires its own pre-write gate cycle):
- `docs/plans/fastdraft-2/operator-context-pack.md` — Operator Context Pack (G0.1 Light)
- `<izzi-revenue-dashboard>/REPO-LAYOUT-NOTE.md` — Ari Repo Layout Note (G3.0 Light, authored by Ari in active workspace)

---

## Appendix A — Tools Under Consideration

In-chat surface; not yet in Second Brain. Format: name | status | role | next-gate.

- **Ruflo** | advisory only, sandboxed, no install | pilot deferred to post-FastDraft #3 | revisit decision triggered by #3 retrospective; any pilot scoped read-only on a single artifact class
- **Perplexity API** | manual use only | retrieval adapter candidate | G1.3 Full + Spend/Auth/Data gates after ≥5 real jobs of evidence
- **Tavily / Exa / Brave search APIs** | not adopted | retrieval adapter candidates | same as Perplexity API
- **Google Places API / structured-source APIs** | manual/public use only; API not adopted | structured retrieval adapter | G1.3 Full + Auth/Data gates when first API job needs it
- **Attio / Folk / Notion-as-CRM / Airtable as CRM** | not adopted | CRM candidate | revisit after research workflow volume justifies entity/relationship needs
- **axe-core / Lighthouse** | not yet wired | AutoResearch evaluator candidate for P3 metrics | gate when first P3 loop proposed

---

## Appendix B — Decisions Log

Q1 vanilla default + libs w/ justification | Q2 med spa #2, ≤3 scouting, one primary at a time, #3 picked to stress-test | Q3 skill location resolves via Repo Layout Note | Q4 N=2 = v0.1 eligibility not lock; variants preserved | Q5 Premium Service Showroom = first promotion candidate post-#2 | Q6 Sticky Narrative Anchor = Candidate-Risky | Q7 v8.2 read-only | Q8 Spatial Blueprint = JSON-with-schema | Q9 liberal override surface, no layout reinvention | Q10 Skill-Promotion Candidates section in Review Log

Q-A Research Coordinator stays Atlas v1 | Q-B agent-attempts-with-gates on #2 | Q-C immediate interrupt 1/4/5/6/8, batch rest | Q-D session-end self-eval folds into close | Q-E hard evidence for Spend/Auth/Data/Customer-facing | Q-F TUC list yes, chat/handoff until Gate O

Q-G 3 med spas + 3 scouting (6 total) | Q-H Atlas drafts, David spot-checks med spas | Q-I no overnight v1, ~1hr kill range | Q-J default needs-manual-transcript-extraction | Q-K new metric/pipeline = own G-AR.0 + G-AR.1 | Q-L forward-only labeling | G-AR.0 = Light default, Full under paid/private/substantial-effort

Q-M lead with three v1 lanes, five-pipeline map as §2 | Q-N Ruflo on TUC chat surface + plan appendix; Second Brain entry when Gate O | Q-O Ruflo critiques via David relay | Q-P single control-plane = ADR-006 candidate, separate turn | Q-Q #3 by explicit David call | Q-R COI disclosure rule adopted

Q-S workspace A (existing non-git `izzi-revenue-dashboard` for #2) | Q-T screenshot tooling C (preserve legacy + add fastdraft proofs path) | Q-U 15% unverifiable-rate threshold | Q-V Skill Spec Template deferred, before first N=2 promotion candidate | Q-W `fastdraft/<id>/` canonical, `prototypes/` legacy | Q-X v8.2 enforcement staged (instruction v1, mechanical pending Ari proposal) | Q-Y pattern menu = seed source not yet superseded | Q-Z Repo Layout Note promoted to G3.0 Light

NEW (post Q-Z): FastDraft #2 Operator Context Pack required pre-run (G0.1 Light) | Open follow-ups: workspace git decision, agent context fragmentation

Pre-write edits (v0.2 final): E1 workspace-relative paths in implementation text | E2 Google Places = manual/public until G1.3/Auth/Data | E3 proposed target file paths recorded | E4 Operator Context Pack may launch with Repo Layout fields `pending G3.0`, updated post-G3.0 | E5 FastDraft #2 = public-source/public-web facts only unless Data gate approved | E6 (inline at write) Data scope clarified with explicit inclusive list (target's public website, public Google profile/manual listings, public social pages, public directories, publicly visible brand/assets) and exclusive list (private, login-walled, paid/API/auth-based, customer-derived, non-public data) | E7 Second Brain duplication deferred (§7)

— end of tool-access-workstream-scaling-plan-v0.2.md —
