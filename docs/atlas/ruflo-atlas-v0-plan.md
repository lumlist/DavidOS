# Ruflo Atlas v0 Plan

Status: Draft
Branch: platform/atlas-ruflo-v0
Purpose: Define how Atlas will be built on Ruflo or Claude Flow without overengineering DavidOS.

## Current Finding

The available npm package is ruflo, not ruvflo.
The related package family also includes claude-flow and @claude-flow/cli.
Claude Code is not currently installed on the VPS path.

## Atlas Role

Atlas is the primary AI consultant, operator, and systems architect for DavidOS.
Atlas helps David build, maintain, and improve DavidOS while supporting active workstreams such as FamilyAI, DavidAIStory, AI agents, experiments, and future businesses.

## Design Principle

Atlas should use existing tools by default.
Atlas should not recreate Hermes, Claude Code, GitHub, MCP, or orchestration logic unless a repeated workflow gap proves custom process is needed.
Custom logic should be created only when it improves speed, quality, safety, cost, or consistency in a measurable way.

## Target Architecture

- David talks to Atlas as the primary interface.
- DavidOS stores durable context, goals, project states, policies, prompts, and diagnostics.
- Ruflo or Claude Flow may become the orchestration substrate for Atlas.
- Claude Code may become the repo-native engineering execution layer.
- Hermes remains a proven worker until Ruflo is validated.
- GitHub remains the durable backup and audit trail.

## v0 Scope

Atlas v0 should:

1. Load DavidOS context before recommendations.
2. Know current project states across FamilyAI, DavidOS, and DavidAIStory.
3. Route tasks to the right tool or agent.
4. Preserve approval gates for risky actions.
5. Improve itself after friction, errors, or end-of-day review.

## Approval Gates

Atlas or workers may inspect, summarize, plan, and draft.
Atlas must ask before file edits, commits, pushes, credentials, paid services, Supabase, Vercel, production systems, or sensitive data handling.

## Install Sequence

1. Verify package names and versions.
2. Install and authenticate Claude Code only after approval.
3. Install Ruflo or Claude Flow only after Claude Code is working.
4. Run one read-only Atlas task.
5. Compare Ruflo output against current ChatGPT plus Hermes workflow.
6. Expand permissions only if the test improves speed, quality, and reliability.

## Open Questions

- Should Atlas v0 run primarily through Ruflo, Claude Code, or a hybrid?
- What is the minimum useful Ruflo test?
- Which tasks should remain in Hermes?
- What permissions should Atlas have by default?
- How should Atlas measure speed, security, cost, consistency, and goal alignment?
