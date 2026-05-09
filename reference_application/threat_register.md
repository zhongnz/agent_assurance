# Threat register — claims-processing agent reference deployment

*Structured threat enumeration produced by the synthesis methodology applied to the deployment specified in `deployment_specification.md`. The register is organised by OWASP Top 10 for Agentic Applications categories as the consensus ground-truth taxonomy, supplemented by the cross-cutting threat patterns from §3.2 of the position paper. Each threat is paired with the deployment-specific configuration that creates exposure, the severity classification, and the evidence requirements the methodology's evidence-first principle imposes.*

## Conventions

Severity classifications follow a four-tier scale: *Critical* (high likelihood of exploitation, high consequence, no compensating controls in current configuration); *High* (moderate likelihood of exploitation or high consequence with insufficient compensating controls); *Medium* (lower likelihood of exploitation, or sufficient compensating controls reducing residual risk); *Low* (theoretical exposure with sufficient mitigation in current configuration).

Each threat references the relevant control(s) from the matrix at `paper/control_matrix.md` that the methodology recommends for treatment. Where multiple controls apply in combination, all are listed.

## OWASP-category threats

### ASI01: Agent Goal Hijack — High severity

**Threat.** Incoming claim submissions are untrusted input the agent processes without the requesting customer's prior authorisation of any specific action. Submissions could include embedded instructions intended to manipulate the agent's reasoning — directing recommendation outcomes, exfiltrating data through the recommendation text, or invoking tools outside the claim's intended scope.

**Configuration exposure.** All seven of the deployment's tool integrations process content that may have originated from claim submissions, either directly (claim text fields, uploaded documents parsed via the document-parsing MCP server) or indirectly (vehicle-data lookups based on claim-submitted vehicle identifiers). The auto-approval threshold compounds the exposure: successfully manipulated low-value claims produce payment instructions without human review.

**Compensating controls in current configuration.** None specifically targeting this threat. The auto-approval threshold is calibrated for cost-impact rather than for goal-hijack mitigation.

**Evidence requirements.** Runtime capture of the assembled prompt the model received at each invocation, including retrieved context and tool outputs that informed the agent's recommendation. Without this evidence, post-incident reconstruction of whether goal hijack occurred at any specific recommendation is impossible.

**Recommended controls.** ZC-01 (asynchronous-processing risk gating), LT-01 (lethal-trifecta architectural review), AT-01 (runtime evidence capture).

### ASI02: Tool Misuse — Medium severity

**Threat.** The agent's tool inventory includes write-capable tools (claims-status updates, payment instruction submission for auto-approved claims, recommendation drafts) that could be invoked outside their intended scope through manipulated reasoning or compositional exploitation.

**Configuration exposure.** The claims-database MCP server's write access to claims-status updates is the most consequential write capability. Payment instruction submission is downstream of recommendation auto-approval rather than directly invoked by the agent, which provides an architectural break that limits direct exposure but does not eliminate it.

**Compensating controls in current configuration.** Per-tool input validation at MCP-server level for the first-party servers; vendor-supplied servers' input validation per vendor specifications; community-maintained servers' input validation cannot be relied upon.

**Evidence requirements.** Per-tool-invocation logs with full input and response capture. Existing logs satisfy this requirement at MCP-server level; orchestration-layer logs are sufficient for first-party-server invocations and must be supplemented for community-server invocations.

**Recommended controls.** TP-01 (tool metadata integrity), TP-02 (third-party MCP server qualification), TF-01 (toxic-flow analysis).

### ASI03: Identity & Privilege Abuse — High severity

**Threat.** The service-account principal model creates an authority gap between the agent's effective authority (broad: read access across all customer records) and the requesting customer's authority (narrow: limited to their own records). Manipulation of the agent's reasoning context can exploit the gap to retrieve records the requesting customer is not authorised to see.

**Configuration exposure.** Every customer interaction with the agent inherits the same service-account authority. The orchestration layer's prompts attempt to constrain the agent's behaviour to retrieving only the requesting customer's records, but the architectural authority is unconstrained. The General Analysis Supabase/Cursor disclosure of July 2025 demonstrated this pattern in a comparable architecture.

**Compensating controls in current configuration.** Orchestration-layer prompts encouraging the agent to scope retrieval to the requesting customer's records.

**Evidence requirements.** Per-invocation logs of database queries with the customer-identity context the agent's reasoning was conditioned on; cross-reference of retrieved records against the requesting customer's identity at audit time.

