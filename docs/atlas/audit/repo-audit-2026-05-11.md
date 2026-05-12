# DavidOS Ecosystem Repo Audit — 2026-05-11

Auditor: Atlas-equivalent agent, run from a clean Workspace session against fresh shallow clones of `lumlist/DavidOS`, `lumlist/familyAI`, and `lumlist/DavidAIStory`. Canonical truth used for "is this stale?" judgments: today's `README.md`, `docs/sessions/NEXT-SESSION-OPEN.md`, `docs/atlas/identity/README.md`, and `docs/decisions/ADR-001..003` in DavidOS (commit `5ba14ee`).

---

## Executive summary

- **DavidOS contains two parallel realities.** Today's truth (hermes-workspace + Anthropic OAuth + Paperclip-frozen + Atlas-as-memo-library) is captured in 6 new files at the root and under `docs/decisions/` and `docs/atlas/identity/`. Everything else — most of `docs/atlas/`, the entire `docs/sessions/` lifecycle, `scripts/session.py`, `scripts/render-daily-view.py`, `docs/atlas/identity/atlas-agent-record.json`, and several "v0" UI plans — still describes a Paperclip-Atlas world that has been frozen. **~25 files are stale enough to mislead a fresh Workspace session that loads them as context.**
- **The agent role section in `david-ai-workspace-v0.md` (the vision doc the new README points to) is 100% empty.** Eight agents are listed with no Purpose / Responsibilities / Approval-required fields filled. This is the single most visible gap relative to the vision principle "decisions need rationale, evidence, confidence level, revisit dates."
- **`docs/decisions/` is now the right ADR substrate, but only three ADRs exist.** Many prior decisions (OpenRouter daily cap, productivity-scheduler diagnosis, the Stage 2.5 / 2.6 / 2.7 bundle decisions David approved on DAV-17, the model-pin via `-z` finding, the Stage 1 raw/wiki/output/archive layout) are documented only in scattered memos. They should be retro-ADR'd or explicitly retired so the directory stays the single source.
- **`familyAI` looks frozen mid-sprint.** A solid Day-1/Day-2 scaffold + a deep product-strategy sprint (13 docs under `docs/product/`) exist, but `07-recommended-mvp.md` was intentionally not produced, Migration 001 is still un-applied, and there are no commits or doc updates that reference the 2026-05-11 stack migration. Nothing in familyAI knows hermes-workspace exists. That's not yet a bug (familyAI is downstream) but it's worth flagging: when DavidOS-foundation work claims to enable FamilyAI, no familyAI artifact corroborates it.
- **`DavidAIStory` is clean and minimal.** 10 files. The only stale element is the daily/weekly log content being frozen at 2026-05-08 — three days before the canonical migration this audit is anchored to. The "comeback story" hasn't captured the day Paperclip was deprecated, which is arguably the most important narrative beat of the week.

---

## Repo: DavidOS

### Inventory (file tree snapshot)

69 tracked files. Top-level layout:

```
README.md                              ← canonical (2026-05-11)
david-ai-workspace-v0.md               ← vision doc; agent role sections empty
.gitignore

docs/
  agent-operating-rules.md             ← pre-Paperclip era
  context-packs.md                     ← pre-Paperclip era
  daily-command-center.md              ← pre-Paperclip era
  daily-dashboard-v0.md                ← pre-Paperclip era
  diagnostic-loop-v0.md                ← pre-Paperclip era
  project-registry.md                  ← stale; FamilyAI/DavidOS only, no FamilyAI v2026-05-08+ artifacts referenced
  tool-stack-inventory.md              ← OpenRouter/Hermes-only era, no Workspace
  tomorrow-start.md                    ← 2026-05-08 era
  tomorrow-systems-building-plan.md    ← 2026-05-09 era
  weekly-review.md                     ← all TBD
  archive/README.md                    ← Stage-1 scaffold
  daily/README.md, today.{md,html}     ← rendered 2026-05-10 against Paperclip; outdated within hours
  output/README.md                     ← Stage-1 scaffold
  raw/README.md                        ← Stage-1 scaffold
  wiki/README.md                       ← Stage-1 scaffold
  decisions/                           ← NEW canonical
    README.md, ADR-001, ADR-002, ADR-003
  sessions/                            ← Stage-2.5/2.6 workflow, post-Paperclip orphan
    NEXT-SESSION-OPEN.md               ← NEW canonical
    drafts/{README, session-start-draft, session-end-draft, parking-lot}.md
    offline-queue/README.md
    submitted/{README, 2026-05-11T03-27-session-end, 2026-05-11T03-27-debrief}.md
  atlas/
    atlas-operating-spec.md            ← Paperclip-era; describes Atlas as preloaded persona
    agent-expansion-policy-v0.md       ← Paperclip-bound (7-field schema assumes Paperclip)
    agentic-os-video-evaluation-v0.md
    approval-policy-v0.md              ← references Paperclip throughout
    comment-conventions-v0.md          ← [SESSION START], [APPROVAL: ...] tags — only meaningful inside Paperclip
    context-refresh-protocol.md
    davidos-operating-ui-v1-plan.md           ← superseded by ADR-001
    davidos-operating-ui-v1-plan-revised.md   ← superseded by ADR-001
    davidos-operating-ui-v1-requirements.md   ← superseded by ADR-001
    davidos-session-workflow-v0.md            ← stage-2.5 design memo, Paperclip-bound
    domain-deep-dive-skill-v0.md
    memory-curation-policy-v0.md       ← references Paperclip docs API
    paperclip-atlas-activation-context.md     ← obsolete (Paperclip frozen)
    paperclip-reference-sources.md            ← obsolete (Paperclip frozen)
    paperclip-setup-plan.md                   ← obsolete (Paperclip frozen)
    paperclip-v0-workspace-structure.md       ← obsolete (Paperclip frozen)
    ruflo-atlas-v0-plan.md             ← describes Ruflo as candidate orchestrator; not chosen
    tool-selection-policy.md           ← references Paperclip, Hermes-via-OpenRouter, Opus
    memory-curation-policy-v0.md
    archive/{tool-selection-policy-v0-static-routing, davidos-session-workflow-design-v0}.md
    identity/                          ← NEW canonical
      README.md, atlas-agent-record.json, dav-17-comments.json
    runs/2026-05-09-atlas-activation-memo-v0.md
    templates/{session-start, session-end-notes, parking-lot, offline-work-item,
              decision-request, deep-dive-request, build-request, daily-note}.md

scripts/
  session.py                ← targets Paperclip API on 127.0.0.1:3100; reads `agentId` of paused Atlas
  session-config.json       ← `paperclipApiBase: http://127.0.0.1:3100/api`, DAV-22 issue ID
  render-daily-view.py      ← reads Paperclip API; would fail today (no service on :3100)
  repo-quality-review.sh    ← still useful; tool-agnostic
