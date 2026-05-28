---
fastdraft_id: 2
artifact_type: operator_context_pack
created_at: 2026-05-28
updated_at: 2026-05-28
author: atlas
status: updated
schema_version: 0.1
version: 0.2
supersedes: v0.1 (committed at f898203)
plan_version: 0.2
plan_commit: 105ce1b
---

# FastDraft #2 Operator Context Pack v0.2

Status: updated post-G3.0 — reflects G3.0-approved Repo Layout values and adds the Relationship-Disclosed Boundaries section.
Plan reference: `docs/plans/tool-access-workstream-scaling-plan-v0.2.md`
Plan commit: `105ce1b`
Lineage: fd-002 is the first DavidOS-governed FastDraft; v8.2 / Custom Scapes = pre-governed FastDraft #1 reference lineage.
Scope: FastDraft #2, M Vince Nail Spa (mvincenailspa.com) — beauty/nail salon prototype, internal-first unless David later approves customer-facing use.

Note on artifact_type: this Pack uses `artifact_type: operator_context_pack`, which extends the v0.2 plan §5.0 enum (`brief|sources|facts|blueprint|build_log|review`). Enum extension to be reconciled in a future plan revision.

## Purpose

This packet is the shared run context for FastDraft #2. It exists to reduce fragmented agent context across Atlas, Ari/Codex, Gemini, Claude Code, NotebookLM, Perplexity, and Ruflo.

It is a document, not a service. No automated shared-state integration is assumed in v1.

## Version + Supersession

