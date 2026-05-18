# Architecture Decision Records (ADRs)

This directory captures significant architectural and strategic decisions about DavidOS and the surrounding stack. Each ADR records the **context**, **decision**, **rationale**, **consequences**, and **re-evaluation triggers** so future-David (and future iZZi customers inheriting this pattern) can understand why things are the way they are.

## Format

Filename: `ADR-NNN-short-kebab-case-title.md`

Status values: `Proposed`, `Accepted`, `Deprecated`, `Superseded by ADR-XXX`

## Creating a new ADR

Copy [`ADR-template.md`](./ADR-template.md) to `ADR-NNN-short-title.md`, fill it in, and add a line to the index below.

## Index

- [ADR-001](./ADR-001-adopt-hermes-workspace.md) — Adopt hermes-workspace over custom UI build (2026-05-11)
- [ADR-002](./ADR-002-anthropic-oauth-over-api-key.md) — Anthropic OAuth over API key for daily driver (2026-05-11)
- [ADR-003](./ADR-003-paperclip-frozen-atlas-memo-library.md) — Paperclip frozen; Atlas as memo library (2026-05-11)
- [ADR-004](./ADR-004-workspace-native-approval-mechanism.md) — Workspace-native approval mechanism (2026-05-11)
- [ADR-005](./ADR-005-governed-intent-protocol.md) — Governed Intent Protocol; supersedes 2026-05-14 Fix 13 framing (2026-05-17)
- [ADR-006](./ADR-006-opus-default-control-plane.md) — Opus-default control plane, Sonnet-delegated execution (2026-05-17)

## Approvals log

[`approvals-log.md`](./approvals-log.md) — durable append-only index of every approval (created with ADR-004). Atlas reads this at session start to know what's already authorized.

## Pending / candidate ADRs

- Retro-ADR for Stage 1 folder layout (`raw/wiki/output/archive/daily/atlas` curation scheme)
