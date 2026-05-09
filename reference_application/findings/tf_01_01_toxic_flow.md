# Finding TF-01-01: Toxic-flow analysis not performed; compositional paths uncharacterised

*Engagement-style finding produced by the synthesis methodology applied to the reference deployment specified in `deployment_specification.md`. The finding addresses the deployment's failure to perform static toxic-flow analysis of its authorised tool inventory, with the consequence that compositional paths from untrusted-input nodes through privileged-data-access nodes to egress nodes are not enumerated, classified, or governed.*

## Severity and classification

**Severity: High.**

**Regulatory anchors.** AI Act Article 15 (cybersecurity) — *Indirect*; AI Act Article 11 (technical documentation) — *Analogical*; DORA Article 25 (digital operational resilience testing) — *Indirect*; DORA Article 5 (ICT risk) — *Indirect*.

**OWASP ASI references.** ASI02 (Tool Misuse) + ASI04 (Agentic Supply Chain Vulnerabilities), in compositional reference.

**Cross-cutting patterns.** Toxic flows directly; lethal trifecta where the compositional paths realise the trifecta's pattern; identity and privilege abuse where compositional paths exploit the principal-propagation gap.

**Methodology controls implicated.** TF-01 (toxic-flow analysis of authorised tool inventory); TF-02 (cross-deployment flow review); LT-01 (lethal-trifecta architectural review); LT-02 (egress-channel inventory and control).

## The methodology gap

The methodology's TF-01 control requires static toxic-flow analysis of the agent's authorised tool inventory before production deployment, identifying paths from untrusted-input nodes through privileged-data-access nodes to egress nodes. Identified flows must be reviewed against deployment configurations and either remediated, gated by compensating controls, or accepted as residual risk by an accountable executive.

The reference deployment has not undergone toxic-flow analysis. The deployment's tool-invocation patterns have been considered at component level — each MCP server's individual access scope, each tool's individual input validation, each output's individual handling — but the compositional patterns through which sequences of tool invocations can produce attack paths have not been enumerated.

The omission is consequential because the threats the analysis surfaces are specifically the threats that per-component analysis cannot surface. A toxic-flow analysis is not a substitute for per-component review; it is complementary to it, addressing the layer at which composition produces emergent attack surfaces individual components cannot.

## Compositional paths in the reference deployment

A complete toxic-flow analysis of the deployment is the work the TF-01 remediation requires. This finding does not substitute for that work; it surfaces representative paths that the analysis would enumerate, demonstrating the analysis's value and the scope of risk currently uncharacterised.

