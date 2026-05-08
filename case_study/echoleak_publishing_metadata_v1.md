# Publishing Metadata — EchoLeak Case Study

*Day-12 deliverable from the case study build plan. Recommended choices for title, subtitle, byline, abstract, target audience, and publication channel. Each section explains the choice and gives alternatives where the call is judgement-dependent.*

## Title

The strongest single choice is the working title already on the document:

**EchoLeak: a case study in agent-assurance methodology**

It works on three levels. It names the incident every technical reader recognises (EchoLeak), declares the document's form (a case study, which sets reader expectations correctly), and signals the methodological frame (agent-assurance methodology, which is the field the position paper is contributing to). The title makes a promise the document keeps and doesn't promise more.

Three alternatives, each defensible for different reasons:

- **EchoLeak as a case for compositional assurance.** Punchier, leads with the methodology contribution rather than the incident. Risk: a reader unfamiliar with the term "compositional assurance" may not engage; the term is the case study's contribution rather than a pre-existing handle.
- **What an agent-assurance review of EchoLeak would have produced.** More direct about the document's form, which is itself a recommendation about what such reviews should look like. Risk: phrasing as "would have produced" front-loads the counterfactual mood that some readers find weak.
- **EchoLeak: composition, assurance, and the limits of per-component review.** Three-noun rhythm gives a more academic-paper feel. Useful if the case study were being submitted to a journal or conference; less appropriate for blog or LinkedIn distribution.

My recommendation is the working title. Direct, accurate, and the kind of title a reader will use to refer to the document later — which matters for sharing.

## Subtitle

Subtitles do real work for case studies because they tell a reader scanning a list of links what the document is actually for. The case study has at least three audiences (engagement-driving readers, methodology-curious readers, technical readers interested in EchoLeak specifically) and the subtitle has to land for all three without trying too hard.

Recommended:

**Applying a synthesis methodology for autonomous AI agent assurance to CVE-2025-32711, retrospectively, to demonstrate what the methodology produces against a documented incident.**

This is twenty-six words; long for a subtitle but doing real work. It tells the reader: the document is methodology-driven (synthesis methodology for autonomous AI agent assurance), it's retrospective (not a prevention claim), it's about a specific real thing (CVE-2025-32711), and the goal is demonstration (not security analysis).

A shorter alternative: **Retrospectively applying a synthesis methodology for AI agent assurance to CVE-2025-32711.** Eleven words. Loses the "to demonstrate what the methodology produces" framing, which is the part that does the most work managing reader expectations.

My recommendation is the longer version. Subtitles aren't the place to be terse if the extra words prevent reader confusion.

## Byline

**Peter Zhong**

Optionally append affiliation if the venture has a name and you want to attach the case study to it. If it doesn't, name only. If the venture has a placeholder name not yet stable, leave it off — naming a placeholder venture in the byline would lock you into language you haven't committed to.

If Elliott Ash is co-author or named as scientific advisor, the byline could be:

**Peter Zhong, with scientific advisory from Elliott Ash (ETH Zurich)**

Be careful here. Naming Elliott as scientific advisor on the case study attaches his name to claims he hasn't reviewed. If you want the case study to carry his association, send it to him for review first; if you don't want to wait for that, name only yourself. The position paper has not yet been formally reviewed by Elliott (per earlier conversation), so attaching his name to the case study before the paper review is sequenced would be premature.

My recommendation is name only on the case study, with the position paper carrying Elliott's affiliation when it gets to that stage.

## Abstract / publication-page summary

Different from the case study's section 8 (which closes the document) and different from the case study itself. This is the 100-150 word standalone summary that appears on the publication page, on LinkedIn, in the document's own metadata for sharing. A reader reading nothing else gets this.

Recommended:

**EchoLeak (CVE-2025-32711) was a zero-click data-exfiltration vulnerability in Microsoft 365 Copilot, disclosed by Aim Labs in January 2025 and patched by Microsoft in May 2025. This case study applies a synthesis methodology for autonomous AI agent assurance to the EchoLeak configuration retrospectively, demonstrating what the methodology's outputs — threat register, toxic-flow analysis, runtime context capture specification, control matrix application, and supervisor-engageable engagement finding — produce when applied to a documented incident. The methodology is preliminary; this case study is one of several intended applications. The contribution is not a critique of Microsoft's response, which was prompt and effective, but a demonstration that agent assurance can be operationally specified against real configurations rather than only described in principle.**

