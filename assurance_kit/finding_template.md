# Finding [CONTROL-ID-XX]: [short title]

*Engagement-style finding addressing a specific gap identified in the gap analysis. Anchored to regulatory and standards references; specifies evidence reviewed, recommendation, and residual risk after the recommendation is implemented. Mirrors the structure of `reference_application/findings/*.md`.*

## Severity and classification

*Severity:* [Critical / High / Medium / Low].

*Regulatory anchors:* [AI Act Article(s) — *Direct* / *Indirect* / *Analogical*; DORA Article(s) — *Direct* / *Indirect* / *Analogical*; GDPR Article(s) where relevant; institution-specific anchors.]

*OWASP ASI references:* [ASI categories implicated; for compositional patterns, list the categories with "in compositional reference" annotation.]

*Cross-cutting patterns:* [lethal trifecta / toxic flows / tool poisoning / identity and privilege abuse / zero-click exfiltration, as applicable.]

*Matrix control(s) addressed:* [TP-01, IA-01, LT-01, etc.]

## Configuration

[Description of the deployment configuration that produces the gap. Cite the relevant sections of `deployment_specification.md`.]

## Threat realised

[How the gap manifests as risk in the deployment. Cite the threat register's relevant entries. Reference comparable documented incidents where they exist (EchoLeak, AgentFlayer, etc.) for context, with explicit care not to conflate the deployment with the incident.]

## Evidence reviewed

[List of evidence the finding rests on: the deployment specification, the threat register, the gap analysis, runtime logs where available, any specific incident or audit material. Date the evidence; specify the period covered for runtime data.]

## Recommendation

[Concrete remediation steps anchored to the matrix control(s). Each step should be operationally specific enough that the institution can sequence implementation. Acknowledge dependencies on other findings or institutional decisions where they exist.]

## Residual risk after recommendation

*Residual risk:* [Critical / High / Medium / Low / Accepted].

[Description of what risk remains after the recommendation is implemented. The methodology supports decision-making about residual risk, not its elimination. The residual-risk articulation must acknowledge what the recommendation does and does not address.]

## Acceptance

*Accountable executive:* [name, role — e.g., CRO].

*Acceptance date:* [YYYY-MM-DD].

*Review cadence:* [annual / quarterly / per material change].

*Notes:* [optional brief notes on acceptance conditions, compensating controls relied on, or specific assumptions named.]

## See also

- `residual_risk_acceptance_template.md` — for the full acceptance artifact if this finding's residual risk is being formally accepted
- `paper/control_matrix.md` — the matrix control(s) this finding addresses
- `reference_application/findings/` — worked examples (`ia_01_01_principal_propagation.md`, `lt_01_01_lethal_trifecta.md`, `tf_01_01_toxic_flow.md`)
