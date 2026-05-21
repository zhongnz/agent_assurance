# Changelog

Version history of the position paper *Agent Assurance in Regulated Financial Services* (working title) and accompanying repository.

## v0.8.14 — May 2026

Third-audit traceability and release-integrity pass. No substantive change to the methodology; the fixes address overstated coverage claims, an internal contradiction in the reference application, evidence-register imprecision, and the security-disclosure channel.

**OWASP coverage claim corrected (maps vs covers).** `README.md`, `briefing/briefing_note.md`, and `paper/control_matrix.md` previously asserted that the 26 controls "cover all ten OWASP Top 10 for Agentic Applications categories." The Coverage Notes of the matrix (revised in v0.8.7) explicitly acknowledge ASI05 (Unexpected Code Execution) as a coverage gap in v1.0 — RO-01 was reanchored as out-of-OWASP-taxonomy in the same revision. The README, briefing, and matrix introduction are now updated to say the matrix *maps* all ten categories and *covers* nine, with ASI05 acknowledged as a coverage gap in v1.0.

**ASI07/IC-01 contradiction in the reference application resolved.** `reference_application/threat_register.md` previously classified the deployment's shared foundation-model API, orchestration framework, and evidence-capture infrastructure under ASI07 (Insecure Inter-Agent Communication) with IC-01 as a recommended control. `reference_application/gap_analysis.md` correctly states that shared resource access is not inter-agent communication and marks IC-01 not applicable. The threat register is now updated to mark ASI07 as not applicable in the current single-agent configuration, with the cross-deployment infrastructure concerns reclassified under TF-02 (cross-deployment flow review) and CF-01 (failure-domain isolation and cascade prevention), aligning with the gap analysis. Aggregate severity counts updated accordingly: now 1 Critical + 6 High + 4 Medium + 1 Low.

**Verification scope clarified.** `README.md` previously read "the verification log documents the audit trail for every load-bearing claim in the paper." The log records the 51 markers identified in the position paper's v0.7 verification round; the control matrix, the case study, and the reference application carry their own citations and are not exhaustively audited in the log. The claim is now scoped accordingly.

**DNB verification entry strengthened to primary source.** `supporting/verification_log.md` §1.3 DNB entry previously cited only Stibbe and Lexology secondary analyses for the DNB *AI bij verzekeraars* publication, when the DNB primary publication is accessible at dnb.nl. The entry now cites the DNB primary publication with the secondary analyses as corroboration.

**AI Act and DORA article enumeration in source_status updated.** `supporting/source_status.md:19,21` listed AI Act articles "6, 12, 14, 15" and DORA articles "9, 17–18, 24–27, 28" — a subset of what the position paper and the control matrix actually cite. The enumeration is now expanded to reflect the actual citation footprint: AI Act Articles 9, 10, 11, 12, 13, 14, 15, 17, 19, 23, 26 plus Article 6(2) and Annex III; DORA Articles 5, 6, 8, 9, 11, 12, 13, 17, 18, 25, 26, 27, 28, 29, 30.

**Private Vulnerability Reporting enabled.** GitHub's Private Vulnerability Reporting feature has been enabled on the repository, providing a dedicated private channel for sensitive disclosures (https://github.com/zhongnz/agent_assurance/security/advisories/new). `SECURITY.md` now references this as the primary disclosure path; `.github/ISSUE_TEMPLATE/config.yml` updates the security contact link to point at the PVR form rather than the SECURITY.md document. The previous "contact mechanism on the author's GitHub profile" framing was unspecific for a security-adjacent repository.

**CITATION.cff `preferred-citation` block added.** The top-level `type: software` (the CFF schema default for repositories) is retained for the repository-as-artifact citation; a `preferred-citation:` block of `type: report` now provides reference managers with publication-style metadata (title, authors, year, URL, DOI, abstract) for citing the paper itself rather than the repository. This addresses the audit observation that citing a documents-only repository as "software" reads oddly to academic readers.