This is 132 words. It does the four things a publication-page abstract needs to do: anchor the incident (sentence one), describe the document (sentence two with the named methodology outputs), set expectations about scope and contribution (sentence three), and pre-empt the most likely misreading (sentence four about Microsoft's response). The Microsoft framing in particular matters: a reader who lands on the document expecting a security-firm critique of Microsoft and finds a methodology paper instead will bounce; a reader who knows going in that this is methodology-not-critique will engage.

## Target audience description

For internal use and for any publication-channel description that asks "who is this for." Distinct from the abstract.

The case study addresses four audiences in this order of intended salience:

**Risk and assurance practitioners in regulated EU financial services.** Heads of model risk, CROs, CISOs, Heads of AI Governance at Tier-2 European banks and insurers. The case study's primary work for this audience is showing what an agent-assurance engagement output actually looks like, in supervisor-engageable form.

**AI security and AI governance researchers.** Researchers and practitioners working on the technical and methodological problems agent assurance raises. The case study's work for this audience is the alignment between the synthesis methodology's *principal-bound* design principle and Aim Labs's *LLM Scope Violation* terminology — the convergence is itself a research-relevant finding.

**Regulators and supervisor-adjacent staff.** EU national supervisors, ECB SSM, EIOPA, and equivalents who are forming positions on agent assurance. The case study's work for this audience is demonstrating what regulator-legible methodology output looks like in practice.

**General technical readers interested in EchoLeak.** The case study is a methodologically structured analysis of an incident the technical community already knows about; readers who arrived for EchoLeak content will find a different framing than the disclosing firm's writeup, the academic paper, or the technical security press provided.

## Publication channel

Three options, ranked by what they signal and what they cost.

**Personal blog or Substack.** Lowest cost, most editorial control, longest archive life, but lowest discoverability if the channel doesn't have an existing readership. Substack adds a subscription mechanism that compounds over time. If you don't have an existing newsletter or blog with readers, this is the right choice anyway — building the channel is itself a venture asset, and the case study is exactly the kind of content that grows a newsletter for the audience the venture wants to reach.

**LinkedIn long-form.** Native to the audience that matters most for engagement-driving conversations (risk and assurance practitioners). LinkedIn's reach mechanics favour this kind of content reasonably well. Cost: LinkedIn's archive is poor and the document is harder to link to externally as canonical. Strongest as a launch surface, weaker as the long-term home.

**Combination: personal site as canonical, LinkedIn long-form as launch.** Publish the canonical version on your blog or Substack. Cross-post a substantively shortened version (1,500-2,000 words, the compressed argument plus the LT-01-01 finding) on LinkedIn with a link to the full document. This gets the LinkedIn audience reach without making LinkedIn the canonical home.

My recommendation is the combination, with the canonical home being whatever blog or Substack you can stand up cleanly. If standing up a blog is itself a multi-day decision and you want to publish faster, LinkedIn-only as launch is fine, and the canonical home can move later.

## Short-form announcement

For LinkedIn post or X thread or whatever direct distribution channel accompanies publication. Roughly 150-200 words.

**EchoLeak (CVE-2025-32711) was the zero-click vulnerability in Microsoft 365 Copilot disclosed by Aim Labs in January 2025. Microsoft patched it server-side in May 2025; no customers were affected. The technical analysis has been thoroughly documented elsewhere.**

**This case study takes a different angle: what would an agent-assurance methodology — the kind that needs to exist for European banks and insurers deploying AI agents under DORA, the AI Act, and supervisory expectations now forming — actually produce when applied to the EchoLeak configuration?**

**The answer is operationally specifiable. Threat register, toxic-flow analysis, runtime context capture, control matrix application, supervisor-engageable engagement finding. Each is concrete; each anchors to existing regulation and standards; each demonstrates that agent assurance can be specified rather than only described.**

**A finding worth sitting with: the methodology's "principal-bound" design principle and Aim Labs's "LLM Scope Violation" terminology — independently developed, from different starting points — converge on the same architectural concern. That convergence is itself evidence that the concept is real.**

**Full case study: [link]. Companion to a position paper currently in preparation.**

That's 192 words. Designed to be quoted in pieces — the title-bar facts in paragraph one, the framing in paragraph two, the methodology output list in paragraph three, the convergence finding in paragraph four, the call-to-action in paragraph five. A reader who reads only paragraph one gets the basics; a reader who reads through paragraph four understands the case study's contribution.

## Final checklist before publishing

Before clicking publish on whichever channel:

The position-paper title is finalised, or the placeholder `[Position Paper Title TK]` in the case study is appropriately handled. If the paper still doesn't have a final title, the case study can use a working substitution like "the position paper *Agent Assurance in Regulated Financial Services*" with a note that this is a working title.

The byline reflects what you actually want public. Once published, the byline is harder to change than any other element.

The publication channel is selected and the canonical URL is stable. If you publish on a personal site, that site exists, the URL is permanent, and the document won't move. If you publish on LinkedIn first, decide what the canonical-home migration plan is.

The short-form announcement matches the case study's substantive claims and doesn't overstate. The convergence finding is real and worth highlighting; "The answer is operationally specifiable" is a confident claim the case study supports. Don't add claims to the announcement that the case study doesn't make.

A friendly, qualified reader (not Elliott — too senior to ask for this kind of pre-publication review unless it serves a specific purpose) reads the document end-to-end and flags anything that surprised or confused them. This is optional but high-leverage; an hour of one peer's reading time can save the document from a confusion that affects every reader who follows.

The case study sits with you for 24-48 hours after the final draft before publication. This is not always possible, but if the schedule allows, the post-final-draft pause catches the kind of issues that only become visible when the writer is no longer in drafting mode.