```

### Findings by dimension

#### Inconsistencies (stale claims vs canonical truth)

These files contradict today's truth. Each entry is `<path>:<line> — <stale claim>` followed by what canonical truth says.

1. **`docs/atlas/atlas-operating-spec.md:139-149` — "Atlas v0 is implemented through: Paperclip as the company-style control plane and primary UI ... Atlas as the system-layer AI systems consultant inside Paperclip."**
   Canonical truth (ADR-001 + ADR-003): Paperclip is FROZEN; daily driver is hermes-workspace; Atlas is a memo library, not a runtime persona.

2. **`docs/atlas/atlas-operating-spec.md:144` — "Hermes as the current Atlas runtime ... ideally configured to the strongest appropriate model."**
   Canonical truth (NEXT-SESSION-OPEN + README): "Sonnet-class only. No Opus without explicit approval." The "strongest appropriate model" phrasing is exactly the open door this policy was tightened to close.

3. **`docs/atlas/paperclip-atlas-activation-context.md:25` — "Model: Opus 4.7 through Hermes / OpenRouter if available."**
   Canonical truth: Sonnet-only via Anthropic OAuth (ADR-002). Opus is explicitly off the table without approval. OpenRouter is paused (ADR-002).

4. **`docs/atlas/identity/atlas-agent-record.json:13` — `"model": "anthropic/claude-sonnet-4.6"` (with `"effort": "high"`).**
   Sonnet is correct as a model choice, but the model ID is from Paperclip's Hermes adapter config. If someone re-spawns Atlas from this record in Workspace, the literal `anthropic/claude-sonnet-4.6` string won't be a valid Workspace model selector and the `adapterType: hermes_local` is now meaningless. The README at `docs/atlas/identity/README.md` says "use as inputs to fresh sessions" — but the file itself doesn't say which fields are still load-bearing.

5. **`docs/atlas/paperclip-setup-plan.md` (entire file) — "By the end of the working session, Paperclip should capture the initial DavidOS operating system with Atlas activated."** Whole document is a setup plan for the now-frozen tool. ADR-003 supersedes.

6. **`docs/atlas/paperclip-reference-sources.md` (entire file) — "Local Paperclip repo mirror: /home/hermes/reference/paperclip ... Before recommending non-trivial Paperclip setup changes, Atlas should review the relevant local Paperclip docs."** Obsolete by ADR-003.

7. **`docs/atlas/paperclip-v0-workspace-structure.md:9-15` — "Paperclip is the current UI/control plane ... Active Agent: Atlas."** Obsolete by ADR-001/003.

8. **`docs/atlas/davidos-operating-ui-v1-plan.md` (entire 250+ lines) and `-plan-revised.md` (similar size) — both describe Paperclip + Obsidian-MCP + Langfuse + a thin custom Daily Operating View as v1.** ADR-001 supersedes with hermes-workspace. The v1 plans should be retired or at minimum prepended with a "SUPERSEDED — see ADR-001" banner.

9. **`docs/atlas/davidos-operating-ui-v1-requirements.md:14-23` — "Paperclip as primary control plane ... Obsidian-MCP over the DavidOS git repo ... Langfuse (self-hosted) ... Daily Operating View."** Same staleness as #8.

10. **`docs/atlas/davidos-session-workflow-v0.md` (entire) — describes the session lifecycle entirely in terms of Paperclip issue comments (`[SESSION START]`, `[SESSION END]`, `[APPROVAL: …]` tagged on a Paperclip session-tracker issue).** Paperclip is frozen; this lifecycle has no executor today. NEXT-SESSION-OPEN.md is the actual session memo now.

11. **`docs/atlas/approval-policy-v0.md` (entire) — every approval flow describes posting `[APPROVAL-REQUEST]` comments on Paperclip issues; structure assumes a heartbeat parser; references DAV-17 § numbers throughout.** The substantive policy (what requires approval, what's pre-approved) survives the migration — but the *mechanism* (Paperclip comment tags) does not. Either retain as a policy spec with a note that mechanics need a workspace-native replacement, or rewrite for workspace.

12. **`docs/atlas/comment-conventions-v0.md` (entire) — 16-tag taxonomy for Paperclip comments.** Same: the taxonomy is genuinely useful but the substrate is gone. Workspace conversations don't have `[APPROVAL: code-change]` comment threads.

13. **`docs/atlas/memory-curation-policy-v0.md:8-14` — "Storing prose memory in Paperclip DB fields ... use `output/` and attach as a Paperclip document; the document's body is also persisted in Paperclip DB."** Paperclip DB is no longer in scope.

14. **`docs/atlas/agent-expansion-policy-v0.md:38-43` — Permissions block has "projects: [<project-id>, ...]   labels: [<label>, ...]   # which Paperclip labels does this agent watch".** Paperclip-projects and labels don't exist any more. The 7-field schema itself is reusable; the field names are not.

15. **`docs/atlas/tool-selection-policy.md:51-53` — "Hermes: repo-grounded work, structured research, long-running analysis, drafting, and documentation support."** Reads as if Hermes is a sibling of Workspace; the current architecture has Hermes (gateway/runtime) underneath Workspace (UI). Minor but propagates confusion.

16. **`docs/atlas/tool-selection-policy.md:129` — "Atlas should avoid bias toward any current tool, including Paperclip ... or custom DavidOS tooling."** Paperclip should drop from the list now that it's not active.

17. **`docs/atlas/runs/2026-05-09-atlas-activation-memo-v0.md` — describes the DAV-1 Paperclip activation run.** Historical artifact, but should be re-tagged "historical — Paperclip era, see ADR-003" or moved under `docs/atlas/archive/`.

18. **`docs/atlas/ruflo-atlas-v0-plan.md` (entire) — proposes Ruflo / Claude Flow / Claude Code as candidate orchestrators.** The "Atlas runtime" question was effectively closed by adopting hermes-workspace. Ruflo and Claude Flow are not in scope. This doc should be archived.

19. **`docs/daily/today.md` — generated 2026-05-10 from the now-defunct Paperclip API.** Lists DAV-17, DAV-22, etc., references `http://127.0.0.1:3100/issues/...`. Today.md should either be regenerated against the new stack or removed until the renderer is ported. Currently misleading.

