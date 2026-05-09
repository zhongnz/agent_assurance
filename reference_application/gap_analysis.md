# Gap analysis — claims-processing agent reference deployment

*Comparison between the deployment's current-state configuration (as specified in `deployment_specification.md`) and the methodology-recommended target-state configuration. The analysis identifies which controls from the matrix at `paper/control_matrix.md` are partially in place, which are absent, and which are present but with assumption gaps that require remediation.*

## Conventions

Each control from the matrix is evaluated against three possible states. *Present* means the control's substantive requirements are implemented in the current deployment, possibly with operational refinements still useful but not addressing material gaps. *Partially present* means some elements of the control's requirements are implemented, but material gaps remain. *Absent* means the control's substantive requirements are not implemented in the current deployment.

For each Partially-present and Absent control, the gap analysis specifies the gap, the operational consequences of the gap, and the recommended remediation path. The gap analysis does not estimate implementation cost or timeline; those are properly the institution's operational decisions.

## Tool-poisoning controls

### TP-01: Tool metadata integrity verification — Absent

**Gap.** No tool metadata integrity verification is in place at session initialisation. Tool metadata from all seven MCP servers is consumed at session initialisation without cryptographic verification against an internal registry. Modifications to tool metadata between session initialisations are not detected.

**Operational consequence.** Metadata-layer tool-poisoning attacks would not be detected. The two community-maintained MCP servers carry the highest exposure given their absence of contractual integrity obligations, but vendor-supplied and first-party servers are also exposed in principle.

**Remediation.** Establish an internal tool-definition registry. Implement cryptographic hashing of tool metadata at session initialisation with verification against the registry. Define the change-control process for registry updates. Define the alerting and response procedure for hash mismatches.

### TP-02: Third-party MCP server qualification — Partially present

**Gap.** The two vendor-supplied MCP servers operate under contractual obligations including security posture, data handling, and incident notification. The two community-maintained MCP servers operate without contractual obligations and have not undergone the institution's third-party-risk-management qualification.

**Operational consequence.** The deployment's exposure to the community-maintained servers is not characterised. The institution has no formal mechanism to assess the maintainers' security discipline, change-management practices, or incident response.

**Remediation.** Either replace community-maintained MCP servers with first-party or vendor-contracted equivalents, or establish a qualification process for community-maintained servers that documents the absence of contractual obligations and the compensating controls required.

### TP-03: First-party tool change control — Partially present

**Gap.** First-party MCP servers operate under the institution's general IT change-control discipline. Specific change-control procedures for tool definition changes — distinct from underlying server-implementation changes — are not documented.

**Operational consequence.** Tool definition changes propagate through general IT change control without the specific scrutiny tool-poisoning risk would warrant.

**Remediation.** Document tool-definition-specific change-control procedures, including who may modify tool definitions, the testing required before changes propagate to the agent's session-initialisation flow, and the audit-trail requirements.

## Identity and privilege controls

### IA-01: Principal propagation through tool chains — Absent

**Gap.** The deployment uses a single `claims_agent` service account for all customer interactions. The requesting customer's identity is communicated to the agent through the claim payload but is not propagated to the tool-invocation layer. Downstream resource access is authorised against the service account's authority, not against the requesting customer's authority.

**Operational consequence.** The agent's effective authority is broader than any individual customer's authority. Manipulation of the agent's reasoning context can exploit the gap to retrieve records the requesting customer is not authorised to see.

**Remediation.** Implement per-request scope narrowing at the policy-administration system, constraining the agent's effective authority to the customer whose claim is being processed. Where per-request scope narrowing is not architecturally feasible at the resource layer, implement compensating controls at the agent layer that validate retrieved records against the requesting customer's identity before the records are incorporated into reasoning context.

This gap is the subject of finding IA-01-01 (`findings/ia_01_01_principal_propagation.md`).

### IA-02: Service-account authority limitation — Partially present

**Gap.** The `claims_agent` service account has read access to all customer records, all policies, all claims. The authority is not scoped to the minimum required for the agent's deployed function — by design, since the deployment's intended workflow requires reading any customer's records on demand.

**Operational consequence.** Where principal propagation (IA-01) is not implemented, the service account's broad authority is the operative authority for all agent actions. Service-account authority limitation is the structural fallback when principal propagation is not in place.