- This is v0.2, status `updated`, pending fresh G0.1 Light reaffirmation (the relationship boundary is substantive new operating context, not just G3.0 value-fill).
- v0.1 was approved at G0.1 Light on 2026-05-28 (approvals-log row in commit `d60d462`); v0.1 file artifact lives at commit `f898203`.
- v0.2 changes vs v0.1:
  - Frontmatter: `version: 0.2`, `status: updated`, `supersedes: v0.1 (committed at f898203)`.
  - Header: lineage line added (fd-002 first governed; v8.2 = pre-governed FD#1).
  - Scope: target named as M Vince Nail Spa, category beauty/nail salon (was "med spa prototype").
  - "Pending G3.0 Repo Layout Fields" section replaced by "Repo Layout (approved at G3.0)" with concrete values.
  - New top-level section: "Relationship-Disclosed Boundaries" (between Data Scope and Source Rules).
  - Open Decisions updated: items resolved at G3.0 moved out; screenshot proof helper added as Before-#2 item.
- Subsequent Run-level reissues bump minor version (v0.3, ...) and record what changed in this block.
- Superseded versions remain as in-repo history under the file's git log.

## Run Roles

**David:**
- Final owner-belief, taste, customer-facing, scope, pricing, and outreach decisions.

**Atlas:**
- Control plane and Research Coordinator.
- Owns gates, sequencing, synthesis, and plan alignment.

**Ari/Codex:**
- Local workspace execution, repo hygiene, screenshots, browser verification, and Repo Layout Note.

**Claude Code:**
- Implementation worker/reviewer when invoked.
- No autonomous pattern selection, outreach, deployment, package changes, or writes outside approved scope.

**Gemini:**
- Visual-spatial critique and design reasoning.
- Vision/screenshot review adapter, not orchestrator.

**NotebookLM:**
- Raw source ingestion and analysis only.
- Not canonical memory.

**Perplexity:**
- Manual retrieval/synthesis adapter only.
- Not fact owner or research owner.

**Ruflo:**
- Advisory only, sandboxed, no active integration.

## Target Business

- **Name:** M Vince Nail Spa
- **URL:** https://www.mvincenailspa.com/
- **Category:** beauty/nail salon (NOT med spa — earlier plan-v0.2 framing of "med spa" for FastDraft #2 is now stale; cleanup deferred to a future plan revision)
- **Selection:** David, 2026-05-28, recorded in approvals-log G3.0 row (commit `3ef9206`)

## Active Workspace

FastDraft #2 uses existing non-git workspace.

Workspace identifier (operator-document use; not for code paths):
`C:\Users\David\Documents\Codex\2026-05-20\i-want-to-create-a-durable\izzi-revenue-dashboard`

Known local facts:
- Host project is Vite/React, but FastDraft output defaults to vanilla HTML/CSS/minimal JS.
- Existing screenshot tool: `scripts/screenshot-prototype.ts`.
- Existing prototypes live under `prototypes/`.
- v8.2 reference lives at `prototypes/premium-outdoor-living-v8-2-service-showroom/`.
- Existing `.claude/settings.local.json` only allows WebFetch to dribbble.com.
- This workspace is not git-backed, so AutoResearch does not run here.

The plan's hard refusal on "absolute machine paths in HTML/CSS/JS/assets" applies to code references only, not to operator documents identifying the workspace.

## Repo Layout (approved at G3.0)

Approved at G3.0 Light on 2026-05-28 (approvals-log row in commit `3ef9206`). Ari/Codex Repo Layout Note canonical lives at `<izzi-revenue-dashboard>/REPO-LAYOUT-NOTE.md` in the active workspace; this section mirrors the approved values for in-repo durability.

- **FastDraft target directory:** `fastdraft/fd-002-mvince-nail-spa/`
- **Allowed write scope:** `REPO-LAYOUT-NOTE.md` and `fastdraft/fd-002-mvince-nail-spa/**`
- **v8.2 read-only enforcement:** by instruction only; mechanical enforcement (e.g., `.claude/settings.json` deny-write, OS-level ACL) deferred to a later proposal turn from Ari
- **Screenshot proof helper:** still needs implementation before G3.2 — not present at G3.0 approval time
- **Local server / browser verification path:** Vite dev server in the existing izzi-revenue-dashboard workspace (specifics in Ari's Repo Layout Note)
- **Skill location:** no Claude Code WOW skill is active for FastDraft #2; future project-local skill location, if later approved after N=2 reuse evidence, is `.claude/skills/`; no skill creation or skill installation is authorized by this Pack or by G3.0.

G3.0 does NOT authorize build, retrieval, package changes, deployment, or customer-facing action.

## Data Scope

FastDraft #2 uses public-source/public-web facts only.

**Included** without Data gate:
- M Vince Nail Spa's public website (mvincenailspa.com)
- public Google profile/manual listings
- public social pages accessible without login
- public directories
- publicly visible brand/assets

**Excluded** unless Data gate approved:
- private data
- login-walled content
- paid/API/auth-based sources
- customer-derived data
- non-public data

## Relationship-Disclosed Boundaries

David has a personal connection to M Vince Nail Spa through his girlfriend. This connection is disclosed up front and creates the following operating constraints for FastDraft #2:

**Forbidden as fact sources** (no Data gate approved):
- private/internal employee knowledge
- non-public customer information
- girlfriend-provided operational details (pricing not on the public site, internal scheduling practices, staff dynamics, business plans, etc.)
- anything observed in person by David or his girlfriend that is not also independently published on a public source

**F4 fact-tracing discipline:**
- Relationship-channel tips MAY guide research direction (e.g., "look at how they describe their gel manicure service" is a fine prompt for what to research).
- Every load-bearing fact in the Fact Pack MUST trace to a public source recorded in the Source Log with a proper completeness label.
- A tip that surfaces a topic does NOT count as the source for that topic — independent public-source verification is still required.
- If a fact only exists via the relationship channel and not on any public source, it is `[unverifiable]` and refused for load-bearing use.

**Pipeline 5 implication (deferred):** If at Step 13 David decides to show FastDraft #2 externally to M Vince Nail Spa as a real proposal, the relationship connection becomes a Pipeline 5 disclosure question (how/when to disclose, by whom). That decision is deferred to Step 13 and outside the scope of this Pack.

**Revisit trigger:** any request to relax this boundary requires an explicit Data gate decision logged in the approvals log; it is not an in-session call.

## Source Rules

Every source gets a completeness label:
- `transcript-available`
- `metadata-only`
- `visual-only`
- `source-inaccessible`
- `needs-manual-transcript-extraction`

Default when source completeness is unclear:
`needs-manual-transcript-extraction`

Extractor refuses non-transcript-available sources for load-bearing claims unless override is logged.

## Source Log Row Shape

Each source row includes:
`source_id`, `url`, `retrieved_at`, `adapter`, `source_completeness`, `override_reason`, `source_snapshot_path`, `linked_claims`

Adapter enum (full, per plan §2 Pipeline 1):
`manual-web | perplexity-manual | tavily | exa | brave | direct-fetch | google-places-manual | other:<name>`

Note: `tavily`, `exa`, `brave` are deferred adapters — listed for log-recognition only and remain behind G1.3 + Auth/Data gates. They are not in active use during FastDraft #2.

## Artifact Layout

FastDraft artifacts use repo-relative paths (leading slash in narrative is conceptual shorthand; implementation paths have no leading slash):

```
fastdraft/fd-002-mvince-nail-spa/
  brief/
  sources/
  facts/
  blueprint/
  build/
  proofs/
  review/
```

Proof screenshots:
- `proofs/desktop-latest.png`
- `proofs/mobile-latest.png`
- `proofs/archive/<timestamp>-desktop.png`
- `proofs/archive/<timestamp>-mobile.png`
- `proofs/archive/<timestamp>-desktop-above-fold.png`
- `proofs/archive/<timestamp>-mobile-above-fold.png`

Note: the screenshot proof helper that writes to this layout still needs implementation before G3.2 (tracked in Open Decisions).

## Gates For This Run

**Pre-run:**
- G0.1 Light — Operator Context Pack approval (v0.1 approved at commit `d60d462`; v0.2 pending reaffirmation)
- G3.0 Light — Ari Repo Layout Note approval (approved at commit `3ef9206`)

**Research:**
- G1.0 Light — Research Brief
- G1.1 Light — shortlist
- G1.2 Light by default — Fact Pack handoff
- G1.2 escalates to Full if any load-bearing claim is `[contradicted]` or `[unverifiable]`, or unverifiable-rate exceeds 15%

**Build:**
- G3.1 Light — Spatial Blueprint
- G3.2 Light — first rendered draft
- G3.3 Full — declared complete

**Review:**
- G4.1 Light — Review Log
- G4.2 Full — promotion candidate advancement

**Customer-facing:**
- G5.1 Full — outbound
- G5.2 Full — external pricing/scope
- G5.3 Light — internal prep pack
- G5.4 Full — learnings filed back

## Hard Refusals

Agents refuse (mirrored from plan v0.2 §6):
- Writes into v8.2.
- Candidate-Risky in lead viewport / primary service explanation.
- Autonomous outbound to any external party.
- Layout reinvention inside a skill (override surface limits stand).
- AutoResearch loop without all 5 preconditions.
- Orchestration role for any tool other than Atlas.
- Absolute machine paths in HTML/CSS/JS/assets — workspace-relative only.
- Ingestion of non-public/customer-derived data without an approved Data gate.

## Pattern Guidance

The pattern shortlist for FastDraft #2 is a Step 6 artifact under Pipeline 2 discipline (G2.1 Light for new Pattern Cards, G2.4 Light for alternate variants). It is NOT pre-resolved in this Pack.

Standing notes from plan v0.2 §2 Pipeline 2:
- **Sticky Narrative Anchor** = Candidate-Risky. Allowed for internal experiments; blocked from customer-facing lead viewport / primary service explanation until proven.
- **Premium Service Showroom** = first promotion candidate after FastDraft #2 unless disproved.

Skill creation:
- No Claude Code WOW skill creation during FastDraft #2.
- N=2 successful real uses required before v0.1 skill eligibility; one FastDraft cannot self-promote.

## Gemini Use

Gemini may be used for:
- visual-spatial critique inside the G3.2 → G3.3 iteration loop (not as a separate gate)
- screenshot review
- design pattern analysis
- generated/internal visual direction support

Gemini should not:
- verify facts
- make customer-facing decisions
- become the orchestrator
- override David's owner-belief judgment

## Claude Code Use

Claude Code may receive:
- scoped file paths
- Fact Pack excerpt
- Spatial Blueprint excerpt
- allowed write paths
- hard refusals
- screenshot/proof expectations

Claude Code should not receive the whole Second Brain by default.

## Open Decisions

**Before #2 starts:**
- screenshot proof helper implementation (pending; blocks G3.2)

**Decide after #2 ships:**
- whether #2 remains internal-only or becomes customer-facing later (David at Step 13; if external, triggers Pipeline 5 relationship-disclosure question per Relationship-Disclosed Boundaries section)
- git-backed workspace strategy after #2 (FastDraft workspace, benchmark workspace, or both)
- deeper agent-context integration after Context Pack trial

## Distribution

**Atlas:**
Reads from the DavidOS repo (canonical) and any synced VPS clone.

**Ari/Codex:**
Uses as local run reference.

**Claude Code:**
Receives scoped excerpts only.

**Gemini:**
Receives pasted/uploaded packet for critique passes.

**NotebookLM / Perplexity:**
Outputs fold into Research Brief / Source Log, not into this packet directly.

## Approval

G0.1 Light reaffirmation for v0.2 means:
- v0.2 reflects G3.0-approved values correctly
- the new Relationship-Disclosed Boundaries section is approved as binding operating context
- F4 fact-tracing discipline is approved as binding
- the v0.1 G0.1 approval (commit `d60d462`) carries forward in spirit; v0.2 supersedes v0.1 as the operative Pack

G0.1-v0.2 does NOT authorize Step 3 retrieval. G1.0 (Research Brief approval) must still pass before Step 3.

— end of operator-context-pack.md —
