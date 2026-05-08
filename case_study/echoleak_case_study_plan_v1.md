# EchoLeak Case Study — Build Plan

*A retrospective application of the synthesis methodology to CVE-2025-32711. Document, not code. One to two weeks of focused writing. Output is a publishable analytical artifact that serves three purposes: demonstrates methodology in operation, surfaces tooling specs for the subsequent build, and functions as a network-mapping artifact that people can read and respond to.*

## What you're building

A 5,000-8,000 word analytical document that takes a real, well-documented agent incident — EchoLeak (CVE-2025-32711) — and applies the synthesis methodology to it retrospectively. The document answers, in structured form: what the threat register would have flagged before the incident; where the toxic-flow analysis would have caught the composition; what runtime context capture would have preserved at the moment of exploitation; which controls from the matrix would have applied; what the supervisory-engageable finding would have looked like.

The document is publishable. The audience is general — the same audience the briefing note targets, but in a longer and more analytical form. Format is editorial-quality long-form, not academic paper, not consulting deliverable. Closer to a Stratechery or Lawfare piece than to either a Big Four assurance document or a security-firm research report.

## Why EchoLeak specifically

Three reasons to anchor on EchoLeak rather than another incident.

First, the documentary base is exceptional. CVE record with Microsoft as CNA. Aim Labs technical writeup. arXiv academic case study (2509.10540). Checkmarx independent technical analysis. SOC Prime, Information Security Buzz, and other secondary coverage. The chain of evidence is more complete than for any other agent incident.

Second, the paper already opens with EchoLeak. Building the case study around it means the case study and the paper reinforce each other, and any reader of one can see the other lands. The case study extends the paper's vignette into a full analytical artifact rather than introducing a new anchor.

Third, EchoLeak is a "boundary case" agent — clearly satisfies foundation-model reasoning and persistent state, exhibits tool-like retrieval behaviour, but with constrained delegated authority. This is actually advantageous for the case study: it forces explicit handling of where the methodology bites and where its bite is conditional on architectural specifics, which is more honest and more interesting than a maximal-agent case where the methodology applies straightforwardly.

## Document structure

Eight sections, roughly proportional in length to importance:

**1. The incident** (~600 words). Plain narrative reconstruction. What was disclosed, by whom, when. Mechanism: how the email-borne instructions reached Copilot's reasoning context, how the model produced the instruction-following behaviour, how the markdown-image exfiltration channel composed with the Microsoft Teams proxy to bypass content security policy. No methodology yet — just the facts as the public record establishes them.

**2. What each component did** (~600 words). The composition-vulnerability framing. The mailbox indexer worked. The retrieval system worked. The model invocation worked. The egress channel was sanctioned. Each component evaluated against its own controls behaved as designed. The vulnerability lived between the components, not within any of them. This section grounds the methodology argument: existing per-component controls couldn't have caught EchoLeak, and the methodology needs to be tested against that fact.

**3. What the threat register would have flagged** (~800 words). Apply the OWASP Top 10 for Agentic Applications categories and the five cross-cutting patterns from §3.2 to the EchoLeak deployment as it existed pre-disclosure. Most relevant categories: ASI03 (prompt injection), ASI04 (tool exploitation), the lethal trifecta pattern (private data + untrusted content + external communication). Be honest about which patterns the methodology surfaces vs. which are visible only with hindsight. The threat register is one of the methodology's most-cited outputs; this section is where its analytical content gets concrete.

**4. Where toxic-flow analysis would have caught the composition** (~700 words). Apply compositional analysis to the Copilot tool inventory. Untrusted-input source: incoming email indexed into retrievable storage. Sensitive-data access: retrieval over user's tenant content. Egress channel: markdown image rendering proxied through Teams. The path from one to the next to the third is exactly the toxic-flow pattern §3.2.4 describes. Acknowledge the boundary case: Copilot's "tools" aren't MCP-shaped, so the analysis adapts the methodology rather than applying it cleanly. The honest treatment of that adaptation is part of what makes the case study credible.

**5. What runtime context capture would have preserved** (~600 words). At the moment of exploitation, what did the model see, and what would assurance-grade context capture have stored? The retrieved email content with embedded instructions; the tool definitions available; the model's reasoning trace; the markdown image URL the model generated; the dispatch of the URL to the rendering proxy. The point of this section is that even where the threat register and toxic-flow analysis don't catch a composition prospectively, runtime evidence makes the after-the-fact reconstruction possible — and reconstruction is what supervisory dialogue depends on.

**6. Which controls from the matrix would have applied** (~700 words). Walk through TP-01, IA-01, LT-01, TF-01, ZC-01 against EchoLeak. Some apply directly, some apply with adaptation, some don't apply at all. Be specific about each. This section is the methodology's translation layer made visible: regulators want to know "which controls bear on this threat," and the case study shows the answer.

**7. The supervisory-engageable finding** (~800 words). Generate one finding in the §5.4 format, applied to EchoLeak. Title, OWASP category mapping, regulatory anchoring (DORA, AI Act, GDPR, applicable national regimes), evidence reviewed, recommendation, residual risk, ownership. This is the section that demonstrates "this is what the methodology produces when applied to a real incident" and is the most concrete operational output.

**8. What this case study establishes and what it does not** (~500 words). Closing in the §5.5 mode. The case study establishes that the methodology is operationally specifiable against a real incident with real evidence; it does not establish that the methodology would have prevented EchoLeak (the methodology is for assurance, not prevention); it does not claim Microsoft's response was inadequate (Microsoft's response was prompt and effective); it does claim that the supervisory dialogue this case study enables would have been substantively richer than what the public record currently supports.

