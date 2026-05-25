# Agent Assurance in Regulated Financial Services

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20379746.svg)](https://doi.org/10.5281/zenodo.20379746)

A position paper, control matrix, applied case study, reference application, briefing surface, and supporting credibility documents on assurance methodology for autonomous AI agents deployed by European banks and insurers. The methodology is preliminary; the architectural argument is not.

## Quick start for practitioners

**Use this if you need to answer:**

- What tools can our agent call, and what authority does it exercise?
- Can untrusted input reach sensitive data and an egress channel?
- What evidence would we show a supervisor about residual risk?
- What's been accepted, by whom, and against what compensating controls?

**In two to four weeks, the methodology can produce a first-pass draft of:**

- Agent inventory and tool-authority map
- Deployment specification documenting architecture and principal model
- Threat register (OWASP ASI + cross-cutting patterns) with severity classification
- Toxic-flow analysis of the authorised tool inventory
- Gap analysis against the v1.0 control matrix
- Engagement-style findings with regulatory and standards anchoring
- Residual-risk acceptance(s) by accountable executive
- Evidence-capture inventory and gaps
- Consolidated supervisor-engageable repository

The `assurance_kit/` directory carries nine markdown templates corresponding to these outputs. The reference application at `reference_application/` shows a completed example against a hypothetical insurance claims-processing deployment. `MINIMUM_VIABLE_ASSURANCE.md` (root) selects ten of the matrix's twenty-six controls as a first-pass adoption subset.

Full operationalisation — institution-wide inventory, second-line review cadence, adversarial testing programme, runtime evidence-capture infrastructure, supervisor-engagement repository under change-control — follows the 30/90/180-day cadence in §7 of the position paper. The two-to-four-week framing above is the first-pass draft; §7 is the operational target.

## What's here

The repository hosts six substantive artifacts: a position paper articulating a synthesis methodology for agent assurance, a control matrix populating the methodology with operational specifications, an applied case study demonstrating the methodology against a documented incident (EchoLeak / CVE-2025-32711), a reference application demonstrating the methodology against a hypothetical deployment, a general-audience briefing surface, and supporting evidentiary documentation that makes the work auditable.

The position paper is the conceptual foundation. The control matrix populates the framework the paper describes. The case study and reference application are the methodology's two demonstrations — retrospective against a real incident, prospective against a constructed deployment. The briefing surface compresses the paper for readers who need orientation rather than depth.

## Scope

The methodology is **EU-first, not EU-only.** The architectural argument, design principles, threat taxonomy, and control-matrix structure are cross-jurisdictional — they address properties of autonomous AI agents that do not change at borders. The operational specifications in v1.0 are calibrated to EU regulatory architecture (DORA, EU AI Act, ISO/IEC 42001, NIST AI RMF, OWASP Top 10 for Agentic Applications, GDPR).

Adaptation to UK, US, Singaporean, Canadian, or other supervisory regimes is welcome as community contribution. The canonical methodology remains EU-calibrated through v1.0; jurisdictional adaptations would be reviewed for inclusion in future versions as community-contributed or experimental profiles. Readers from outside the EU are welcome — the architectural content is portable, and the regulatory anchoring layer is the part that adaptation would replace. See `CONTRIBUTING.md` for the engagement channels and `ROADMAP.md` for what is anticipated through v1.0.

## Repository layout

```
.
├── README.md
├── CHANGELOG.md
├── LICENSE
├── CITATION.cff
├── CONTRIBUTING.md
├── SECURITY.md
├── paper/
│   ├── full.md                            consolidated 27,000-word paper
│   └── control_matrix.md                  v1.0 control matrix, 26 controls
├── case_studies/
│   └── echoleak.md                        the case study (5,400 words)
├── reference_application/
│   ├── README.md                          orientation for the directory
│   ├── deployment_specification.md        the §5 deployment, operationally detailed
│   ├── threat_register.md                 structured threat enumeration
│   ├── gap_analysis.md                    current-state vs target-state per control
│   └── findings/                          three engagement-style findings
├── briefing/
│   ├── briefing_note.md                   one-page summary (~580 words)
│   ├── general_audience_abstract.md       ~180-word standalone abstract
│   └── visual.svg                         single-page architectural visual
├── supporting/
│   ├── verification_log.md                audit trail for 51 verified claims
│   └── source_status.md                   sources catalogued into four evidentiary buckets
├── assurance_kit/                          markdown templates for applying the methodology
│   ├── README.md
│   ├── agent_inventory_template.md
│   ├── deployment_specification_template.md
│   ├── threat_register_template.md
│   ├── toxic_flow_analysis_template.md
│   ├── gap_analysis_template.md
│   ├── finding_template.md
│   ├── residual_risk_acceptance_template.md
│   ├── supervisory_engagement_pack_template.md
│   └── evidence_capture_checklist.md
├── MINIMUM_VIABLE_ASSURANCE.md             ten-control subset for first-pass adoption
└── ROADMAP.md                              direction for v0.9, v1.0, and what is out of scope
```

## Suggested reading order

By time available:

**Five minutes** — read `briefing/briefing_note.md`. The one-page summary tells you what the methodology is, why existing approaches don't address agent assurance, and where to go for more.

**Twenty minutes** — read `briefing/briefing_note.md` and then `case_studies/echoleak.md`'s section 7 (the supervisory-engageable finding). Together they give you the methodology in compressed form plus a worked example of what it produces.

**Half an hour** — read the full case study (`case_studies/echoleak.md`). The case study applies the methodology retrospectively to CVE-2025-32711 (EchoLeak), demonstrating each of the methodology's outputs — threat register, toxic-flow analysis, runtime context capture specification, control matrix application, supervisor-engageable finding — against a real documented incident.

**Two to three hours** — read the position paper at `paper/full.md`. The paper develops the architectural argument, examines the established assurance disciplines and develops the necessary-but-insufficient critique, articulates the threat taxonomy, develops the synthesis methodology with five design principles, applies the methodology to a reference deployment, maps the regulatory horizon, and offers operational recommendations.

By interest:

**For the methodology itself**: paper sections 1, 2, and 4. Section 1 establishes that agents are a structurally distinct assurance object; section 2 develops the necessary-but-insufficient critique of the established disciplines; section 4 articulates the synthesis methodology.

**For the regulatory and supervisory framing**: paper sections 1.3 and 6. Section 1.3 surveys the supervisory communications that have made agent assurance an active concern; section 6 maps the regulatory horizon including DORA, the AI Act, and the supervisory expectations now forming.

**For methodology in operation**: the case study, the reference application, and paper section 5 (the reference deployment specification). The case study at `case_studies/echoleak.md` applies the methodology retrospectively to a documented incident; the reference application at `reference_application/` applies it prospectively to a hypothetical deployment with full structured outputs (threat register, gap analysis, findings).

**For the operational specification of the methodology**: `paper/control_matrix.md`. The matrix populates the methodology's framework with 26 controls mapping all ten OWASP Top 10 for Agentic Applications categories (with ASI05 Unexpected Code Execution acknowledged as a coverage gap in v1.0), the five cross-cutting threat patterns, and additional governance and evidence-capture areas, with full regulatory and standards anchoring.

**For the evidentiary discipline**: `supporting/verification_log.md` and `supporting/source_status.md`. The verification log documents the audit trail for the 51 load-bearing claims identified in the position paper's v0.7 verification round, resolved against primary or directly-corroborating sources; the source status document catalogues sources into four evidentiary buckets. The control matrix, case study, and reference application carry their own citations and are not exhaustively audited in the verification log.

## How to engage

The work is offered as a contribution to a developing field, not as a definitive statement of it. Reactions of any kind are welcome.

For substantive comments on the paper or case study, GitHub Issues is the cleanest channel. Issues can reference specific sections, support threaded discussion, and remain visible for other readers who may have similar questions. See `CONTRIBUTING.md` for issue conventions and the kinds of engagement that are most useful.

For private feedback, professional inquiries, or engagement opportunities, reach out via the contact link on the author's GitHub profile.

For sensitive disclosures (security concerns about the methodology, identification of confidential information, or similar concerns warranting non-public channels), see `SECURITY.md`.

## Status

The repository is at v0.8.24 (see CHANGELOG) and is maintained by Fengze Zhong. The position paper's substantive content is at the v0.8.1 level — three rounds of structured self-review by the author, four rounds of source verification, all 51 verification markers resolved against primary or directly-corroborating sources, editorial compression applied. External review has not yet occurred; external-reviewer feedback is the explicit v0.9 milestone per `ROADMAP.md`. Subsequent point versions (v0.8.2 through v0.8.23) added the control matrix, the reference application materials, repository hygiene infrastructure, the project-level roadmap, contribution scaffolding, the assurance kit and MVA operational layer, a release checklist, and successive rounds of correctness, traceability, and citation-currency fixes documented in the CHANGELOG; the paper's argument and citations are stable across these. The roadmap at `ROADMAP.md` articulates anticipated direction for v0.9 and v1.0.

The methodology is preliminary — described as v1.0 of an artifact that will revise as it meets engagement reality. Specific controls in the framework will be refined; the architectural argument and design principles are stable.

The case study is the first applied demonstration of the methodology against a documented incident. The reference application is the first applied demonstration against a constructed deployment. Additional case studies and reference applications are likely as the work progresses.

## A note on what the work does and does not claim

The methodology produces assurance, not prevention. The framework's outputs help institutions deploy autonomous agents with structured, supervisor-engageable positions about residual risk; they do not guarantee that incidents will not occur.

The methodology is for institutional assurance posture, not for governance of which deployments to authorise. The latter is upstream work the methodology supports but does not substitute for.

The methodology is anchored in the regulatory and standards stack that European financial-services institutions are already subject to — DORA, the EU AI Act, ISO/IEC 42001, NIST AI RMF, and OWASP's Top 10 for Agentic Applications. The framework is offered as a contribution to existing supervisory and standards work, not as a replacement for any of it.

## Citation

The working title for the paper is *Agent Assurance in Regulated Financial Services*. If you cite the work, please include the version (see CHANGELOG) and the DOI of the specific release you are citing.

The most recently DOI-minted release is v0.8.23 ([10.5281/zenodo.20379746](https://doi.org/10.5281/zenodo.20379746)). Each tagged release receives its own version-specific DOI; the version-by-version archive trail is:

| Version | DOI | Release theme |
|---|---|---|
| v0.8.23 | [zenodo.20379746](https://doi.org/10.5281/zenodo.20379746) | post-audit citation-currency catch-up; release checklist |
| v0.8.22 | [zenodo.20379642](https://doi.org/10.5281/zenodo.20379642) | deep-audit fixes to v0.8.21 operational layer |
| v0.8.21 | [zenodo.20379437](https://doi.org/10.5281/zenodo.20379437) | assurance kit, MVA, practitioner quick-start |
| v0.8.20 | [zenodo.20379193](https://doi.org/10.5281/zenodo.20379193) | scope positioning (EU-first, not EU-only) |
| v0.8.19 | [zenodo.20379095](https://doi.org/10.5281/zenodo.20379095) | author metadata (ORCID, bio); captures v0.8.18 |
| v0.8.17 | [zenodo.20344693](https://doi.org/10.5281/zenodo.20344693) | citation currency + convention completeness |
| v0.8.16 | [zenodo.20344315](https://doi.org/10.5281/zenodo.20344315) | fourth-audit propagation fixes |
| v0.8.15 | [zenodo.20344199](https://doi.org/10.5281/zenodo.20344199) | author-name correction |
| v0.8.14 | [zenodo.20320343](https://doi.org/10.5281/zenodo.20320343) | third-audit traceability; captures v0.8.13 |
| v0.8.12 | [zenodo.20308910](https://doi.org/10.5281/zenodo.20308910) | open-source consistency pass |
| v0.8.11 | [zenodo.20308659](https://doi.org/10.5281/zenodo.20308659) | initial public release |

v0.8.13 and v0.8.18 were untagged maintenance commits; their changes are captured in v0.8.14 and v0.8.19's archives respectively.

A copy-and-paste BibTeX entry for the most recently DOI-minted release:

```bibtex
@misc{zhong2026agentassurance,
  author    = {Zhong, Fengze},
  title     = {Agent Assurance in Regulated Financial Services},
  year      = {2026},
  publisher = {Zenodo},
  version   = {v0.8.23},
  doi       = {10.5281/zenodo.20379746},
  url       = {https://github.com/zhongnz/agent_assurance}
}
```

A `CITATION.cff` file in the repository root provides citation metadata in the Citation File Format, including the DOI as an identifier. GitHub renders this metadata in the repository sidebar, allowing readers to cite the work in standard formats.

## About the author

Fengze Zhong is an independent researcher. Previously a researcher at the NYU Center for Data Science, working on agentic governance for financial services. ORCID: [0009-0004-7926-8495](https://orcid.org/0009-0004-7926-8495). Contact via the GitHub profile ([@zhongnz](https://github.com/zhongnz)) or the channels documented in `SECURITY.md`.

## License

The work in this repository is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). You are free to share and adapt the material for any purpose, including commercially, with appropriate credit. See `LICENSE` for the full terms.
