# Workspace

Documentation specific to the hermes-workspace UI installation and configuration. The Workspace is the daily-driver multi-agent surface for DavidOS, adopted 2026-05-11 ([ADR-001](../decisions/ADR-001-adopt-hermes-workspace.md)).

## Contents

- [`baseline-config.md`](baseline-config.md) — profile, default model, theme, permissions, session hygiene

## Why a separate directory

Workspace-level concerns (UI configuration, profile setup, session-management patterns) are distinct from agent-level concerns (`docs/atlas/`), decision-level concerns (`docs/decisions/`), and architecture-level concerns (`docs/architecture/`). Keeping them in one place makes the customer-zero pattern reusable — a future iZZi customer onboarding to a Workspace deployment can read this directory as their setup guide.

## What's here vs. elsewhere

| Topic | Lives in |
|---|---|
| Workspace install procedure | This directory (eventually) |
| Stack and service architecture | [`docs/architecture/`](../architecture/) |
| Why hermes-workspace was chosen | [ADR-001](../decisions/ADR-001-adopt-hermes-workspace.md) |
| Auth setup | [ADR-002](../decisions/ADR-002-anthropic-oauth-over-api-key.md) |
| Agent definitions and policies | [`docs/atlas/`](../atlas/) |
| Current session state | [`docs/sessions/NEXT-SESSION-OPEN.md`](../sessions/NEXT-SESSION-OPEN.md) |