**Recommended controls.** IA-01 (principal propagation through tool chains), IA-02 (service-account authority limitation), IA-03 (authentication strength for high-authority actions).

### ASI04: Agentic Supply Chain Vulnerabilities — High severity

**Threat.** Two vendor-supplied and two community-maintained MCP servers expand the deployment's supply-chain attack surface. Vendor servers' security posture depends on contractual obligations; community-maintained servers' security posture depends on the maintainers' discipline, which the institution cannot verify through any contractual mechanism.

**Configuration exposure.** Tool metadata from any of the four non-first-party servers is consumed at session initialisation. A metadata-poisoning attack on either community-maintained server could manipulate the agent's reasoning across all sessions in which the affected tool is consulted. The MCPTox benchmark documented this pattern's exploitability across MCP-integrated configurations.

**Compensating controls in current configuration.** Vendor servers operate under contractual obligations; community-maintained servers carry no such obligations. No tool metadata integrity verification is in place at session initialisation.

**Evidence requirements.** Per-session capture of tool metadata hashes against an internal registry of approved tool definitions; alerting on hash mismatches.

**Recommended controls.** TP-01 (tool metadata integrity), TP-02 (third-party MCP server qualification), TP-03 (first-party tool change control), TF-01 (toxic-flow analysis).

### ASI05: Resource Overload — Low severity

**Threat.** Adversarial submissions could attempt to exhaust agent resources — tokens, retrieval-store quota, foundation-model API rate limits — to deny service or to force degraded operating modes that bypass security controls.

**Configuration exposure.** Per-session token budgets are configured at the orchestration layer; foundation-model API rate limits are vendor-imposed; retrieval-store quota is generously provisioned. Cross-deployment resource sharing introduces additional exposure: overload in the customer-service triage agent could affect the claims-processing agent.

**Compensating controls in current configuration.** Per-session token budgets; orchestration-layer timeout configuration; foundation-model API's own rate limiting.

**Evidence requirements.** Resource-consumption logs per session; rate-limit alerts; degradation-mode triggers and their consequences.

**Recommended controls.** RO-01 (resource-consumption limits and degradation behaviour), CF-01 (failure-domain isolation).

### ASI06: Memory & Context Poisoning — High severity

**Threat.** The vector store of past claim summaries introduces content the agent's earlier reasoning produced into current reasoning context. If the agent's earlier reasoning was manipulated (through goal hijack at any past session), the resulting summary is poisoned, and the poison propagates forward into reasoning over related claims.

**Configuration exposure.** Vector-store retrieval at session initialisation pulls in summaries of past claims from the same customer, similar claims, and claims with similar fact patterns. A successful goal-hijack attack at one session can shape the agent's reasoning across many subsequent sessions over related claims. The latent nature of memory poisoning makes it particularly difficult to detect — the agent's reasoning over poisoned context produces plausible-looking outputs.

**Compensating controls in current configuration.** None specifically targeting this threat. Vector-store writes occur under orchestration-layer discipline only.

**Evidence requirements.** Vector-store write logs with provenance per entry; periodic integrity scanning of stored summaries against current ground-truth claim records; behavioural-baseline monitoring to detect drift attributable to memory poisoning.

**Recommended controls.** MC-01 (retrieval-context integrity), MC-02 (memory-poisoning detection and response), RA-01 (agent-behaviour drift detection).

### ASI07: Insecure Inter-Agent Communication — Medium severity

**Threat.** The deployment shares foundation-model API access, orchestration-framework infrastructure, and parts of the evidence-capture infrastructure with two other internal agent deployments. Cross-deployment communication paths are present but not analysed in current configuration.

**Configuration exposure.** Indirect exposure rather than direct: the claims agent does not directly communicate with the customer-service triage agent or the internal-operations workflow agent. However, shared retrieval stores and shared evidence-capture infrastructure create paths through which one agent's outputs could reach another's reasoning context, by design or by exploitation.

**Compensating controls in current configuration.** Logical separation between deployment configurations at orchestration layer; no shared agent-to-agent message channels by design.

**Evidence requirements.** Cross-deployment infrastructure inventory; identification of any shared state or shared reasoning context across deployments; adversarial testing of cross-deployment exposure.

**Recommended controls.** IC-01 (inter-agent message authentication and policy enforcement), TF-02 (cross-deployment flow review).

### ASI08: Cascading Failures — Medium severity