20. **`docs/daily-command-center.md` and `docs/daily-dashboard-v0.md` — both predate the Daily Operating View work in `docs/atlas/davidos-operating-ui-v1-*.md` AND postdate them depending on which doc you read.** Three "daily" surfaces (`daily-command-center.md`, `daily-dashboard-v0.md`, `daily/today.{md,html}`) coexist without a pointer telling a fresh reader which is canonical.

21. **`docs/tool-stack-inventory.md:16` — "Paperclip | Possible future AI labor control plane | ... Test later".** Wrong direction — Paperclip has been tested and frozen. Should say "Tested, frozen 2026-05-11. See ADR-003."

22. **`docs/tool-stack-inventory.md:15` — "OpenRouter | Model access for Hermes | Flexible model routing | Key/security and model cost management needed | Keep".** Wrong — ADR-002 paused OpenRouter.

23. **`docs/tomorrow-start.md`, `docs/tomorrow-systems-building-plan.md` — both reference May 8/9 plans that have been executed.** Useful as historical record; not useful as forward-looking. Should move under `docs/archive/`.

24. **`docs/project-registry.md:10-12` — "FamilyAI | Active | Define MVP wedge ... Active Tools | ChatGPT, Hermes, GitHub, Supabase, Vercel | TBD".** Doesn't include Workspace; uses "ChatGPT" which is not in the canonical stack.

25. **`docs/agent-operating-rules.md:65-67` — "Hermes main agent works. Hermes delegation passed a simple subagent smoke test, but prior research delegation failed to write expected files."** Stale runtime observation from May 8.

26. **Last-name typo audit (Mizzard).** I grepped every file for "Mizzard" — zero matches. The instruction warned about it; nothing in the current tree exhibits it. Worth noting since this was an explicit check.

#### Redundancy

1. **Three overlapping daily surfaces.** `docs/daily-command-center.md`, `docs/daily-dashboard-v0.md`, `docs/daily/today.md`. All three try to be "the start-of-session view." The first two are stub templates with `TBD` filled in; the third is a snapshot from a tool no longer running. Consolidate to one canonical surface (NEXT-SESSION-OPEN.md is closest right now).

2. **Three v1 UI memos that describe the same architecture.** `docs/atlas/davidos-operating-ui-v1-requirements.md` (the DAV-16 memo, 30k chars), `docs/atlas/davidos-operating-ui-v1-plan.md` (DAV-17 first cut, 24k chars), `docs/atlas/davidos-operating-ui-v1-plan-revised.md` (DAV-17 post-approval revision, 12k chars). All three describe a stack that ADR-001 has replaced. Should be archived under one umbrella note "Pre-Workspace v1 design memos (superseded by ADR-001)."

3. **Two session-workflow specs.** `docs/atlas/davidos-session-workflow-v0.md` (the Stage 2.5 v0 spec) AND `docs/atlas/archive/davidos-session-workflow-design-v0.md` (the prior design memo). The archive file is correctly archived; the active one is now itself obsolete and should follow.

4. **Two tool-selection policies.** `docs/atlas/tool-selection-policy.md` (active draft) and `docs/atlas/archive/tool-selection-policy-v0-static-routing.md` (older static version). Correctly versioned, but the active one still references Paperclip / Ruflo / Opus and overlaps significantly with `docs/agent-operating-rules.md` (a pre-Atlas-era doc covering similar ground at the project level).

5. **Approval gate rules appear in four places.** `david-ai-workspace-v0.md:179-202` (the vision-level list), `docs/agent-operating-rules.md:7-31`, `docs/atlas/atlas-operating-spec.md:61-71`, and `docs/atlas/approval-policy-v0.md` (the canonical Paperclip-tagged version). Three of them say roughly the same thing in slightly different wording; the fourth attaches the mechanism. After the migration there's an opportunity to pick one canonical list.

6. **Two project registries.** `docs/project-registry.md` and the "Project Registry" table inside `david-ai-workspace-v0.md`. They disagree (the vision doc only lists FamilyAI and Personal AI Workspace; the registry adds the AI Workspace Diagnostic Service business idea). One should reference the other.

7. **Template proliferation under `docs/atlas/templates/`.** 8 templates exist; `daily-note.md`, `decision-request.md`, `deep-dive-request.md`, `build-request.md` are still useful regardless of substrate. The `session-start-template.md`, `session-end-notes-template.md`, `parking-lot-template.md`, and `offline-work-item-template.md` are scaffolding for the Paperclip-bound session workflow. Either port to workspace-native form or archive.

#### Noise

1. **`david-ai-workspace-v0.md:33-97` — 8 agent role sections, every Purpose/Responsibilities/Approval-required field empty.** This is the vision doc the new README explicitly elevates as "the durable why." Currently it advertises 8 agents with nothing to say about any of them.

2. **`david-ai-workspace-v0.md:108-114` — Work Queue with empty `Today / This Week / Waiting on Agent / Waiting on Me / Blocked` sections.** Header without body. Either populate, point to NEXT-SESSION-OPEN as the live version, or delete.

3. **`david-ai-workspace-v0.md:118-131` — Decision Log / Automation Candidates / Tool Stack — three empty markdown tables with only headers.** Decision Log is now `docs/decisions/`. Tool Stack is now the README. Automation Candidates is unfilled. Either point to the live homes or delete the tables.

4. **`david-ai-workspace-v0.md:135-166` — Context Packs section is an empty form with bullet stubs ("Professional background:", "Current priorities:", etc.).** `docs/context-packs.md` has the filled-out version. The form in the vision doc is dead weight.

5. **`docs/daily-command-center.md` and `docs/weekly-review.md` — both templates with every field set to TBD.** Possibly intentional as templates, but neither is named `*-template.md`, neither lives under `docs/atlas/templates/`, and neither is referenced from the canonical surface. Two unfilled forms hanging in the docs root.

