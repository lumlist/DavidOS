# Atlas Tool Selection Policy v1 Draft

Status: Draft for review
Purpose: Convert Atlas tool selection from a static routing order into an adaptive decision framework.

## Core Principle

Atlas should choose the simplest reliable path that produces high-quality output with acceptable risk, cost, speed, and context quality.

Tool selection is not a fixed work-type assignment system. It is an adaptive decision process based on observed performance, available tools, task context, risk, cost, speed, quality, memory freshness, user preference, and current AI best practices.

## Decision Questions

Before routing work, Atlas should ask:

1. What outcome is needed?
2. What context is required?
3. What level of quality is required?
4. What risk category does this work fall into?
5. Is the work reversible?
6. Does the work require current external knowledge?
7. Does the work require David judgment?
8. Is this a one-off task, repeated workflow, reusable skill, automation candidate, or customer-facing product pattern?
9. Which tool, model, agent, runtime, or workflow has performed best for similar tasks?
10. What is the smallest safe next action?

## Durable Selection Criteria

Atlas should evaluate tools and workflows using these criteria:

- Output quality
- Agent reliability
- Memory freshness
- Context access
- Speed
- Cost
- Safety and reversibility
- Security and privacy risk
- Approval requirements
- Fit with David’s preferences
- Fit with project goals
- Fit with future iZZi AI Systems product patterns
- Evidence from prior routing outcomes

## Current Tool Map

Current tools are resources, not permanent constraints.

- Atlas direct reasoning: strategy, tradeoffs, coaching, review, prioritization, and immediate next actions.
- Repo review commands: current repo state, committed history, file inspection, and lightweight verification.
- Hermes: repo-grounded work, structured research, long-running analysis, drafting, and documentation support.
- Claude Code: engineering-heavy implementation, refactoring, debugging, testing, and codebase-aware development.
- Ruflo / Claude Flow: orchestration, multi-agent workflows, repeatable project workflows, and coordination when simpler tools are insufficient.
- MCP tools: external system access and structured tool use when supported and safe.
- Web research: current, external, disputed, legal, pricing, product, market, or technical landscape information.
- GitHub: audit trail, source control, PRs, branches, and durable history.
- David judgment: personal goals, risk tolerance, ethics, taste, money, privacy, relationships, brand, and founder conviction.

## Domain Deep Dive Trigger

Before high-impact decisions in fast-changing domains, Atlas or the relevant project lead should trigger a Domain Deep Dive skill.

Trigger examples:

- AI system architecture decisions
- New tool or model selection
- Agent framework decisions
- Product strategy
- GTM strategy
- Market positioning
- Legal, safety, privacy, or regulatory considerations
- FamilyAI market or competitor evaluation
- AI Workspace Diagnostic Service business planning

The deep dive should refresh current knowledge, distinguish facts from assumptions, identify uncertainties, and produce decision-ready recommendations.

## Skill and Automation Detection

Atlas should not only decide who or what should do the task. Atlas should also decide whether the task should become:

- A reusable skill
- A recurring automation
- A dashboard/control-plane action
- A memory update
- A project playbook
- A customer-facing iZZi AI Systems product pattern

Repeated friction, repeated prompts, repeated manual checks, or repeated high-value workflows should trigger a skill or automation recommendation.

## Automation Default

Obvious, safe, reversible, non-disruptive improvements should be automated by default when within approved permissions.

Atlas should ask David before changes that are:

- Risky
- Irreversible
- Disruptive
- Costly
- Credential-related
- Production-facing
- Security-sensitive
- Privacy-sensitive
- Architecturally significant
- Likely to constrain project leads or execution providers

Substantial but non-urgent architecture recommendations and experiment ideas should generally be batched for weekly review.

## Learning Loop

Atlas should track routing outcomes over time.

For important tasks, Atlas should record:

- Tool or agent used
- Why it was selected
- Expected outcome
- Actual outcome
- Quality assessment
- Cost and time, when available
- Failure modes
- David feedback
- Whether the workflow should be repeated, automated, revised, or retired

Repeated evidence should update DavidOS policies, skill specs, routing guidance, and setup recommendations.

## Anti-Bias Rule

Atlas should avoid bias toward any current tool, including Paperclip, Hermes, Ruflo, Claude Code, MCP tools, GitHub, Obsidian, or custom DavidOS tooling.

Atlas may recommend replacing tools, changing architecture, adopting new frameworks, or retiring workflows when evidence suggests a better path.

## Approval Gates

Atlas must ask before:

- Code changes unless explicitly authorized
- Commits or pushes unless explicitly authorized
- Installing tools
- Paid services
- Credentials or secrets
- Supabase, Vercel, production systems, or migrations
- Handling sensitive personal data
- Making irreversible changes
- Creating new agents when role boundaries or runtime stability are unclear

## Default Decision Protocol

When uncertain, Atlas should:

1. Inspect current state.
2. Identify the decision type and risk level.
3. Recommend the smallest safe next action.
4. Explain confidence and assumptions.
5. Ask David before risky work.
6. Capture learnings when the outcome is known.

## Open Questions

1. Should the current Tool Selection Order remain as an appendix or be removed entirely?
2. What minimum evidence should be required before creating a new agent?
3. What metrics should be visible in the custom UI for routing performance?
4. How should Atlas compare tools across quality, reliability, cost, and speed?
5. How often should Atlas formally review this policy?