**Remediation.** Quarterly review of service-account authority scope. Identify any authority granted that is not required for current function. Where the authority must remain broad (because principal propagation is not implemented and the agent must access any customer's records), document the justification and the compensating controls in place.

### IA-03: Authentication strength for high-authority actions — Partially present

**Gap.** Auto-approval at €2,500 produces payment instruction submission without human review. The action is high-consequence (irreversible payment from institutional funds) but is authenticated against the service account only. No additional authentication strength is required for the auto-approval action class.

**Operational consequence.** A successful manipulation of the agent's reasoning at any low-value claim produces an auto-approved payment instruction with no human review. The auto-approval threshold is the most consequential authentication gap in the deployment.

**Remediation.** Either lower the auto-approval threshold (reducing the population of claims processed without human review), introduce a secondary authentication step for auto-approval (an additional check against an independently-derived risk score, or a sample-based human review of auto-approved claims), or re-classify auto-approved claims as conditional approvals with delayed payment release.

## Lethal-trifecta and compositional controls

### LT-01: Lethal trifecta architectural review — Absent

**Gap.** The deployment exhibits the lethal trifecta but has not undergone explicit architectural review of the trifecta configuration. The trifecta's compositional risk has not been documented; compensating controls have not been tested against documented threat scenarios; residual risk has not been explicitly accepted by an accountable executive.

**Operational consequence.** The deployment operates under implicit acceptance of trifecta risk rather than explicit acceptance. If a trifecta-pattern incident occurs, the institution has no documentation of the risk having been considered, the compensating controls considered effective, or the executive having accepted the residual risk knowingly.

**Remediation.** Conduct architectural review of the lethal-trifecta configuration as required by control LT-01. Produce the documented inventory of trifecta configurations, compensating-control design, threat-scenario test results, and explicit residual-risk acceptance by an accountable executive.

This gap is the subject of finding LT-01-01 (`findings/lt_01_01_lethal_trifecta.md`).

### LT-02: Egress-channel inventory and control — Absent

**Gap.** The deployment's egress channels are not enumerated as a discrete inventory. Recommendation drafts (routed to adjusters), payment instruction submission (for auto-approved claims), claims-status updates (communicated to customers via the institution's notification system), and any markdown rendering in adjuster-facing outputs are present but not inventoried as a discrete attack surface.

**Operational consequence.** Defence-in-depth at the egress layer is uneven. Markdown rendering in adjuster-facing outputs has no specific egress-control posture; payment instruction submission has indirect controls through the payment system but no agent-layer controls.

**Remediation.** Inventory all egress channels through which agent outputs can produce outbound communication. Classify each by destination trustworthiness. Apply controls scaled to destination class.

## Toxic-flow controls

### TF-01: Toxic-flow analysis — Absent

**Gap.** Static toxic-flow analysis of the deployment's authorised tool inventory has not been performed. Compositional paths from untrusted-input nodes through privileged-data-access nodes to egress nodes are not enumerated in current documentation.

**Operational consequence.** Compositional risks beyond the most direct lethal-trifecta path are not surfaced. Specific paths involving the community-maintained MCP servers' outputs flowing into vendor-server inputs (e.g., vehicle-data registry → repair-shop estimate) are not analysed.

**Remediation.** Conduct static toxic-flow analysis of the deployment's authorised tool inventory using compositional-analysis tooling (Snyk Agent Scan TF001 or equivalent functionality). Document identified flows, severity classifications, remediation or compensating-control decisions, and residual-risk acceptance.

This gap is the subject of finding TF-01-01 (`findings/tf_01_01_toxic_flow.md`).

### TF-02: Cross-deployment flow review — Absent

**Gap.** The claims-processing agent shares foundation-model API access, orchestration-framework infrastructure, and parts of evidence-capture infrastructure with two other internal agent deployments. Cross-deployment compositional risks are not analysed.

**Operational consequence.** Cross-deployment cascade paths are not characterised. A compromise in either of the other deployments could propagate through shared infrastructure into the claims agent in ways that have not been considered.

**Remediation.** Cross-deployment flow analysis identifying shared infrastructure components and tracing compositional paths spanning deployments. Adversarial testing of cross-deployment exposure.

## Zero-click and asynchronous-processing controls

### ZC-01: Asynchronous-processing risk gating — Partially present

