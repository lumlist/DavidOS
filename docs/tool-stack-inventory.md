# Tool Stack Inventory

Purpose: Track tools, what they are used for, what they are good at, and whether they should remain in the personal AI workspace.

## Current Tools

| Tool | Current Use | Strength | Weakness / Risk | Keep / Test / Drop |
|---|---|---|---|---|
| ChatGPT | Expert advisor, strategy, writing, reasoning, planning | Strong reasoning, continuity, guidance | Needs structured external memory for complex projects | Keep |
| Hermes | VPS-based agent execution, repo docs, research artifacts | Can read/write repo files and run agent workflows | Delegation/write behavior needs inspection after every run | Keep/Test |
| GitHub | Version control and audit trail | Durable project memory and decision history | Requires discipline | Keep |
| VPS | Remote working environment | Persistent compute environment | Needs security and operational hygiene | Keep |
| Supabase | FamilyAI backend candidate | Fast app backend | Migration paused pending MVP clarity | Keep/Pause |
| Vercel | Deployment | Fast preview deployments | Not relevant to current research sprint | Keep |
| OpenRouter | Model access for Hermes | Flexible model routing | Key/security and model cost management needed | Keep |
| Paperclip | Possible future AI labor control plane | Could manage goals, budgets, agents, governance | Too early to adopt tonight | Test later |
| Perplexity | Research support | Fast web synthesis | Requires source verification | Test |
| NotebookLM | Source-grounded synthesis | Good for uploaded documents | Less useful for agent execution | Test |
| Claude | Strong writing/reasoning alternative | Strong long-form analysis | Separate context silo | Test |

## Model Escalation Rules

| Task | Model Tier |
|---|---|
| Routine drafting | Mid-tier |
| Research organization | Mid-tier |
| Source-quality review | Strongest available |
| Product wedge decision | Strongest available |
| Legal/privacy risk critique | Strongest available plus human expert |
| Final MVP recommendation | Strongest available plus founder decision |

## Open Questions

1. Should Paperclip be tested once there are 5+ recurring agents?
2. Should this workspace become a Git repo?
3. Should dashboards live in markdown, Notion, local app, or custom UI?
4. Which tools should be connected through APIs?
5. Which data should stay local only?
