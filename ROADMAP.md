# Roadmap

*Direction rather than schedule. Open-source projects rarely commit to timelines and this one does not. What follows is what is anticipated for subsequent versions, what would constitute v1.0, and what is deliberately out of scope.*

## v0.9 — anticipated

Subsequent point-version revisions are expected to incorporate, in roughly the following order of likelihood:

- **External-reviewer feedback.** The position paper's substantive content (at the v0.8.1 level, stable through subsequent point versions) has been through three rounds of peer review and four rounds of source verification; further review by external readers will inform v0.9 revisions to the argument and supporting evidence.

- **Additional case studies.** The EchoLeak case study at `case_studies/echoleak.md` is the first applied demonstration of the methodology against a documented incident. Subsequent disclosed incidents that exercise the methodology's analytical content — incidents that exhibit different combinations of the §3.2 cross-cutting patterns, that occur in different deployment contexts, or that surface methodology gaps — are likely candidates.

- **Control matrix revisions.** The control matrix at `paper/control_matrix.md` is v1.0. Revisions in response to new threat patterns, supervisory guidance shifts, or engagement findings will follow the matrix's own revision protocol; the published matrix tracks separately from any institution's local adaptation.

- **Reference applications for additional deployment configurations.** The reference application at `reference_application/` covers a single hypothetical insurance claims-processing agent on LangGraph + MCP. A banking-sector configuration (payments / treasury / credit-decisioning domain) and a non-MCP architectural configuration are likely subsequent applications.

## v1.0 — milestone definition

v1.0 is the point at which the methodology has been applied to one or more live engagements and revised based on the empirical contact. The current methodology is described throughout as v1.0 of an artifact that will revise as it meets engagement reality; v1.0 of the *published* methodology corresponds to the first version where that revision has occurred against real deployment configurations rather than constructed ones.

What v1.0 does *not* require: completeness across all deployment configurations, agreement from all reviewers, supervisory endorsement, or formal attestation pathways. Those remain ongoing rather than terminal.

## Out of scope (deliberately)

The following are not in scope for any version through v1.0. The methodology may be adapted to these by others under the project's license; the published methodology does not undertake the adaptations.

- **Non-EU regulatory regimes as canonical work.** The canonical methodology in v1.0 is calibrated to the EU regulatory architecture (AI Act, DORA, ISO/IEC 42001, NIST AI RMF, OWASP Top 10 for Agentic Applications). Extensions to UK PRA / FCA, US FRB / OCC / FDIC, OSFI E-23, MAS, or other supervisory regimes are not in scope for the canonical work through v1.0 — the regulatory anchoring layer would need substantial re-grounding for each. *Jurisdictional adaptations are welcome as community contributions,* however, and would be reviewed for inclusion in future versions as community-contributed or experimental profiles. The methodology is *EU-first, not EU-only*; see the README's Scope section.

- **Foundation-model layer engagement.** The methodology addresses deployers of agent systems, not providers of foundation models. Provider-side assurance is downstream of the foundation-model vendor's own work and outside the methodology's scope.

- **A continuous-assurance platform.** Automation of the methodology's evidence-capture and gap-analysis outputs in software — a possible future work-stream beyond the analytical methodology this repository carries — is not in scope and has no spec in this repository.

- **Working-code proof-of-concept.** A working agent deployment with applied methodology was a deferred work-stream. The case study and reference application together demonstrate the methodology's analytical content; a working-code PoC is not anticipated through v1.0. Future engagement may produce specific pull for working code, at which point a build plan can be reconstructed against the specific need.

- **Formal attestation pathway.** Formal attestation under ISAE 3000 (IAASB) or AT-C 205 (AICPA) requires partnership with qualified practitioners. The methodology is calibrated to support such pathways but the published version does not constitute attestation, certification, or rating.

## How to contribute

Contributions most welcome:

- **Substantive critique** of the methodology's argument, framework-anchoring choices, threat-taxonomy treatment, or regulatory characterisation.
- **Corrections** to factual claims, source citations, identifiers, dates, or cross-references.
- **Extension proposals** within EU scope: additional deployment configurations, additional threat patterns or cross-cutting patterns, additional regulatory anchors that warrant explicit treatment.
- **Engagement experience** from applying the methodology to live or simulated deployments — particularly observations about which controls translated cleanly into operational specifications and which required substantial adaptation.
- **Editorial feedback** on prose clarity, structural organisation, or accessibility for the methodology's named audiences (senior risk and compliance leaders, supervisory staff, technical AI security community).

The forms of contribution above are tracked through GitHub Issues and pull requests; see `CONTRIBUTING.md` for conventions, and `SECURITY.md` for the channel for sensitive disclosures.

## No timeline

The repository does not commit to release timelines. Quiet periods reflect either stability of the methodology against the current landscape or accumulation of changes warranting a coordinated release rather than continuous trickle. Release activity is visible in `CHANGELOG.md` and through GitHub's release feed; readers seeking notification can use GitHub's repository-watch mechanism.