**Gap.** The deployment processes claim submissions in a queue-driven asynchronous workflow. Outbound tool invocations triggered by submission content are not gated against documented threat scenarios for zero-click exfiltration. Auto-approval is the most consequential ungated outbound action.

**Operational consequence.** Manipulation of the agent's reasoning over claim submission content can produce ungated outbound actions, including auto-approved payment instructions.

**Remediation.** Implement runtime policy gates on outbound tool invocations triggered by claim submission content. Policies should derive from documented threat scenarios including the patterns surfaced in §3.2.5 of the position paper.

### ZC-02: Content-source provenance preservation — Absent

**Gap.** Recommendation drafts to human adjusters do not preserve the provenance of source documents influencing the recommendation in a form that cannot be suppressed by content within the agent's reasoning context. Adjusters have no automatic mechanism to trace a recommendation back to the specific evidentiary basis the agent used.

**Operational consequence.** A reference-mention bypass — analogous to EchoLeak's pattern — that suppresses source attribution would prevent adjusters from verifying the recommendation's evidentiary basis. Even in the absence of attack, adjusters cannot efficiently audit the recommendation's reasoning chain.

**Remediation.** Implement provenance-preservation infrastructure that operates outside the agent's content-generation path; sources and the agent's reasoning over them are recorded by orchestration-layer logic and surfaced to adjusters regardless of the agent's output content.

## Memory and context controls

### MC-01: Retrieval-context integrity — Absent

**Gap.** Vector-store writes occur under orchestration-layer discipline only. Indexing-pipeline writes are not authenticated against a separate integrity authority; retrieval queries are not scoped to authorised indices through a separate access control beyond the orchestration layer's own logic.

**Operational consequence.** A compromise of the orchestration layer or of the agent's reasoning that produced a vector-store write could result in poisoned content propagating to subsequent sessions undetected.

**Remediation.** Establish separate privilege classes for the indexing pipeline, the retrieval pipeline, and the agent's reasoning over retrieved content. Authenticate indexing-pipeline writes against an integrity authority distinct from the agent. Log retrieval queries with provenance.

### MC-02: Memory-poisoning detection and response — Absent

**Gap.** No memory-poisoning detection is in place. The vector store is not subject to integrity scanning, behavioural anomaly detection, or content-pattern monitoring.

**Operational consequence.** Memory poisoning, once introduced, propagates without detection until behavioural drift becomes apparent at aggregate level. The detection horizon is potentially measured in months.

**Remediation.** Implement detection mechanisms for content suggesting injection in the vector store. Documented response procedures triggered by detection — including content removal, affected-session identification, and post-removal behavioural recalibration.

## Resource overload controls

### RO-01: Resource-consumption limits — Partially present

**Gap.** Per-session token budgets are configured at the orchestration layer. Foundation-model API rate limiting is vendor-imposed. Cross-deployment resource sharing has no documented degradation behaviour.

**Operational consequence.** Most overload scenarios produce graceful degradation; cross-deployment overload could produce undocumented behaviour in one or both affected deployments.

**Remediation.** Document degradation behaviour across the deployment's component inventory, including cross-deployment scenarios. Test that limit-triggered degradation does not produce security-control bypasses.

## Evidence-capture controls

### AT-01: Runtime evidence capture — Partially present

**Gap.** Captured evidence is sufficient to reconstruct tool invocations and their responses but is not structured to support reconstruction of the agent's reasoning context — specifically, the assembled prompt the model received at each invocation, including the retrieved vector-store content. The orchestration logs note *that* retrieval occurred but do not preserve *what* was retrieved.

**Operational consequence.** After-the-fact reconstruction of any specific recommendation can establish what the agent did but not why the model produced the recommendation it did. This is the configuration's most consequential evidence gap.

**Remediation.** Expand runtime capture to include the assembled prompt the model received at each invocation, retrieved context, the tool definitions available, the model's reasoning trace where available, and the egress request made on response render. Capture must be data-minimised, access-controlled, encrypted, retention-governed, and privacy-reviewed under GDPR Article 25.

### AT-02: Evidence-capture privacy controls — Partially present

**Gap.** The institution has GDPR-compliant data handling discipline at organisational level. Evidence-capture infrastructure as a discrete privacy concern has not been subjected to specific privacy-impact assessment.

