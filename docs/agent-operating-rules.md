# Agent Operating Rules

## Core Rule

Agents are allowed to help me move faster, but they should not create false confidence.

## Agents May Do Without Approval

- Draft documents
- Summarize uploaded files
- Organize notes
- Create checklists
- Identify risks
- Suggest next steps
- Compare options
- Create research plans
- Prepare prompts

## Agents Require Approval Before

- Spending money
- Creating accounts
- Sending emails or messages
- Posting publicly
- Changing production systems
- Applying database migrations
- Editing legal/privacy claims
- Making final business decisions
- Deleting files
- Committing or pushing code unless explicitly authorized

## Model Escalation Rules

Use cheaper or mid-tier models for:

- Drafting
- Organizing
- Summarizing
- Routine research
- First-pass analysis

Use strongest available models for:

- Make-or-break strategy decisions
- Product wedge selection
- Legal/privacy risk review
- Competitive threat assessment
- Final synthesis
- Investor-style critique
- Any decision where bad assumptions could materially harm the business

## Evidence Standards

For research claims, separate:

- Evidence observed
- Interpretation
- Assumption
- Open question

Any load-bearing claim needs a source, screenshot, quote, or direct user evidence.

## Current Known Tool Issue

Hermes main agent works.

Hermes delegation passed a simple subagent smoke test, but prior research delegation failed to write expected files. For now, inspect all outputs before trusting them.

---

## Repo Review Worker Rules

Agents may perform repo quality reviews when asked by Atlas or the founder.

Agents may:
- Inspect branch and git status
- Inspect recent commits
- List files and markdown headings
- Summarize completed work
- Identify stale, duplicate, or contradictory docs
- Recommend next sprint steps
- Draft worker packets
- Propose markdown-only edits

Agents must not:
- Commit or push without explicit founder approval
- Modify application code without explicit approval
- Modify migrations without explicit approval
- Touch Supabase or Vercel without explicit approval
- Print or expose credentials, API keys, tokens, or secrets
- Delete files without explicit approval
- Treat a candidate concept as an approved MVP decision

Repo review outputs should separate:
- Evidence from repo state
- Interpretation
- Assumption
- Recommended next action
