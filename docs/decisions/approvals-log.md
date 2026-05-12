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

## Revocations and modifications

*None yet.*

## Notes on retroactive entries

The first four rows above (ADR-001 through ADR-004) were retroactively logged on 2026-05-11 — they were approved during the day's work but the log didn't exist yet. ADR-001/002/003 are dated their actual approval date. From 2026-05-12 forward, approvals are logged as they happen.

The two Light approvals at the bottom were also retroactive — both were approved in-conversation today without using the formal format, but they're durable enough to be worth logging. Future Light approvals will use the format defined in ADR-004.