**Operational consequence.** Expanded evidence capture (per AT-01 remediation above) would amplify the privacy attack surface; the existing discipline is sufficient for current capture but not for the expanded capture the methodology recommends.

**Remediation.** Conduct privacy-impact assessment of the evidence-capture infrastructure, particularly anticipating the expansion required by AT-01. Implement data-minimisation, access-control, encryption, retention-governance, and redaction mechanisms with privacy-relevant content classes excludable by design.

### AT-03: Evidence-store reconstruction queryability — Absent

**Gap.** Existing logs are stored in formats that support per-system queries but do not support cross-system reconstruction queries. A reconstruction query for "what did the agent see when processing claim X" requires custom code to assemble logs from MCP-server logs, orchestration logs, foundation-model API logs, and database audit logs.

**Operational consequence.** Reconstruction queries during incident response or supervisory dialogue require custom engineering work each time. The latency between question and answer is high; the cost of asking the question is correspondingly high.

**Remediation.** Establish a query layer over the evidence store that supports the standard reconstruction-query patterns (per-session, per-output, per-network-anomaly, per-input-pattern) without custom code per query type.

## Supervisory readiness controls

### HC-01: Supervisory-engagement repository — Absent

**Gap.** The deployment's documentation is distributed across multiple systems: deployment design documents in the IT portfolio, change-control records in the change-management system, threat-model documents in the risk function, audit logs across multiple systems. No consolidated repository exists for supervisory engagement.

**Operational consequence.** Supervisory inquiries require translation work to produce. The institution cannot, on supervisory request, produce the documentation relevant to any specific obligation under any specific regulatory regime without engineering effort.

**Remediation.** Establish a consolidated supervisory-engagement repository for the deployment, structured to support supervisor-engageable retrieval. Inventory record, regulatory mapping, accountability documentation, threat register, gap analysis (this document), toxic-flow analysis, adversarial testing results, implemented control documentation, residual-risk acceptance, and runtime evidence supporting each control's operation.

### HC-02: Second-line review cadence — Partially present

**Gap.** The deployment is reviewed by second-line risk functions on the institution's general AI-deployment review cadence. Specific cadence proportional to the deployment's risk classification is not documented.

**Operational consequence.** The cadence is uniform across deployments rather than calibrated to risk profile. Higher-risk deployments do not receive the additional scrutiny their classification would warrant.

**Remediation.** Document review cadence per deployment risk classification. Implement quarterly review for high-risk deployments (which this configuration is, given the trifecta and principal-model gaps).

## Governance-process controls

### GP-01: Deployment authorisation — Partially present

**Gap.** The deployment was authorised through the institution's general IT-deployment authorisation process. The authorisation record references the deployment's intended function and accountable executive but does not specifically document the deployment's principal model, threat surface, and compensating controls in the form GP-01 requires.

**Operational consequence.** The authorisation record does not establish that the authorising executive considered the principal-model gap, the trifecta configuration, or the auto-approval threshold's specific risk profile at the point of authorisation.

**Remediation.** Re-authorisation under the methodology's GP-01 form, with the authorisation record explicitly addressing principal model, threat surface, accountable executive, and references to completion of preconditions (LT-01, TF-01, the relevant additional controls).

### GP-02: Adversarial testing programme — Partially present

**Gap.** Quarterly red-team exercises are conducted on the deployment. The exercises are calibrated to general security-testing scope rather than to the specific threat patterns the methodology identifies (indirect prompt injection, tool poisoning, zero-click exfiltration, lethal-trifecta exploitation).

**Operational consequence.** The red-team exercises produce findings in their current scope but do not exercise the methodology's specific threat patterns systematically.

**Remediation.** Calibrate the adversarial testing programme to the methodology's threat-pattern coverage. Where the institution falls within DORA TLPT scope, align with the threat-led penetration testing regime.

### GP-03: Methodology revision and learning — Absent

**Gap.** The institution does not currently track its agent assurance methodology against the published methodology version. The institution's controls are derived from internal frameworks rather than from the synthesis methodology this gap analysis applies.

**Operational consequence.** The institution's methodology will not benefit from revisions to the synthesis methodology, supervisory communications shaping the field, or engagement findings from comparable deployments.

**Remediation.** Establish a revision tracking mechanism. The institution's adoption of the synthesis methodology (which this gap analysis presumes) is the precondition for the revision tracking; this remediation is downstream of the institution's decision to adopt.