6. **`docs/sessions/drafts/parking-lot.md`, `session-end-draft.md` — both contain only template text (no real entries).** Inert per design, but worth noting they exist with no current data. Fine — these are working drafts. Just flagging that "look at the parking lot" surfaces nothing today.

7. **`scripts/session.py` and `scripts/render-daily-view.py` — both unrunnable today.** `session.py` would call `http://127.0.0.1:3100/api` (Paperclip) and post to DAV-22 (a Paperclip issue ID). `render-daily-view.py` reads the same API. Neither has been deleted; both will silently fail on the next session-start attempt. Either remove or stub with a clear "Paperclip-bound; see ADR-003" message.

8. **`scripts/session-config.json` — names a `sessionTrackerIssueId` and `agentId` that only exist inside the frozen Paperclip data dir.** Dead config.

#### Vision alignment

Against `david-ai-workspace-v0.md` design principles (lines 11-20):

| Principle | Current state |
|---|---|
| "AI should increase clarity, not create noise." | **Partial.** The canonical 6 new files do this well. The remaining 25 stale Paperclip-era files actively create noise — a fresh Workspace session loading the repo as context would inherit two contradictory worldviews. |
| "Decisions need rationale, evidence, confidence level, revisit dates." | **Mostly met.** ADR-001..003 do this well — each has Context / Decision / Rationale / Consequences / Re-evaluation triggers. The pre-ADR decisions are scattered (in plan memos, in session debriefs, in `docs/atlas/approval-policy-v0.md`). They could be back-filled. |
| "Use stronger models for make-or-break decisions; cheaper for routine." | **Codified now** (ADR-002 commits to Sonnet-only with API-key fallback). The old "Opus 4.7 through Hermes / OpenRouter" line in `paperclip-atlas-activation-context.md` directly contradicts the new policy and is the kind of stale residue that would mislead an agent. |
| "Durable context in structured docs, not scattered chats." | **Met in principle, contradicted in practice.** Six fresh canonical files versus tens of thousands of words in `docs/atlas/` that describe a different operating model. A long-running Workspace agent fed this corpus would have to weigh which of two parallel realities to act on. |
| "Automate only after manual understanding." | **Met.** No new automation has shipped since ADR-001; scheduling has not been re-introduced. |
| "Approval gates for spending, messages, production edits, accounts, legal/privacy, major business decisions." | **Met in policy, mechanism gone.** The substantive list is duplicated in 4 places (see Redundancy #5); the Paperclip `[APPROVAL: <kind>]` mechanism that enforced it is no longer running. There's currently no workspace-native equivalent. |

#### Gaps

1. **Agent role definitions empty.** `david-ai-workspace-v0.md:33-97` — eight agents named with no fields filled. Either delete the section or fill the seven that are still part of the post-migration vision (Chief of Staff, Research, Product Strategy, GTM, Personal Life Admin, Health and Fitness, Finance/Admin, Tooling and Automation).

2. **No `docs/architecture/` or `docs/workspace/` directories** despite the README pointing to them ("`docs/architecture/` — stack diagrams ...; `docs/workspace/` — Workspace baseline configuration"). The README documents intent; the directories don't exist yet. Either create stubs with READMEs or remove the references.

3. **No baseline-config doc.** NEXT-SESSION-OPEN.md cites `docs/workspace/baseline-config.md` as "next entry point." The file does not exist.

4. **No `docs/decisions/README.md` ADR-creation template.** The directory README is clean and good. An `ADR-template.md` next to it (or a one-line "copy ADR-001 to start" pointer) would lower the bar for the next ADR. Especially since several decisions are still un-ADR'd (e.g., the OpenRouter cap, the Stage-1 folder layout, the choice to keep `agent-expansion-policy-v0.md`'s 7-field schema even though Paperclip is gone).

