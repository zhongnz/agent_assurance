# Agent Assurance

*Agent assurance methodology for regulated EU financial services. Position paper, case study, distribution surface, supporting documentation, and operational scaffolding.*

This repository contains the project's full set of artifacts as of May 2026. The intellectual contribution is in the position paper and the case study; everything else either supports or distributes them.

If you are reading the work for the first time, the suggested entry sequence depends on what you have time for: 5 minutes — the briefing note. 15 minutes — the briefing note plus the case study's section 7 (the supervisory-engageable finding). 30 minutes — the full case study. Several hours — the position paper.

## Layout

```
.
├── paper/                      # The canonical position paper
│   ├── paper_sections_1_to_8_v0.8.1.md   # Current consolidated paper
│   ├── sections/               # Per-section files (substance identical to consolidated)
│   ├── archive/                # Superseded versions retained for verification anchor
│   ├── revision_history.md     # Internal revision history through v0.8.1
│   ├── verification_log_v0.8.md  # Audit trail for the 51 verification markers
│   └── appendix_c_source_status_v1.md  # Source-status appendix (four buckets)
├── case_study/                 # EchoLeak case study + supporting research
├── distribution/               # Audience-facing surface (briefing, abstract, visual, wrapper)
├── elliott/                    # Elliott Ash review package
├── plans/                      # Operational plans (PoC build plan)
└── decks/                      # Slide decks
```

## The canonical work

**`paper/paper_sections_1_to_8_v0.8.1.md`** — the position paper, current version. ~27,000 words across eight sections, working title *Agent Assurance in Regulated Financial Services*. The substantive contribution: the architectural argument, the necessary-but-insufficient critique of the established disciplines, the threat taxonomy, the synthesis methodology with five design principles, the reference application, the regulatory horizon, the operational recommendations, and the closing on what the paper does and does not do. Through three rounds of peer review and four rounds of source verification.

**`paper/sections/section_01_*.md` through `section_08_*.md`** — the same content as the consolidated paper, split into per-section files. Useful for editing and for sending parts of the paper without sending the whole thing. Identical in substance to the consolidated file.

**`paper/archive/paper_sections_1_to_8_v0.8.md`** — the v0.8 paper, retained as the historical anchor for the verification round before editorial compression. v0.8 was the version against which all 51 [VERIFY:] markers were resolved against primary sources; v0.8.1 is the editorial compression on top of that. If a reader ever asks "show me the paper at the point of full primary-source verification, before editorial polish," this is the answer.

**`case_study/echoleak_case_study_v2.md`** — the case study, polished and ready to publish. ~5,400 words applying the synthesis methodology retrospectively to CVE-2025-32711 (EchoLeak). The case study is the methodology's first demonstration against a real documented incident.

## The audience-specific surface

**`distribution/abstract_general_v1.md`** — 190-word general-audience abstract. The workhorse two-paragraph summary, written for distribution to readers who haven't seen the paper or case study before.

**`distribution/briefing_note_v1.md`** — 547-word one-page summary. Four paragraphs and a bulleted principles list, designed for a reader who has 3-5 minutes and wants to know what the methodology is and whether it warrants further engagement.

**`distribution/agent_assurance_visual_v1.svg`** — the one-page SVG visual. A 5x3 grid of architectural properties × established disciplines, with synthesis layer adjacent. Spatially compresses the paper's argument into one image.

**`distribution/wrapper_sample_tier2_risk_v1.md`** — sample audience-specific wrapper for Tier-2 European bank and insurer risk leaders. Cover note plus reading-order recommendation; demonstrates the wrapper pattern. Three additional audience wrappers (collaborators, regulators, conference circuit) were sketched but not built.

## The Elliott-specific package

These three artifacts were built to send the paper to Elliott Ash (scientific advisor, ETH Zurich) for review. Built but not yet used; available if you decide to circulate the paper to him.

