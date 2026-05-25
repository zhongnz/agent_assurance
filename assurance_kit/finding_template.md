# Finding [CONTROL-ID-XX]: [short title]

*Engagement-style finding addressing a specific gap identified in the gap analysis. Anchored to regulatory and standards references; specifies evidence reviewed, recommendation, residual risk, ownership, implementation considerations, and connections to other findings. Mirrors the structure of `reference_application/findings/*.md`.*

## Severity and classification

*Severity:* [Critical / High / Medium / Low].

*Regulatory anchors:* [AI Act Article(s) — *Direct* / *Indirect* / *Analogical*; DORA Article(s) — *Direct* / *Indirect* / *Analogical*; GDPR Article(s) where relevant; institution-specific anchors.]

*OWASP ASI references:* [ASI categories implicated; for compositional patterns, list the categories with "in compositional reference" annotation.]

*Cross-cutting patterns:* [lethal trifecta / toxic flows / zero-click exfiltration, as applicable. Note that tool poisoning and identity-and-privilege abuse are typically captured under ASI04 and ASI03 categories rather than as standalone cross-cutting; memory-and-context poisoning is captured under ASI06.]

*Matrix control(s) addressed:* [TP-01, IA-01, LT-01, etc.]

## [Body — adapt to finding type]

[The worked findings in `reference_application/findings/` use variable analytical sections under this heading, calibrated to the specific gap. Section names that recur in worked examples include: *The configuration*, *The structural failure mode*, *Compositional path realisation*, *Compensating controls in current configuration*, *Why the matrix specifies this control as Absent*, *Pattern documented in production*. Adapt the body sections to the finding's analytical content; do not constrain to fixed headings. Cite the deployment specification, threat register, and gap analysis sections that ground the finding.]

## Evidence reviewed

[List of evidence the finding rests on: deployment specification, threat register, gap analysis, runtime logs where available, specific incident or audit material. Date the evidence; specify the period covered for runtime data.]

## Recommendation

[Concrete remediation steps anchored to the matrix control(s). Each step should be operationally specific enough that the institution can sequence implementation. Acknowledge dependencies on other findings or institutional decisions where they exist.]

## Residual risk after recommendation

*Residual risk:* [Critical / High / Medium / Low / Accepted].

[Description of what risk remains after the recommendation is implemented. The methodology supports decision-making about residual risk, not its elimination. The residual-risk articulation must acknowledge what the recommendation does and does not address.]

## Ownership and accountability

Across the three lines of defence, named individuals or functions:

- **First line:** deployment owner / operations lead — [name, role]
- **Second line:** ICT risk / model risk / enterprise risk function — [name, role]
- **Third line:** internal audit owner — [name, role]
- **Accountable executive:** typically CRO — [name, role]

Ownership is named here to make the recommendation actionable; formal residual-risk acceptance (signature and acceptance date) is captured separately in `residual_risk_acceptance_template.md`.

## Implementation considerations

[Operational concerns the institution should weigh in implementing the recommendation: dependencies on other findings, time and effort estimates (where known), trade-offs the recommendation entails (latency vs assurance, breadth vs depth, capacity vs scope), compensating controls available during the implementation period, sequencing relative to other deployments under assessment.]

## Connection to other findings

[How this finding relates to others in the engagement:
- Findings that share dependencies (e.g., "IA-01 finding remediation is precondition for this finding's recommendation").
- Findings that compose (e.g., "this finding + LT-01-XX together address the lethal-trifecta configuration's exposure").
- Findings that depend on this one (e.g., "AT-03 finding depends on AT-01 finding's evidence capture being in place").]

## Acceptance

*If the residual risk is formally accepted, the acceptance is recorded in `residual_risk_acceptance_template.md` and referenced here once signed.*

- *Acceptance reference:* [residual_risk_acceptance_template.md entry, or "pending" while the recommendation is under implementation].
- *Acceptance date:* [YYYY-MM-DD if signed; else "pending"].
- *Review cadence:* [from the acceptance artifact].

## See also

- `residual_risk_acceptance_template.md` — full acceptance artifact this finding feeds when residual risk is signed off
- `paper/control_matrix.md` — the matrix control(s) this finding addresses
- `reference_application/findings/` — worked examples (`ia_01_01_principal_propagation.md`, `lt_01_01_lethal_trifecta.md`, `tf_01_01_toxic_flow.md`)
