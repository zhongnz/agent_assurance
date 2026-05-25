# Reference application — claims-processing agent

*Worked application of the synthesis methodology to the hypothetical insurance claims-processing agent deployment described in §5 of the position paper. The materials in this directory produce the artifacts the methodology generates against the deployment, complementing the prose walk-through in §5 with the structured outputs an actual engagement would produce.*

## What's here

This directory contains the methodology's outputs against the §5 reference deployment as discrete artifacts:

**`deployment_specification.md`** — restructured specification of the §5 deployment with operational detail expanded for engagement use. Drawn from §5.2 of the paper, with additional architecture, principal-model, and evidence-capture detail.

**`threat_register.md`** — structured threat enumeration organised by OWASP Top 10 for Agentic Applications categories and the cross-cutting threat patterns from §3.2. Each threat is paired with the deployment-specific configuration that creates exposure, severity classification, evidence requirements, and recommended controls from the matrix at `paper/control_matrix.md`.

**`gap_analysis.md`** — comparison between the deployment's current-state configuration and the methodology-recommended target-state configuration. Each control from the matrix is evaluated as Present, Partially present, Absent, or Not applicable, with gap, operational consequence, and recommendation per Partially-present and Absent control.

**`findings/`** — three engagement-style findings demonstrating the methodology's terminal output form:
- `ia_01_01_principal_propagation.md` — the principal-propagation gap (extended from §5.4 of the paper).
- `lt_01_01_lethal_trifecta.md` — the lethal-trifecta architectural configuration without explicit residual-risk acceptance.
- `tf_01_01_toxic_flow.md` — the absence of toxic-flow analysis of the authorised tool inventory.

The full engagement output would include findings of comparable structure for each High-severity Absent or Partially-present control the gap analysis identifies — approximately fifteen such controls in the reference deployment — plus a larger set of secondary findings covering operational hygiene, documentation gaps, and lower-severity issues. The three findings included demonstrate the form across different control families and severity levels.

## Relation to the assurance kit

The reference application's artifacts are the worked examples for the templates in `assurance_kit/` (at the repository root). Each artifact here corresponds to a template there:

- `deployment_specification.md` ↔ `assurance_kit/deployment_specification_template.md`
- `threat_register.md` ↔ `assurance_kit/threat_register_template.md`
- `gap_analysis.md` ↔ `assurance_kit/gap_analysis_template.md`
- `findings/*.md` ↔ `assurance_kit/finding_template.md`
- `findings/tf_01_01_toxic_flow.md` is also the worked example for `assurance_kit/toxic_flow_analysis_template.md`

Practitioners applying the methodology to their own deployment start with the templates; the worked examples here are the reference for what populated outputs look like.

## Relation to the rest of the repository

The reference application is one of two worked applications of the methodology in the repository. The case study at `case_studies/echoleak.md` applies the methodology retrospectively to a real documented incident (CVE-2025-32711). The reference application here applies it prospectively to a hypothetical deployment matching patterns observable in production European insurer AI deployments.

The two applications produce complementary credibility. The case study demonstrates the methodology against a real incident, addressing the reader's question of "does this work against a real attack." The reference application demonstrates the methodology against a constructed deployment, addressing the reader's question of "does this produce specific outputs against a specific configuration."

## What this reference application establishes and what it does not

**It establishes** that the methodology produces specific, structured outputs against a specific deployment configuration; that the design principles produce coherent guidance under application; that the framework's outputs are calibrated for supervisory and second-line engagement; and that the gap between current-state and target-state configurations can be characterised systematically.

**It does not establish** that the methodology's findings would be empirically accurate at deployment scale (the reference deployment is hypothetical, and the findings are the methodology's logical output rather than findings against an observed system); that the controls are operationally feasible at the cost and integration complexity an institution would actually accept; or that the methodology's findings would scale across the diversity of agent deployment configurations institutions actually operate.

The §5.5 closing of the position paper articulates the boundaries in similar terms; the reference application's materials sit within those boundaries.