**Threat.** A failure or compromise in any single component (foundation-model API unavailability, MCP-server outage, retrieval-store corruption, evidence-capture interruption) could cascade through the deployment, producing operational disruption or security-control bypasses.

**Configuration exposure.** Foundation-model API unavailability would halt the deployment; MCP-server outages produce per-server functional gaps but the agent's behaviour under partial tool unavailability is not characterised; retrieval-store corruption would propagate poisoned content; evidence-capture interruption would create blind spots in post-incident reconstruction. Cross-deployment cascade paths through shared infrastructure are present.

**Compensating controls in current configuration.** Foundation-model API has vendor-side redundancy; orchestration layer has retry logic; MCP-server outages produce graceful errors. No documented degradation behaviour for partial failures or for evidence-capture interruption.

**Evidence requirements.** Failure-mode test reports across the deployment's component inventory; cascade-prevention control specifications; tabletop exercise reports for cross-deployment cascade scenarios.

**Recommended controls.** CF-01 (failure-domain isolation and cascade prevention), RO-01 (resource-consumption limits and degradation behaviour).

### ASI09: Human-Agent Trust Exploitation — High severity

**Threat.** The agent's recommendations to human adjusters (for claims above €2,500 or with risk flags) influence human decisions. A manipulated recommendation that appears confident, well-reasoned, and properly evidenced could lead an adjuster to accept it without independent verification. For auto-approved claims, no human review occurs at all.

**Configuration exposure.** The auto-approval threshold removes human-in-the-loop verification for 60% of claims by volume. For claims above the threshold, the recommendation's persuasive form influences the adjuster's verification depth. A reference-mention bypass — analogous to the EchoLeak attack pattern — that suppresses the agent's source attribution would prevent adjusters from tracing the recommendation back to its evidentiary basis.

**Compensating controls in current configuration.** Adjuster training on AI-supported decision-making; institutional policy on adjuster review depth for AI-recommended claims.

**Evidence requirements.** Per-recommendation provenance preservation that cannot be suppressed by content within the agent's reasoning context; adjuster decision logs distinguishing AI-recommended outcomes from adjuster-modified outcomes.

**Recommended controls.** ZC-02 (content-source provenance preservation), AT-01 (runtime evidence capture), RA-01 (agent-behaviour drift detection), IA-03 (authentication strength for high-authority actions).

### ASI10: Rogue Agents — Medium severity

**Threat.** Sustained injection campaigns, undetected memory poisoning, or behavioural drift over time could produce an agent whose actions deviate materially from baseline expected behaviour without triggering any specific incident detection. The drift's cumulative effect could be material before any specific anomaly surfaces.

**Configuration exposure.** No behavioural-drift detection is in place. Foundation-model behaviour is presumed stable across the deployment period; the model is pinned to a specific version, but the prompt construction and retrieved context evolve continuously and could carry drift not attributable to model changes.

**Compensating controls in current configuration.** Quarterly red-team exercises; informal review of agent recommendations sampled by adjusters; outcome monitoring at aggregate level.

**Evidence requirements.** Baseline behavioural characterisation; ongoing behavioural-drift monitoring with documented alerting thresholds; response procedures including rate-limiting, scope-narrowing, isolation, and decommissioning.

**Recommended controls.** RA-01 (agent-behaviour drift detection and response), MC-02 (memory-poisoning detection), GP-02 (adversarial testing programme).

## Cross-cutting threat patterns

### Lethal trifecta — Critical severity

**Pattern.** The deployment exhibits all three capabilities the lethal trifecta names: sensitive data access (broad read access to policy, claims, customer records via service-account credentials); exposure to untrusted input (claim submissions, document content, vehicle-data registry results, fraud-detection scoring inputs); egress capability (recommendation drafts that are routed to adjusters; payment instructions for auto-approved claims; claims-status updates communicated to customers).

**Pattern realisation.** The compositional path runs from claim submission (untrusted input) → retrieval over claims/customer/policy databases (privileged data access) → recommendation drafting (egress through adjuster routing or payment instruction submission). Each component is individually defensible; the composition is the threat.

**Severity rationale.** Critical because no compensating control specifically addresses the compositional risk; the auto-approval threshold compounds the egress channel by removing human-in-the-loop verification for 60% of claims by volume.

**Recommended controls.** LT-01 (lethal trifecta architectural review), LT-02 (egress-channel inventory and control), TF-01 (toxic-flow analysis).

### Toxic flows — High severity

