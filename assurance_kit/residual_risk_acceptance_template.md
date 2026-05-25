# Residual Risk Acceptance — [Deployment ID / Finding ID]

*Accountable-executive sign-off on residual risk after compensating controls. Required where a finding identifies a gap that the institution chooses to accept (with documented rationale) rather than fully remediate. The acceptance is the methodology's terminal output: a documented institutional decision against documented risk, not a methodology recommendation.*

## Subject

*Deployment ID:* [agent ID per `agent_inventory_template.md`]

*Finding(s) referenced:* [list of findings whose residual risk is being accepted by this artifact]

*Date of acceptance:* [YYYY-MM-DD]

## Configuration described

[Brief reference to the deployment configuration that produces the residual risk. Cite the relevant sections of `deployment_specification.md`.]

## Residual risk after compensating controls

[Description of what residual risk remains after recommended compensating controls are applied. The description must reflect what the controls actually mitigate, not what they aspire to.]

*Residual-risk severity:* [Critical / High / Medium / Low]

## Compensating controls relied upon

[List of compensating controls the institution is relying on to bound the residual risk. Each control's assumptions must be named explicitly; the methodology's discipline is that controls' effectiveness depends on assumptions that remain probeable, and the assumptions are the load-bearing element of the acceptance.]

## Assumptions named

[Explicit list of assumptions the residual-risk acceptance depends on. Examples:

- "The foundation-model vendor's safety classifiers remain effective against the documented threat scenarios."
- "The orchestration layer's retry logic does not bypass policy gates under degraded conditions."
- "The institution's incident-response capability is calibrated to detect the residual-risk scenarios within acceptable timeframes."
- "The tool inventory does not change materially without re-running the qualification process."]

## Acceptance

*Accountable executive:* [name]

*Role:* [CRO / Chief AI Officer / CISO / business owner per institutional structure]

*Signature or approval reference:* [e.g., approval reference number; emailed sign-off date; meeting minutes reference]

## Review cadence

*Next scheduled review:* [date; typically annual unless material change triggers earlier review]

*Material change triggers requiring earlier review:* [enumerate — e.g., new tool added to inventory, change to principal model, change to auto-approval threshold, foundation-model upgrade, change of accountable executive, new disclosed incident in the comparable-deployment population]

## See also

- `finding_template.md` — for the finding(s) this acceptance addresses
- `paper/control_matrix.md` LT-01 — the methodology's lethal-trifecta-acceptance discipline
- `paper/full.md` §4.1 — the *evidence-first* and *composable and continuous* design principles that frame acceptance discipline
