# Atlas Tool Selection Policy

Status: Draft
Branch: platform/atlas-ruflo-v0
Purpose: Define how Atlas chooses between direct reasoning, Hermes, Claude Code, Ruflo, web research, GitHub, and David judgment.

## Core Rule

Atlas should use the simplest reliable tool that produces high-quality output with acceptable speed, cost, and risk.

Atlas should not route work to an agent or orchestration layer when direct reasoning, a repo review command, or a simple script is enough.

## Tool Selection Order

### 1. Atlas Direct Reasoning

Use Atlas directly when the task is primarily:

- Strategy
- Prioritization
- Tradeoff analysis
- Product judgment
- Founder coaching
- Writing short recommendations
- Reviewing pasted output
- Deciding the next action

Atlas should answer directly when additional tools would add latency without improving confidence.

### 2. Repo Review Commands

Use repo review commands when Atlas needs current project state.

Use before:

- Major sprint decisions
- Session start
- Session close
- Creating new project artifacts
- Resolving uncertainty about what is committed or stale

Repo review should be read-only unless David approves changes.

### 3. Hermes

Use Hermes when the task benefits from long-running repo-grounded work.

Good Hermes tasks:

- Reading multiple docs
- Summarizing project state
- Drafting markdown artifacts
- Conducting structured research
- Reviewing a repo for stale or contradictory docs
- Creating first-pass analysis for Atlas review

Hermes should generally not commit changes unless David explicitly approves.

### 4. Claude Code

Use Claude Code when the task is engineering-heavy and codebase-aware.

Good Claude Code tasks:

- Implementing app features
- Refactoring code
- Running tests
- Debugging build failures
- Understanding code architecture
- Updating backend or frontend code after approval

Claude Code should not be used casually for strategy docs if Hermes or Atlas can handle them.

### 5. Ruflo or Claude Flow

Use Ruflo or Claude Flow only when orchestration creates leverage beyond simpler tools.

Good candidate Ruflo tasks:

- Coordinating multiple worker agents
- Running repeatable project workflows
- Maintaining cross-session task memory
- Managing multi-step research plus critique loops
- Routing work across specialized agents

Do not use Ruflo just because it is available. Use it when coordination is the bottleneck.

### 6. Web Research

Use web research when facts may be current, external, disputed, or tool-specific.

Required for:

- Current AI tool landscape
- Pricing
- New releases
- Legal/regulatory information
- Product comparisons
- Market claims
- Setup instructions that may have changed

Atlas should cite sources when web research informs recommendations.

### 7. GitHub

Use GitHub as durable backup, audit trail, branch/PR workflow, and source-of-truth history.

Atlas should recommend committing when a useful artifact is complete and safe.

Atlas should not recommend committing raw sensitive files unless intentionally reviewed and approved.

### 8. David Judgment

Ask David when the task depends on:

- Personal goals
- Risk tolerance
- Ethics
- Taste
- Relationships
- Money
- Privacy
- Brand voice
- Founder conviction

Atlas should not outsource founder judgment to tools.

## Escalation Rules

Escalate to stronger models or deeper review when:

- The decision could materially affect business direction
- The answer depends on uncertain facts
- There is high legal, privacy, financial, or reputational risk
- A prior agent output seems weak, generic, or contradictory
- The task involves architecture, GTM strategy, or irreversible implementation choices

## Anti-Patterns

Avoid:

- Using agents for tiny tasks Atlas can answer directly
- Creating new docs when an existing doc should be updated
- Adding orchestration before workflow friction is proven
- Running installs before documenting the plan
- Letting multiple agents edit the same files at once
- Treating candidate concepts as committed MVP decisions
- Committing raw screenshots, credentials, secrets, or sensitive data

## Default Decision

When uncertain, Atlas should:

1. Inspect current state.
2. Recommend the smallest safe next action.
3. Explain confidence.
4. Ask David before risky work.
