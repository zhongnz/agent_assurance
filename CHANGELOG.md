# Changelog

Version history of the position paper *Agent Assurance in Regulated Financial Services* (working title) and accompanying repository.

## v0.8.5 — May 2026

Repository cleanup and consistency review.

Removed five internal scaffolding files that documented process or preparation rather than substantive contribution:

- `case_studies/echoleak_build_plan.md` — internal build plan documenting how the case study was produced.
- `case_studies/echoleak_research_notes.md` — working research notes from the case-study build.
- `case_studies/echoleak_publishing_metadata.md` — internal publication-decision notes.
- `elliott_package/cover_note.md` — personally addressed cover note prepared for scientific advisor review.
- `elliott_package/executive_summary.md` — executive summary calibrated to the scientific advisor specifically.

The case study itself (`case_studies/echoleak.md`) stands on its own; its production scaffolding does not need to be public. The Elliott-specific package was preparation for a review process that may yet happen but does not need to sit in the public repo as documentation of intent. The `elliott_package/` directory is removed; the `case_studies/` directory now contains only the case study itself.

Consistency fixes following a holistic review:

- `supporting/source_status.md` — corrected stale reference from `verification_log_v0.8.md` to `verification_log.md` (the file was renamed in the earlier cleanup; this reference was missed).
- `case_studies/echoleak.md` — corrected nested-italics markdown issue in opening epigraph (paper title as italic within an italic block was breaking the surrounding emphasis).
- `briefing/general_audience_abstract.md` — removed `— v1` suffix from title (holdover from earlier filename versioning convention) and removed `[Word count: 190]` inline metadata; updated content to reflect the matrix and reference application as separate artifacts in the repo rather than as in-paper concepts.
- `briefing/briefing_note.md` — closing paragraph updated to mention the control matrix, case study, and reference application as artifacts alongside the paper.
- `README.md` — `What's here` section rewritten to acknowledge the five substantive artifacts (paper, control matrix, case study, reference application, briefing surface) rather than just the paper and case study; status section reframed to distinguish repository version (v0.8.5) from paper substantive-content version (v0.8.1 level, stable across v0.8.2–v0.8.5); word count claims updated.

The repository now contains thirty-three files: the substantive contribution (paper, control matrix, case study, reference application), the distribution surface (briefing note, abstract, visual, wrapper sample), the supporting credibility documents (verification log, source status), the operational repository hygiene (README, CONTRIBUTING, SECURITY, LICENSE, CITATION, CHANGELOG), and the slide decks.

## v0.8.4 — May 2026

Operational hygiene additions to support the repository as a public artifact:

- `CONTRIBUTING.md` — documents the kinds of engagement that are most useful (substantive critique, corrections, extension proposals, engagement experience, editorial feedback), how to engage (GitHub Issues for substantive comments, private contact for non-public feedback), issue and pull request conventions, and what the repository is not (not a security advisory channel, not a regulatory inquiry channel, not a substitute for assurance engagement).

- `SECURITY.md` — documents the channel for sensitive disclosures (methodology errors with security consequences, identification of confidential information, information about non-public incidents, concerns about adversarial use of the work). Distinguishes the repository's appropriate scope from vulnerability disclosure channels for specific products.

- `CITATION.cff` — citation metadata in the Citation File Format. GitHub renders this metadata in the repository sidebar, allowing readers to cite the work in standard formats.

- Revision protocol added to the control matrix at `paper/control_matrix.md`. The protocol specifies semantic versioning, triggers for revision, authorisation, documentation, notification mechanism, stability commitments within a major version, cadence (no fixed cadence), and the relationship between the published matrix and institutional local adaptations.

The PoC build plan previously at `operational/poc_build_plan.md` was removed. The PoC was never claim-bearing in the position paper or elsewhere in the work; the case study and reference application together demonstrate the methodology's analytical content well enough that a working-code PoC adds little marginal credibility relative to its substantial cost. Future engagement may produce specific pull for working code, at which point a build plan can be reconstructed against the specific need; the reference application materials provide most of the spec a future PoC would require.

The additions and the removal are operational rather than substantive; they do not change the methodology or its claims.

## v0.8.3 — May 2026

Reference application materials added at `reference_application/`. The directory contains the methodology's outputs against the §5 reference deployment as discrete artifacts:

