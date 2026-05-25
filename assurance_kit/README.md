# Assurance Kit

*Templates for applying the synthesis methodology to a specific agent deployment. The templates correspond to the methodology's named outputs from the position paper and to the worked examples in the reference application; they are the bridge between "read the paper" and "run an assessment."*

## What's here

The kit contains nine markdown templates corresponding to the methodology's named outputs:

| Template | Purpose | Methodology reference |
|---|---|---|
| `agent_inventory_template.md` | Institution-wide inventory of agent deployments | §7 recommendations (30-day work) |
| `deployment_specification_template.md` | Per-deployment specification (architecture, tools, principal model, authority) | §5.2; §7 (90-day work); mirrors `reference_application/deployment_specification.md` |
| `threat_register_template.md` | Structured threat enumeration organised by OWASP ASI + cross-cutting patterns | §3 / §5.3; §7 (90-day work); mirrors `reference_application/threat_register.md` |
| `toxic_flow_analysis_template.md` | Compositional analysis of the authorised tool inventory (TF-01 operationalised) | §3.2.4 / §5.3; §7 (90-day work); mirrors `reference_application/findings/tf_01_01_toxic_flow.md` |
| `gap_analysis_template.md` | Control-by-control evaluation against the v1.0 control matrix | §5.3 / §5.4; §7 (90-day work); mirrors `reference_application/gap_analysis.md` |
| `finding_template.md` | Engagement-style finding for an individual gap, anchored to regulatory and standards references | §5.4; mirrors `reference_application/findings/*.md` |
| `residual_risk_acceptance_template.md` | Accountable-executive sign-off for residual risk | LT-01; evidence-first principle |
| `supervisory_engagement_pack_template.md` | Consolidated supervisory-engageable repository | HC-01; §7 (180-day work) |
| `evidence_capture_checklist.md` | Runtime evidence-capture requirements | AT-01, AT-02, AT-03; §7 (180-day work) |

## How to use

A first assessment of a single agent deployment moves through, in order:

1. **Agent inventory** across institutional scope (if not already maintained).
2. **Deployment specification** for the agent under assessment; the evidence-capture posture is documented in §8 of the specification and revisited at step 8 below.
3. **Threat register** against that deployment.
4. **Toxic-flow analysis** of the authorised tool inventory; the analysis's identified flows feed the threat register's *Toxic flows* cross-cutting section.
5. **Gap analysis** of the deployment against the v1.0 control matrix, including the AT-01 / AT-02 / AT-03 evidence-capture row that draws on step 2 and the `evidence_capture_checklist.md`.
6. **Findings** for each gap warranting documentation.
7. **Residual-risk acceptance** per finding (or rolled-up acceptance per deployment).
8. **Evidence-capture inventory** consolidated against the checklist; gaps return to step 5.
9. **Supervisory engagement pack** consolidating the above.

Steps 1 and parts of step 2 map to §7's 30-day cadence. Steps 2–6 map to §7's 90-day cadence. Steps 7–9 map to §7's 180-day cadence. The Quick-start in the repository README claims a first-pass draft of these outputs can be produced in two to four weeks; full operationalisation per §7 takes longer.

The reference application at `reference_application/` shows a completed example against a hypothetical insurance claims-processing deployment. Treat the worked example as the reference; treat the templates as the starting point for your own deployment.

`MINIMUM_VIABLE_ASSURANCE.md` at the repository root selects ten of the twenty-six controls as a first-pass adoption subset. Where the full control matrix is too heavy for initial adoption, the MVA is the tractable entry point.

## What this kit is not

The kit is template scaffolding, not a turnkey methodology. The substantive judgement work — threat enumeration, severity classification, gap remediation, residual-risk acceptance — is the engagement; the templates structure that work for visibility and consistency.

The kit is also not formal-attestation infrastructure. Outputs are assurance-ready evidence in the methodology's terms, not attestation under ISAE 3000 or AT-C 205. Those pathways require partnership with qualified practitioners and sit outside the methodology's scope.

## See also

- `paper/full.md` — the position paper's argument and methodology
- `paper/control_matrix.md` — the v1.0 control matrix (26 controls)
- `reference_application/` — worked example showing the kit applied to a hypothetical deployment
- `MINIMUM_VIABLE_ASSURANCE.md` (repository root) — ten-control subset for first-pass adoption
- `CONTRIBUTING.md` — engagement channels for corrections, extensions, and engagement experience
