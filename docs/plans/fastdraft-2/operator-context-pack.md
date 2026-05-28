---
fastdraft_id: 2
artifact_type: operator_context_pack
created_at: 2026-05-28
updated_at: 2026-05-28
author: atlas
status: draft
schema_version: 0.1
plan_version: 0.2
plan_commit: 105ce1b
---

# FastDraft #2 Operator Context Pack v0.1

Status: draft for G0.1 approval
Plan reference: `docs/plans/tool-access-workstream-scaling-plan-v0.2.md`
Plan commit: `105ce1b`
Scope: FastDraft #2, med spa prototype, internal-first unless David later approves customer-facing use.

Note on artifact_type: this Pack uses `artifact_type: operator_context_pack`, which extends the v0.2 plan §5.0 enum (`brief|sources|facts|blueprint|build_log|review`). Enum extension to be reconciled in a future plan revision.

## Purpose

This packet is the shared run context for FastDraft #2. It exists to reduce fragmented agent context across Atlas, Ari/Codex, Gemini, Claude Code, NotebookLM, Perplexity, and Ruflo.

It is a document, not a service. No automated shared-state integration is assumed in v1.

## Version + Supersession

- This is v0.1, status `draft`, pending G0.1 Light approval.
- After G3.0 approval (Ari Repo Layout Note), this Pack is updated with concrete Repo Layout values; version bumps to v0.2, status becomes `updated`.
- Subsequent Run-level reissues bump minor version (v0.3, v0.4, ...) and record what changed.
- Superseded versions are not deleted; they remain as in-repo history under the file's git log.

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

## Pending G3.0 Repo Layout Fields

These remain pending until Ari Repo Layout Note approval:
- exact FastDraft #2 target directory
- skill location
- write permission scope
- v8.2 mechanical read-only proposal
- FastDraft proof screenshot path
- local server/browser verification path

G1.0 may proceed with these pending. G3.1 may not.

## Data Scope

FastDraft #2 uses public-source/public-web facts only.

**Included** without Data gate:
- target business public website
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
fastdraft/<id>/
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

## Gates For This Run

**Pre-run:**
- G0.1 Light — Operator Context Pack approval
- G3.0 Light — Ari Repo Layout Note approval

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
- exact FastDraft #2 target business (David selects at Step 1)
- exact target directory inside `izzi-revenue-dashboard` (pending G3.0)
- proof screenshot workflow (pending G3.0)
- v8.2 mechanical enforcement (pending G3.0; instruction-level enforcement active immediately)

**Decide after #2 ships:**
- whether #2 remains internal-only or becomes customer-facing later (David at Step 13)
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

G0.1 Light approval means:
- this packet is sufficient to begin Research Brief work
- Repo Layout fields may remain `pending G3.0`
- no build begins until G3.0 and G3.1 pass

G0.1 does NOT authorize Step 3 retrieval. G1.0 (Research Brief approval) must still pass between G0.1 and Step 3.

— end of operator-context-pack.md —
