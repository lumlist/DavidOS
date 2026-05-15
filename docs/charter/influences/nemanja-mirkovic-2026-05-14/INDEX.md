# Raw Material Index — Nemanja Mirkovic: "15 Hermes Agent use cases I wish I tried sooner"

**Captured:** 2026-05-15 00:08 CDT (video uploaded 2026-05-14)
**Source video:** [https://www.youtube.com/watch?v=gpJNLgv3vdw](https://www.youtube.com/watch?v=gpJNLgv3vdw)
**Channel:** Nemanja Mirkovic — [LinkedIn](https://www.linkedin.com/in/nemanja-mirkovic/) · [X @Nemanjadotcom](https://x.com/Nemanjadotcom) · [GitHub](https://github.com/nemanjadotcom)
**Business context:** Founder of [PressWhizz](https://presswhizz.com/) (SEO/backlinks product)
**Video duration:** 11:58 | **Views at capture:** 3,400 | **Upload date:** 2026-05-14

---

## Purpose of this document

This is a **raw material index**, not an analysis. It points to the primary source materials extracted from the video. Analysis, principle extraction, comparison to DavidOS, and adoption recommendations are Atlas's job — he should consume the raw materials directly, not this document's framing.

The Computer-Sonnet pass that produced this file was deliberately limited to:
- Extraction (transcript, screenshots, metadata)
- Time-coding (mapping screenshots to timestamps and topics)
- Inventory (cataloging the file artifacts)

No principle extraction. No framework synthesis. No tool-choice reasoning. No comparison work.

---

## Materials available for Atlas's analysis

All files are at `/home/hermes/projects/personal-ai-workspace/docs/charter/influences/nemanja-mirkovic-2026-05-14/` once committed:

| File | Description | Bytes / Lines |
|---|---|---|
| `video.info.json` | Full YouTube metadata, including description with timestamp index and tool list | ~50 KB |
| `transcript-cleaned.txt` | Cleaned timestamped transcript (every line tagged with `[HH:MM:SS]`) | 296 lines |
| `video.en.vtt` | Raw WebVTT subtitles (preserved for reference) | ~94 KB |
| `screenshots/frame_*.jpg` | 26 screenshots at key timestamps | varies |

The video file itself (`video.mp4`, 22.7 MB) lives in the Computer workspace but is too large to commit. Atlas can work entirely from the transcript + screenshots + metadata.

---

## Video structure (from author's own timestamp index in description)

```
00:00  Why I changed how I use Hermes Agent
00:40  Hermes as an AI operator, not builder
01:00  Backlink ordering CLI example
01:40  My 15 favorite Hermes Agent use cases
02:00  SEO analyst agent
02:40  Lead scraping + enrichment workflow
03:30  CRM + inbox management
04:00  Sales call analyst
04:20  Research agent for AI/news summaries
05:20  Content production workflows
05:50  Content repurposing
06:00  Second brain systems
06:30  Executive assistant workflows
07:00  Business analyst + KPI reporting
07:20  Operations employee
07:50  Customer support workflows
08:00  Shopify assistant
08:30  Investment analyst agent
09:50  Advisory council with NotebookLM
11:20  Final thoughts + how to apply this
```

The author's framing claim, from the description:
> "Framework: Claude/Codex build the systems → Hermes operates them"

---

## Screenshot index — what's visible at each timestamp

Each screenshot is at `screenshots/frame_<HH-MM-SS>.jpg`. Visual content notes are descriptive only, not interpretive.

| Screenshot | What's on screen |
|---|---|
| `frame_00-00-25.jpg` | Headline title slide: "Hermes Agent / I've been using it wrong / Hermes is an operator, not a builder" + supporting paragraph + three tags ("Claude / Codex build", "Hermes operates", "Digital employees") |
| `frame_00-00-50.jpg` | Two-column comparison labeled "Builders vs Operators": Claude Code/Codex side and Hermes Agent side, each with 4 bullet descriptors |
| `frame_00-01-15.jpg` | Code editor screen (VS Code or similar) showing PressWhizz CLI work — visible file tree on left includes `presswhizz-cli/`, `agents`, `cmd`, `internal`, `pkg`, `scripts`, `space`, `qa/ignore`, `qo_mod`, `README.md`, plus markdown displayed in main panel with shell commands referencing `presswhizz`, `presswhizz --json`, `agent install`, etc. |
| `frame_00-01-45.jpg` | Full sidebar list of his 15 "employees" with names + tag-style descriptors (e.g., "SEO Analyst — ranking losses · content updates", "Lead Scraper + Enrichment — prospecting · enrichment · CRM sync") |
| `frame_00-02-15.jpg` | "SEO Analyst" spec card. Shows uniform 4-field schema: INPUTS / PROCESSING / OUTPUTS / business outcome at bottom. Category tag in corner: GROWTH EMPLOYEE |
| `frame_00-02-50.jpg` | Same template, "Lead Scraper + Enrichment", GROWTH EMPLOYEE |
| `frame_00-03-30.jpg` | "Sales / CRM Assistant", GROWTH EMPLOYEE |
| `frame_00-03-50.jpg` | (Repeat / overlap) Sales/CRM Assistant visible |
| `frame_00-04-10.jpg` | "Sales Call Analyst", GROWTH EMPLOYEE |
| `frame_00-04-30.jpg` | "Research Assistant", CONTENT EMPLOYEE |
| `frame_00-05-00.jpg` | Mid-section — research agent output sample visible |
| `frame_00-05-30.jpg` | "Content Producer", CONTENT EMPLOYEE |
| `frame_00-05-55.jpg` | "Repurposing Engine", CONTENT EMPLOYEE |
| `frame_00-06-15.jpg` | "Second Brain", CONTENT EMPLOYEE |
| `frame_00-06-45.jpg` | "Executive Assistant", BUSINESS EMPLOYEE |
| `frame_00-07-10.jpg` | "Business Analyst", BUSINESS EMPLOYEE |
| `frame_00-07-30.jpg` | "Operations Employee", BUSINESS EMPLOYEE |
| `frame_00-07-55.jpg` | "Customer Support / Community", BUSINESS EMPLOYEE |
| `frame_00-08-15.jpg` | "Shopify Store Assistant", COMMERCE EMPLOYEE |
| `frame_00-08-45.jpg` | "Investment Analyst", THINKING EMPLOYEE |
| `frame_00-09-15.jpg` | Workspace screenshot ("Mission Control"). Visible channel list in left sidebar: `events`, `Server Boosts`, "Text Channels" (general, hermes-Structure, morning-brief, 09/16/2026, announcements), "Videos" (How to use Hermes Agent for free, Hermes use cases video), "Investments" (investment-analysis, portfolio-tracker), "Apps" (sara, warren). Main panel shows investment analyst output with structured per-stock notes. |
| `frame_00-09-45.jpg` | Continued investment analyst output — more detailed structured analysis ("MSFT: core position", "NVDA: smaller aggressive satellite", META analysis section, "Position Framing" with bucket/ticker/example weight logic) |
| `frame_00-10-15.jpg` | "Advisory Council", THINKING EMPLOYEE |
| `frame_00-10-45.jpg` | Code editor showing his NotebookLM Council workspace file tree. Visible files: `agents/skills`, `NOTEBOOKLM-COUNCIL/`, `bm-council/SKILL.md`, `notebooklm-council/.claude`, `notebooklm-council/skills`, `gnit-me`, `grill-me`, `output/`, `github-repo`, `SKILL.md`, `notebooklm-council.html` (?), `AGENTS.md`, `presswhizz-council-overview.html`, `skills-lock.json`, `USER.md`. Right panel shows a chat interface with a query about NotebookLM connection. |
| `frame_00-11-15.jpg` | Same workspace, chat panel now shows results. Visible content includes structured response with items: "Sales call intelligence", "Offer optimization agent", "Content repurposing agent", "Customer proof flywheel", "Operations bottleneck finder", "The Core Difference" |

---

## Author's complete tool stack (from video description)

Tools the author names explicitly in the description:

- Hermes Agent
- Claude
- Codex
- NotebookLM
- Firecrawl
- Clay
- Apify
- SERPer (Serper)
- Ahrefs
- Semrush
- Shopify MCP
- HighLevel CRM

Additional tools surfaced in transcript but not in description:
- AnyMailFinder (lead enrichment)
- Instantly (outbound email via MCP)
- Pinecone (mentioned for Second Brain, "more advanced")
- Obsidian (mentioned for Second Brain, "everyone loves it, will give it a try")
- Supabase (mentioned in Second Brain category)
- DataForSEO (visible in SEO Analyst spec card)
- Discord (visible in Customer Support spec card)
- Google Search Console, GA4 (visible in SEO Analyst spec card)

---

## Key transcript markers — author-stated claims worth noting verbatim

These are direct quotes from the transcript. They are surfaced here for Atlas to evaluate, not interpreted.

**On builder vs operator (00:24–00:40):**
> "It absolutely can do all those things, but as we can see here it's slower and less token efficient than Claude or Codex in building apps or internal tools or systems. So these days I prefer to use Hermes as an operator or AI employee within the system that I build with Claude or Codex."

**On the concrete grounding example (00:55–01:40):**
> "I'm building this CLI that can connect your agent to the marketplace and order backlinks on your behalf... I would be using Codex and not Hermes to build this and to test this. And Hermes can operate this CLI and order backlinks for me, but I wouldn't be using Hermes to build this actual project."

**On finding ideas from the Nous community (01:53–02:00):**
> "If you want more ideas, you can find a ton of them here on News Research [Nous Research] website. And you can just browse and get ideas how people are using Hermes Agent."

**On the Research Agent's self-improvement (04:42–05:01):**
> "The beauty of it is it's self-improving, so that when I rate the results, it comes up with better results the next day. And this is how it looks. So, basically every day I receive one message like this..."

**On the Content Producer being self-referential (05:24–05:40):**
> "If let's say I spot a news about, let's say Hermes agent, I can send this to my Hermes agent, and then it creates the idea for a video. That's kind of how I came up with this. I saw the blog post here, and I sent it to my agent, and we worked out an idea for this video."

**On Second Brain tool choice (06:13–06:25):**
> "Notebook LM is just my preferred tool. Obsidian, I've only briefly tested, everyone loves it. I will give it a try, I promise, and then I will report back. And Pinecone is a bit more advanced, it's a database. So, it's a whole different video."

**On Business Analyst scoping (07:17–07:24):**
> "Obviously, scope it so that you don't give it sensitive information."

**On Operations Employee cron (07:32–07:40):**
> "It has a cron job, you can schedule it on a recurring basis, so it's really good at that."

**On the agent reading dashboards (08:20–08:30):**
> "Anything that you can read on the dashboard, the agent can read as well. So, you can see how that powerful that can be."

**On the Investment Analyst integration (09:21–09:39):**
> "It also has my portfolio tracker that I created with Cloud [Claude] and Codex. And now this agent can use the portfolio tracker. I just send it a screenshot when I make a trade, and it automatically logs everything into the portfolio tracker, which has now everything I need, including options tracking. Which is something I was missing with all the these other portfolio trackers."

**On the Advisory Council mechanism (09:50–10:23):**
> "The idea is to populate notebooks with YouTube videos, books, interviews, transcripts of your favorite... It can be a YouTuber, it can be an influencer, or a writer. And then you can query Notebook LM about their knowledge and to actually get context out of this material so that you can use it in Cloud [Claude]."

**Closing framing (11:31–11:43):**
> "Find a bottleneck, find something that takes your time, even if it's scrolling through social media. You can automate that so that you can get more for your time with Hermes Agent."

---

## What Atlas should do with these materials

This is documented separately in his task prompt. The high-level expectation is:
1. Read the raw materials directly (transcript + all relevant screenshots)
2. Do his own extraction of patterns, principles, and tool-choice reasoning
3. Compare against current DavidOS substrate
4. Propose specific adoption actions with justification and tradeoffs
5. Recommend a research-automation plan for capturing this kind of leading-builder content going forward

**Computer-Sonnet's job ended at extraction and indexing.** Anything beyond that — pattern recognition, principle extraction, framework synthesis, comparison — is Atlas's pass.