Total target: 5,300 words. Slack for one or two sections to run longer if the analysis warrants: ceiling 8,000 words.

## Week 1: Research and structure

**Days 1-2: Source assembly.** Pull together every primary and well-corroborated secondary source on EchoLeak. The Aim Labs writeup (primary). The CVE record with Microsoft's CNA scoring (primary). The arXiv case study 2509.10540 (academic). Checkmarx's technical analysis (independent corroboration). Microsoft's eventual remediation announcement. Any subsequent academic citations of the incident. Build a source manifest with reliability ratings — this is also rehearsal for how the case study handles evidence.

**Day 3: Structure and outline.** Produce a detailed outline with section-level word budgets and the specific claims each section will make. The outline is where the analytical work happens; the writing should be assembly. If you can't outline a section in two pages, you don't yet understand what the section says.

**Days 4-5: Sections 1 and 2.** The narrative reconstruction and the per-component analysis. These sections are the most factual and the easiest to write — start here to build momentum and lock in the documentary baseline before applying the methodology.

**Risk this week.** Source overload. The temptation will be to read every secondary source and incorporate every detail. Resist. The case study isn't a literature review; it's an analytical application. Read enough to be confident in the facts, then move to writing.

## Week 2: Methodology application and finalisation

**Days 6-8: Sections 3, 4, and 5 — the methodology core.** Threat register, toxic-flow analysis, runtime context capture. These are the highest-leverage sections and the ones most likely to surface methodology gaps. Write them in order; each builds on the previous.

**Days 9-10: Sections 6 and 7 — controls and finding.** The translation layer and the operational output. Section 7 (the supervisory-engageable finding) is the artifact's punchline. Spend the time it deserves.

**Day 11: Section 8 closing and full pass.** The closing handles boundaries explicitly. The full pass tightens prose, checks citations, and verifies the document reads well end-to-end.

**Day 12: External-share polish and metadata.** Title, subtitle, byline, abstract, target audience description. Decide on publication channel (personal blog, LinkedIn long-form, Substack, or repository README — each has different reach and signal). Write the one-paragraph teaser you'll use in distribution.

**Day 13-14: Buffer and unblocking.** Software builds run long; writing builds run long too. Two days of buffer absorbs typical overrun. If the buffer isn't needed, use it to draft the LinkedIn post or short-form announcement that will accompany publication.

## What the case study should NOT do

Do not claim the methodology would have prevented EchoLeak. The methodology is assurance, not prevention. Stating this clearly is part of what makes the case study credible.

Do not criticise Microsoft. Microsoft's CNA assignment, prompt patching, and public acknowledgement were appropriate. The case study uses EchoLeak as a documented incident to demonstrate methodology, not as evidence of vendor failure.

Do not attempt to be the definitive analysis of EchoLeak. The disclosing security firm and the academic literature have that role. The case study's role is to demonstrate what the synthesis methodology produces when applied to a documented incident — a different and additive contribution.

Do not over-anchor on Copilot specifics. The methodology is for autonomous agents in regulated financial services; EchoLeak is the testbed because of its documentary completeness, not because Copilot is the target market. The case study's framing should make this explicit.

Do not extend into recommendations for Microsoft 365 deployers. That's product advice, not assurance methodology demonstration. If the analysis surfaces deployer-relevant points, they belong in a separate document.

## Success criteria

At the end of two weeks, you should have:

1. A 5,000-8,000 word analytical document, publication-quality, that takes a reader through the EchoLeak incident and the synthesis methodology applied to it.
2. A short-form announcement (LinkedIn post, blog teaser) ready to accompany publication.
3. A clearer specification for the assurance tooling that would follow — specifically, what the threat register schema, the toxic-flow analyzer, and the runtime context capture utility need to handle to produce the case study's outputs reproducibly. This becomes the spec for the eight-week tooling build.
4. A signal-collection mechanism: people who read and respond will self-identify into the audiences worth engaging, and the case study's reach will tell you something about which audiences exist.

If you're at day 14 and three of these are true, you're done. If only one or two are true, the case study isn't done yet and the tooling build should not start.

## After the case study

The case study delivers its own value. It also produces inputs to the next phase. Three concrete handoffs to the subsequent tooling build:

- **Schema specifications.** The threat register and finding documents the case study generates make explicit what fields, references, and outputs the tooling needs to support.
- **Test cases.** EchoLeak becomes a regression test for the tooling: when the tooling is built, it should be able to reproduce the case study's outputs from the EchoLeak incident as input.
- **Methodology gaps.** The case study will surface places where the methodology is underspecified — analytical edge cases, ambiguous definitions, places the framework principles don't translate cleanly into operational steps. These gaps go into the methodology backlog and inform v0.9 of the paper.

The case study, in this framing, is not a precursor to the tooling — it's the spec for the tooling. The build sequence is: case study → tooling specs → tooling → tooling applied to additional public agent systems → published portfolio of methodology applications.

That portfolio, eventually, is what your engagement conversations will rest on. Not "I built an agent and assured it" but "I have applied this methodology to several documented configurations and here are the outputs."

## Starting point

Today: confirm publication channel, lock in the source list, block fourteen days in your calendar starting on a date you'll actually keep. Write down the answer to "if I'm at day 7 and behind, what gets cut?" — having the cut decision pre-made prevents mid-build paralysis.