**Versions bumped to v0.8.14; date-released 2026-05-21.** README status section updated.

## v0.8.13 — May 2026

Post-public-release calibration pass following a second deep audit. The fixes correct a small number of substantive and rhetorical issues that the audit surfaced; the methodology is unchanged.

**`briefing/briefing_note.md` opening paragraph and cybersecurity sentence reframed.** The opening previously read "In June 2025, security researchers demonstrated that a single email could cause..." which collapsed three EchoLeak milestones (January 2025 PoC and private disclosure; May 2025 server-side fix; June 2025 public disclosure) into one date. Updated to anchor on the public-disclosure event ("In June 2025, the public disclosure of CVE-2025-32711 showed..."). The cybersecurity-discipline sentence previously read "Cybersecurity presumes attackers detectable at the network perimeter or by per-action access checks" — a perimeter framing that has been superseded by zero-trust architecture (NIST SP 800-207, August 2020) which the paper §2.3 itself recognises; updated to "Cybersecurity — including the zero-trust architecture that succeeded the perimeter model — addresses attackers through identity, access, and per-action authorisation; agent attacks operate inside fully-authorised workflows..."

**`case_studies/echoleak.md` subtitle disclosure framing.** Previously read "disclosed by Aim Labs in January 2025 and patched by Microsoft in May 2025" — conflating private MSRC disclosure (January) with public disclosure (11 June). Updated to "privately reported to Microsoft by Aim Labs in January 2025, patched server-side in May 2025, and publicly disclosed on 11 June 2025."

**`case_studies/echoleak.md` "convergence" framing calibrated.** Two paragraphs (in §6 IA-01 mapping and §8 What the case study establishes) previously framed the convergence between the methodology's *principal-bound* design principle and Aim Labs's "LLM Scope Violation" terminology as "external corroboration of the framework that the framework's own development could not provide." Both framings draw on the same underlying tradition (confused-deputy reasoning, zero-trust principal-propagation, the NIST SP 800-207 lineage that §4.1 itself anchors to); the convergence is consistent with that shared lineage rather than independent corroboration. Updated to "the convergence is not independent corroboration of the framework; it indicates that the architectural concern is recognised across the security-research and assurance-methodology communities, which is a useful signal for the methodology's standing without overclaiming what a single convergence demonstrates."

**`case_studies/echoleak.md` LT-01-01 finding compensating-controls description.** Previously read "five compensating controls... Each was bypassed." Reference-mention markers are a UI provenance signal manipulated by an embedded directive in the attacker-controlled content, not a security control bypassed at the system layer. Updated to distinguish "four security guardrails" (XPIA classifier, external-link redaction, image redaction, browser-enforced CSP — each bypassed) from "a UI provenance signal" (reference-mention markers — instructed-away rather than bypassed).

**`case_studies/echoleak.md` LT-01-01 ASI references clarified.** The finding lists ASI01+ASI06+ASI09 as its compositional reference; the matrix's LT-01 control uses a generic ASI01+ASI02+ASI03 reference. A parenthetical now notes that EchoLeak's deployment-specific composition substitutes ASI06+ASI09 for ASI02+ASI03 to reflect the RAG-spraying retrieval-poisoning mechanism and the UI-trust manipulation.

**`paper/full.md` §1.3 firm-naming line generalised.** The line previously named "JPMorgan, Goldman Sachs, ING among them" with no primary-source citation, sitting in a paragraph otherwise meticulous about source discipline. Generalised to "several major European and US banks" rather than retaining unsourced specificity.

**`README.md` artifact count reconciled to six.** The opening tagline and the "What's here" paragraph previously enumerated five artifacts in differing breakdowns (one omitted the briefing surface; one demoted supporting documents to a trailing sentence) while the CITATION.cff abstract lists six. Both README sentences now enumerate six artifacts consistently: position paper, control matrix, case study, reference application, briefing surface, supporting credibility documents.