## Inter-agent and cascading controls

### IC-01: Inter-agent message authentication — Not applicable in current configuration

**Gap.** The deployment does not currently implement direct agent-to-agent communication. The shared infrastructure with other internal agents (foundation-model API, orchestration framework, evidence-capture infrastructure) is shared resource access rather than inter-agent communication.

**Operational consequence.** No direct exposure to inter-agent communication risks in current configuration. Future evolution of the deployment toward multi-agent architecture would introduce IC-01 as an applicable control.

**Remediation.** None in current configuration. Re-evaluate if multi-agent architecture is introduced.

### CF-01: Failure-domain isolation — Partially present

**Gap.** Foundation-model API redundancy is vendor-side. Orchestration-layer retry logic handles transient errors. Cross-deployment failure scenarios — where one of the institution's internal agents fails or is compromised in ways that affect the others — are not characterised.

**Operational consequence.** Cross-deployment cascade paths are present but not analysed. A compromise of any of the three internal agents could propagate through shared infrastructure into the others in ways that have not been considered.

**Remediation.** Failure-mode testing across the deployment's component inventory. Tabletop exercises simulating cross-deployment compromise.

## Rogue-agent controls

### RA-01: Agent-behaviour drift detection — Absent

**Gap.** No baseline behavioural characterisation has been documented. No drift-detection mechanism is in place. The deployment's six months of production operation produces a body of operational data from which a baseline could be derived, but the derivation has not occurred.

**Operational consequence.** Behavioural drift attributable to memory poisoning, sustained injection campaigns, or model-behaviour evolution would not be detected until it produced specific anomalies surfacing through outcome monitoring at aggregate level. The drift's cumulative effect could be material before any specific anomaly surfaces.

**Remediation.** Document baseline behavioural characterisation from the deployment's six-month operational history. Implement drift-detection mechanism calibrated to distinguish legitimate behavioural evolution from anomalous drift. Document response procedures including rate-limiting, scope-narrowing, isolation, and decommissioning.

## Aggregate gap assessment

Of the 26 controls in the matrix, the deployment has zero in fully-Present state. Twelve are Partially present (TP-02, TP-03, IA-02, IA-03, ZC-01, RO-01, AT-01, AT-02, HC-02, GP-01, GP-02, CF-01).

Thirteen are Absent (TP-01, IA-01, LT-01, LT-02, TF-01, TF-02, ZC-02, MC-01, MC-02, AT-03, HC-01, GP-03, RA-01). The components of partially-present controls that fall short of substantive requirements compound the absent set without adding to its count.

One (IC-01) is not applicable in current configuration.

The aggregate gap is substantial but is consistent with the deployment's characterisation as a stress case representative of patterns observable in the market. The methodology's value at this configuration is the systematic surfacing of the gaps; the institution's response to the gaps — which to remediate, in what order, with what compensating controls in the interim — is operational decision-making the methodology supports rather than substitutes for.

## Priority remediation guidance

The methodology does not specify priority order; remediation prioritisation is properly the institution's decision based on risk appetite, operational constraints, and regulatory exposure. The following observations may inform prioritisation:

The principal-model gap (IA-01) is the deployment's structural authority gap and underlies the lethal-trifecta and toxic-flow patterns. Remediation here reduces residual risk across multiple controls.

The runtime evidence-capture gap (AT-01) is the precondition for after-the-fact analysis of any specific incident, including incidents that will inevitably occur at this deployment. Remediation here is foundational for the methodology's evidence-first principle to operate.

The auto-approval-threshold gap (component of IA-03) is the deployment's most consequential authentication gap, removing human-in-the-loop verification for 60% of claims by volume. Remediation is operationally complex but high-leverage.

The lethal-trifecta and toxic-flow analysis gaps (LT-01, TF-01) are the methodology's flagship analytical exercises. Their absence is the most visible gap to a serious second-line or supervisory reviewer.

The supervisory-engagement repository gap (HC-01) is the gap that materialises the absence of all the others when supervisory inquiry occurs. Even where individual controls remain absent, a documented repository establishes that the institution has thought systematically about the configuration's risks.

These five remediations together would move the deployment from its current configuration to one substantially closer to the methodology's recommended target state, addressing the highest-leverage subset of the absent and partially-present controls.
