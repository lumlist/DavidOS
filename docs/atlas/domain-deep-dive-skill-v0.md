# Domain Deep Dive Skill v0

Status: Draft
Owner: Atlas / DavidOS
Purpose: Define a reusable research and decision-support skill for agents making high-impact recommendations in fast-changing domains.

## Purpose

The Domain Deep Dive skill helps Atlas, project lead agents, and strategic decision-making agents refresh current domain knowledge before making important recommendations.

Agents should not rely only on stale memory when advising on strategy, architecture, tooling, product direction, GTM, safety, legal/regulatory considerations, or business model decisions.

## Trigger Conditions

Invoke this skill when a recommendation depends on current or specialized domain knowledge, especially for:

- AI system architecture
- Model, tool, framework, or provider selection
- Agent orchestration and MCP strategy
- Product strategy
- Market positioning
- Competitive landscape
- GTM or pricing strategy
- Safety, legal, privacy, or regulatory considerations
- FamilyAI market, web monitoring, parental controls, assisted living, or dependent care decisions
- AI Workspace Diagnostic Service business planning
- Customer-facing iZZi AI Systems product design

## Ad Hoc Trigger

David, Atlas, or a project lead may trigger a Domain Deep Dive manually at any time by specifying:

1. Domain
2. Decision context
3. Time horizon
4. Required output
5. Known constraints
6. Sources or competitors to include
7. Confidence threshold
8. Cost/time limit

## Automatic Trigger

Agents should recommend or invoke this skill automatically when:

- The domain is fast-changing.
- Prior context may be stale.
- The decision could materially affect product, architecture, business direction, cost, security, or reputation.
- The agent detects uncertainty that current research could reduce.
- A project planning council needs current landscape context.

If the deep dive is low-risk and within approved permissions, agents may run it directly. If it is costly, time-consuming, privacy-sensitive, or likely to disrupt work, agents should ask David first.

## Input Schema

A Domain Deep Dive request should include:

- Domain
- Decision to support
- Key questions
- Scope boundaries
- Time horizon
- Required source types
- Known assumptions
- Known constraints
- Desired output format
- Confidence requirements
- Cost/time budget
- Memory storage target

## Research Workflow

1. Restate the decision and research scope.
2. Identify what current knowledge is required.
3. Review existing DavidOS/project memory first.
4. Search current external sources when needed.
5. Separate facts, trends, assumptions, uncertainties, and opinions.
6. Compare competing tools, approaches, or market positions.
7. Identify risks, tradeoffs, and open questions.
8. Produce decision-ready recommendations.
9. Store raw research, cleaned knowledge, and final output in the appropriate memory layer.
10. Record lessons to improve future deep dives.

## Source Quality Rules

Prefer:

- Official documentation
- Primary sources
- Research papers
- Technical docs
- Product release notes
- Pricing pages
- Reputable industry analysis
- Credible user evidence when clearly labeled
- Direct competitor/product pages

Avoid over-weighting:

- Generic blog posts
- Unverified social media claims
- Vendor hype
- Stale tutorials
- Single-source conclusions

When sources disagree, the output should explain the disagreement and confidence level.

## Output Format

A Domain Deep Dive output should include:

1. Decision supported
2. Executive summary
3. Current landscape
4. Key findings
5. Options considered
6. Recommended path
7. Risks and tradeoffs
8. What would change the recommendation
9. Open questions for David
10. Suggested next action
11. Memory updates created or recommended
12. Skill improvement notes

## Memory Storage Rules

Use the DavidOS memory pattern once available:

- raw: source notes, transcripts, screenshots, rough extracts, messy research
- wiki: cleaned durable knowledge, concepts, comparisons, reusable insights
- output: final decision memos, recommendations, plans, decks
- archive: deprecated or superseded research

Until the memory structure is finalized, store final outputs in the relevant project docs and clearly label raw versus durable material.

## Cost and Time Controls

Each deep dive should state:

- Expected effort level: light, standard, deep, or exhaustive
- Expected runtime
- Expected cost if available
- Stop condition
- Whether David approval is needed before continuing deeper

Default effort levels:

- Light: quick landscape refresh and recommendation
- Standard: multi-source research with structured output
- Deep: broad research, comparison, and decision memo
- Exhaustive: only with explicit approval

## Self-Improvement Loop

After each deep dive, record:

- Was the output useful?
- Was the scope correct?
- Were sources high quality?
- Was the research too shallow or too broad?
- Did the recommendation help the decision?
- What should change next time?
- Could any part become a reusable sub-skill or automation?
- Could the workflow be cheaper, faster, or more reliable?

Repeated lessons should update this skill spec, project playbooks, and Atlas operating policy.

## Example Uses

### Atlas

Deep dive on modern AI systems, agent frameworks, MCP, memory, observability, model selection, cost optimization, governance, and AI operating system business models before making iZZi AI Systems architecture recommendations.

### FamilyAI Lead

Deep dive on child web monitoring, parental control competitors, teen safety trends, assisted living, dependent care, family intelligence products, privacy concerns, and regulatory considerations before product strategy decisions.

### DavidAIStory Editor

Deep dive on personal knowledge capture, life logging, journaling tools, story extraction workflows, and narrative memory systems before recommending capture architecture.

### AI Systems Business Lead

Deep dive on AI consulting, managed AI workspaces, diagnostic offers, agent ops, tool audits, pricing, and customer willingness to pay before business model decisions.

## Relationship to Tool Selection Policy

The adaptive tool-selection policy should trigger this skill before high-impact decisions in fast-changing domains.

The Domain Deep Dive skill should also evaluate whether the research workflow itself should become more automated, cheaper, faster, or more reusable over time.

## Open Questions

1. Should Domain Deep Dive outputs use a standard scoring rubric?
2. Should Atlas be allowed to run standard deep dives automatically, or only light dives without approval?
3. How should source quality be measured in the custom UI?
4. How should deep dive results update memory without polluting durable knowledge?
5. What is the right review cadence for improving this skill?
