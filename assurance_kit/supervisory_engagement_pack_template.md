# Supervisory Engagement Pack — [Deployment ID]

*Consolidated supervisory-engageable repository for a single agent deployment. The pack contains the methodology's per-deployment outputs in a single retrievable structure suitable for second-line review or supervisory dialogue without translation work. Implements HC-01 (Supervisory-engagement repository) from the v1.0 control matrix.*

## Pack contents

The pack consolidates the following artifacts, dated and version-tagged. The pack itself is a folder structure or document repository; this template specifies the inventory of artifacts the pack must contain.

| Artifact | Source template | Date | Version |
|---|---|---|---|
| Agent inventory entry | `agent_inventory_template.md` | [YYYY-MM-DD] | [vX.Y] |
| Deployment specification | `deployment_specification_template.md` | [YYYY-MM-DD] | [vX.Y] |
| Regulatory mapping | (Regulatory mapping section below) | [YYYY-MM-DD] | [vX.Y] |
| Accountability documentation | (Accountability section below) | [YYYY-MM-DD] | [vX.Y] |
| Threat register | `threat_register_template.md` | [YYYY-MM-DD] | [vX.Y] |
| Gap analysis | `gap_analysis_template.md` | [YYYY-MM-DD] | [vX.Y] |
| Findings | `finding_template.md` × N | [YYYY-MM-DD] | [vX.Y] |
| Residual-risk acceptances | `residual_risk_acceptance_template.md` × N | [YYYY-MM-DD] | [vX.Y] |
| Adversarial test results | (institution-specific; references GP-02) | [YYYY-MM-DD] | [vX.Y] |
| Evidence-capture inventory | `evidence_capture_checklist.md` | [YYYY-MM-DD] | [vX.Y] |
| Runtime evidence references | (data-room reference or storage path) | continuous | n/a |

## Regulatory mapping

[Per-deployment mapping of applicable regulatory obligations to the controls and evidence that address them. Format: regulation / article / obligation → matrix control(s) → evidence artifact(s).]

| Regulation | Article / clause | Obligation summary | Methodology control(s) | Evidence artifact |
|---|---|---|---|---|
| AI Act | Art. 12 | Record-keeping | AT-01, AT-02, AT-03 | Runtime evidence-capture infrastructure documentation |
| AI Act | Art. 14 | Human oversight | IA-03, ZC-01 | Authentication architecture, runtime gates documentation |
| AI Act | Art. 15 | Accuracy, robustness, cybersecurity | RO-01, CF-01, RA-01 | (per deployment) |
| DORA | Art. 9 | Protection and prevention | IA-01, IA-02, ZC-01 | (per deployment) |
| DORA | Art. 17 | ICT-related incident management | (institution-level incident response) | Incident-response plan reference |
| GDPR | Art. 25 | Data protection by design | AT-02 | Evidence-capture privacy controls documentation |
| | | | | |

## Accountability

Named individuals across the three lines of defence:

- **First line.** Deployment owner / operations lead: [name, role]
- **Second line.** ICT risk / model risk / enterprise risk function: [name, role]
- **Third line.** Internal audit owner: [name, role]
- **Accountable executive.** Typically CRO: [name, role]

## Repository structure and access controls

[Folder structure and access controls for the pack itself. Specify retention period — institutional policy, minimum 6 months per AI Act Article 26(6) for high-risk systems, longer per institutional risk-appetite.]

[Specify access controls: who can read the pack, who can update individual artifacts, who can approve residual-risk acceptances. The pack's integrity discipline matters for supervisory engagement.]

## Update cadence

[How often the pack is refreshed:

- Per material change (new tool, principal-model change, auto-approval threshold change, foundation-model upgrade, change of accountable executive).
- Per scheduled review (typically quarterly for high-risk deployments, semi-annually for medium-risk, annually for low-risk).
- Per supervisory engagement event (examination, inquiry, thematic review).]

## See also

- `paper/control_matrix.md` HC-01 — the matrix specification for this control
- `reference_application/` — worked example of the artifacts that populate the pack
- `paper/full.md` §7 — recommendations covering the supervisory-ready repository's role in the 30/90/180-day cadence
