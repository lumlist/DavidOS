# Karrigan Intake + LAOP Roadmap
`docs/roadmap/2026-05-19-karrigan-intake-and-laop-roadmap.md`

> **STATUS: ROADMAP / INTAKE ONLY — NON-AUTHORITY-BEARING.**
> This document does NOT create, activate, or authorize Karrigan. Karrigan is a **named-future stub, execution_authority=none**. No authority, persistent memory, independent system inspection, workflow capability, /goal use, or external-action capability is granted by this document. It records accepted intent and simulated planning evidence only. Supersedes-by-extension (does not edit) `docs/roadmap/2026-05-14-karrigan-intent-capture.md`.

## 1. Purpose
Durable record of the Karrigan intake arc: normalized intake, LAOP gate plan, dry-run evidence, output-shape refinement, targeted re-test result, non-gating operating model, and carried residuals. Exists now because the targeted re-test lifted the MVP dry-run to RUN PASS; prior gates correctly refused this doc as premature while the run was CONDITIONAL.

## 2. Source Basis
Final Karrigan intake DOCX (2026-05-18); in-session normalized intake summary; LAOP planning proposal; MVP dry-run execution report; output-shape refinement proposal; targeted dry-run re-test report; David's ratified clarifications on memory, source-traceability, model/cost, non-gating model, placement, and KPI framework. No external sources.

## 3. Karrigan Purpose & Scope  `[ACCEPTED-INTENT]`
Karrigan improves how David operates AI systems — prompt quality, context packaging, decision framing over AI outputs, session flow, handoff quality, approval discipline, operator learning. Atlas manages the system; Karrigan improves how David operates it. **Out of scope:** personal-life/schedule/general-productivity coaching; system control.

## 4. MVP-Safe Definition  `[ACCEPTED-INTENT]`
Chat-only, invoked-on-demand, advisory, non-executing. No persistent memory writes; read-only context only when David provides or Atlas surfaces it; no independent system inspection; no external actions; no registry/manifest/workflow/goal/agent-activation changes. Not Sonnet-only, not Opus-everything.

## 5. Future-State Definition  `[ACCEPTED-INTENT]`
A long-term operator-improvement layer. Every capability beyond MVP is separately proposed, governed, manifest-bound where required, and proven safe before use. Never a general personal-life manager.

## 6. Normalized Intake Summary  `[ACCEPTED-INTENT]`
Canonical structure §A–§I: A Mission/Rationale · B Functions & Bounded Context (owns operator-side AI interaction quality; does not own architecture/governance/execution/etc.) · C Read/Remember/Never-Access (C2-gate: no auto-persist in MVP) · D Sensitive Surfaces · E Operating Shape · F Coordination (F1 Atlas decides / F2 Karrigan improves) · G Source-Traceability contract · H Model/Cost · I Versioning. Full normalized text retained from the accepted gate-2 summary.

## 7. LAOP Gates G1–G12 (concise)  `[ACCEPTED-INTENT]`
Proving sequence; default per gate = "stays blocked"; no gate grants authority.
- G1 Intent confirmation · G2 Bounded-context/narrow-interface · G3 Atlas/Karrigan boundary (resolves OQ4 trigger) · G4 Memory/source-of-truth (carries OQ1, decides nothing) · G5 Source-traceability preservation · G6 Sensitive-surface · G7 Model/cost · G8 Preliminary success-signal (no KPI finalization) · G9 Decision Protocol dry-run · G10 MVP dry-run mode · G11 Agent-placement/operating-surface analysis (identify-only; applies to Atlas too) · G12 Activation-proposal gate (only if ever appropriate; David-only L1 Full; Atlas may only propose).
Each gate: purpose / inputs / output / pass·fail·inconclusive / judge / MVP-vs-future / stays-blocked. Full per-gate detail retained from the accepted LAOP planning proposal.

## 8. Dry-Run Evidence Summary  `[SIMULATED-EVIDENCE]`
Chat-only simulation; no real Karrigan ran.
- MVP dry-run (7 scenarios + stress + friction + decision-support + boundary floors): **RUN CONDITIONAL** — passed governance/scope/boundaries/decision-support; friction CONDITIONAL on thin value-density when relaying short already-tagged Atlas output (R6).
- Output-shape refinement: invocation rule, stand-down rule, 5 modes, graduated source-preserving rule, value-density self-check — accepted as the R6 design fix.
- Targeted re-test (S2-R, Stress-R, Standdown-1/2, R7, Non-gating): **TARGETED RETEST PASS**, all 6 cases. RUN CONDITIONAL **lifted to RUN PASS**. R6 resolved. R7 resolved-in-simulation (R7-impl carried).