- `deployment_specification.md` — restructured specification of the §5 deployment with operational detail expanded for engagement use (~2,100 words).
- `threat_register.md` — structured threat enumeration organised by OWASP Top 10 for Agentic Applications categories and the cross-cutting threat patterns (~3,400 words).
- `gap_analysis.md` — comparison between the deployment's current-state configuration and the methodology-recommended target-state configuration, per control from the matrix (~3,600 words).
- `findings/` — three engagement-style findings (IA-01-01 principal propagation, LT-01-01 lethal trifecta, TF-01-01 toxic-flow analysis) demonstrating the methodology's terminal output form (~6,800 words across the three).

The reference application closes the gap between the paper's "applied to a reference deployment" claim and the production of the structured artifacts the methodology generates. The §5 walk-through of the methodology against the reference deployment is in prose; the reference application produces the artifacts the prose describes.

The reference application complements the EchoLeak case study at `case_studies/echoleak.md`. The case study applies the methodology retrospectively to a real documented incident; the reference application applies it prospectively to a hypothetical deployment.

## v0.8.2 — May 2026

Full control matrix v1.0 added as a companion document at `paper/control_matrix.md`. The matrix presents 26 controls covering the OWASP Top 10 for Agentic Applications categories (ASI01-ASI10) including dedicated controls for inter-agent communication (IC-01), cascading failures (CF-01), and rogue-agent behavioural drift (RA-01); the five cross-cutting threat patterns; and additional governance, evidence-capture, and supervisory-readiness areas. Five of the 26 controls are reproduced from §4.3 of the paper (where they were presented as illustrative); 21 are new.

References in the paper to "Appendix B" or "a forthcoming companion artifact" updated to reference the now-existing matrix at `paper/control_matrix.md`. The §4.4 paragraph titled "The full control matrix is forthcoming" updated to "The full control matrix" with corrected body text.

The matrix's coverage notes document which OWASP categories, cross-cutting patterns, design principles, and regulatory anchors each control engages. Coverage is comprehensive across all ten OWASP categories, with dedicated controls for every category.

## v0.8.1 — May 2026

Editorial compression pass applied across all sections. Total reduction: ~2.8% of paper length (788 words from 27,791 to 27,003). Section-level compression ranged from 1.1% (§7) to 6.4% (§2). The cuts removed repeated framings, recap paragraphs, and verbose connective phrasing without modifying argument or citations.

Marker count corrected: section sub-totals sum to 51 (9+5+17+10+4+5+1), not 52 as some earlier summaries had said.

Source-status appendix added as a separate companion document, organising sources into four evidentiary buckets.

Abstract added to the consolidated paper (prepended as an unnumbered section before §1).

## v0.8 — May 2026

All 51 verification markers from v0.7 resolved through primary-source web verification.

§1 (9 markers) — EchoLeak (CVE-2025-32711, Microsoft as CNA, 11 June 2025, Aim Labs as discloser; mechanism description with reference-style markdown via Microsoft Teams proxy); SpAIware (20 Sep 2024 BSides Vancouver Island), AgentFlayer (6 Aug 2025 Black Hat USA, Bargury and Sharbat), Shadow Escape (22 Oct 2025 Operant); MCP origin (25 Nov 2024 Anthropic) and AAIF donation (9 Dec 2025); ECB SSM Priorities 2026-2028 (18 Nov 2025); BaFin ICT-AI guidance dates; DNB *AI bij verzekeraars* (27 Mar 2025) with 15-of-36 statistic; ACPR Beau Lisbon speech (27 Oct 2025) and *Archives de philosophie du droit* article; EIOPA BoS-25-360 (6 Aug 2025); CBEST (2014) and TIBER-EU (May 2018); AI Act Article 12 exact text; SR 26-2 supersession framing.

§2 (5 markers) — PRA SS1/23 (17 May 2023, effective 17 May 2024); ISO 42001:2023 (December 2023); NIST AI RMF 1.0 (January 2023) and NIST AI 600-1 (July 2024); ISO 27001:2022 (October 2022); NIST CSF 2.0 (26 February 2024); NIST SP 800-207 (August 2020); MCP 18 June 2025 specification (OAuth 2.0 RS classification, RFC 9728 PRM, RFC 8707 Resource Indicators).