**`elliott/abstract_v1.md`** — academic abstract drafts (A claim-first, A' claim-first with split definition, B vignette-first). A' is the locked-in version.

**`elliott/cover_note_elliott_v1.md`** — ~370-word cover note framing the paper for Elliott specifically, with three high-level feedback questions. Two placeholders remain for your judgement: salutation register and timing line.

**`elliott/executive_summary_v1.md`** — 770-word executive summary with thesis, eight-section walk-through, four areas where Elliott's perspective would be especially useful, and pointer to §8.2 for boundaries.

## The case-study supporting documents

**`case_study/echoleak_case_study_plan_v1.md`** — the two-week build plan that produced the case study. Eight-section structure with proportional word budgets, day-by-day deliverables, and risk callouts.

**`case_study/echoleak_research_notes_v1.md`** — primary-source research notes from the case-study build. Five-step attack chain, RAG spraying technique, LLM Scope Violation terminology, bypassed defences inventory, OWASP categorisation, Microsoft response, source manifest. Working notes rather than a polished artifact, but the research compounds — the same notes will support any future case study on agent-security incidents.

**`case_study/echoleak_publishing_metadata_v1.md`** — publishing metadata for the case study. Title, subtitle, byline guidance, abstract, target audience description, channel guidance, short-form announcement draft, final-checklist items.

## The operational scaffolding

**`paper/appendix_c_source_status_v1.md`** — the source-status appendix the third reviewer suggested. Catalogues the paper's load-bearing sources into four evidentiary buckets (primary regulatory documents, direct technical disclosures, secondary technical analyses, inferential or generalised claims) with reading guidance.

**`plans/poc_build_plan_v1.md`** — eight-week build plan for the proof-of-concept (Version 2: working agent + applied methodology in a Git repository). Self-build, week-by-week deliverables. Currently deferred — the case study was identified as the right substitute for an assurance venture's first artifact, and the PoC build is on hold pending strategic clarity.

**`paper/revision_history.md`** — internal revision history of the position paper through v0.8.1. Documents what changed in each version and why.

**`paper/verification_log_v0.8.md`** — the audit trail for all 51 verification markers resolved during the v0.8 round, organised by section. Documents primary or directly-corroborating sources for every load-bearing claim.

## The slide decks

**`decks/Agent-Assurance-Overall-Plan.pptx`** — venture overview deck.

**`decks/Position-Paper-Outline.pptx`** — the position paper presented in slide form.

**`decks/Technical-Appendix-v0.4.pptx`** — technical appendix deck with the fact-check log slides updated to v0.8 status. The fact-check log slides 19-20 document every correction and verification round.

## How the artifacts compose for different uses

For an academic-style review by Elliott or another senior reader: the position paper plus the verification log plus the revision history. The Elliott-specific cover note and executive summary are available if helpful, though Elliott himself doesn't need orienting artifacts.

For a Tier-2 risk-leader engagement conversation: the briefing note as opener, the one-page visual as memorable anchor, position paper sections 1, 4, 6, and 7 as targeted depth, the case study as proof of methodology in operation. The Tier-2 wrapper sample illustrates how to assemble this combination as a package.

For a conference submission or industry-publication piece: the general-audience abstract becomes the submission abstract, the case study becomes the submitted piece, the position paper is referenced as the methodological foundation. The publishing metadata document handles supporting material around the case study itself.

For an investor or collaborator who wants to understand the venture: the briefing note plus the case study. The position paper is available as depth-evidence backstop but isn't necessarily read in full.

For someone discovering the work cold (through Substack, LinkedIn, or word of mouth): the case study is the entry point, with the position paper available as the canonical methodology reference.

## Status notes

**The position paper has not yet been sent to Elliott for review.** The Elliott-specific package is built and ready when you decide to circulate.

**The case study is publishable as soon as the byline and channel decisions are made.** The working-title substitution has been applied; remaining decisions are operational rather than substantive.

**The PoC build is on hold.** The eight-week build plan exists and could be executed if specific conversations require working code rather than analytical artifacts.

**Three additional audience wrappers (collaborators, regulators, conference circuit) are not built.** Wrapper-building was deemed downstream of network clarity; building them speculatively would risk producing artifacts for hypothetical rather than real conversations.

**The continuous-assurance platform — stage two of the venture's services-to-platform-to-rating-authority arc — has no spec.** Correctly out of scope for the current phase.