**Pattern.** The deployment's tool inventory contains multiple compositional paths from untrusted-input nodes through privileged-data-access nodes to egress nodes. The path realised by the lethal-trifecta pattern above is the most direct, but is not unique. Other paths include: customer-uploaded document → document-parsing community MCP server (untrusted output) → fraud-detection scoring (privileged inference) → recommendation. Or: customer-submitted vehicle identifier → vehicle-data registry community MCP server (untrusted output) → repair-shop estimate vendor MCP (privileged inference using attacker-influenced input) → recommendation.

**Severity rationale.** High because multiple distinct compositional paths exist, each individually defensible at component level. Static toxic-flow analysis would surface the paths systematically; the deployment has not undergone such analysis.

**Recommended controls.** TF-01 (toxic-flow analysis), TF-02 (cross-deployment flow review), LT-02 (egress-channel inventory and control).

### Zero-click exfiltration — Medium severity

**Pattern.** The deployment's processing of incoming claim submissions exhibits the asynchronous-processing property in attenuated form. Claim submissions arrive without explicit user action at the moment of agent processing; the agent processes claims in a queue-driven workflow rather than in real-time response to user prompts. Unlike EchoLeak, the user (the customer) is not in the loop at the moment of action — the customer submits the claim and waits for outcome — but neither is an attacker indirectly influencing a non-attacker user.

**Pattern realisation.** Less direct than EchoLeak's mailbox-indexing case but structurally analogous: untrusted content (claim submission) is processed asynchronously by an agent with broad authority over the institution's records, with no user-in-the-loop verification of the processing. Auto-approval extends the exposure: the action (payment instruction) executes without human review.

**Severity rationale.** Medium rather than High because the customer is the direct submitter and benefits from successful processing, reducing the attacker-tractable scenarios; an attacker would need to be either the customer themselves (claims fraud, an established threat with existing controls) or a third party submitting claims under another's identity (impersonation, which has authentication controls upstream of the agent).

**Recommended controls.** ZC-01 (asynchronous-processing risk gating), ZC-02 (content-source provenance preservation), AT-01 (runtime evidence capture).

### Memory and context poisoning — High severity

**Pattern.** The vector store of past claim summaries introduces persistent state that propagates across sessions. Manipulation at one session affects reasoning over subsequent sessions, with the propagation visible only through behavioural drift over time.

**Severity rationale.** High because the latent nature of the threat makes detection difficult and the propagation horizon long; a single successful manipulation could shape reasoning over related claims for months before behavioural drift becomes apparent.

**Recommended controls.** MC-01 (retrieval-context integrity), MC-02 (memory-poisoning detection and response), RA-01 (agent-behaviour drift detection).

## Aggregate severity assessment

Two threats are classified Critical (lethal trifecta as cross-cutting pattern). Six are High (ASI01, ASI03, ASI04, ASI06, ASI09; toxic flows; memory and context poisoning). Five are Medium (ASI02, ASI07, ASI08, ASI10; zero-click exfiltration). One is Low (ASI05).

The classification reflects the deployment's deliberate calibration as a stress case rather than a recommendation. A more conservative deployment configuration — first-party MCP servers only, principal propagation through tool chains, no auto-approval, supervised vector-store writes — would substantially reduce the residual risk profile. The methodology's value at deployments with conservative configurations is the discipline of treating residual risk explicitly even where its severity is lower; the deployment described here surfaces the methodology's analytical content most fully.

## Evidence-requirements summary

Across the threats enumerated above, the deployment requires substantial expansion of its evidence-capture posture to support the methodology's evidence-first principle. Specifically:

- Runtime capture of the assembled prompt the model received at each invocation, including retrieved vector-store content and tool-output content (currently absent).
- Per-session capture of tool metadata hashes against an internal registry of approved tool definitions (currently absent).
- Vector-store write logs with provenance per entry (partially captured at orchestration layer).
- Behavioural-drift monitoring against a documented baseline (currently absent).
- Per-recommendation provenance preservation that cannot be suppressed by content within the agent's reasoning context (currently absent).
- Failure-mode and cascade-prevention test reports (currently absent).

The aggregate gap between current evidence posture and methodology-required evidence posture is the most consequential operational finding from this register. The findings document `findings/at_01_01_evidence_capture.md` (where present) elaborates this gap into an engagement-style finding.

The methodology's recommendation is not that all of the above evidence be captured uniformly. The evidence-first principle requires designed capture, with privacy properties documented and assured under GDPR Article 25. The institution's specific data-protection posture, retention policies, and operational constraints will shape which evidence is captured at what granularity.