## 9. Output-Shape Refinement  `[ACCEPTED-INTENT]`
- **Invocation rule:** invoke when input is disordered, long, ambiguous, high-stakes, or transformation-heavy.
- **Stand-down rule:** stand down / one-line minimal when Atlas output is already short, clear, tagged, actionable; obvious low-risk approval; or Karrigan would mostly repeat Atlas. Stand-down is a valid first-class output.
- **5 modes:** prompt-improvement · source-preserving summary · decision-support · missing-context · session-flow (each with concision ceiling + preserve/exclude).
- **Value-density self-check (pre-emit):** reducing load? preserving fidelity where load-bearing? adding decision clarity? reducing real risk? avoiding unnecessary length? Any failure on load/clarity/risk → shrink or stand down.

## 10. Non-Gating Operating Model  `[ACCEPTED-INTENT]`
Context-aware, not default-interventionist. Operator-support layer, NOT an approval gate. Engages when useful, stands down when redundant. Karrigan is never a mandatory approval/translation/routing layer; Atlas and future-agent recommendations and system actions are NOT gated behind Karrigan.

## 11. Memory Posture & OQ1  `[ACCEPTED-INTENT / DEFERRED-GATE]`
System-memory read allowed when needed and exposed by Atlas/David. Raw Karrigan↔David conversation isolated by default. **Invariant:** raw conversation must not auto-propagate to Atlas/system/project/agent memory. MVP = no persistent Karrigan memory writes. Future: propose-distilled → David/Atlas-approve → broader memory. **OQ1** (separate profile vs. shared-with-gates vs. none vs. distilled-only) is deferred to its own sub-gate before any persistent-memory proposal.

## 12. Source-Traceability Posture  `[ACCEPTED-INTENT]`
Preserve-verbatim: Atlas raw inputs, epistemic tags, confidence, named residual risks, approval intensity. Interpretation visibly distinct from raw output; source reachable in one step. Traceability scales with source disorder (graduated, not flat): clean+short+tagged → stand down; long/mixed-confidence/ambiguous/high-judgment → full traceability block.

## 13. Model/Cost Posture  `[ACCEPTED-INTENT]`
Quality-sensitive and cost-aware. Opus-class when necessary (high-judgment/ambiguous/complex/consequential/novel); cheaper/bounded when sufficient; lowest-cost strategy that reliably meets the bar. Invoked on demand in MVP; not always-on, not a background monitor. No Hermes config change implied.

## 14. Sensitive Surfaces  `[ACCEPTED-INTENT]`
D1 external actions / D2 spend / D3 legal-privacy / D4 health-finance — all blocked-in-MVP, possible-future, separately gated. D5 account/credential — never accessed. Never-access set and no-auto-propagation invariant hold in all options.

## 15. Residuals & Future Gates  `[mixed — labeled per row]`

| ID | Item | Status |
|----|------|--------|
| R1/OQ1 | Memory-store architecture | DEFERRED-GATE |
| OQ2 | Memory-promotion approval mechanism | DEFERRED-GATE |
| OQ4 | Defer-to-Atlas vs advise-directly trigger — formal ratification | EVIDENCED (S6+non-gating); ratify at LAOP G3 |
| OQ5 | Cost ceiling / usage-monitoring concretes | DEFERRED-GATE |
| R3/OQ3 | Operator-improvement success-signal definition | CANDIDATES IDENTIFIED; finalize at KPI gate |
| R5 | Placement-analysis charter + Agent/Skill KPI framework | FUTURE-GATE (placement also covers Atlas) |
| R7-impl | Real-impl reliability of buried-signal detection (not keyword stand-down) | FUTURE-IMPL-RISK; condition on G12 |
| R8 | Doc prose-bloat risk | MITIGATED (this doc kept concise) |
| R6 | Output-shape value-density | RESOLVED-IN-SIM |
| R7 | Stand-down overcorrection | RESOLVED-IN-SIM (R7-impl open) |

## 16. Explicit Non-Actions — What This Document Does NOT Do  `[NON-AUTHORITY-PLANNING]`
Does not create or activate Karrigan; grant execution authority; modify registries/manifests; adopt or run /goal; create workflows; create persistent memory; authorize independent system inspection; authorize external actions; change the Decision Protocol; constitute an agent contract; or edit `2026-05-14-karrigan-intent-capture.md`. Karrigan remains a named-future stub, execution_authority=none.