**`CITATION.cff` DOI identifier descriptions extended.** Both identifier entries now include the forward-pointing language indicating that subsequent tagged releases receive their own version-specific DOIs; the v0.8.11 entry is labelled as the prior tagged release.

**`README.md` and `CITATION.cff` versions bumped to v0.8.13.**

## v0.8.12 — May 2026

Open-source consistency pass following a deep audit against OSS conventions. No substantive change to the methodology; the fixes bring the repository surface into consistency with public-project conventions.

`LICENSE` replaced with the full canonical Creative Commons Attribution 4.0 International legal text (previously held only the human-readable summary plus a link to the canonical text). The full text is what GitHub's license detection and downstream adopters expect.

`CITATION.cff` extended with top-level `repository-code` and `url` fields per the CFF 1.2.0 schema convention; the DOI identifier description clarified to note that the listed DOI archives v0.8.11 and that subsequent tagged releases receive their own version-specific DOIs.

`ROADMAP.md` v0.9 anticipation paragraph reframed to reference the paper's substantive-content level (v0.8.1, stable through v0.8.12) rather than the now-stale v0.8.8 anchor. The "continuous-assurance platform" out-of-scope entry rewritten to describe what the platform would be in repository-facing terms, removing private-business-plan framing.

`README.md` opening tagline and "What's here" reconciled to the same five-artifact framing (position paper, control matrix, case study, reference application, supporting documents) carried in the CITATION.cff abstract. The Status section's "final pre-public-release content trim" qualifier removed. The maintainer's name (Peter Zhong) added to the Status section. A copy-and-paste BibTeX citation snippet added to the Citation section.

`CHANGELOG.md` v0.8.10 entry's trailing "ahead of the transition from private working repository to public open-source project" clause trimmed; the deletion description stands on its own.

`SECURITY.md` opening of the "How to report" section reframed: the apologetic "the maintainer is solo" clause removed; response-time framing kept.

`supporting/verification_log.md` title updated to remove the stale "v0.8" anchor (the log is the living audit register; the version anchor read as frozen-in-time). First-person voice in three audit notes ("specific details I have not independently confirmed") rewritten in passive voice. The "Items still pending direct primary-source verification before publication" section heading renamed to "Pending verification," since the work is no longer pre-publication.

`briefing/visual.svg` footer attribution updated from "Position paper · v0.8 · figure 1" to "Agent assurance methodology · figure 1," removing the stale version anchor.

`.gitignore` added with basic entries for common operating-system, editor, and tool artifacts (the file had been removed during the v0.8.5 refresh; re-added here as standard OSS hygiene).

`README.md` and `CITATION.cff` versions bumped to v0.8.12; date-released advanced to 2026-05-20.