**Path 1: Direct lethal-trifecta path.** Claim submission (untrusted-input source, indexed at intake) → orchestration-layer prompt construction including submission content (composing untrusted-input with the agent's reasoning) → policy-administration MCP server retrieval (privileged-data access via service account) → recommendation drafting incorporating retrieved content (egress through adjuster routing or auto-approval payment instruction). The path is direct; each component is permitted; the composition is the trifecta's realisation in this deployment. This path is the focus of the LT-01-01 finding.

**Path 2: Vehicle-data registry compositional path.** Claim submission (untrusted) → vehicle-data registry MCP server lookup using submission-derived identifiers (community-maintained server, output integrity not verified) → repair-shop estimate MCP server invocation using vehicle-data output (vendor-supplied server, but operating on attacker-influenced input) → recommendation drafting incorporating estimate (egress). The path traverses a community-maintained server and a vendor-supplied server in sequence; the community server's outputs influence the vendor server's inputs; manipulation at the community server propagates through the vendor server into the recommendation. This path is unique to the deployment's mixed-server configuration.

**Path 3: Document-parsing compositional path.** Customer-uploaded document (untrusted, particularly when the document is not authored by the customer themselves — e.g., a third-party repair estimate or medical report) → document-parsing community MCP server (community-maintained, parsing logic not verified) → orchestration-layer assembly of parsed content into reasoning context (composing untrusted-output with retrieved customer records) → recommendation drafting (egress). The path is structurally similar to EchoLeak's pattern: an untrusted document's content reaches the agent's reasoning context through a tool that processes the document.

**Path 4: Memory-poisoning compositional path.** Past claim submission containing manipulated content → orchestration-layer summary writing to vector store (the manipulated content shapes the agent's earlier reasoning, which shapes the summary) → vector-store retrieval at subsequent session (the poisoned summary enters reasoning context for an unrelated claim) → recommendation drafting at the subsequent session (egress, on a claim not directly involving the original submission). The path operates across sessions and across customers; the poisoning's propagation horizon is the vector store's retention period.

**Path 5: Cross-deployment compositional path.** Customer interaction with the customer-service triage agent (one of the institution's other internal agents) → triage agent's evidence-capture writes to shared infrastructure → claims-processing agent's evidence-capture infrastructure receives the writes (no separation between deployments at evidence layer) → claims-processing agent's reasoning context potentially reads cross-deployment evidence at session initialisation. The path's realisation depends on specific evidence-capture architecture; whether the path is exploitable depends on configuration not yet specified at deployment.

These five paths are illustrative rather than exhaustive. A complete toxic-flow analysis would enumerate substantially more, classify each by likelihood and consequence, and address each with remediation, gating, or explicit residual-risk acceptance.

## Operational consequences of the gap

In the absence of toxic-flow analysis, the deployment operates with three classes of operational consequence.

**Compositional risks are accepted by deployment authorisation rather than by explicit consideration.** Authorising executives have no documented inventory of compositional paths, no documented assumptions about which paths are mitigated by which controls, and no documented residual-risk acceptance. If a compositional-pattern incident occurs, the institution has no documentation of the risk having been considered.

**Per-component controls' effectiveness against compositional threats is not characterised.** The institution's existing controls — service-account access controls, MCP-server input validation, orchestration-layer prompts — were each designed against component-level threats. Their effectiveness against compositional threats is implicit rather than tested. Specifically, the institution does not know which of the existing controls degrade gracefully against compositional attacks and which fail.

**Vendor and community-MCP-server qualification cannot be calibrated to compositional risk.** The vendor-supplied servers and community-maintained servers contribute to compositional paths in ways the institution has not characterised. Qualification of vendors and community maintainers is therefore calibrated to component-level criteria (security posture, contractual obligations, change-management discipline) rather than to compositional-risk contribution. The two community-maintained servers' actual contribution to deployment risk is greater than their component-level qualification suggests.

## The pattern is documented in production

The toxic-flow pattern is well-evidenced in disclosed agent-security incidents. EchoLeak (CVE-2025-32711, June 2025) is the canonical case: five individual controls (XPIA classifier, link redaction, image redaction, Content Security Policy, reference-mention markers) each operated correctly, and the chain composing across them produced the exfiltration. AgentFlayer (Black Hat USA, 6 August 2025) demonstrated comparable patterns across multiple agent configurations. Shadow Escape (22 October 2025) demonstrated further variants. The methodology's case-study analysis of EchoLeak (`case_studies/echoleak.md`) treats the toxic-flow analysis as the methodology output most directly suited to catching such patterns prospectively.

The Snyk × Invariant Labs productisation (24 June 2025) of toxic-flow analysis (TF001 issue class in Snyk Agent Scan) provides commercial tooling for the analysis. The MCPTox benchmark (arXiv:2508.14925, August 2025) documents the metadata-poisoning surface that toxic-flow analysis surfaces structurally. The analysis is not theoretical; it is operationally available.

## Evidence reviewed

- The deployment's tool-inventory documentation (the seven MCP servers and their tool definitions).
- The deployment's threat-model document, dated at original deployment authorisation.
- Sample tool-invocation logs covering thirty days of production operation.
- Vendor MCP server contracts and security postures.
- Community-maintained MCP server documentation (publicly available).
- Cross-deployment infrastructure inventory at the institution's internal agent platform.

## Recommendation

**Recommended remediation.** Conduct static toxic-flow analysis of the deployment's authorised tool inventory using compositional-analysis tooling. Two implementation options:

1. **Snyk Agent Scan (TF001 issue class) or equivalent commercial tooling.** Where the institution's procurement and vendor-relationship policies permit, commercial tooling provides analysis that is calibrated to current attack patterns and updated as new patterns are documented.

2. **Equivalent in-house implementation.** Where commercial tooling is not feasible, in-house implementation using compositional-analysis logic against the MCP server inventory is feasible. The methodology's case study (`case_studies/echoleak.md`, section 4) describes the analysis approach in implementable terms.

The analysis's products:

1. **Identified flows.** Enumerated paths from untrusted-input nodes through privileged-data-access nodes to egress nodes, classified by node type and severity.

2. **Severity classifications.** Each flow classified as Critical, High, Medium, or Low based on likelihood and consequence.

3. **Remediation or compensating-control decisions.** Each flow either remediated (path eliminated through tool-inventory or architecture change), gated by compensating controls (path retained but mitigated), or accepted as residual risk by an accountable executive.

4. **Documented assumption set.** For gated flows, the assumptions on which the gating's effectiveness depends, identified explicitly.

5. **Re-analysis triggers.** Specification of what configuration changes trigger re-analysis (new MCP server, foundation-model change, principal-model change, etc.).

**Cross-deployment flow review.** The TF-02 control extends the analysis to compositional paths spanning the institution's multiple agent deployments. The work is downstream of the per-deployment TF-01 analysis but should not be deferred indefinitely; cross-deployment paths are a specific risk surface the per-deployment analysis cannot surface.

## Residual risk after recommendation

**Residual risk: Medium.**

The toxic-flow analysis surfaces compositional paths systematically; once surfaced, paths can be addressed through remediation, gating, or explicit acceptance. The analysis is therefore strongly leveraged: the analytical output substantially reduces residual risk by making implicit risk explicit.

The residual risk reflects three considerations.

The analysis is necessarily limited to paths discoverable through the analysis methodology. Paths involving novel compositions, paths exploiting model-behaviour properties not captured in the tool-graph abstraction, and paths emerging from runtime configurations not visible at static analysis time are out of the analysis's surface. The methodology's continuous-and-composable principle requires that the analysis is repeated as configurations change, but novel attack surfaces between analyses remain a residual exposure.

Compensating controls' effectiveness against gated flows depends on the assumptions identified in the analysis. Assumptions that prove false in adversarial conditions degrade the gating's effectiveness; the methodology's continuous-and-composable principle requires that the adversarial-testing programme (GP-02) probes the assumptions over time, but residual exposure between assumption-validity checks remains.

Cross-deployment paths surfaced by TF-02 may not be remediable through per-deployment changes alone; some require institution-level architectural decisions about evidence-capture infrastructure, foundation-model API access, or orchestration-framework deployment patterns. Remediation timelines for such paths are correspondingly longer.

## Ownership and accountability

**Designated accountable.** ICT risk function.

**First-line.** Deployment technical leadership for the tool-inventory specification; agent architecture team for the analysis's input gathering.

**Second-line.** ICT risk function for the analytical review and residual-risk acceptance; vendor-management function for tools sourced from third parties; CISO function for the security-architecture dimension.

**Cross-functional dependencies.** The analysis's output informs the LT-01 architectural review's compensating-control design; the timing of the two reviews should be coordinated.

## Implementation considerations

A toxic-flow analysis on a deployment of this scope is approximately one to two weeks of focused work for an analyst familiar with the deployment's architecture. The work is iterative — initial enumeration, refinement against deployment specifics, severity classification, remediation/gating decisions per flow.

The analysis's value is highest when conducted before changes (so changes can be designed around the analysis's findings). Conducted after deployment, as in this case, the analysis surfaces gaps that may have been avoidable with earlier analysis but remain addressable.

Re-analysis is required on material change to tool inventory or configuration. The same definition of "material" applies as in the LT-01 finding.

## Connection to other findings

This finding is closely connected to several others in the engagement output:

- **IA-01-01** (principal-propagation gap) is one of the architectural conditions the toxic-flow analysis surfaces in compositional paths. Path 1 (the direct trifecta path) and several others depend on the principal-propagation gap.
- **LT-01-01** (lethal trifecta) is the architectural-review counterpart to the toxic-flow analysis. The two findings are complementary: TF-01 surfaces compositional paths analytically, LT-01 reviews the trifecta configuration architecturally.
- **TP-02 finding** (third-party MCP server qualification) addresses the supply-chain dimension that contributes to compositional paths involving community-maintained servers.
- **ZC-02 finding** (content-source provenance preservation) addresses the human-trust-exploitation dimension of compositional paths reaching adjuster review.

The analysis's outputs feed into multiple downstream remediation efforts; the analysis is therefore one of the higher-leverage interventions in the engagement.

## A note on tooling availability

The methodology's claim that compositional analysis is operationally specifiable depends on tooling that did not exist before mid-2025. The Snyk × Invariant Labs productisation (June 2025) and the academic work on tool-poisoning detection (MCPTox, arXiv:2508.14925, August 2025) make the analysis tractable. Earlier analyses of comparable agent deployments would have required custom tooling per analysis. The current state is that commercial and academic tooling support the analysis at production scale; the methodology's recommendation is to use available tooling rather than to develop in-house capability where commercial options serve.

The institution's choice between commercial tooling and in-house implementation is a procurement and operational decision rather than a methodology decision. Either choice produces the analysis's substantive output.
