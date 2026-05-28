---
artifact_type: roadmap
created_at: 2026-05-28
updated_at: 2026-05-28
author: atlas
status: draft
canonicality: planning_backlog
---

# iZZi OS Agent Operating Roadmap

Status: planning/backlog artifact. This file records the ordered operating-system sequence for the AI workspace. It is not itself an authority grant, agent charter, write permission, provider exception, or Second Brain policy.

Canonical authority remains in:
- DavidOS repo governance artifacts;
- ADRs;
- approvals log;
- provider-routing register;
- future approved agent ownership and harness artifacts.

## Current canonical / non-canonical boundaries

- DavidOS repo is canonical for governance, approvals, provider routing, agent ownership, and harness rules.
- Obsidian / Second Brain is not canonical yet.
- Obsidian may later receive summaries or mirrors after Second Brain connection rules are defined.
- Rufi/Ruflo role design is accepted as working design input only, not canonical.
- No standalone Ruflo charter should be created before the Agent Functional Ownership Register and iZZi OS agent harness clarify ownership, write class, sandbox, review, and promotion rules.

## Ordered roadmap

| Order | Item | Status | Canonicality | Notes |
|---|---|---|---|---|
| 1 | Finish provider-routing documentation/logging | In progress | Canonical docs/logging | ADR-007 and Provider Routing Register are already durable at commit `51bb070`; approvals-log row still needs to be written. |
| 2 | Update FastDraft #2 Operator Context Pack v0.3 | In progress | Canonical run context after approval/write | Pack v0.3 should record provider-routing state, FastDraft state, and retrieval pause. |
| 3 | Log G1.0 | Pending | Approval log canonical once written | Required before FastDraft retrieval resumes. Do not infer G1.0 from adjacent approvals. |
| 4 | Resume FastDraft retrieval | Blocked on G1.0 durable log | Execution, not governance | Retrieval remains paused until G1.0 is durably logged. Must stay inside ADR-007/provider-register constraints. |
| 5 | Agent Functional Ownership Register | Pending | Future canonical register | Should define agent/tool ownership boundaries, functional scope, authority, and escalation paths. Rufi/Ruflo working design belongs here first. |
| 6 | First Principles v0.1 | Pending | Future canonical or near-canonical principles artifact | Should distill operating principles for iZZi OS / AI workspace without overfitting to one agent. |
| 7 | Write class taxonomy | Pending | Future canonical governance artifact | Should classify sandbox writes, preview updates/proposals, canonical writes, live/customer-facing writes, external actions, and approval intensity. |
| 8 | Digest cadence | Pending | Future operating rule | Use “David-approved digest cadence,” not fixed weekly digest. Cadence belongs under ownership/harness rules. |
| 9 | Sandbox boundary | Pending | Future canonical harness rule | Define where agents may experiment, what can be self-evaluated, what needs independent review, and what cannot leave sandbox without approval. |
| 10 | Evidence-gate ledger | Pending | Future canonical/operational ledger | Track evidence thresholds for promotion, customer-facing claims, source completeness, and review decisions. |
| 11 | Source-completeness propagation | Pending | Future harness/data rule | Preserve source-completeness labels across NotebookLM, Gemini, Perplexity/manual, Codex/Ari, Atlas, and any downstream artifacts. |
| 12 | Risk-proportional review routing | Pending | Future harness rule | Ruflo may self-evaluate sandbox work with COI disclosure, but canonical/live promotion requires risk-proportional independent review. |
| 13 | Agent harnessing | Pending | Future canonical harness | Implement agent roles, route constraints, sandbox boundaries, review routing, and promotion paths. |
| 14 | Connection to Second Brain | Pending | Future integration policy | Define what may be mirrored into Obsidian, what remains canonical in DavidOS, and how summaries avoid becoming silent authority. |
| 15 | Consolidated AI workspace / command center | Pending | Future product/system design | Should integrate agent status, gates, backlog, docs, retrieval, reviews, and promotion state without bypassing approvals. |
| 16 | iZZi Webservices sprint | Pending | Execution sprint after enough OS scaffolding | Should use the operating system rather than create parallel undocumented process. |

## Rufi/Ruflo working-design carry-forward

Rufi/Ruflo design is accepted as working design input only.

Carry forward these constraints into the Agent Functional Ownership Register and iZZi OS agent harness:

1. Use “David-approved digest cadence,” not fixed weekly digest.
2. Reads from approved canonical docs are generally allowed for analysis; writes outside sandbox are governed by write class.
3. Use “preview dashboard updates/proposals,” not “preview dashboard merges.” Live/canonical merges remain gated.
4. Perplexity API is off-limits. Perplexity Pro/manual may be recommended or routed through David/Atlas under ADR-007 provider policy.
5. Google/NotebookLM automated ingestion remains pending route/source verification; read-only use must preserve source-completeness labels.
6. Ruflo may self-evaluate sandbox work with COI disclosure, but promotion to canonical/live requires risk-proportional independent review.
7. Controlled scope creep is allowed only when visible, reversible, logged, and reviewable.

## Operating notes

- Keep this roadmap lightweight. It is a sequencing aid, not a doctrine sink.
- Promote items into canonical artifacts only through explicit approval gates.
- Do not let roadmap existence authorize work that still needs a gate.
- Prefer the smallest next canonical artifact that removes the current bottleneck.
- Current bottleneck: G1.0 is not durably logged, so FastDraft retrieval remains paused.

— end of izzi-os-agent-operating-roadmap.md —