*(Post-tag note.)* Following the v0.8.12 release tag, Zenodo minted DOI [10.5281/zenodo.20308910](https://doi.org/10.5281/zenodo.20308910) for the v0.8.12 archive. In a follow-up commit, `README.md` (badge, Citation section text, BibTeX) and `CITATION.cff` (identifiers block) were updated to reference the v0.8.12 DOI as the current and the v0.8.11 DOI as the prior historical archive.

## v0.8.11 — May 2026

Operational scaffolding for the open-source project framing.

`.github/ISSUE_TEMPLATE/` added with five templates matching the engagement categories in `CONTRIBUTING.md`: substantive critique, correction, extension proposal, engagement experience, editorial feedback. The templates channel contributions into the forms that are most useful for an evolving methodology repository.

`.github/ISSUE_TEMPLATE/config.yml` disables blank issues and surfaces `SECURITY.md` and the private-contact channel as alternative routes for non-issue concerns.

`.github/PULL_REQUEST_TEMPLATE.md` added to structure pull request descriptions around scope, affected sections, change type, rationale, and a small checklist.

`README.md` gains a CC BY 4.0 license badge near the title for at-a-glance license identification.

`CITATION.cff` version and date-released bumped to current state. The file had drifted from `0.8.5` / `2026-05-08` to the actual v0.8.10 / 18 May 2026 over the recent revision rounds; the citation metadata is now in sync with the repository state.

The additions do not change the methodology or any substantive artifact; they support the project's contribution surface.

## v0.8.10 — May 2026

Content trim reducing the repository to its substantive artifacts. The following are removed:

- The `decks/` directory and its three slide decks (`Agent-Assurance-Overall-Plan.pptx`, `Position-Paper-Outline.pptx`, `Technical-Appendix.pptx`). The decks duplicated content the position paper, the control matrix, and the verification log carry authoritatively; the fact-check log slides in particular were a presentation rendering of material in `supporting/verification_log.md`.

- `briefing/wrapper_sample_tier2_risk.md`. The sample audience-specific wrapper carried a `[name]` placeholder template that reads as draft scaffolding rather than substantive content; the wrapper pattern is an operational distribution choice rather than methodology material.

- `paper/section_01_*.md` through `paper/section_08_*.md`. The per-section files duplicated content the consolidated `paper/full.md` carries; the duplication served editing convenience that is no longer load-bearing now that the paper's substantive content has stabilised at the v0.8.1 level.

`README.md` updated to reflect the new file set: layout block trimmed, the "per-section files in paper/" alternative in the reading-order guidance removed, status bumped to v0.8.10.

These deletions do not change the methodology, the argument, or any of the substantive artifacts (position paper, control matrix, case study, reference application, briefing surface, supporting credibility documents). They reduce the repository to its substantive content.

## v0.8.9 — May 2026

`ROADMAP.md` added at the root. The roadmap articulates direction for v0.9 and v1.0, what is deliberately out of scope through v1.0, and what kinds of contributions are most welcome. It is the project-level document that distinguishes an active project from a static publication — without committing to timelines the project does not control.

The addition supports the open-source publication mode the work sits in. The repository's prior artifacts (paper, control matrix, case study, reference application, briefing surface, supporting credibility documents) document what the work *is*; the roadmap documents where the work is *going*. Both are required for readers to engage with the work as an ongoing project rather than as a static publication.

`README.md` updated to reference `ROADMAP.md` in the repository layout block and to bump the version reference from v0.8.8 to v0.8.9.

## v0.8.8 — May 2026

Matrix-structural pass deferred from v0.8.7. The fixes apply the matrix's own §4.2 conventions consistently across all 26 controls; they do not change any control's substance.

**Cross-cutting-patterns field added on eight controls.** RO-01, AT-02, AT-03, HC-01, HC-02, GP-01, GP-02, and GP-03 previously omitted the *Cross-cutting patterns* field that the §4.2 convention specifies. Each now carries the field with content reflecting the control's relationship to §3.2's five cross-cutting patterns. RO-01 acknowledges that resource overload sits adjacent to rather than within the §3.2 patterns. The seven cross-cutting/governance/audit controls each note that they apply across all five patterns.

***Gap* mapping-strength label applied where previously "None".** AT-02, AT-03, HC-01, HC-02, GP-01, and GP-03 previously stated "OWASP ASI references. None ([rationale])," which is inconsistent with the §4.2 convention defining *Gap* as the label for "no specific anchor exists, and the absence is itself part of the methodology's contribution." Each control now uses the *Gap* label with a brief explanation of why no OWASP ASI category applies and what the underlying anchor is (typically a design principle plus a regulatory or standards reference outside the OWASP taxonomy). GP-02's existing "Cross-cutting; testing programme covers all categories" framing is preserved as an alternative defensible labelling for a control whose ASI scope genuinely is all categories.

**DORA Article 17 / Article 18 packaging error corrected.** ZC-01, MC-02, and AT-03 previously cited "DORA Articles 17–18" with the Article 17 label only. Article 17 is the ICT-related incident management process; Article 18 is the classification of ICT-related incidents. The two articles are now cited separately with each carrying its proper label and an appropriate mapping-strength annotation per control.

**IC-01 single-agent applicability flag added.** The control entry now carries an *Applicability* field stating that IC-01 applies to deployments using inter-agent communication patterns and is not applicable to single-agent deployments. This aligns the matrix with the §5 prose's treatment of IC-01 as not applicable to the reference deployment.

**AT-01 GDPR Article 25 repositioned.** The control's GDPR Article 25 anchor previously sat in the *Derivation* field with a *Direct* mapping-strength label that the *Derivation* convention does not contemplate. The anchor now sits in *Regulatory anchors* with the *Direct* label; *Derivation* references the anchor without re-labelling.

**Conventions section: AI Act Article 15 mapping note added.** A brief note now explains the labelling rule: Article 15 is cited as *Direct* where a control directly produces one of Article 15's three named qualities (accuracy, robustness, cybersecurity) at the level of the quality itself, and as *Indirect* where the control implements a specific mechanism in service of Article 15's broader objectives. This addresses the audit's "inconsistency without explicit justification" by making the rule explicit. Per-control labels are not changed; the rule is articulated to support readers in interpreting them.

**README status updated.** v0.8.7 → v0.8.8.

The audit's remaining items have been addressed; the matrix is internally consistent against its own §4.2 conventions across all 26 controls.

## v0.8.7 — May 2026

Second round of correctness fixes following deeper audit. The fixes do not change the methodology or its claims; they correct factual errors, taxonomy errors, and traceability gaps the audit surfaced.

**ASI05 taxonomy correction.** `paper/control_matrix.md` and `reference_application/threat_register.md` previously labelled ASI05 as "Resource Overload"; OWASP's Top 10 for Agentic Applications (December 2025) identifies ASI05 as **Unexpected Code Execution**. The matrix's RO-01 control is reanchored as a *Gap* relative to the OWASP taxonomy — resource overload is an operational-resilience concern addressed by DORA and ISO 27001 capacity management rather than an OWASP ASI category. The Coverage Notes acknowledge ASI05 (Unexpected Code Execution) as a coverage gap in matrix v1.0, with the note that deployments where the agent generates, modifies, or runs code require additional controls beyond v1.0. The threat register adds an ASI05 (Unexpected Code Execution) section confirming the threat is not present in the reference deployment's configuration, and reframes its resource-overload section as an out-of-OWASP-taxonomy operational-resilience concern. Aggregate severity counts are updated: 1 Critical, 6 High, 5 Medium, 1 Low (was 1 Critical, 7 High, 5 Medium, 1 Low; the duplicate cross-cutting "Memory and context poisoning" was removed in this round — see below).

**Approximately fifteen primary controls → twenty-five applicable controls.** `paper/full.md` and `paper/section_05_applied_demonstration.md` previously said "approximately fifteen primary controls and a larger set of supporting controls"; the §5.3 enumeration explicitly lists 25 selected controls (5 primary in §4.3 plus 20 further). The text is corrected to "twenty-five applicable controls — the matrix's twenty-six minus IC-01, which is not applicable to the deployment's single-agent configuration." The downstream "fifteen primary findings" formulations (in `paper/full.md`, `paper/section_05_applied_demonstration.md`, `reference_application/README.md`, `reference_application/findings/lt_01_01_lethal_trifecta.md`) are reanchored to the gap analysis: the methodology produces a primary finding for each High-severity Absent or Partially-present control, of which the gap analysis surfaces approximately fifteen.

**§5.3 lethal-trifecta egress externality.** `paper/full.md` and `paper/section_05_applied_demonstration.md` previously characterised the deployment's egress as internal-only with insider-attacker scenarios. The deployment in fact has customer-facing notification channels (per `deployment_specification.md`, `threat_register.md`, `gap_analysis.md`, `findings/lt_01_01_lethal_trifecta.md`); the §5.3 paragraph is corrected to reflect that recommendation routing, payment instructions, and customer notifications all constitute egress, with the customer-notification channel constituting an external destination outside the institution's perimeter.

**Cross-cutting threat patterns standardised at five.** The paper's §3.2 names five cross-cutting patterns (tool poisoning, identity & privilege abuse, lethal trifecta, toxic flows, zero-click exfiltration). The matrix's Coverage Notes previously listed six (adding memory and context poisoning); the threat register previously included a separate "Memory and context poisoning" cross-cutting section that duplicated ASI06. The matrix Coverage Notes are updated to reflect five with an explicit note that memory and context poisoning is treated under ASI06 rather than as a sixth pattern. The threat register's duplicate cross-cutting section is removed; its introduction is updated to note that tool poisoning and identity & privilege abuse are treated within the matching ASI categories (ASI04 and ASI03 respectively) since their content overlaps materially.

**Verification log §6.5 → §6.4.** `supporting/verification_log.md:123` previously cited a non-existent §6.5 for CBEST/TIBER-EU; the correct anchor is §6.4.

**EchoLeak January 2025 disclosure.** The case study's recurring "January 2025 disclosure to MSRC" claim now has its own verification-log entry, with HackTheBox, Checkmarx, and SOC Prime confirmed as convergent secondary sources for the disclosure timeline. Previously the verification log only confirmed the 11 June 2025 CVE publication, leaving the case study's January 2025 anchor unsupported in the audit register.

**Case study finding count (4, not 5).** `case_studies/echoleak.md:135` previously said "five primary findings"; §6 of the case study explicitly states three of the five matrix controls apply directly, one applies with adaptation, and TP-01 does not apply, yielding four primary findings (LT-01, TF-01, IA-01, ZC-01).

**Case study §1.1 anchor.** `case_studies/echoleak.md:109` previously cited a "§1.1 footnote" for Copilot's constrained delegated-authority configuration; the claim sits in §1.1 body, not the footnote (which addresses source attribution only). Anchor updated to "§1.1 boundary note."

**TP-02 DORA Article 28/29/30 disambiguation.** `paper/control_matrix.md:55` previously cited Articles 29 and 30 with near-identical "key contractual provisions" labels. Article 29 is preliminary assessment of ICT concentration risk and further sub-outsourcing arrangements; Article 30 is key contractual provisions. The anchors are corrected and disambiguated.

**Finding IA-01-01 title.** The reference application's finding doc previously titled "Principal-propagation gap in claims-processing agent" is renamed to match the paper's §5.4 title: "Service-account authority exceeds requesting-principal authority across customer record retrieval."

**DNB statistic standardised.** Five different phrasings of the DNB *AI bij verzekeraars* 15-of-36 statistic across `paper/full.md`, `paper/section_01_shape_of_the_problem.md`, `paper/section_06_regulatory_horizon.md`, `reference_application/deployment_specification.md`, and `supporting/verification_log.md` are standardised on "fraud detection and claim-amount estimation," matching the verification log's canonical phrasing.

**Wrapper sample matrix reference.** `briefing/wrapper_sample_tier2_risk.md` previously placed the control matrix "in §4" of the paper; the matrix is a companion artifact at `paper/control_matrix.md`. The wrapper is updated to reflect this.

**AT-01 cross-cutting-patterns field.** `paper/control_matrix.md:387` previously misused the cross-cutting-patterns field for a design-principle reference. Updated to name the §3.2 patterns and note evidence capture as the operational expression of the *evidence-first* design principle.

**Twelve → thirteen control families.** `paper/control_matrix.md:639` previously said "Twenty-six, organised across twelve control families"; the actual count is thirteen (TP, IA, LT, TF, ZC, MC, RO, AT, HC, GP, IC, CF, RA).

**README status update.** `README.md:83` updated from v0.8.5 to v0.8.7 with corresponding extension of the version range.

**Deferred to a future revision.** The audit also surfaced matrix-structural items the v0.8.7 fixes do not address: the *Cross-cutting patterns* field is missing on 8 of 26 controls (RO-01, AT-02, AT-03, HC-01, HC-02, GP-01, GP-02, GP-03); AI Act Article 15's mapping-strength label is inconsistent (Indirect on most controls, Direct on RO-01/CF-01/RA-01); AT-02/AT-03/HC-01/HC-02/GP-01/GP-03 use "OWASP ASI references. None" instead of the *Gap* mapping-strength label the §4.2 convention defines; ZC-01/MC-02/AT-03 cite "DORA Articles 17–18" with the Article 17 label only; IC-01's single-agent inapplicability is not flagged in the matrix entry; AT-01's GDPR Article 25 anchor sits in the *Derivation* field rather than *Regulatory anchors*; the Conventions list at line 17 omits the TF prefix; and the Coverage Notes' ASI04 line includes IC-01 and CF-01 although IC-01's primary anchor is ASI07. These items will be addressed in a v0.8.8 matrix-structural pass.

## v0.8.6 — May 2026

Correctness and consistency fixes following peer review. The fixes do not change the methodology or its claims; they correct factual errors and traceability gaps in the v0.8.5 release.

§6.2 (`paper/full.md`, `paper/section_06_regulatory_horizon.md`) and the verification log entry — Digital Omnibus state updated. The provisional agreement reached in the early hours of 7 May 2026, confirming the deferred dates of 2 December 2027 (Annex III) and 2 August 2028 (Annex I), is now reflected; the prior framing of the trilogue process as "in motion at the time of writing" has been replaced with a post-agreement framing acknowledging that formal adoption is pending. Sources include the Council of the EU press release of 7 May 2026 and convergent law-firm analyses (Bird & Bird, IAPP, DLA Piper, Hogan Lovells, Timelex, Ropes & Gray, A&O Shearman, NicFab).

§5.3 (`paper/full.md`, `paper/section_05_applied_demonstration.md`) — three traceability fixes:

- The matrix-contributed-controls paragraph rewritten to use actual matrix control IDs (TP-02, TP-03, IA-02, IA-03, LT-02, TF-02, ZC-02, MC-01, MC-02, RO-01, AT-01–AT-03, HC-01, HC-02, GP-01–GP-03, CF-01, RA-01) rather than naming controls absent from the matrix (foundation-model version pinning, service-account credential rotation, incident-response controls aligned with DORA Article 17). Incident response under DORA Article 17 is reframed as an institutional obligation outside the matrix's scope that HC-01 informs but does not displace. IC-01 is noted as not applicable to the single-agent configuration.

- The current-state-assessment paragraph reframed to describe the structured threat register paired with the deployment specification, rather than naming a separate threat-model document and a standalone toxic-flow analysis. The toxic-flow analysis is now described as elaborated through a dedicated engagement-level finding rather than a standalone artifact, matching what the reference application produces.

- The control-selection-phase paragraph reframed to describe the gap analysis as the integrated form of the control-matrix extract, control-gap memo, and initial remediation guidance that an actual engagement might separate into discrete artifacts.

Reference-application count fixes:

- `reference_application/gap_analysis.md` — corrected aggregate counts. Twelve controls are Partially present (was "Eight … the count above is 12 which corrects an earlier draft count" — a half-completed edit); thirteen are Absent (was "Fourteen"); one (IC-01) is Not applicable; zero are fully Present. Counts sum to the matrix's 26.

- `reference_application/threat_register.md` — corrected aggregate severity counts to match the threat headings: one Critical (the lethal trifecta), seven High, five Medium, one Low (was "two Critical and six High").

- `reference_application/threat_register.md` — removed the cross-reference to `findings/at_01_01_evidence_capture.md`, which does not exist as a finding in the reference application; the evidence-capture gap is described in the threat register and gap analysis without a dedicated finding document.

`case_studies/echoleak.md` — position-paper reference updated from "(working title; in preparation)" to a reference to `paper/full.md` in this repository, the paper now being available alongside the case study.

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
