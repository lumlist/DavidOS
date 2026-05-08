# Context Packs

Purpose: Store durable context that can be reused by ChatGPT, Hermes, Claude, or any future agent system.

## Personal Context Pack

### Professional Background

- 13+ years in eCommerce, marketplace, and business development across Amazon and Walmart.
- Experience includes seller recruitment, strategic account management, SMB seller acquisition, onboarding, lifecycle systems, operational workflows, and programmatic recommendations.
- Strongest professional patterns: customer acquisition, onboarding, activation, segmentation, scalable support, GTM strategy, executive storytelling, and AI-enabled workflow design.

### Current Priorities

1. Build FamilyAI / FamilyOS into a viable business.
2. Create a personal AI workspace and agent operating system.
3. Explore whether AI workspace diagnostics and implementation could become a service business.
4. Improve health, fitness, and personal routines.
5. Build durable systems for managing business ideas, research, decisions, and execution.

### Communication Preferences

- Direct, structured, and practical.
- Avoid vague encouragement.
- Push back when assumptions are weak.
- Separate facts, assumptions, recommendations, and decisions.
- Provide copy-pasteable commands when working in terminal.
- Prefer step-by-step execution when doing technical work.

### Decision-Making Preferences

- Move fast, but do not create false confidence.
- Use evidence and critique for make-or-break decisions.
- Use stronger models for major strategy, legal/privacy, product, and investment decisions.
- Use cheaper or mid-tier models for drafting, organizing, and routine research.
- Preserve important decisions in durable docs.

### Current Business Focus

FamilyAI / FamilyOS is the active primary business exploration.

Current strongest wedge conviction:
- Child Web Safety and Growth Copilot

Likely long-term platform:
- Family Command Center

Important adjacent expansion:
- Dependent Care Coordination Copilot

### Sensitive Boundaries

- Agents should not spend money, create accounts, send messages, post publicly, apply migrations, edit production systems, or make legal/privacy conclusions without explicit approval.
- Sensitive personal, financial, legal, health, relationship, or business information should be handled carefully.
- Secrets, API keys, credentials, and tokens should never be printed, committed, or pasted into chat.

---

## FamilyAI Context Pack

### Current Phase

FamilyAI is in a product-definition and research sprint before committing to a production backend path or applying Migration 001 to the main remote Supabase dev project.

### Current Repo

`/home/hermes/projects/familyAI`

### Current Branch Pattern

- `main`: stable merged sprint foundation
- `product/research-sprint-day-1`: active research branch

### Current Strategic Direction

The founder's strongest emotional conviction is Child Web Safety and Growth Copilot.

The key thesis:
- AI will compound disconnection and online influence risks for families.
- Current parental-control tools may be too punitive, blunt, or easy to bypass.
- FamilyAI should help parents understand, support, and connect rather than simply surveil or punish.

### Current Research State

Day 1 child safety research exists, but Opus reviewed it and found it is not decision-grade yet.

Known issues:
- Some claims may be stale, weakly sourced, or fabricated-looking.
- Bark AI features must be verified.
- Competitor matrix needs expansion.
- Parent quotes need real links or composite labels.
- Legal/privacy questions need expert review before launch.
- Willingness-to-pay and teen acceptance are still unproven.

### Current Rule

Do not create `docs/product/07-recommended-mvp.md` until research blockers are addressed.

Do not apply Migration 001 remotely until the sprint produces a clearer MVP and backend recommendation.

---

## Tooling Context Pack

### VPS

Primary VPS user:
`hermes`

Primary FamilyAI repo:
`/home/hermes/projects/familyAI`

Personal AI workspace:
`/home/hermes/projects/personal-ai-workspace`

SSH pattern:
`ssh hermes@159.223.166.217`

### Hermes

Hermes main agent works with OpenRouter when launched with:

`OPENROUTER_API_KEY="$OPENROUTER_API_KEY" hermes`

Delegation passed a simple subagent smoke test, but prior delegated research failed to write expected files. Inspect all outputs before trusting them.

### Known Security Rules

- Do not expose API keys in screenshots or grep output.
- Keep secret redaction enabled.
- Run secret scans before commits involving research prompts or generated docs.
- Commit only after inspecting generated files.