§3 (17 markers) — OWASP Top 10 for Agentic Applications (9 December 2025 launch at London Agentic Security Summit / Black Hat Europe 2025); MCPTox (arXiv:2508.14925); General Analysis Supabase/Cursor disclosure (6 July 2025) with Simon Willison and Supabase corroboration; Asana incident (4-17 June 2025, ~1,000 customers, tenant-isolation logic flaw); lethal trifecta coined by Simon Willison (16 June 2025); Snyk × Invariant (24 June 2025); Month of AI Bugs (August 2025, 20+ disclosures); GDPR Articles 33/34; AI Act Annex III 5(b)/(c); FSB report (14 November 2024); macroprudential references consolidated to forms supported by available evidence.

§4 (10 markers) — GDPR Article 25; ISAE 3000 (IAASB) and AT-C 205 (AICPA); cross-walking references (CSA CCM, NIST 800-53 to ISO 27001, CIS Controls); CBEST and TIBER-EU dates; DORA Articles 24-27; NIST SP 800-207; AI Act Articles 14 and 15; DORA Articles 9, 17, 18, 28; ISO 42001 Annex A.6.2; NIST AI RMF Manage 2.

§5 (4 markers) — EIOPA digitalisation evidence consolidated to Opinion BoS-25-360 plus the DNB statistic; LangGraph current state (LangChain Inc., MIT-licensed, production users including Klarna, Replit, Elastic, Uber, J.P. Morgan); deployment-configuration framing converted to plain acknowledged limitation; DORA Article 17 specifics.

§6 (5 markers) — Digital Omnibus on AI (19 November 2025, COM(2025) 836, deferral to 2 December 2027 and 2 August 2028; 28 April 2026 trilogue without agreement; further trilogue 13 May 2026); AI Act timeline by category; GPAI applicability 2 August 2025; DNB and CSSF Second Thematic Review (16 May 2025, 461 institutions, 86% response rate); BoE FPC *Financial Stability in Focus: AI in the financial system* (9 April 2025); BIS publications generalised to forms supported by available evidence; CBEST and TIBER-EU dates.

§7 (1 marker) — AgentDojo confirmed as active NeurIPS 2024 benchmark (Debenedetti et al.), maintained at ETH Zurich's SPY Lab, extended by UK and US AI Safety Institutes.

Word count: 27,791 (from 27,661 in v0.7).

## v0.7 — May 2026

Section 1 verification round. EIOPA-BoS-25-360 verified directly from primary-source PDF. EBA AI Act mapping verified (factsheet 21 November 2025; full annex letter to Berrigan/Viola 17 December 2025). ACPR Beau Lisbon speech (27 October 2025) confirmed alongside *Archives de philosophie du droit* Tome 66 article (November 2025; ACPR site 12 December 2025). BaFin *Guidance on ICT Risks in the Use of AI at Financial Entities* confirmed (18 December 2025 German publication; 30 January 2026 English publication).

## v0.6 — May 2026

Peer review feedback incorporated. SR 26-2 supersession of SR 11-7 reflected throughout §2.1. Lingering DORA RTS reference in §2.3 corrected (2025/532 is subcontracting; 2025/1190 is TLPT). EchoLeak CVSS scoring split between Microsoft CNA (9.3 Critical) and NVD (7.5 High). MCPTox publication-status precision improved (arXiv August 2025; AAAI 2026 proceedings). Toxic-flow sourcing tightened to separate MCPTox metadata-poisoning support, Snyk/Invariant compositional methodology, and the paper's regulator-legible contribution. Privacy and data-minimisation caveat added to the evidence-first principle in §4.1. Ownership column added to the control matrix in §4.2 and applied to the five illustrative controls in §4.3. Section 5 retitled to "Illustrative Reference Application." §2.3 cybersecurity critique sharpened to recognise the discipline's breadth and locate the precise gap at semantic instruction-following inside authorised workflows and compositions of permitted calls. Section 8 compressed from 2,205 to 1,015 words.

## v0.5 — May 2026

DORA RTS verification. DORA article ranges verified (5-16 ICT risk management; 17-23 incident management; 24-27 testing; 28-30 third-party general; 31-44 critical-third-party oversight). MCP authorisation verified as optional in protocol with the framework requiring conformance for regulated deployments. LangGraph verified as LangChain framework. §3.1 evidence-grade convention introduced. §3.2.1 tool poisoning narrowed to metadata-only definition with MCPTox as canonical example. §4.2 mapping-strength convention introduced (Direct, Indirect, Analogical, Gap) and applied to the illustrative controls in §4.3. Section 8 added as the closing.

## Pending verification

None. All identified verification markers resolved as of v0.8.
