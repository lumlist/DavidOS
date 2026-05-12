# Approvals Log

> **Append-only.** Atlas (or any operator) appends one row per approval at session end. Do not edit prior entries in place — revocations and modifications are new rows. See [ADR-004](./ADR-004-workspace-native-approval-mechanism.md) for the mechanism, intensity levels, expiry rules, and format guidance.

## Format

| Column | What goes in it |
|---|---|
| Date | YYYY-MM-DD when the approval was given |
| Intensity | `Light` or `Full` per ADR-004 |
| Topic | Short title — what was approved |
| Decision | `Approved` / `Approved with modification` / `Denied` / `Revoked` |
| Expires | `Permanent`, a YYYY-MM-DD date, or `n/a (tactical)` |
| Link | Path to the ADR, session debrief, or other artifact capturing detail |

## Active approvals

| Date | Intensity | Topic | Decision | Expires | Link |
|------|-----------|-------|----------|---------|------|
| 2026-05-11 | Full | Adopt hermes-workspace as daily driver (vs custom build or hermes-desktop) | Approved | 2026-08-11 | [ADR-001](./ADR-001-adopt-hermes-workspace.md) |
| 2026-05-11 | Full | Anthropic OAuth (Claude Pro/Max) over API key for daily-driver auth | Approved | 2026-08-11 | [ADR-002](./ADR-002-anthropic-oauth-over-api-key.md) |
| 2026-05-11 | Full | Freeze Paperclip; treat Atlas as memo library not preloaded runtime | Approved | Permanent | [ADR-003](./ADR-003-paperclip-frozen-atlas-memo-library.md) |
| 2026-05-11 | Full | Workspace-native approval mechanism (this log + two intensities + 90-day default expiry on policy approvals) | Approved | 2026-08-11 | [ADR-004](./ADR-004-workspace-native-approval-mechanism.md) |
| 2026-05-11 | Light | Use `david@lumlist.app` as canonical git commit email for lumlist/* repos | Approved | Permanent | This-session conversation |
| 2026-05-11 | Light | Switch DavidAIStory to inflection-point capture cadence (4-6 entries/year) over daily/weekly logs | Approved | Permanent | [DavidAIStory PR #1](https://github.com/lumlist/DavidAIStory/pull/1) |
| 2026-05-11 | Light | Skip Hermes update tonight (`9a63b5f → e855825`); take at next session start before substantive work | Approved | n/a (tactical) | [Session-end debrief](../sessions/submitted/2026-05-12T04-00-session-end.md) |
| 2026-05-11 | Light | Defer M6b iZZi Builder Services scoping to next session; preserve fresh attention for research + scoping arc | Approved | n/a (tactical) | [Session-end debrief](../sessions/submitted/2026-05-12T04-00-session-end.md) |
| 2026-05-11 | Light | M6b approach: AI-assisted research phase before committing to one-pager; combine consulting + tooling targeting solo-founder / non-technical-operator / small-business mix | Approved (open to amendment) | 2026-08-11 | [Session-end debrief](../sessions/submitted/2026-05-12T04-00-session-end.md) |
| 2026-05-12 | Light | Pre-session offline prep on M6b framing (Layer A scope, two-category taxonomy with conversion, 5-fork vocabulary, multi-tenancy principle, self-improvement as system tenet, Business-Model Lead as Layer 2 template) | Approved as pre-Atlas thinking (subject to Atlas review next session) | 2026-08-12 | [Offline-work memo](../sessions/offline-work/2026-05-12-pre-session-prep.md) |
| 2026-05-12 | Light | Parallel research subagent scope: registries + best-practices for AI-system risk and self-improvement | Approved | n/a (tactical) | [Offline-work memo](../sessions/offline-work/2026-05-12-pre-session-prep.md) |
| 2026-05-12 | Light | Defer A/B/C direction decision (continue M6b vs. pivot to substrate-first vs. hybrid) to fresh judgment at next session start | Approved | n/a (tactical) | [Offline-work memo](../sessions/offline-work/2026-05-12-pre-session-prep.md) |
| 2026-05-12 | Light | Route high-leverage structural decisions through Atlas first, not David alone; codify as a system pattern | Approved | Permanent | [Offline-work memo](../sessions/offline-work/2026-05-12-pre-session-prep.md) |
| 2026-05-12 | Soft fork | Option B — Pivot to substrate-first development path. Pause M6b process work; scope and ship a dedicated Substrate Brief covering Charter Regression Suite, Agent Roles / Capabilities Register, Decisions / Open Questions Register, Session-Start Substrate Manifest, and Tool Registry scaffolding. Resume M6b immediately once those items ship. | Approved under Sonnet 4.6 with disclosure that Opus was not available at decision time; recommended by Atlas with High confidence on directional call, Medium on execution shape. M6b will become the acceptance test for whether the substrate actually works. | 2026-08-12 (review at substrate completion or 3-session checkpoint, whichever first) | [Atlas recommendation captured in this session; full reasoning in chat transcript] |
| 2026-05-12 | Light | Add to Substrate Brief scope: Opus access via Hermes gateway. Currently Hermes only exposes a single configured default model to gateway clients; multi-model exposure for Workspace's model picker is a genuine substrate gap. Design properly in the Substrate Brief rather than patch tonight. | Approved | n/a (rolls into Substrate Brief) | [Approvals log] |
| 2026-05-12 | Light | Pattern to codify in future charter patch: within a single Atlas task, use Sonnet by default and escalate to Opus only for high-judgment synthesis components (structural recommendations, fork analysis, novel architecture proposals, charter or ADR drafts). Drop back to Sonnet for routine components (file reads, search, format compliance, summarization). Atlas should state which model is in use when switching. | Approved as future patch — lands after Opus access is wired in the Substrate Brief | Permanent | [Approvals log] |

## Revocations and modifications

*None yet.*

## Notes on retroactive entries

The first four rows above (ADR-001 through ADR-004) were retroactively logged on 2026-05-11 — they were approved during the day's work but the log didn't exist yet. ADR-001/002/003 are dated their actual approval date. From 2026-05-12 forward, approvals are logged as they happen.

The two Light approvals at the bottom were also retroactive — both were approved in-conversation today without using the formal format, but they're durable enough to be worth logging. Future Light approvals will use the format defined in ADR-004.
