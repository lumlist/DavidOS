# Ruflo Atlas v0 Plan

Status: Draft
Branch: platform/atlas-ruflo-v0
Purpose: Define how Atlas, Paperclip, Ruflo, Claude Flow, Hermes, and DavidOS should fit together without overengineering the system.

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

## Paperclip Architecture Update

Paperclip is the preferred candidate for the company-style control plane.

Atlas should not be trapped inside Ruflo. Atlas should operate at the system layer as David’s primary AI systems consultant, advisor, and chief of staff.

Ruflo or Claude Flow should be treated as orchestration providers available to Atlas or project leads when they improve outcomes. Hermes remains a proven worker and may continue to be used directly or through future integrations.

Paperclip should represent the AI organization: Atlas at the system layer, project leads for major workstreams, and execution providers such as Hermes, Ruflo, Claude Code, MCP tools, web research, scripts, and GitHub.

Atlas should not impose system-layer rules that unnecessarily constrain project leads or orchestration providers. If a system policy conflicts with a project lead’s proposed approach, Atlas should surface the tradeoff and help David decide.

Atlas remains tool-agnostic. Its advantage is continuously evaluating which tools, workflows, and providers best serve David’s goals as the system evolves.

Atlas also has a side hustle: helping David build a tool-agnostic AI-system diagnostic tool and business.

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