5. **No retro-ADR for the Paperclip productivity-scheduler diagnosis.** This was a multi-hour investigation that drove the migration. ADR-003 references it; no standalone diagnosis memo exists in the live tree (it's in the Session Debrief comments under `docs/sessions/submitted/2026-05-11T03-27-debrief.md`, but a future iZZi customer inheriting this pattern would not find a clean "here's why Paperclip's productivity-review scheduler is unworkable" doc).

6. **No iZZi customer-zero template doc.** The README and ADRs both invoke the "iZZi customer-zero" pattern ("every config/architectural decision should be reusable across future iZZi AI Systems customers OR explicitly David-specific"). There is no single doc that says what reusable looks like. Pattern is asserted; pattern is not visible.

7. **No update to `david-ai-workspace-v0.md` to reflect the migration.** The vision doc still says (line 24) the Core Areas include "FamilyAI / FamilyOS" — unchanged. It does not reflect the foundation-first sequencing decision (DavidOS → FamilyAI → iZZi Builder Services) that the README and NEXT-SESSION-OPEN both now treat as canonical.

#### Customer-zero test

For each David-specific artifact: is it appropriately David-specific (his personal data, goals) or should it become a reusable iZZi pattern?

| Artifact | David-specific or generalize? | Notes |
|---|---|---|
| `docs/context-packs.md` Personal Context Pack | David-specific | Personal background, sensitive boundaries — correctly David-specific. |
| `docs/context-packs.md` FamilyAI Context Pack | David-specific to FamilyAI | Correctly project-specific. |
| `docs/context-packs.md` Tooling Context Pack | **Should generalize.** | Hard-codes David's VPS IP, SSH user `hermes`, repo paths. A future iZZi customer should inherit a parameterized version (`operator_name`, `host_ip`, `repo_root`). |
| `david-ai-workspace-v0.md` Agent Roles (empty) | **Should generalize.** | The eight agents (Chief of Staff, Research, etc.) are the roster any iZZi customer would inherit. Fill these as customer-zero defaults; let each customer override. |
| Approval gates list | **Already general.** | The list ("spending money, sending messages, editing production systems, ...") is content-free of David specifics. Good. |
| ADR format | **Already general.** | ADR-001..003 are tightly scoped to DavidOS, but the structure (Context / Decision / Rationale / Consequences / Re-evaluation) is the reusable template. |
| `docs/atlas/agent-expansion-policy-v0.md` 7-field schema | **Generalize, drop Paperclip names.** | Role / Guardrails / Permissions / Memory boundaries / Runtime validation / Approval policy / Success metrics is genuinely a reusable customer-template field. Strip Paperclip-specific Permissions sub-fields. |
| `docs/atlas/templates/{decision-request,deep-dive-request,build-request}.md` | **Already general.** | Generic enough to be the reusable issue-template kit. |
| `scripts/repo-quality-review.sh` | **Mostly general; David-paths leak.** | The case statement (line 11-18) hard-codes `/home/hermes/projects/...` paths. Should accept `$REPO_ROOTS` via env. |
| Daily Operating View concept | **Generalize.** | The idea (single-page rollup of pending approvals / open decisions / system health / memory freshness) is the reusable iZZi customer pattern. The current implementation is Paperclip-coupled — that's where reuse breaks. |

---

## Repo: familyAI

### Inventory (file tree snapshot)

97 tracked files. Day-2 scaffold of a pnpm + Next.js monorepo plus a thorough product-strategy sprint:

- **Code/infra scaffold:** `apps/web/` (Next.js + Tailwind), `packages/{agents,db,evals,shared,tools,ui}/` (each with `src/index.ts` placeholder + README + tsconfig + .eslintrc), `infra/`, `evals/`, GitHub Actions CI (`.github/workflows/ci.yml`), Vercel preview deploy, Prettier/EditorConfig. Real but skeletal.
- **Supabase:** one migration file `20260507221532_001_foundation.sql`, locally validated, never applied to remote.
- **Day-1 docs** (`docs/00-*` through `docs/10-*`): founder brief, setup log, MVP PRD, system architecture, agent catalog, permission model, memory policy, security checklist, eval plan, 30-day roadmap, open questions.
- **Day-2 docs** (`docs/11-supabase-schema-plan.md`, `12-first-migration-plan.md`, `13-venture-thesis-and-mvp-sprint.md`).
- **Product sprint (`docs/product/01-*` through `13-*`):** opportunity map, customer segments, wedge scorecard, GTM options, MVP candidates, trust/safety/privacy model, customer discovery plan, backend implications, strategy critique, founder conviction, research sprint plan. 12 docs. **Note: `07-recommended-mvp.md` is deliberately absent** (per D-004 in `08-decision-log.md` — recommendation withheld pending founder review + customer discovery).
- **Prompts** (`docs/prompts/`): Day-1 generation, Day-2 scaffold, Day-2 schema planning, Day-2 first-migration, plus product-sprint prompts.

### Findings by dimension

#### Inconsistencies

1. **`docs/00-founder-brief.md:64-104` lists "Initial Stack" including Clerk, Trigger.dev/Inngest, Stripe, Resend, PostHog, Sentry, LangSmith/Helicone, RuFlo "later".** None of these are installed. The README at the root says "no product functionality yet." That's accurate, but the brief reads as if these are decided commitments, not candidates.

2. **`docs/00-founder-brief.md:97-102` — "Experimental Multi-Agent Sandbox: RuFlo later, not in the critical path."** Consistent with the DavidOS ruflo-atlas-v0-plan.md (which proposes Ruflo as candidate). DavidOS has since dropped Ruflo from active consideration (adopted hermes-workspace instead). FamilyAI doesn't know this.

3. **No reference anywhere in familyAI to hermes-workspace, Hermes the agent runtime, Atlas, DavidOS as the foundation, or the 2026-05-11 migration.** That's not a contradiction per se, but the DavidOS README claims FamilyAI is downstream of the new foundation. FamilyAI is at the moment unaware of any of that. Worth noting because the cross-repo story breaks: DavidOS says "FamilyAI inherits this stack;" FamilyAI's setup log says "Hermes (Day 1-2 build operator) ... OpenRouter ... Hermes delegation passed a simple subagent smoke test."

4. **`docs/00-setup-log.md:118` — "Hermes main agent works with OpenRouter when launched with `OPENROUTER_API_KEY="$OPENROUTER_API_KEY" hermes`."** Same OpenRouter-default issue as DavidOS' tooling-context-pack. Out of date.

5. **`docs/product/13-research-sprint-plan.md` opens with "Sprint v0.1 — Created: May 2026" and is dated 3-5 days of work,** but no synthesis doc (`docs/product/14-research-sprint-synthesis.md`) exists in the repo. The sprint was planned but neither the synthesis nor the killed-here memo appears to have been written. Either the work hasn't happened or it happened elsewhere; an internal observer can't tell which.

#### Redundancy

1. **`docs/01-mvp-prd.md` vs `docs/product/05-mvp-candidates.md`.** The PRD describes "Candidate 1 (Family Coordination Hub)" as the MVP; the candidates doc explicitly recommends NOT committing yet and lays out 5 alternatives. The PRD is from Day 1; the candidates doc is from the sprint. Neither references the other. A new reader sees a finalized PRD and a "we haven't decided yet" candidate-comparison side by side.

2. **`docs/04-permission-model.md`, `docs/05-memory-policy.md`, `docs/product/06-trust-safety-privacy-model.md` — all three describe consent/permission/audit/privacy rules.** Three docs, overlapping content. Worth a single canonical "FamilyAI trust model" doc with sections, or explicit "doc X is the canonical version; doc Y is the source critique" labels.

3. **`docs/13-venture-thesis-and-mvp-sprint.md` and `docs/product/13-research-sprint-plan.md`.** Identical-numbered docs in different folders; one is the charter, one is the research plan. Both legitimate; naming collision is confusing.

4. **`docs/prompts/day1-doc-generation.md` and `docs/prompts/day2-*.md`.** Useful as a record of how Hermes was bootstrapped on Day 1 and Day 2. Not redundant against anything else, but they're operational artifacts living in a docs tree — could move to `docs/archive/` once their bootstrap purpose is complete.

#### Noise

1. **`docs/00-setup-log.md` mixes durable status with task-list ephemera.** The "Day 2 Checklist" (lines 19-46) is checked off and complete; that data belongs in a CHANGELOG or a closed Day-2 retrospective, not in the live setup log alongside "Current Phase / Current Blocker / Next Step." Splitting it would prevent the setup log from getting noisier with each phase.

2. **`docs/10-open-questions.md` (not read but inferred from inventory)** — open questions over a month old are likely either decided or stale.

3. **The empty `infra/.gitkeep`, `evals/.gitkeep`, `apps/.gitkeep`, `packages/.gitkeep` — fine.** Just noting these exist; they're standard practice.

#### Vision alignment

Against DavidOS' design principles:

- **"AI should increase clarity, not create noise."** FamilyAI's docs are denser than necessary for what's actually built (Day-2 scaffold). 23 docs to describe ~10 working pages of code. Not a bug per se — this is intentional "documentation before code" — but worth noting that the doc-to-code ratio is extreme right now.
- **"Decisions need rationale, evidence, confidence level, revisit dates."** `docs/product/08-decision-log.md` does this well for sprint-era decisions. Earlier decisions (D-001..D-003 carried forward from pre-sprint) are similarly captured. **This is the strongest example in the ecosystem of the vision principle implemented well.**
- **"Use stronger models for make-or-break decisions."** No model assignments are written down in familyAI. The DavidOS Sonnet-only policy doesn't reach into familyAI artifacts.
- **"Approval gates."** Approval principle is encoded in the architecture (`02-system-architecture.md` "approval-before-effect"). Good.

#### Gaps

1. **No synthesis doc closing the product sprint.** Plan exists; no closure. The user's last meaningful familyAI session ended mid-sprint.

2. **No reference to hermes-workspace as the upstream operating UI.** When FamilyAI does resume, the operator (whoever spawns the next session) will need to know they're working inside Workspace, not Paperclip, not ChatGPT.

3. **Migration 001 status indefinite.** "Locally validated, not applied remotely." This is the documented decision (D-001), but no revisit date is set.

4. **`docs/03-agent-catalog.md` lists 6 agents (Orchestrator, Document, Calendar, Task, Memory, Safety/Consent) — none defined as a concrete agent in hermes-workspace.** Same shape as DavidOS' empty Agent Roles section — the agents are specified at architecture level and named, but no runtime exists for them.

#### Customer-zero test

FamilyAI is iZZi's first downstream product, not its first customer. It's appropriately family-specific. The reusable patterns sit in DavidOS, not familyAI. The right question for familyAI is: when iZZi takes its first paying customer, will the patterns that worked on familyAI generalize to a different domain? The product-sprint structure (founder-conviction → opportunity-map → wedge-scorecard → mvp-candidates → trust-model → decision-log → research-sprint-plan) is genuinely reusable across domains, and is the strongest customer-zero asset in this repo. The Day-1 doc set (mvp-prd / system-architecture / agent-catalog / permission-model / memory-policy / security-checklist / 30-day-roadmap / build-backlog / eval-plan / open-questions) is similarly reusable scaffolding. Both should be lifted into an iZZi customer template eventually.

---

## Repo: DavidAIStory

### Inventory (file tree snapshot)

10 tracked files. Clean.

```
README.md
docs/story/
  00-story-bible.md
  01-founder-timeline.md
  02-daily-story-log.md
  03-weekly-story-recaps.md
  04-media-format-ideas.md
  05-capture-system-plan.md
  06-fast-capture-workflow.md
prompts/story/
  daily-story-checkin.md
  weekly-story-recap.md
```

### Findings by dimension

#### Inconsistencies

1. **Most recent timeline / daily log / weekly recap entry is 2026-05-08.** The 2026-05-11 stack migration is arguably the most significant story beat of the week (Paperclip frozen, hermes-workspace adopted, Atlas re-cast as memo library, full architectural reset). It's not captured. The story is missing its inflection point.

2. **`docs/story/01-founder-timeline.md:24-44` only contains one entry (2026-05-08).** Format header says "For each entry include: Date, Event, Why it mattered, Emotional state, Artifact." That's good. Just nothing past that one day.

#### Redundancy

1. **`docs/story/05-capture-system-plan.md` and `docs/story/06-fast-capture-workflow.md`** describe substantially the same end-to-end capture workflow (David bullets → AI drafts → David approves → commit). Minor differences in field lists. Could consolidate to one canonical workflow doc.

#### Noise

1. **`docs/story/04-media-format-ideas.md` — six format ideas (founder diary, doc series, build-in-public thread, comeback essay, consulting origin story, podcast).** Not noisy per se; useful taxonomy. But until any of these formats are actually being produced, this is aspirational. Worth noting only because the story system as built right now consists of one timeline entry and one daily log entry — six format options is a lot of options for one day of content.

#### Vision alignment

The story-capture system aligns well with "automate only after manual understanding." David has the templates and the prompts; the capture is meant to be lightweight; the AI assistance is downstream of David providing bullets. Good.

What's missing: any evidence the system is being used. The vision says "preserve the truth of the journey." The truth currently preserved is a single breakthrough day from 3+ days ago, before the actual interesting work (migrating a whole stack, freezing a tool, re-casting an agent role) happened.

#### Gaps

1. **No 2026-05-09, -10, -11 daily entries.** The migration days are uncaptured.
2. **No weekly recap for week of 2026-05-12 (or week-rolling treatment).** The 2026-05-05 recap is the only one.
3. **No "system meta" entry explaining how the capture system itself evolved.** The story-system docs describe the workflow but the workflow has not produced output for 3 days.

#### Customer-zero test

DavidAIStory is uniquely David-specific (it is literally his personal narrative). Nothing here generalizes to a customer template, and nothing should. The structure (Story Bible, Founder Timeline, Daily/Weekly logs, Media Format ideas, Capture System Plan) could become a template *style* if iZZi ever offered a "founder-story-capture" sub-service, but the contents are unambiguously personal. Correctly David-specific.

---

## Cross-repo coherence

The three repos tell a story together. Does the story hold?

| Claim | Holds? | Notes |
|---|---|---|
| "DavidOS is the foundation for FamilyAI." (README, ADRs) | **Partially.** | The DavidOS README asserts this. FamilyAI's repo has no awareness of DavidOS as a foundation — no doc references hermes-workspace, no doc references Atlas, no doc references the post-migration stack. The relationship is asserted upstream and not received downstream. |
| "DavidAIStory captures the journey of building DavidOS, FamilyAI, etc." (DavidAIStory README) | **Partially.** | Story system exists. Day 2026-05-08 captured. Days -09, -10, -11 (the actually interesting days) are uncaptured. Architecturally sound; behaviorally stalled. |
| "Atlas is a memo library re-spawnable into Workspace; the canonical assets are under `docs/atlas/identity/`." (DavidOS) | **Yes, with caveat.** | The identity README + JSON + DAV-17 comments are present. The JSON has stale fields (Paperclip-specific `agentId`, `companyId`, `adapterType: hermes_local`, `runtimeConfig.heartbeat`). A "what's still load-bearing in this record" annotation would help. |
| "Paperclip is frozen." (DavidOS ADR-003) | **Yes structurally, no informationally.** | ADR-003 asserts it. ~10 active-tense docs still under `docs/atlas/` assume Paperclip is live. None have been struck through, banner-noted, or moved to `docs/atlas/archive/`. |
| "Workspace is the daily driver." (DavidOS README, ADR-001) | **Yes.** | NEXT-SESSION-OPEN.md, README, ADR-001 are consistent. |
| "OpenRouter is paused; OAuth via Claude Pro/Max is canonical." (DavidOS ADR-002) | **Yes structurally.** | Old references to OpenRouter remain in tool-stack-inventory.md and context-packs.md. |

### Orphan references

References from one repo or canonical file to a path/concept that does not actually exist:

1. `README.md:36` — "`docs/architecture/`" — directory does not exist.
2. `README.md:37` — "`docs/workspace/`" — directory does not exist.
3. `NEXT-SESSION-OPEN.md:68` — "`docs/workspace/baseline-config.md` — profile name, default model, theme, permissions" — file does not exist.
4. `docs/atlas/context-refresh-protocol.md:80` — references `docs/atlas/` content as if Atlas is still actively reading it on heartbeat. No heartbeat exists.
5. `docs/atlas/identity/README.md:23` — references `docs/sessions/submitted/2026-05-11T03-27-debrief.md` as "canonical handoff." That file exists and is good. ✓
6. `docs/atlas/davidos-session-workflow-v0.md` — references `scripts/session.py` as the executor of session start/end. The script exists but points at Paperclip API; will fail on run.
7. `docs/decisions/ADR-003-paperclip-frozen-atlas-memo-library.md:33` — references `docs/atlas/identity/README.md`. Exists. ✓
8. `david-ai-workspace-v0.md:103` — Project Registry table lists "FamilyAI: Active | Define MVP wedge | Research sprint synthesis | Hermes + ChatGPT | TBD." `Hermes + ChatGPT` is not the canonical FamilyAI stack post-migration; it's the pre-Workspace stack, and the synthesis doc doesn't exist in familyAI.

---

## Recommended next actions

Prioritized. Effort estimates are rough wall-clock with a clean session.

### High priority

1. **Move Paperclip-era `docs/atlas/` files to `docs/atlas/archive/paperclip-era/`.** 
   Effort: 15 minutes (just `git mv`).
   Rationale: This is the single highest-leverage cleanup. The fresh canonical files are surrounded by ~10 obsolete files that read as active. Archiving them resolves most of the "two parallel realities" problem in one move.
   Files to move: `paperclip-setup-plan.md`, `paperclip-reference-sources.md`, `paperclip-v0-workspace-structure.md`, `paperclip-atlas-activation-context.md`, `davidos-operating-ui-v1-plan.md`, `davidos-operating-ui-v1-plan-revised.md`, `davidos-operating-ui-v1-requirements.md`, `davidos-session-workflow-v0.md`, `ruflo-atlas-v0-plan.md`, `runs/2026-05-09-atlas-activation-memo-v0.md`.

2. **Fill (or delete) the empty Agent Role sections in `david-ai-workspace-v0.md`.** 
   Effort: 30-60 min if filling; 5 min if deleting and pointing to a future ADR-004.
   Rationale: Single most visible vision-doc gap. The README points to this file as "the durable why."
   Recommendation: Fill three roles initially (Chief of Staff, Research, Tooling and Automation) with concrete Purpose / Responsibilities / Approval-required. Mark the other five "TBD — see ADR-004 (open)." Better honest TBD than empty headers.

3. **Stub `docs/workspace/baseline-config.md` and `docs/architecture/README.md`.** 
   Effort: 20-30 min.
   Rationale: Both are referenced by canonical files. Their absence makes the README and NEXT-SESSION-OPEN feel forward-dated. Even a one-paragraph stub each unblocks future writes.

4. **Disable or stub `scripts/session.py` and `scripts/render-daily-view.py`.** 
   Effort: 10 min.
   Rationale: Both target a service that no longer exists. Running them silently fails. Either prepend a fail-loud `sys.exit("Paperclip-bound — see ADR-003")` or move under `scripts/archive/`. Update `scripts/session-config.json` similarly.

5. **Regenerate or remove `docs/daily/today.{md,html}`.**
   Effort: 5 min to remove, 1-2 hours to port the renderer to a Workspace-native data source.
   Rationale: The current today.md shows DAV-17 / DAV-22 from Paperclip URLs that no longer resolve. A reader has no way to know it's a stale snapshot. Removing or stamping STALE is fastest.

6. **Add ADR-004 (or equivalent) covering "Atlas role section in vision doc + post-Paperclip approval mechanism."**
   Effort: 30-45 min for the ADR itself.
   Rationale: The Paperclip `[APPROVAL: <kind>]` comment mechanism is gone, but the approval gates remain canonical policy. The current substrate is "David approves in Workspace conversation." That's a real decision; it deserves an ADR. Captures *how* approvals are now signaled.

### Medium priority

7. **Capture 2026-05-09 / -10 / -11 in DavidAIStory.** 
   Effort: 30-60 min.
   Rationale: Three days of substantial structural work, including the most consequential architectural pivot in the project's life, are uncaptured in the very repo designed to capture them.

8. **Annotate `docs/atlas/identity/atlas-agent-record.json` with "still load-bearing" / "Paperclip-only" markers.**
   Effort: 15 min — either as inline JSON comments (non-standard) or a sibling `atlas-agent-record.notes.md`.
   Rationale: If a future operator re-spawns Atlas from this record, they shouldn't have to guess which fields still apply. Specifically: `model` (still load-bearing, but reformat to Workspace-style ID), `adapterType: hermes_local` (Paperclip-only), `agentId` / `companyId` (Paperclip-only), `capabilities` (still load-bearing).

9. **Consolidate the redundant daily surfaces.**
   Effort: 1-2 hours.
   Rationale: `docs/daily-command-center.md`, `docs/daily-dashboard-v0.md`, `docs/daily/today.md`, `docs/sessions/NEXT-SESSION-OPEN.md` — four candidates for "where do I start a session." Pick one canonical (recommend NEXT-SESSION-OPEN), make the others either pointers or archive entries.

10. **FamilyAI: add a single line to `docs/00-setup-log.md`** noting that the upstream operating stack moved on 2026-05-11 (Hermes-workspace + Anthropic OAuth) so the next FamilyAI session knows where it lives.
    Effort: 5 min.
    Rationale: Cross-repo coherence. Currently FamilyAI is unaware of DavidOS's foundation work.

11. **Retro-ADR the Stage 1 folder layout** (the `raw/wiki/output/archive/daily/atlas` curation scheme).
    Effort: 30 min.
    Rationale: This was a substantive decision (DAV-17 Stage-1 bundle approval). The folders exist; the policy file (`docs/atlas/memory-curation-policy-v0.md`) describes the rules but in Paperclip-bound language. An ADR re-grounds the policy in the post-Workspace world.

12. **Decide what to do with the 5 still-valid Atlas policy files** (`approval-policy-v0.md`, `agent-expansion-policy-v0.md`, `comment-conventions-v0.md`, `memory-curation-policy-v0.md`, `tool-selection-policy.md`). 
    Effort: 30 min to triage, hours to rewrite if that's the path.
    Rationale: Each has a substrate-independent core and a Paperclip-specific mechanism layer. Pick: archive whole / rewrite for workspace / extract the substance into new policy files. Three of these are likely keep-and-rewrite; two could be archived.

### Low priority

13. **Move `docs/tomorrow-start.md` and `docs/tomorrow-systems-building-plan.md` to `docs/archive/`.**
    Effort: 5 min.

14. **Update `docs/tool-stack-inventory.md`** to reflect Workspace + OAuth + Sonnet-only + Paperclip-frozen.
    Effort: 15 min. (Or archive — the README already covers the live stack.)

15. **Fill or archive `docs/weekly-review.md`** (currently all TBD).
    Effort: 15 min.

16. **Add an `ADR-template.md` next to `ADR-001..003`.**
    Effort: 10 min.

17. **`scripts/repo-quality-review.sh` — parameterize the hard-coded `/home/hermes/projects/...` paths via env.**
    Effort: 30 min.
    Rationale: Customer-zero test — the script is useful enough to generalize.

---

## Files I'd touch in a follow-up PR

Prioritized so a one-shot PR is feasible. Each line: `<path> — <nature of edit>`.

**Tier 1 — pure archival (mechanically safe, restores canonical clarity):**

- `docs/atlas/paperclip-setup-plan.md` — `git mv` to `docs/atlas/archive/paperclip-era/`.
- `docs/atlas/paperclip-reference-sources.md` — same.
- `docs/atlas/paperclip-v0-workspace-structure.md` — same.
- `docs/atlas/paperclip-atlas-activation-context.md` — same.
- `docs/atlas/davidos-operating-ui-v1-plan.md` — same, then update any inbound references to ADR-001.
- `docs/atlas/davidos-operating-ui-v1-plan-revised.md` — same.
- `docs/atlas/davidos-operating-ui-v1-requirements.md` — same.
- `docs/atlas/davidos-session-workflow-v0.md` — same; create a 1-line successor pointer `docs/atlas/SESSION-WORKFLOW.md → see NEXT-SESSION-OPEN.md`.
- `docs/atlas/ruflo-atlas-v0-plan.md` — same.
- `docs/atlas/runs/2026-05-09-atlas-activation-memo-v0.md` — same (move to `archive/paperclip-era/runs/`).
- `docs/tomorrow-start.md` — move to `docs/archive/`.
- `docs/tomorrow-systems-building-plan.md` — move to `docs/archive/`.

**Tier 2 — small content edits (low-risk):**

- `david-ai-workspace-v0.md:33-97` — fill or delete the 8 empty Agent Role sections. Recommend filling Chief of Staff, Research, Tooling-and-Automation with current responsibilities; mark the rest "TBD."
- `david-ai-workspace-v0.md:99-114` — remove empty Project Registry table / Work Queue section, or replace with pointer to `docs/project-registry.md` and `NEXT-SESSION-OPEN.md`.
- `david-ai-workspace-v0.md:118-131` — remove empty Decision Log / Automation Candidates / Tool Stack tables; point at `docs/decisions/` and the README.
- `david-ai-workspace-v0.md:135-166` — remove empty Context Pack form; point at `docs/context-packs.md`.
- `david-ai-workspace-v0.md:206-213` — remove the eight Open Questions or convert them to ADR candidates.
- `docs/project-registry.md:9-12` — update "Active Tools" column to reflect post-migration stack.
- `docs/tool-stack-inventory.md:15-16` — update OpenRouter ("Paused; see ADR-002") and Paperclip ("Frozen 2026-05-11; see ADR-003").
- `docs/agent-operating-rules.md` — add a one-line note pointing at ADR-001..003 for current truth; optionally archive.

**Tier 3 — script cleanups:**

- `scripts/session.py:1` — prepend a fail-loud header: `print("ERROR: scripts/session.py targets the now-frozen Paperclip API. See docs/decisions/ADR-003."); sys.exit(1)`. Or move to `scripts/archive/`.
- `scripts/render-daily-view.py:1` — same treatment.
- `scripts/session-config.json` — move to `scripts/archive/`.
- `scripts/repo-quality-review.sh` — parameterize repo paths via env vars (optional / low-pri).

**Tier 4 — new files:**

- `docs/architecture/README.md` — stub (~150 words) explaining the directory, with a Mermaid or ASCII stack diagram (Workspace → Hermes → Anthropic OAuth → VPS).
- `docs/workspace/README.md` — stub.
- `docs/workspace/baseline-config.md` — stub with the explicit fields the README & NEXT-SESSION-OPEN promise (profile name, default model, theme, permissions).
- `docs/decisions/ADR-template.md` — copy ADR-001 stripped of content.
- `docs/decisions/ADR-004-workspace-approval-mechanism.md` — propose how `[APPROVAL: <kind>]` translates to Workspace.
- `DavidAIStory/docs/story/01-founder-timeline.md` — append 3 new entries (2026-05-09, -10, -11) covering the migration days.
- `DavidAIStory/docs/story/02-daily-story-log.md` — same.

**Tier 5 (familyAI, separate PR):**

- `familyAI/docs/00-setup-log.md` — add a one-line "Upstream operating stack migrated 2026-05-11; see lumlist/DavidOS ADR-001..003." Optionally point at the foundation README.

---

End of audit.
