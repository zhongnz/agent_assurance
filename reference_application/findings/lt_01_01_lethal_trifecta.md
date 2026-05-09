# Finding LT-01-01: Lethal-trifecta architectural configuration without explicit residual-risk acceptance

*Engagement-style finding produced by the synthesis methodology applied to the reference deployment specified in `deployment_specification.md`. The finding addresses the deployment's exhibition of all three capabilities the lethal trifecta names — sensitive data access, untrusted input exposure, egress capability — and the absence of explicit architectural review and residual-risk acceptance.*

## Severity and classification

**Severity: Critical.**

**Regulatory anchors.** AI Act Article 15 (cybersecurity, robustness) — *Indirect*; AI Act Article 9 (risk management) — *Indirect*; DORA Article 5 (ICT risk management framework) — *Indirect*; DORA Article 17 (ICT-related incident management) — *Analogical*.

**OWASP ASI references.** ASI01 (Agent Goal Hijack) + ASI02 (Tool Misuse) + ASI03 (Identity & Privilege Abuse), in compositional reference.

**Cross-cutting patterns.** Lethal trifecta primarily; toxic flows in the specific compositional paths the trifecta realises; identity and privilege abuse as a contributing component (the principal-propagation gap is one of the trifecta's enabling architectural conditions).

**Methodology controls implicated.** LT-01 (lethal-trifecta architectural review); LT-02 (egress-channel inventory and control); TF-01 (toxic-flow analysis); IA-01 (principal propagation through tool chains).

## The trifecta configuration

The deployment exhibits the lethal-trifecta pattern in clear form. The agent's authority surface includes:

**Sensitive data access.** Through the `claims_agent` service account's read access to the institution's policy administration system, claims database, customer-record system, document management system, and fraud-detection vendor scoring API. The access surface includes personal data (customer identification, contact details, claim history), special-category personal data (health information for personal-injury claims), commercial information (policy terms, premium calculations), and reputational data (fraud-risk indicators).

**Untrusted input exposure.** Through claim submissions arriving via customer portal or call-centre intake; uploaded documents (photographs, repair estimates, third-party reports); content returned by community-maintained MCP servers (regional vehicle-data registry, document parsing); and content returned by vendor-supplied MCP servers operating on attacker-influenceable input.

**Egress capability.** Through recommendation drafts routed to human adjusters (which include free-form reasoning text); payment instruction submission for auto-approved claims; claims-status updates communicated to customers via institution notification systems; and any markdown rendering in adjuster-facing outputs.

Each capability is individually defensible. Sensitive data access is required for the agent to perform its function. Untrusted input exposure is required because the agent processes incoming claims. Egress capability is required because the agent's purpose is to produce recommendations and trigger downstream actions. The combination is the threat.

## Compositional path realisation

The compositional path runs from incoming claim submission (untrusted-input source) → retrieval over policy and customer databases (composing untrusted-input with sensitive-data access in the LLM's reasoning step) → recommendation drafting and (for auto-approved claims) payment instruction submission (composing the LLM's response generation with downstream institutional actions). The path's components are individually permitted operations; the composition is an attack surface.

The auto-approval threshold compounds the trifecta's exposure substantially. Sixty percent of claims by volume are processed without human review between the agent's recommendation and the payment instruction. Successful manipulation of the agent's reasoning at any low-value claim — through goal hijack, memory poisoning, or compositional exploitation — produces an auto-approved payment with no human verification.

The pattern is documented in production deployments outside this institution. EchoLeak (CVE-2025-32711, Aim Labs / Microsoft, 11 June 2025) demonstrated the lethal-trifecta pattern in Microsoft 365 Copilot configuration; AgentFlayer (Zenity Labs, Black Hat USA 6 August 2025) demonstrated comparable patterns across multiple agent configurations; Shadow Escape (Operant AI, 22 October 2025) demonstrated the pattern in further variants. The threat class is general; the specific compositional path in this deployment is configuration-specific.

## Compensating controls in current configuration

The deployment's defensive posture against the trifecta consists of:

- Service-account access controls limiting the agent to read-and-update operations within a defined tool inventory (the principal-propagation gap addressed by IA-01-01 means the access scope is broad).
- Orchestration-layer prompts encouraging the agent to scope retrieval to the requesting customer's records.
- The auto-approval threshold itself, which limits the financial impact of any single auto-approved claim to under €2,500.
- Aggregate-level outcome monitoring identifying anomalous payment patterns over time.
- Quarterly red-team exercises (calibrated to general security-testing scope rather than to the methodology's specific threat patterns).

No compensating control specifically addresses the compositional risk. The defensive posture relies on the assumption that the orchestration layer's prompts, the service account's authority limits, and the auto-approval threshold's monetary cap together produce acceptable residual risk. The assumption has not been tested against documented threat scenarios drawn from disclosed agent-security incidents.

## The structural failure mode

Each component-level control responds to a single threat. Service-account access controls address the agent's authority scope. Orchestration-layer prompts address the agent's intended behaviour. The auto-approval threshold addresses the consequence cap on individual decisions. Outcome monitoring addresses aggregate anomalies. Red-team exercises address tested threat scenarios.

The compositional threat — manipulation that combines untrusted input, the agent's broad authority, and the egress channel into an exploitation path — is not addressed by any single control. The trifecta's defining property is exactly that no individual control addresses it; the response must be structural.

The structural response the methodology requires is the architectural review LT-01 specifies. The review's product is not a new technical control; the review's product is documentation. Specifically: documented inventory of the trifecta configuration; documented compensating-control design; documented threat-scenario test results; explicit residual-risk acceptance by an accountable executive against documented threat scenarios.

The deployment has none of these documents. Operationally, the trifecta-configuration risk is accepted by deployment authorisation rather than by explicit consideration. If a trifecta-pattern incident occurs at this deployment, the institution has no documentation of the risk having been considered, the compensating controls considered effective, or the executive having accepted the residual risk knowingly.

## Evidence reviewed

- The deployment's architectural documentation specifying retrieval scope, egress channels, and rendering-client behaviour.
- The deployment's threat-model document, dated at original deployment authorisation.
- The deployment's authorisation record under the institution's general IT-deployment authorisation process.
- Sample tool-invocation logs covering thirty days of production operation.
- Quarterly red-team exercise reports for the four quarters preceding the assessment.
- The institution's general AI-deployment risk-management policy.
- The institution's payment system's audit logs for the period covering auto-approved claims processed by the agent.

## Recommendation

**Recommended remediation.** Conduct architectural review of the lethal-trifecta configuration as required by control LT-01. The review's products:

1. **Trifecta inventory.** Documented enumeration of the deployment's data-access, input-exposure, and egress-channel inventory, identifying the trifecta configurations and their compositional paths.

2. **Compensating-control design.** Documented design of compensating controls intended to mitigate trifecta risk, with explicit treatment of how each control addresses the compositional threat (rather than each control's individual contribution).

3. **Threat-scenario test results.** Testing of compensating controls against documented threat scenarios derived from public disclosures (EchoLeak, AgentFlayer, Shadow Escape, others as relevant to the deployment's specific configuration). Tests must be substantive rather than perfunctory; the goal is to demonstrate that compensating controls perform under realistic adversarial conditions, not merely that they are present.

4. **Explicit residual-risk acceptance.** Documented sign-off by an accountable executive (CRO-level) on the residual risk after compensating controls. The acceptance must be explicit about which scenarios are covered, which are not, and what residual exposure the executive is accepting on the institution's behalf.

**Component remediations supporting the architectural review.**

The architectural review's compensating-control design is most effective when supported by the methodology's component-level controls:

- IA-01 remediation (principal propagation) reduces the trifecta's authority gap, narrowing the consequence space of any specific exploitation.
- TF-01 remediation (toxic-flow analysis) surfaces specific compositional paths that the architectural review can address with targeted compensating controls rather than holistic ones.
- ZC-01 remediation (asynchronous-processing risk gating) introduces runtime gates on outbound tool invocations, addressing the egress-channel component of the trifecta.
- ZC-02 remediation (content-source provenance preservation) addresses the human-trust-exploitation dimension of the trifecta when claims are routed to adjusters.

These component remediations are the subjects of separate findings (IA-01-01, TF-01-01, plus additional findings the engagement would produce).

**Authentication-strength reconfiguration of the auto-approval boundary.** The auto-approval threshold's specific contribution to trifecta exposure warrants targeted remediation:

1. Lower the auto-approval threshold to reduce the population of trifecta-exposed actions.
2. Or, introduce a secondary independent verification step (independently-derived risk score, sample-based human review).
3. Or, convert auto-approval to conditional approval with delayed payment release.

The IA-01-01 finding addresses this remediation in component-level terms; here it appears as one of the trifecta's compositional risk reducers.

## Residual risk after recommendation

**Residual risk: High.**

The recommendations address the methodology gap — the absence of structured architectural review, compositional analysis, runtime evidence, and explicit executive acceptance. They do not, individually or collectively, prevent the lethal-trifecta class of attack.

The residual risk reflects three considerations.

The trifecta configuration may be operationally necessary for the deployment's intended function. Removing the trifecta would require either restricting the agent's data access (conflicting with the function), restricting the agent's input exposure (conflicting with the use case), or restricting the agent's egress (conflicting with the deployment's purpose). The compensating controls reduce the trifecta's exploitability without eliminating it.

Compensating controls' effectiveness depends on assumptions that remain probeable. Each compensating control rests on assumptions about adversarial behaviour (the attacker does not have a specific capability, does not target a specific path, does not compose multiple techniques). Real adversaries probe these assumptions. The compensating controls' effectiveness is therefore not absolute; the architectural review's value is that it makes the assumptions explicit, allowing them to be probed in adversarial testing rather than assumed in implicit acceptance.

The methodology supports detection and reconstruction of incidents but does not guarantee prevention. After-the-fact reconstruction enables institutional and supervisory dialogue about what occurred, why, and what should change. It does not prevent the incident itself. The residual risk is the residual exposure to the trifecta class of incident, which the methodology helps the institution manage but does not eliminate.

**Acceptance is a CRO-level decision.** The methodology's contribution is to make the decision an explicit one rather than an implicit one. The CRO, in accepting residual risk after the architectural review, accepts on the institution's behalf an exposure that has been characterised, tested, and documented.

## Ownership and accountability

**Designated accountable.** CRO (for residual-risk acceptance), with CISO function jointly accountable for technical review.

**First-line.** Deployment owner and architecture team for the architectural review's technical inputs.

**Second-line.** Enterprise risk function for the architectural review's risk-management framing; ICT risk function for the technical review; model-risk function for the foundation-model behavioural dimensions.

**Cross-functional dependencies.** The architectural review's threat-scenario testing requires red-team capability calibrated to the methodology's specific threat patterns. Where the institution's red team is calibrated to general security-testing scope, the testing for this review may require external capability or capability development internally.

## Implementation considerations

The architectural review is approximately three to six weeks of focused work for a moderately complex deployment, with the threat-scenario testing as the most variable component depending on the institution's red-team capability. The review's product is a single document; the document's value depends on the substantive engagement of the parties named, not on the document's length.

Re-review is required on material configuration change. "Material" requires definition; a reasonable specification: any change to the agent's tool inventory, any change to the principal model, any change to the auto-approval threshold, any change to the egress channels, any new MCP server integration, any foundation-model upgrade. The institution's general change-control discipline will surface most material changes; the requirement is that LT-01 re-review is triggered by the material-change identification rather than waiting for the next periodic review cycle.

## Connection to other findings

This finding is one of approximately fifteen primary findings the methodology would produce against the reference deployment. The most directly related findings:

- **IA-01-01** (principal-propagation gap) addresses one of the trifecta's enabling architectural conditions.
- **TF-01-01** (toxic-flow analysis gap) addresses the compositional-path analysis that informs the architectural review's compensating-control design.
- **AT-01 finding** (runtime evidence-capture gap) addresses the evidence required to support after-the-fact reconstruction of any trifecta-pattern incident.
- **ZC-01 finding** (asynchronous-processing risk gating) addresses the runtime gating that complements the architectural review's compensating-control design.
- **GP-01 finding** (deployment authorisation gap) addresses the broader question of how trifecta configurations are authorised in the first place.

The findings are not independent; remediation requires coordinated work across them.
