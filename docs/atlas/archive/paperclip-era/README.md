# Paperclip-Era Archive

Files in this directory describe an operating model that was **frozen on 2026-05-11**. They are preserved for historical context but should not be treated as current truth.

## Why these are archived

DavidOS originally ran on Paperclip-Atlas as the daily-driver UI/agent stack. On 2026-05-11 we migrated off Paperclip (productivity-review scheduler auto-block loop, unfixable in config) and adopted hermes-workspace + Anthropic OAuth. See:

- [`docs/decisions/ADR-001-adopt-hermes-workspace.md`](../../../decisions/ADR-001-adopt-hermes-workspace.md)
- [`docs/decisions/ADR-002-anthropic-oauth-over-api-key.md`](../../../decisions/ADR-002-anthropic-oauth-over-api-key.md)
- [`docs/decisions/ADR-003-paperclip-frozen-atlas-memo-library.md`](../../../decisions/ADR-003-paperclip-frozen-atlas-memo-library.md)

## What's in here

| File | What it describes | Superseded by |
|---|---|---|
| `paperclip-setup-plan.md` | Initial Paperclip install plan | ADR-003 |
| `paperclip-reference-sources.md` | Paperclip docs references | ADR-003 |
| `paperclip-v0-workspace-structure.md` | Paperclip-era workspace layout | ADR-001 |
| `paperclip-atlas-activation-context.md` | Atlas activation under Paperclip | ADR-003 |
| `davidos-operating-ui-v1-plan.md` | v1 UI plan (Paperclip + Obsidian-MCP + Langfuse) | ADR-001 |
| `davidos-operating-ui-v1-plan-revised.md` | Revised v1 UI plan | ADR-001 |
| `davidos-operating-ui-v1-requirements.md` | DAV-16 UI requirements memo | ADR-001 |
| `davidos-session-workflow-v0.md` | Paperclip-issue-comment session lifecycle | `docs/sessions/NEXT-SESSION-OPEN.md` + future ADR |
| `ruflo-atlas-v0-plan.md` | Ruflo/Claude Flow as orchestrator candidates | ADR-001 (hermes-workspace adopted) |
| `runs/2026-05-09-atlas-activation-memo-v0.md` | DAV-1 Paperclip activation run | Historical |

## What's still useful in here

Substantive content survives the substrate change even if the mechanism doesn't. If you're looking for:

- **Atlas role definition** → live version in [`docs/atlas/atlas-operating-spec.md`](../../atlas-operating-spec.md) (note: still references some Paperclip mechanics, slated for rewrite)
- **Approval gate policy** → live version in [`docs/atlas/approval-policy-v0.md`](../../approval-policy-v0.md) (substance valid; mechanism needs ADR-004)
- **Session workflow** → [`docs/sessions/NEXT-SESSION-OPEN.md`](../../../sessions/NEXT-SESSION-OPEN.md) is the current canonical session memo
- **UI design intent** → captured in the three v1-plan docs here. Concepts (Daily Operating View, structured context packs) may inform future Workspace customization.
