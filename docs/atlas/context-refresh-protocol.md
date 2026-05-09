# Atlas Context Refresh Protocol

Status: Draft
Branch: platform/atlas-ruflo-v0
Purpose: Define how Atlas refreshes project and system context before making recommendations or routing work.

## Core Rule

Atlas should not rely only on memory when current repo state, project docs, or recent commits can be checked.

Before major work, Atlas should refresh enough context to make a grounded recommendation without creating unnecessary process overhead.

## When To Refresh Context

Atlas should refresh context before:

- Starting a new work session.
- Switching projects.
- Making a major product, architecture, or GTM recommendation.
- Creating a new project artifact.
- Routing work to Hermes, Claude Code, Ruflo, or another worker.
- Committing or recommending a commit.
- Resuming after a long break.
- Resolving uncertainty or contradictory outputs.

Atlas may skip a deep refresh for small, local, low-risk tasks when current context is already clear.

## Refresh Levels

### Level 1: Quick State Check

Use for normal session work.

Check:

1. Current repo.
2. Current branch.
3. Git status.
4. Recent commits.
5. Immediate relevant file preview.

### Level 2: Workstream Context Review

Use when switching into FamilyAI, DavidOS, DavidAIStory, or another major project.

Check:

1. Branch and status.
2. Recent commits.
3. Relevant project docs.
4. Open decisions.
5. Current blockers.
6. Do-not-touch rules.
7. Next milestone.

### Level 3: Major Decision Review

Use before major sprint, architecture, GTM, tool-install, or implementation decisions.

Check:

1. Repo state.
2. Recent commits.
3. Relevant source docs.
4. Prior decisions.
5. Contradictions or stale docs.
6. Approval gates.
7. External facts if current information matters.
8. Confidence level.
9. Recommended smallest safe next action.

## Project Context Sources

### DavidOS

Primary sources:

- docs/atlas/
- docs/daily-dashboard-v0.md
- docs/diagnostic-loop-v0.md
- docs/project-registry.md
- scripts/repo-quality-review.sh

### FamilyAI

Primary sources:

- docs/product/
- docs/product/research/
- docs/prompts/product-sprint/
- current branch and recent commits

Special caution:

- Do not apply migrations unless explicitly approved.
- Do not touch Supabase, Vercel, credentials, or production systems without approval.
- Do not commit raw screenshots or sensitive files.
- Do not turn candidate concepts into MVP commitments prematurely.

### DavidAIStory

Primary sources:

- docs/story/
- prompts/story/
- recent commits

Special caution:

- Preserve honest story details without making the process feel like journaling homework.
- Founder approval is required before committing personal narrative entries.

## Output Format After Refresh

After refreshing context, Atlas should summarize:

1. Current state.
2. What changed recently.
3. Open decisions.
4. Risks or stale docs.
5. Recommended next action.
6. Confidence level.
7. Whether work should stay with Atlas or be delegated.

## Delegation Context Packet

When Atlas delegates work to Hermes, Claude Code, Ruflo, or another worker, include:

- Project name.
- Current branch.
- Goal.
- Files to read.
- Files allowed to edit.
- Files forbidden to edit.
- Constraints.
- Output format.
- Approval gates.
- Whether commits are allowed.

Default: workers may not commit unless David explicitly approves.

## Self-Improvement Trigger

If context refresh reveals repeated friction, missing docs, stale state, command failures, or tool confusion, Atlas should propose one practical DavidOS improvement.

Atlas should prefer improving existing docs or scripts before adding new process.
