# Control Matrix v1.0

*Companion artifact to the position paper* Agent Assurance in Regulated Financial Services *(working title). Implements the synthesis methodology articulated in §4 of the paper as a populated control matrix covering the OWASP Top 10 for Agentic Applications categories, the cross-cutting threat patterns identified in §3.2, and the regulatory and standards architecture the methodology anchors to.*

## Status and scope

This is v1.0 of a living artifact. The matrix is preliminary in the sense that specific controls will be revised as the methodology is applied to live regulated production deployments and as the regulatory landscape evolves. The methodology's structural contribution — the column architecture, the derivation logic, the principle-to-control traceability, the regulatory cross-walking with mapping-strength labels — is stable; the specific control set will accrete and refine.

The matrix presents twenty-six controls mapping the OWASP Top 10 for Agentic Applications categories (ASI01–ASI10) — with ASI05 Unexpected Code Execution acknowledged as a coverage gap in v1.0 (see Coverage notes) — the five cross-cutting threat patterns of §3.2 (tool poisoning, identity and privilege abuse, the lethal trifecta, toxic flows, zero-click exfiltration), and additional control areas that the OWASP categories and the cross-cutting patterns alone do not fully address (memory and context poisoning, resource overload, evidence capture, supervisory-engagement readiness, inter-agent communication, cascading failures, behavioural drift).

Five of the twenty-six controls are reproduced from §4.3 of the paper, where they were presented as illustrative; the remaining twenty-one are introduced here for the first time. The full set is structured for use as input to assurance engagements rather than as a checklist; each control's threat referent, regulatory anchoring, and evidence specification are intended to support institutional decision-making rather than to substitute for it.

## Conventions

Each control specifies a statement, the OWASP categories and cross-cutting patterns it addresses, the regulatory anchors and standards references with explicit mapping-strength labels, the test procedure, the evidence artifact, the frequency of validation, and the ownership across the three lines of defence. Mapping-strength labels follow the convention introduced in §4.2 of the paper: *Direct* (the article addresses the control's subject specifically); *Indirect* (the article requires a broader category of work the control falls within); *Analogical* (the article addresses an analogous concern at a different layer); *Gap* (no specific anchor exists, and the absence is itself part of the methodology's contribution).

A note on AI Act Article 15 mapping. Article 15 names three qualities — accuracy, robustness, cybersecurity — that high-risk AI systems shall achieve in light of their intended purpose throughout the lifecycle. Controls that directly produce one of those qualities at the level of the quality (RO-01 robustness through availability; CF-01 robustness through fault tolerance; RA-01 robustness through behavioural consistency) cite Article 15 as *Direct*. Controls that implement a specific cybersecurity or robustness mechanism in service of Article 15's broader objectives (e.g. tool metadata integrity, principal propagation, retrieval-context integrity) cite Article 15 as *Indirect*. The labels reflect this distinction; alternative labellings are defensible.

Controls are numbered by the OWASP category or threat pattern they primarily respond to. The TP-, IA-, LT-, TF-, ZC- prefixes from the paper's §4.3 are preserved; new controls take prefixes by their primary OWASP category or substantive area (MC for Memory and Context, RO for Resource Overload, AT for Audit Trail, HC for Human Confidence and supervisory readiness, GP for Governance Process, IC for Inter-agent Communication, CF for Cascading Failures, RA for Rogue-Agent and behavioural drift). Numeric suffixes (e.g., TP-01, TP-02) distinguish multiple controls within the same prefix.

The matrix is structured for readability rather than for tooling ingestion; institutions implementing the methodology may convert the matrix to whatever data format their GRC tooling supports.

## Controls addressing tool-poisoning patterns

### TP-01: Tool metadata integrity verification

**Statement.** Tool metadata (descriptions, schemas, parameter definitions, output formats) consumed by the agent must be cryptographically pinned to a specific version and verified against an internal registry of approved tool definitions at session initialisation; modifications to tool metadata between session initialisations require re-approval before the modified metadata is consumed.

**OWASP ASI references.** ASI04 (Agentic Supply Chain Vulnerabilities); ASI02 (Tool Misuse).

**Cross-cutting patterns.** Tool poisoning (metadata layer).

**Regulatory anchors.** AI Act Article 15 (accuracy, robustness and cybersecurity) — *Indirect*; DORA Article 28 (general principles for ICT third-party risk management) — *Analogical*.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.2 (third-party relationships) — *Indirect*; NIST AI RMF Manage 2 (third-party AI systems) — *Indirect*.

**Test procedure.** At each session initialisation, the agent's MCP client computes a cryptographic hash of each consumed tool's metadata and verifies the hash against the internal registry. Hashes that do not match registered values cause session initialisation to fail with a documented exception. Periodic adversarial testing introduces metadata variants to verify the verification step operates.

**Evidence artifact.** Per-session log entry recording the hashes of all consumed tool metadata, with timestamps, registry versions, and verification outcomes.

**Frequency.** Per-session.

**Ownership.** First-line: agent operations team. Second-line: ICT risk function (third-party-supply-chain dimension); vendor-management function (vendor-MCP-server change-control). Joint with CISO function (cryptographic-pinning infrastructure). Designated accountable: ICT risk.

**Derivation.** From the *evidence-first* and *framework-anchored* principles. The control responds to the metadata-layer tool-poisoning pattern specifically. Tool-output content attacks are addressed elsewhere (LT-01, ZC-01).

---

### TP-02: Third-party MCP server qualification

**Statement.** MCP servers operated by third parties (vendors or community-maintained services) must be qualified through a documented process that assesses the server's operator, authentication and authorisation posture, change-management discipline, and security incident response history before the server is added to the institution's approved-tool registry.

**OWASP ASI references.** ASI04 (Agentic Supply Chain Vulnerabilities).

**Cross-cutting patterns.** Tool poisoning.

**Regulatory anchors.** DORA Article 28 (general principles for third-party risk management) — *Direct*; DORA Article 29 (preliminary assessment of ICT concentration risk and further sub-outsourcing arrangements) — *Direct* where the third-party MCP server qualifies under that article's scope; DORA Article 30 (key contractual provisions) — *Direct* for any contractual relationship with the third-party operator, with stricter requirements where the deployment supports critical or important functions.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.2 (third-party relationships) — *Direct*; NIST AI RMF Manage 2 — *Direct*.

**Test procedure.** Pre-onboarding qualification documents the third-party MCP server's operator entity, its security posture (authentication, encryption, access logs), its change-management process, and any disclosed security incidents. Re-qualification occurs annually or on material change.

**Evidence artifact.** Qualification document per third-party MCP server, with operator identity, security-posture assessment, contractual references where applicable, and qualification decision with explicit accountable executive.

**Frequency.** Pre-onboarding; annually thereafter; on material change.

**Ownership.** First-line: vendor-management function. Second-line: ICT risk function for qualification review. Designated accountable: ICT risk function.

**Derivation.** From the *framework-anchored* principle directly. The control extends the third-party-risk-management discipline DORA codifies for ICT third parties to MCP server providers specifically.

---

### TP-03: First-party tool change control

**Statement.** Tools and MCP servers operated internally must be subject to change control procedures specifying who may modify tool definitions, the testing and review required before changes propagate to production, and the audit-trail requirements for tool definition changes.

**OWASP ASI references.** ASI04 (Agentic Supply Chain Vulnerabilities); ASI02 (Tool Misuse).

**Cross-cutting patterns.** Tool poisoning (insider-risk variant).

**Regulatory anchors.** DORA Article 8 (ICT systems, protocols and tools) — *Indirect*; DORA Article 13 (learning and evolving) — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.2 (third-party relationships) — *Analogical* (the standard frames the discipline for third parties; the control extends to first-party tools); ISO/IEC 27001:2022 Annex A.8.32 (change management) — *Direct*; NIST AI RMF Manage 4 — *Indirect*.

**Test procedure.** Change-control records review demonstrates that tool definition changes follow the documented process. Random sampling of changed tools verifies that testing and review steps occurred prior to production propagation.

**Evidence artifact.** Change-control records for each tool definition change, including the requester, the reviewer, the testing record, and the production deployment record.

**Frequency.** Per-change for the change-control event; quarterly for sampling-based audit.

**Ownership.** First-line: agent operations team. Second-line: ICT risk function. Designated accountable: ICT risk function.

**Derivation.** From the *framework-anchored* and *composable and continuous* principles. Internal tools are not exempt from the discipline applied to third parties.

## Controls addressing identity and privilege patterns

### IA-01: Principal propagation through tool chains

**Statement.** Where the agent invokes tools that operate on principal-specific resources, the requesting principal's identity must be propagated through the tool chain such that downstream resource access is authorised against the requesting principal's authority rather than against the agent's authority. Where principal propagation is not architecturally possible, the agent must implement scope-narrowing controls that limit per-request authority to what the requesting principal could have requested directly.

**OWASP ASI references.** ASI03 (Identity & Privilege Abuse).

**Cross-cutting patterns.** Identity and privilege abuse.

**Regulatory anchors.** AI Act Article 14 (human oversight) — *Analogical*; AI Act Article 15 (cybersecurity) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.5.5 (information security) — *Indirect*; NIST AI RMF Manage (MP-5) — *Indirect*; NIST SP 800-207 (Zero Trust Architecture) — *Direct*.

**Test procedure.** Adversarial testing constructs requests in which the requesting principal lacks authority for the action the agent would otherwise be authorised to perform. Tests verify that the agent's response either propagates the requesting principal's identity to the downstream system or applies scope-narrowing logic. Tests are repeated across the deployment's full inventory of tool chains.

**Evidence artifact.** Per-tool-chain documentation of principal propagation mechanism (or scope-narrowing alternative), supplemented by adversarial test logs.

**Frequency.** Per-deployment for documentation; quarterly for adversarial testing.

**Ownership.** First-line: agent architecture and identity-management teams jointly. Second-line: ICT risk and operational risk for principal-model design; legal/privacy for personal-data implications. Designated accountable: CISO function.

**Derivation.** From the *principal-bound* and *evidence-first* principles. Implements the principle at the tool-chain layer.

---

### IA-02: Service-account authority limitation

**Statement.** Where the agent operates under a service account rather than under propagated principal identity, the service account's authority must be explicitly scoped to the minimum required for the agent's deployed function, with any expansion of service-account authority subject to documented review and approval.

**OWASP ASI references.** ASI03 (Identity & Privilege Abuse).

**Cross-cutting patterns.** Identity and privilege abuse (service-account variant).

**Regulatory anchors.** AI Act Article 15 (cybersecurity) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*.

**Standards references.** ISO/IEC 27001:2022 Annex A.5.15 (access control) — *Direct*; NIST SP 800-207 — *Direct*; ISO/IEC 42001:2023 Annex A.5.5 — *Indirect*.

**Test procedure.** Quarterly review of service-account authority scope against agent's operational requirements. Review identifies any authority granted that is not required for current function and either documents justification or removes the authority.

**Evidence artifact.** Service-account authority specification, justification for each authority element, and review records.

**Frequency.** Initial documentation per-deployment; quarterly review.

**Ownership.** First-line: identity-management team. Second-line: ICT risk function. Designated accountable: CISO function.

**Derivation.** From the *principal-bound* principle. Where principal-bound architecture is not feasible, the service-account fallback must be discipline-bounded.

---

### IA-03: Authentication strength for high-authority actions

**Statement.** Agent actions that produce high-consequence outcomes (financial transactions above defined thresholds, regulatory filings, customer-facing communications, irreversible state changes) must require authentication strength appropriate to the action's consequence, with policy specifying when human authentication is required versus when machine authentication is sufficient.

**OWASP ASI references.** ASI03 (Identity & Privilege Abuse); ASI09 (Human-Agent Trust Exploitation).

**Cross-cutting patterns.** Identity and privilege abuse; zero-click exfiltration.

**Regulatory anchors.** AI Act Article 14 (human oversight) — *Direct* for high-risk systems; AI Act Article 15 (cybersecurity) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*.

**Standards references.** ISO/IEC 27001:2022 Annex A.5.16 (identity management) — *Direct*; NIST SP 800-207 — *Direct*; NIST AI RMF Manage (MG-4) — *Indirect*.

**Test procedure.** Per-action-class review verifies that authentication strength matches the policy. Adversarial testing attempts to invoke high-authority actions through lower-authority authentication paths.

**Evidence artifact.** Authentication-policy specification per action class, supplemented by per-action authentication records and adversarial test results.

**Frequency.** Per-deployment for policy; continuous for action records; quarterly for adversarial testing.

**Ownership.** First-line: identity-management and agent operations teams. Second-line: ICT risk function; operational risk for consequence-tiering. Designated accountable: CRO.

**Derivation.** From the *principal-bound* and *composable and continuous* principles. The control gates compositions of permitted actions where the composition produces outcomes the principal model alone does not constrain.

## Controls addressing the lethal trifecta and compositional patterns

### LT-01: Lethal trifecta architectural review

**Statement.** Agent configurations in which the agent simultaneously has access to sensitive data, exposure to untrusted input, and use of an egress channel must undergo architectural review before deployment, with explicit acceptance of the residual risk by an accountable executive. Where compensating controls (human review at specific steps, content filtering, runtime gating) are intended to mitigate the configuration risk, the controls' effectiveness must be tested against documented threat scenarios prior to acceptance.

**OWASP ASI references.** ASI01 (Agent Goal Hijack) + ASI02 (Tool Misuse) + ASI03 (Identity & Privilege Abuse), in compositional reference.

**Cross-cutting patterns.** Lethal trifecta.

**Regulatory anchors.** AI Act Article 15 (cybersecurity, robustness) — *Indirect*; AI Act Article 9 (risk management) — *Indirect*; DORA Article 5 (ICT risk management framework) — *Indirect*.

**Standards references.** Cross-cuts ISO 42001 (no single clause) — *Gap*; NIST AI RMF Map (MP-1) and Manage (MG-3, MG-4) — *Indirect*.

**Test procedure.** Pre-deployment threat-modelling exercise enumerates the agent's data-access, input-exposure, and egress-channel inventory, identifies trifecta configurations, and tests proposed compensating controls against documented threat scenarios derived from public disclosures (EchoLeak, AgentFlayer, Shadow Escape, others as relevant).

**Evidence artifact.** Architectural review document signed by accountable executive, including the trifecta inventory, compensating-control design, test results, and explicit residual-risk acceptance.

**Frequency.** Per-deployment, with re-review on material configuration change.

**Ownership.** First-line: deployment owner and architecture team. Second-line: enterprise risk function with explicit CRO sign-off; joint with CISO and model-risk function for technical review. Designated accountable: CRO.

**Derivation.** From the *composable and continuous* and *evidence-first* principles. The architectural review is the response to the trifecta's compositional character; named executive acceptance distinguishes explicit from implicit risk acceptance.

---

### LT-02: Egress-channel inventory and control

**Statement.** The deployment must maintain an inventory of every channel through which agent outputs can produce outbound communication (markdown rendering, tool invocations, file writes, API calls, message dispatch), classify each channel by the trustworthiness of its destination, and apply controls scaled to the destination class.

**OWASP ASI references.** ASI02 (Tool Misuse); ASI09 (Human-Agent Trust Exploitation).

**Cross-cutting patterns.** Lethal trifecta; zero-click exfiltration.

**Regulatory anchors.** AI Act Article 15 (cybersecurity) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*.

**Standards references.** ISO/IEC 27001:2022 Annex A.8.20 (network security) — *Indirect*; NIST AI RMF Manage (MG-3) — *Indirect*.

**Test procedure.** Inventory review demonstrates that all egress channels are documented. Adversarial testing attempts to discover undocumented egress paths (markdown variants, embedded URLs in tool outputs, asynchronous rendering paths) and verifies they are caught by ingress filtering or post-generation review.

**Evidence artifact.** Egress-channel inventory with classification, control specification per class, and adversarial test results.

**Frequency.** Per-deployment for inventory; quarterly for adversarial testing.

**Ownership.** First-line: agent architecture team. Second-line: CISO function for control specification. Designated accountable: CISO function.

**Derivation.** From the *composable and continuous* principle. The egress inventory is the precondition for understanding the trifecta's scope.

## Controls addressing toxic-flow patterns

### TF-01: Toxic-flow analysis of authorised tool inventory

**Statement.** The agent's authorised tool inventory must undergo static toxic-flow analysis prior to production deployment, identifying paths from untrusted-input nodes through privileged-data-access nodes to egress nodes; identified flows must be reviewed against deployment configurations and either remediated, gated by compensating controls, or accepted as residual risk by an accountable executive.

**OWASP ASI references.** ASI02 (Tool Misuse) + ASI04 (Agentic Supply Chain Vulnerabilities), in compositional reference.

**Cross-cutting patterns.** Toxic flows.

**Regulatory anchors.** AI Act Article 15 (cybersecurity) — *Indirect*; AI Act Article 11 (technical documentation) — *Analogical*; DORA Article 25 (digital operational resilience testing) — *Indirect*; DORA Article 5 (ICT risk) — *Indirect*.

**Standards references.** ISO 42001 Annex A.8.1 (operational security) — *Indirect*; A.7 (third party) — *Indirect*; NIST AI RMF Measure (MS-1) — *Indirect*; Manage (MG-3) — *Indirect*.

**Test procedure.** Static analysis of the deployment's tool inventory using compositional-analysis tooling (Snyk Agent Scan TF001 or equivalent functionality, where the institution's procurement and vendor-relationship policies permit; otherwise equivalent in-house implementation). Analysis output is reviewed jointly by the deployment's technical and risk leadership.

**Evidence artifact.** Toxic-flow analysis report with identified flows, severity classifications, remediation or compensating-control decisions, and residual-risk acceptance documentation.

**Frequency.** Per-deployment; re-analysis on material change to tool inventory or configuration.

**Ownership.** First-line: deployment technical leadership. Second-line: ICT risk function for review and residual-risk acceptance; vendor-management function for tools sourced from third parties. Designated accountable: ICT risk function.

**Derivation.** From the *composable and continuous* principle directly. Compositional analysis is the response to compositional threats.

---

### TF-02: Cross-deployment flow review

**Statement.** Where multiple agent deployments share infrastructure (foundation-model providers, MCP servers, identity services, evidence-capture stores), an additional flow review must consider compositions that span deployments — content from one deployment reaching another, shared context across deployments, cross-deployment authority elevation paths.

**OWASP ASI references.** ASI04 (Agentic Supply Chain Vulnerabilities); ASI06 (Memory & Context Poisoning).

**Cross-cutting patterns.** Toxic flows (cross-deployment variant).

**Regulatory anchors.** DORA Article 6 (governance and organisation) — *Indirect*; DORA Article 8 (ICT systems, protocols and tools) — *Indirect*; AI Act Article 15 — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.5.5 (information security) — *Indirect*; NIST AI RMF Govern (GV-1) — *Indirect*; Manage (MG-3) — *Indirect*.

**Test procedure.** Cross-deployment flow analysis identifies shared infrastructure components and traces compositional paths spanning deployments. Adversarial testing attempts to use one deployment's authority to access resources scoped to another.

**Evidence artifact.** Cross-deployment flow analysis with shared-infrastructure inventory, composition map, and adversarial test results.

**Frequency.** Per-major-deployment; annually for institution-wide review.

**Ownership.** First-line: enterprise architecture function. Second-line: ICT risk function. Designated accountable: ICT risk function.

**Derivation.** From the *composable and continuous* principle, extended beyond single-deployment scope.

## Controls addressing zero-click and asynchronous-processing patterns

### ZC-01: Asynchronous-processing risk gating

**Statement.** Agents authorised to process content in background or asynchronous contexts (monitored inboxes, indexed document stores, scheduled jobs) must implement runtime policy gates on outbound tool invocations triggered by such content, with policies derived from documented threat scenarios for zero-click exfiltration.

**OWASP ASI references.** ASI01 (Agent Goal Hijack) + ASI09 (Human-Agent Trust Exploitation), in compositional reference.

**Cross-cutting patterns.** Zero-click exfiltration.

**Regulatory anchors.** AI Act Article 14 (human oversight) — *Indirect*; AI Act Article 15 (accuracy, robustness and cybersecurity) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*; DORA Article 17 (ICT-related incident management process) — *Analogical* (gate-triggered events feed the institution's incident-management process); DORA Article 18 (classification of ICT-related incidents) — *Indirect*.

**Standards references.** ISO 42001 Annex A.8.3 (human oversight) — *Indirect*; A.5.5 (information security) — *Indirect*; NIST AI RMF Govern (GV-3) — *Indirect*; Manage (MG-4) — *Indirect*.

**Test procedure.** Adversarial testing introduces content with embedded instructions into the agent's monitored corpus and verifies that runtime policy gates either prevent the agent from acting on the embedded instructions or escalate the proposed action for human review.

**Evidence artifact.** Runtime gate configuration documentation; per-incident logs of gate activations; periodic testing reports.

**Frequency.** Per-deployment for configuration; continuous for runtime logs; quarterly for adversarial testing.

**Ownership.** First-line: agent operations team and security operations centre jointly. Second-line: ICT risk function; legal/privacy for evidence-capture content review. Designated accountable: CISO function.

**Derivation.** From the *evidence-first* and *principal-bound* principles. The gate preserves the requesting principal's authority over agent actions even in asynchronous contexts.

---

### ZC-02: Content-source provenance preservation

**Statement.** For agent outputs derived from retrieved or indexed content, the deployment must preserve the provenance of each source document influencing the output, with provenance accessible at output review time and not suppressible by content within the retrieved sources.

**OWASP ASI references.** ASI06 (Memory & Context Poisoning); ASI09 (Human-Agent Trust Exploitation).

**Cross-cutting patterns.** Zero-click exfiltration; memory poisoning.

**Regulatory anchors.** AI Act Article 12 (record-keeping) — *Direct*; AI Act Article 13 (transparency) — *Indirect*; DORA Article 9 — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.2.4 (logging) — *Direct*; NIST AI RMF Govern (GV-1) — *Indirect*; Manage (MG-3) — *Indirect*.

**Test procedure.** Adversarial testing introduces content instructing the agent to suppress source attribution, then verifies the agent's output displays provenance markers across a defined adversarial test set. Provenance preservation is designed to be robust against content-generation-path attempts to suppress markers, recognising that complete unsuppressibility is empirically difficult and depends on the rendering layer's enforcement (per the EchoLeak case study, reference-mention markers were instructed-away by a directive within the attacker-controlled content rather than bypassed at the system layer; the methodology's discipline is to test for the realistic robustness range, not to claim absolute unsuppressibility).

**Evidence artifact.** Provenance-preservation architecture documentation; per-output provenance records; adversarial test results characterising suppression-resistance across the defined test set.

**Frequency.** Per-deployment for architecture; continuous for per-output records; quarterly for adversarial testing.

**Ownership.** First-line: agent architecture team. Second-line: ICT risk function. Designated accountable: CISO function.

**Derivation.** From the *evidence-first* and *regulator-legible* principles. Source provenance is an evidence artifact and is also the regulatory anchor under AI Act Article 12.

## Controls addressing memory and context poisoning

### MC-01: Retrieval-context integrity

**Statement.** Where the agent uses retrieval-augmented generation, the retrieval index's integrity (what documents it contains, how they are indexed, who can write to it) must be governed through documented controls, with separate privilege classes for the indexing pipeline, the retrieval pipeline, and the agent's reasoning over retrieved content.

**OWASP ASI references.** ASI06 (Memory & Context Poisoning); ASI04 (Agentic Supply Chain Vulnerabilities).

**Cross-cutting patterns.** Memory and context poisoning.

**Regulatory anchors.** AI Act Article 10 (data and data governance) — *Direct*; AI Act Article 15 (cybersecurity) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.7 (data for AI systems) — *Direct*; A.5.5 (information security) — *Indirect*; NIST AI RMF Map (MP-3) — *Direct*; Manage (MG-3) — *Indirect*.

**Test procedure.** Retrieval-context governance review verifies that indexing-pipeline writes are authenticated, retrieval queries are scoped to authorised indices, and the agent's reasoning over retrieved content is logged for after-the-fact review. Adversarial testing introduces malicious content into permitted indexing paths.

**Evidence artifact.** Retrieval-context governance specification; indexing-pipeline access logs; per-retrieval log entries; adversarial test results.

**Frequency.** Per-deployment for governance; continuous for logs; quarterly for adversarial testing.

**Ownership.** First-line: data engineering and agent operations teams jointly. Second-line: data governance function; ICT risk function. Designated accountable: ICT risk function.

**Derivation.** From the *evidence-first* and *framework-anchored* principles. The retrieval substrate is itself an attack surface that the methodology treats as a first-class concern.

---

### MC-02: Memory-poisoning detection and response

**Statement.** Where the agent maintains persistent memory across sessions (vector stores, conversation summaries, learned preferences), the memory store must be subject to detection mechanisms for content suggesting injection, with documented response procedures triggered by detection.

**OWASP ASI references.** ASI06 (Memory & Context Poisoning).

**Cross-cutting patterns.** Memory and context poisoning.

**Regulatory anchors.** AI Act Article 15 (cybersecurity) — *Indirect*; DORA Article 17 (ICT-related incident management process) — *Direct* for the response procedure; DORA Article 18 (classification of ICT-related incidents) — *Direct* for the classification of detected events.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.2.6 (incident response) — *Direct*; NIST AI RMF Manage (MG-4) — *Indirect*.

**Test procedure.** Memory-store review introduces seeded injection-pattern content and verifies that detection mechanisms identify it. Response-procedure tabletop exercises verify the procedure is operational.

**Evidence artifact.** Detection-mechanism specification; per-detection incident records; tabletop exercise reports.

**Frequency.** Per-deployment for detection; continuous for incident records; annually for tabletop.

**Ownership.** First-line: agent operations team. Second-line: ICT risk function; CSIRT function. Designated accountable: CISO function.

**Derivation.** From the *evidence-first* principle, supplemented by the regulatory anchoring DORA Article 17 supplies for incident management.

## Controls addressing resource overload and operational resilience

### RO-01: Resource-consumption limits and degradation behaviour

**Statement.** Agent operations must implement resource-consumption limits (per-session token budgets, per-user invocation rate limits, per-deployment infrastructure caps) with defined degradation behaviour when limits are reached, such that resource overload does not cascade into operational failures or security-control bypasses.

**OWASP ASI references.** *Gap* — resource overload is not represented as a category in the OWASP Top 10 for Agentic Applications (December 2025); RO-01 addresses the operational-resilience surface that the OWASP taxonomy leaves to operational-resilience standards (DORA, ISO 27001 capacity management).

**Cross-cutting patterns.** Not directly addressed by §3.2's five patterns; resource overload is an adjacent operational-resilience concern rather than a §3.2 threat pattern, with cascade considerations addressed in CF-01.

**Regulatory anchors.** DORA Article 11 (response and recovery) — *Indirect*; DORA Article 12 (backup, restoration and recovery) — *Indirect*; AI Act Article 15 (robustness) — *Direct*.

**Standards references.** ISO/IEC 42001:2023 Annex A.5.5 (information security) — *Indirect*; ISO/IEC 27001:2022 Annex A.8.6 (capacity management) — *Direct*; NIST AI RMF Manage (MG-4) — *Indirect*.

**Test procedure.** Load testing verifies resource limits trigger correctly. Degradation-behaviour testing verifies that limit-triggered degradation does not produce security-control bypasses or unbounded retries.

**Evidence artifact.** Resource-limit specification; load-test reports; degradation-behaviour test reports.

**Frequency.** Per-deployment for specification; quarterly for testing.

**Ownership.** First-line: agent operations and infrastructure teams. Second-line: ICT risk function. Designated accountable: ICT risk function.

**Derivation.** From the *framework-anchored* principle. DORA's operational resilience requirements apply to agent infrastructure as to any other ICT system.

## Controls addressing evidence and audit

### AT-01: Runtime evidence capture

**Statement.** Each agent invocation must produce a runtime evidence record containing the assembled prompt, the retrieved context, the tool definitions available at the moment of invocation, the model's reasoning trace where available, the tool calls selected, the tool outputs returned, and the final action. Capture must support after-the-fact reconstruction of the invocation from any starting point.

**OWASP ASI references.** ASI09 (Human-Agent Trust Exploitation) as primary anchor; AT-01 contributes evidence support across multiple ASI categories per the Coverage notes, with ASI09 the most direct because runtime evidence is what allows trust-exploitation manipulations to be reconstructed after the fact.

**Cross-cutting patterns.** Applies across all five §3.2 cross-cutting patterns; runtime evidence is the operational expression of the *evidence-first* design principle and the precondition for after-the-fact reconstruction in any of the patterns.

**Regulatory anchors.** AI Act Article 12 (record-keeping) — *Direct*; AI Act Article 26(6) (six-month minimum log retention for deployers of high-risk AI systems) — *Direct*; AI Act Article 19 (automatically generated logs; provider-side log retention) — *Indirect*; DORA Article 9 — *Indirect*; GDPR Article 25 (data protection by design) — *Direct* for the privacy corollary applied across the capture infrastructure.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.2.4 (logging) — *Direct*; ISO/IEC 27001:2022 Annex A.8.15 (logging) — *Direct*; NIST AI RMF Manage (MG-3) — *Indirect*.

**Test procedure.** Evidence-capture audit verifies that captured records support reconstruction of invocations against a sample of recorded sessions. Adversarial testing introduces invocations with specific exploitation patterns to verify the capture preserves the evidence necessary for post-incident analysis.

**Evidence artifact.** Evidence-capture architecture specification; per-invocation evidence records; reconstruction-audit reports.

**Frequency.** Per-deployment for architecture; continuous for records; quarterly for audit.

**Ownership.** First-line: agent architecture and platform teams. Second-line: ICT risk function; data privacy function for content-review and minimisation. Designated accountable: ICT risk function.

**Derivation.** From the *evidence-first* principle, with the privacy discipline anchored in GDPR Article 25 applied throughout the capture infrastructure.

---

### AT-02: Evidence-capture privacy controls

**Statement.** The evidence-capture infrastructure must implement data minimisation, access control, encryption in transit and at rest, retention governance, and privacy-impact assessment, with sensitive content classes (personal data, customer secrets, privileged communications) redactable or excludable by design.

**OWASP ASI references.** *Gap* — evidence-capture privacy controls are not represented in the OWASP ASI taxonomy; the requirement derives from GDPR's data-protection regime and the evidence-first principle's privacy corollary.

**Cross-cutting patterns.** Applies across all five §3.2 patterns; privacy discipline operates on capture irrespective of which pattern's threat triggered the captured event.

**Regulatory anchors.** GDPR Article 25 (data protection by design) — *Direct*; GDPR Article 32 (security of processing) — *Direct*; AI Act Article 10 (data and data governance) — *Indirect*.

**Standards references.** ISO/IEC 27001:2022 Annex A.5.34 (privacy and PII protection) — *Direct*; ISO/IEC 27701:2019 — *Direct*; ISO/IEC 42001:2023 Annex A.7.4 (data quality) — *Indirect*.

**Test procedure.** Privacy-impact assessment of evidence-capture infrastructure. Access-control review verifies role-based limits. Sample sensitive-content audit verifies redaction or exclusion mechanisms function.

**Evidence artifact.** Privacy-impact assessment; access-control specification; redaction-mechanism test results.

**Frequency.** Per-deployment for assessment; quarterly for review.

**Ownership.** First-line: data privacy function. Second-line: legal function. Designated accountable: Data Protection Officer (or equivalent).

**Derivation.** From the *evidence-first* principle's privacy corollary. Evidence capture without privacy discipline is not adequate; it is dangerous.

---

### AT-03: Evidence-store reconstruction queryability

**Statement.** The evidence store must support reconstruction queries (given a session ID, given an output, given a network anomaly, given a malicious input pattern) that return the evidence necessary for after-the-fact analysis without requiring custom code per query type.

**OWASP ASI references.** *Gap* — reconstruction queryability is not represented in the OWASP ASI taxonomy; the requirement derives from the evidence-first principle's after-the-fact reconstruction objective.

**Cross-cutting patterns.** Applies across all five §3.2 patterns; reconstruction supports investigation of incidents arising from any pattern's exploitation.

**Regulatory anchors.** AI Act Article 12 — *Indirect*; DORA Article 17 (ICT-related incident management process) — *Direct* for the response use case.

**Standards references.** ISO/IEC 27001:2022 Annex A.8.15 (logging) — *Indirect*; ISO/IEC 42001:2023 Annex A.6.2.6 (incident response) — *Indirect*.

**Test procedure.** Reconstruction-query test suite covers the standard query patterns and verifies that each returns within defined latency and completeness criteria.

**Evidence artifact.** Reconstruction-query specification; query-suite test results.

**Frequency.** Per-deployment; quarterly review.

**Ownership.** First-line: platform engineering. Second-line: ICT risk function. Designated accountable: ICT risk function.

**Derivation.** From the *evidence-first* principle. Captured evidence that cannot be queried in incident response is functionally not captured.

## Controls addressing supervisory and second-line readiness

### HC-01: Supervisory-engagement repository

**Statement.** For each agent deployment, the institution must maintain a supervisory-engagement repository containing inventory record, regulatory mapping, accountability documentation, threat register, gap analysis, toxic-flow analysis, adversarial testing results, implemented control documentation, residual-risk acceptance, and runtime evidence supporting each control's operation. The repository must support supervisor-engageable retrieval without translation work.

**OWASP ASI references.** *Gap* — the supervisory-engagement repository is not represented in the OWASP ASI taxonomy; the requirement derives from the *regulator-legible* design principle and the documentation/cooperation obligations of the AI Act and DORA.

**Cross-cutting patterns.** Applies across all five §3.2 patterns; the repository consolidates findings, evidence, and residual-risk acceptances across all pattern-specific controls.

**Regulatory anchors.** AI Act Article 26 (obligations of deployers of high-risk AI systems, including cooperation with competent authorities and incident notification) — *Direct*; DORA Article 5 (ICT risk management framework) — *Indirect*; DORA Article 6 (governance and organisation) — *Indirect*. *(The matrix v1.0 previously cited AI Act Article 19 with the label "technical documentation retention" and AI Act Article 23 with the label "cooperation with competent authorities" — both were misnamings. Article 19 is "Automatically generated logs" (a provider obligation); Article 23 is "Obligations of importers." The corrected anchor for a deployer-side supervisory-engagement repository is Article 26.)*

**Standards references.** ISO/IEC 42001:2023 Annex A.6.1 (organisational roles, responsibilities and authorities) — *Direct*; NIST AI RMF Govern (GV-1) — *Direct*.

**Test procedure.** Repository review verifies the documented inventory is complete and accessible. Tabletop supervisory-engagement exercise verifies the repository supports supervisory inquiries without translation.

**Evidence artifact.** The repository itself, plus tabletop exercise reports.

**Frequency.** Per-deployment for repository; quarterly for tabletop.

**Ownership.** First-line: deployment owner. Second-line: enterprise risk function for repository governance. Designated accountable: CRO.

**Derivation.** From the *regulator-legible* and *evidence-first* principles. The repository is the operational expression of the regulator-legibility design principle.

---

### HC-02: Second-line review cadence

**Statement.** Second-line risk functions must conduct periodic review of agent deployments at a cadence proportional to the deployment's risk classification, with review covering the deployment's threat register status, residual-risk acceptance currency, control-test results, and supervisory communications received.

**OWASP ASI references.** *Gap* — second-line review cadence is not represented in the OWASP ASI taxonomy; the requirement derives from the institution's three-lines-of-defence governance discipline and the *framework-anchored* design principle.

**Cross-cutting patterns.** Applies across all five §3.2 patterns; second-line review covers controls anchored to all patterns.

**Regulatory anchors.** DORA Article 5 (ICT risk management framework) — *Direct*; DORA Article 6 (governance and organisation) — *Direct*; AI Act Article 17 (quality management system) — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.5 (organizational context) — *Direct*; A.6.1 — *Direct*; NIST AI RMF Govern (GV-1, GV-2) — *Direct*.

**Test procedure.** Second-line review records show the documented cadence is being met. Sample review verifies that reviews engage substantively with the deployment's risk profile.

**Evidence artifact.** Second-line review records per deployment per period.

**Frequency.** Quarterly for high-risk deployments; semi-annually for medium-risk; annually for low-risk.

**Ownership.** Second-line risk function. Designated accountable: CRO.

**Derivation.** From the *framework-anchored* and *composable and continuous* principles.

## Controls addressing governance process

### GP-01: Deployment authorisation

**Statement.** Agent deployments must be authorised through a documented process specifying the deployment's intended function, principal model, threat surface, and accountable executive, with authorisation contingent on completion of LT-01, TF-01, and the relevant additional controls applicable to the deployment.

**OWASP ASI references.** *Gap* — deployment authorisation is institutional governance rather than an OWASP-categorised threat surface; the requirement is anchored in ISO 42001's policy framework and the AI Act's risk-management and deployer obligations, and operates as the precondition for the substantive controls.

**Cross-cutting patterns.** Applies across all five §3.2 patterns; deployment authorisation covers controls addressing all patterns.

**Regulatory anchors.** AI Act Article 17 (quality management system) — *Direct*; AI Act Article 26 (deployer obligations) — *Direct* for high-risk deployments; DORA Article 5 (ICT risk management framework) — *Direct*; DORA Article 6 (governance and organisation) — *Direct*.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.1 (organizational roles, responsibilities and authorities) — *Direct*; A.5.4 (policies for AI) — *Direct*; NIST AI RMF Govern (GV-1) — *Direct*.

**Test procedure.** Authorisation-record review verifies that all production deployments have valid authorisation records, that authorisation preconditions were met before authorisation, and that re-authorisation has been completed where required.

**Evidence artifact.** Per-deployment authorisation document with the deployment's intended function, principal model, threat surface, accountable executive, and references to completion of preconditions.

**Frequency.** Pre-deployment; on material change; periodic re-authorisation per institution policy.

**Ownership.** First-line: deployment owner. Second-line: enterprise risk function. Designated accountable: CRO.

**Derivation.** From the *framework-anchored* principle. The control is the institutional artifact that makes deployment subject to assurance discipline rather than implicit through deployment.

---

### GP-02: Adversarial testing programme

**Statement.** The institution must operate an ongoing adversarial testing programme covering its agent deployment portfolio, with testing scope including indirect prompt injection scenarios, tool poisoning scenarios, zero-click exfiltration scenarios, and lethal-trifecta exploitation scenarios. The programme must align to the institution's threat-led penetration testing regime where DORA TLPT applies.

**OWASP ASI references.** Cross-cutting; the testing programme covers all OWASP ASI categories.

**Cross-cutting patterns.** Applies across all five §3.2 patterns; the testing programme covers indirect prompt injection (lethal trifecta + zero-click), tool poisoning, and toxic-flow scenarios as named in the control statement.

**Regulatory anchors.** DORA Article 25 (digital operational resilience testing) — *Direct*; DORA Articles 26–27 (advanced testing through threat-led penetration testing) — *Direct* where TLPT applies; AI Act Article 15 (robustness, cybersecurity) — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.8.4 (verification and validation) — *Direct*; NIST AI RMF Measure (MS-2) — *Direct*; AgentDojo benchmark (Debenedetti et al., NeurIPS 2024) — *Direct* for indirect-prompt-injection scenarios; OWASP Top 10 for Agentic Applications — *Direct* for category coverage.

**Test procedure.** Testing programme records demonstrate scope coverage, test execution, finding remediation, and re-testing. Sample test results verify substantive engagement with documented threat patterns.

**Evidence artifact.** Testing programme specification; per-test reports; remediation tracking; re-test results.

**Frequency.** Continuous programme; per-test cadence per deployment risk classification; annual programme review.

**Ownership.** First-line: agent operations team and security operations centre. Second-line: ICT risk function. Designated accountable: CISO function.

**Derivation.** From the *evidence-first* and *composable and continuous* principles.

---

### GP-03: Methodology revision and learning

**Statement.** The institution must operate a documented mechanism for revising its agent assurance methodology in response to new threat patterns, supervisory communications, and engagement findings, with the revision mechanism tracking the institution's local methodology version against the published methodology version and against the institution's deployment portfolio.

**OWASP ASI references.** *Gap* — methodology revision and learning is institutional process rather than an OWASP-categorised threat surface; the requirement derives from the *composable and continuous* design principle and DORA's learning-and-evolving obligation.

**Cross-cutting patterns.** Applies across all five §3.2 patterns; methodology learning addresses pattern-specific findings as well as cross-pattern observations.

**Regulatory anchors.** DORA Article 13 (learning and evolving) — *Direct*; AI Act Article 17 (quality management system) — *Direct* for high-risk deployments; AI Act Article 9 (risk management system) — *Indirect*.

**Standards references.** ISO/IEC 42001:2023 Annex A.10 (continual improvement) — *Direct*; NIST AI RMF Govern (GV-3) — *Direct*; Manage (MG-1) — *Direct*.

**Test procedure.** Methodology-revision record review verifies tracking. Sample revisions demonstrate the mechanism engaged with substantive triggers (new threat patterns, supervisory communications) rather than reviewing perfunctorily.

**Evidence artifact.** Methodology-revision specification; per-revision records; change log against published methodology.

**Frequency.** Continuous; quarterly review of revision activity; annually for institution-wide assessment.

**Ownership.** Second-line: enterprise risk function with input from CISO and ICT risk functions. Designated accountable: CRO.

**Derivation.** From the *composable and continuous* principle. The methodology itself is subject to the same revision discipline as the deployments it governs.

## Controls addressing inter-agent communication

### IC-01: Inter-agent message authentication and policy enforcement

**Statement.** Where agents communicate with other agents — whether internal multi-agent systems or external agentic services — the deployment must implement message-level authentication, integrity verification, and policy enforcement at every inter-agent boundary, with policies specifying which agents may instruct which others, what action classes are permissible across agent boundaries, and what evidence is captured for cross-agent invocations.

**OWASP ASI references.** ASI07 (Insecure Inter-Agent Communication).

**Applicability.** Applies to deployments using inter-agent communication patterns (multi-agent systems, external agentic services, or agent-to-agent tool invocation across organisational boundaries). For single-agent deployments without inter-agent communication, IC-01 is not applicable; the gap analysis at `reference_application/gap_analysis.md` reflects this for the reference deployment.

**Cross-cutting patterns.** Identity and privilege abuse (cross-agent variant); toxic flows (where compositional flows span agent boundaries).

**Regulatory anchors.** AI Act Article 15 (cybersecurity) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*; DORA Article 8 (ICT systems, protocols and tools) — *Indirect*.

**Standards references.** ISO/IEC 27001:2022 Annex A.5.14 (information transfer) — *Direct*; A.8.20 (network security) — *Indirect*; A.5.15 (access control) — *Indirect*; ISO/IEC 42001:2023 Annex A.5.5 (information security) — *Indirect*; NIST SP 800-207 — *Direct*; NIST AI RMF Manage (MG-3) — *Indirect*.

**Test procedure.** Inter-agent message review verifies that messages are authenticated, integrity-checked, and subject to policy enforcement. Adversarial testing introduces spoofed inter-agent messages and verifies they are rejected. Tests cover both internal multi-agent communication and external agentic-service integrations.

**Evidence artifact.** Inter-agent communication policy specification; message-authentication architecture documentation; per-message logs (with privacy-preserving content treatment); adversarial test results.

**Frequency.** Per-deployment for policy and architecture; continuous for logs; quarterly for adversarial testing.

**Ownership.** First-line: agent architecture team; identity-management team for authentication infrastructure. Second-line: ICT risk function for policy review. Designated accountable: CISO function.

**Derivation.** From the *principal-bound* and *composable and continuous* principles. Inter-agent communication extends the principal-binding question across agent boundaries; per-message policy enforcement is the composable-and-continuous response.

## Controls addressing cascading failures

### CF-01: Failure-domain isolation and cascade prevention

**Statement.** The deployment must implement failure-domain isolation between agents, between agent components (orchestration, retrieval, tool invocation, evidence capture), and between agent deployments sharing infrastructure, with explicit policies for circuit-breaking, error-propagation containment, and cross-domain error escalation. Cascade-prevention controls must be tested against scenarios in which a single component failure or compromise produces error propagation across the deployment.

**OWASP ASI references.** ASI08 (Cascading Failures); ASI04 (Agentic Supply Chain Vulnerabilities) where third-party failures cascade into the deployment.

**Cross-cutting patterns.** Toxic flows (cascading-error variant); resource overload (where overload in one component cascades into others).

**Regulatory anchors.** DORA Article 11 (response and recovery) — *Direct*; DORA Article 12 (backup, restoration and recovery) — *Direct*; DORA Article 13 (learning and evolving) — *Indirect*; AI Act Article 15 (robustness) — *Direct*.

**Standards references.** ISO/IEC 27001:2022 Annex A.5.29 (information security during disruption) — *Direct*; A.5.30 (ICT readiness for business continuity) — *Direct*; ISO/IEC 42001:2023 Annex A.6.2.6 (incident response) — *Indirect*; A.8.4 (verification and validation) — *Indirect*; NIST AI RMF Manage (MG-4) — *Indirect*; Govern (GV-3) — *Indirect*.

**Test procedure.** Failure-mode testing introduces controlled failures into individual components — foundation-model unavailability, MCP-server timeouts, retrieval-store corruption, evidence-capture interruptions — and verifies cascade-prevention controls operate. Tabletop exercises simulate scenarios in which a third-party component compromise propagates through dependent agents. Tests cover both the immediate failure response and the post-failure operational state.

**Evidence artifact.** Failure-domain architecture documentation; cascade-prevention control specification; per-test failure-mode reports; tabletop exercise reports.

**Frequency.** Per-deployment for architecture; semi-annually for failure-mode testing; annually for tabletop.

**Ownership.** First-line: agent architecture team; site-reliability or platform-operations team. Second-line: ICT risk function; operational risk function for cascade-impact assessment. Designated accountable: ICT risk function.

**Derivation.** From the *composable and continuous* principle. Cascade prevention is the operational-resilience face of compositional analysis; the same compositional reasoning that surfaces toxic flows surfaces cascading-failure paths.

## Controls addressing rogue-agent and behavioural-drift patterns

### RA-01: Agent-behaviour drift detection and response

**Statement.** The deployment must implement behavioural-drift detection mechanisms that identify when an agent's actions, tool invocations, reasoning patterns, or output characteristics deviate materially from baseline expected behaviour, with documented response procedures including rate-limiting, scope-narrowing, isolation, and decommissioning. Drift detection must be calibrated to distinguish legitimate behaviour evolution (new use cases, model updates, configuration changes) from anomalous drift indicating compromise, misalignment, or memory poisoning.

**OWASP ASI references.** ASI10 (Rogue Agents); ASI06 (Memory & Context Poisoning); ASI09 (Human-Agent Trust Exploitation) where drift produces deceptive outputs.

**Cross-cutting patterns.** Memory and context poisoning (drift-as-symptom); zero-click exfiltration (drift produced by sustained injection campaigns).

**Regulatory anchors.** AI Act Article 15 (accuracy, robustness) — *Direct*; AI Act Article 26(5) (deployer monitoring obligations for high-risk systems) — *Direct*; AI Act Article 14 (human oversight) — *Indirect*; DORA Article 9 (protection and prevention) — *Indirect*; DORA Article 17 (incident management) — *Direct* for the response procedure.

**Standards references.** ISO/IEC 42001:2023 Annex A.6.2.4 (logging) — *Direct*; A.8.3 (human oversight) — *Direct*; A.8.4 (verification and validation) — *Direct*; NIST AI RMF Measure (MS-2) — *Direct*; Manage (MG-4) — *Direct*; Govern (GV-3) — *Indirect*.

**Test procedure.** Drift-detection mechanism review verifies the mechanism is calibrated against documented baseline behaviour. Adversarial testing introduces sustained subtle injection campaigns to verify drift is detected before the cumulative effect produces material harm. Response-procedure tabletop exercises verify the rate-limiting, scope-narrowing, isolation, and decommissioning steps are operational.

**Evidence artifact.** Baseline-behaviour documentation; drift-detection mechanism specification; per-detection incident records; response-procedure documentation; tabletop exercise reports.

**Frequency.** Per-deployment for baseline and detection mechanism; continuous for incident records; quarterly for adversarial testing; annually for tabletop.

**Ownership.** First-line: agent operations team; security operations centre for detection-and-response integration. Second-line: ICT risk function; model-risk function for behavioural-baseline calibration. Designated accountable: CRO (decommissioning is a CRO-level decision; lower-severity responses can be delegated).

**Derivation.** From the *evidence-first*, *composable and continuous*, and *principal-bound* principles. Drift detection requires runtime evidence (evidence-first); is a continuous discipline rather than a point-in-time test (composable and continuous); and the response-procedure escalation reflects the principle that the agent's authority is bounded by its principal's grant rather than open-ended (principal-bound).

## Coverage notes

**OWASP Top 10 for Agentic Applications coverage.** ASI01 (Agent Goal Hijack) — LT-01, ZC-01, IA-03 via composition. ASI02 (Tool Misuse) — TP-01, TP-03, LT-01, LT-02, TF-01. ASI03 (Identity & Privilege Abuse) — IA-01, IA-02, IA-03, LT-01. ASI04 (Agentic Supply Chain Vulnerabilities) — TP-01, TP-02, TP-03, TF-01, TF-02, MC-01. ASI05 (Unexpected Code Execution) — *Gap*; v1.0 of the matrix does not address agent-generated code execution or sandbox-escape patterns directly. Deployments where the agent generates, modifies, or runs code require additional controls beyond v1.0; the gap is acknowledged here for revision in a future major version. ASI06 (Memory & Context Poisoning) — MC-01, MC-02, ZC-02, TF-02, RA-01. ASI07 (Insecure Inter-Agent Communication) — IC-01, with supporting controls IA-01 and IA-03. ASI08 (Cascading Failures) — CF-01, with supporting controls TF-02 and RO-01. ASI09 (Human-Agent Trust Exploitation) — ZC-01, ZC-02, AT-01, IA-03, LT-02, RA-01. ASI10 (Rogue Agents) — RA-01, with supporting controls MC-01, MC-02, IC-01, AT-01, GP-01, GP-02. Resource overload (out-of-OWASP-taxonomy operational-resilience concern) — RO-01, with cascade considerations in CF-01. The cross-cutting governance controls (GP-01, GP-02, GP-03) establish the institutional framing under which all category-specific controls operate.

**Cross-cutting threat pattern coverage.** The paper's §3.2 names five cross-cutting threat patterns; each receives matrix coverage. Tool poisoning (TP-01, TP-02, TP-03); identity and privilege abuse (IA-01, IA-02, IA-03, with cross-agent extension in IC-01); lethal trifecta (LT-01, LT-02, with composition-tracking via TF-01); toxic flows (TF-01, TF-02); zero-click exfiltration (ZC-01, ZC-02, with composition-tracking via TF-01). Memory and context poisoning is treated under ASI06 above (MC-01, MC-02, ZC-02, RA-01) rather than as a sixth cross-cutting pattern.

**Design-principle coverage.** Each of the five design principles is the explicit derivation source for at least three controls. *Evidence-first* anchors AT-01, AT-02, AT-03, RA-01, plus contributions to most others. *Framework-anchored* anchors TP-02, GP-01, plus contributions throughout. *Regulator-legible* anchors HC-01 directly; the regulator-legibility quality is built into evidence and reporting structure across the matrix. *Composable and continuous* anchors LT-01, LT-02, TF-01, TF-02, GP-02, GP-03, IC-01, CF-01, RA-01. *Principal-bound* anchors IA-01, IA-02, IA-03, IC-01, with contributions to ZC-01 and RA-01.

**Regulatory-anchor coverage.** AI Act: Articles 9, 10, 11, 12, 13, 14, 15, 17, 19, 26 across the matrix (Article 23 was previously listed in this enumeration and in HC-01's anchors as "cooperation with competent authorities"; that was a misnaming — Article 23 is "Obligations of importers," and the correct deployer-cooperation anchor is Article 26, applied throughout). DORA: Articles 5, 6, 8, 9, 11, 12, 13, 17, 18, 25, 26, 27, 28, 29, 30. ISO/IEC 42001:2023: Annexes A.5.4, A.5.5, A.6.1, A.6.2 (sub-clauses .2, .4, .6), A.7, A.8.1, A.8.3, A.8.4, A.10. ISO/IEC 27001:2022: Annexes A.5.14, A.5.15, A.5.16, A.5.29, A.5.30, A.5.34, A.8.6, A.8.15, A.8.20, A.8.32. NIST AI RMF: Govern (GV-1, GV-2, GV-3), Map (MP-1, MP-3, MP-5), Measure (MS-1, MS-2), Manage (MG-1, MG-3, MG-4). NIST SP 800-207. GDPR Articles 25, 32. ISO/IEC 27701.

**Total controls.** Twenty-six, organised across thirteen control families (TP, IA, LT, TF, ZC, MC, RO, AT, HC, GP, IC, CF, RA). Five reproduced from §4.3 of the paper; twenty-one introduced in this matrix.

## Revision protocol

The matrix is v1.0 of a living artifact. The methodology's *composable and continuous* design principle requires that the matrix itself be subject to the same revision discipline as the deployments it governs. This section specifies the revision protocol.

**Versioning.** The matrix carries semantic versioning. Major versions (v2.0, v3.0) reflect structural changes to the methodology — a new design principle, a substantial reorganisation of control families, a fundamental shift in the regulatory anchoring framework. Minor versions (v1.1, v1.2) reflect substantive but bounded changes — addition of new controls, retirement of obsolete controls, material revision to existing controls' specifications. Patch versions (v1.0.1, v1.0.2) reflect editorial corrections, mapping-strength adjustments, or small clarifications that do not materially change a control's substance.

**Triggers for revision.** The following classes of event trigger consideration of matrix revision: publication of new OWASP Top 10 for Agentic Applications (the matrix is anchored to the December 2025 release; subsequent releases warrant re-anchoring); material change to the regulatory framework the matrix anchors to (DORA RTS publications, AI Act amendments through the Digital Omnibus or other instruments, supervisory guidance shifting the substantive expectations); publication of significant new agent-security incidents producing patterns the matrix's existing controls do not adequately address; engagement findings from application of the methodology to live regulated production deployments; scholarly work materially revising the threat taxonomy or assurance methodology landscape.

Triggers do not automatically produce revisions. Each trigger is considered against the question of whether incorporation requires matrix change or can be addressed through engagement guidance below the matrix's level of abstraction.

**Authorisation.** Revision authority for the published matrix rests with the work's maintainer, currently solo. Substantial revisions (new or retired controls, material changes to existing controls) follow the issue-and-pull-request process documented in `CONTRIBUTING.md`, with public discussion preceding incorporation. Patch-level revisions (editorial corrections, mapping-strength adjustments) may be incorporated directly with the change documented in the CHANGELOG.

**Documentation.** Each revision is documented in the CHANGELOG entry for the version that introduces it. The documentation specifies what changed, why, and what implementation implications follow for institutions whose internal methodology tracks against this published methodology.

**Notification.** The matrix is hosted in a public GitHub repository; readers seeking notification of revisions can use GitHub's repository-watch mechanism. A formal subscriber list, mailing list, or notification service is not currently maintained; if engagement scale warrants, this may be revisited.

**Stability commitment.** Within a major version, no existing control's identifier (TP-01, IA-01, etc.) is reassigned. Controls may be retired (the identifier is preserved, the control is marked retired, with rationale in the CHANGELOG); new controls take the next available identifier in the relevant family. Within a major version, no existing control's substantive requirements are weakened; revisions either maintain or strengthen the underlying assurance discipline.

**Cadence.** No fixed revision cadence is specified. The matrix revises in response to triggers, not in response to calendar. Quiet periods reflect either stability of the underlying landscape or absence of triggering events; the absence of revision is not evidence of work having ceased.

**Local adaptation.** Institutions adopting the methodology will commonly maintain local matrix versions reflecting institution-specific configuration (additional controls for institution-specific risks, modified test procedures reflecting institutional tooling, ownership specifications reflecting the institution's three-lines-of-defence structure). Local versions track against the published version; the GP-03 control in the matrix specifies the discipline for this tracking. Local versions are not revisions of the published matrix; they are derived works the institution maintains.

## What this matrix does not deliver

It does not deliver an effectiveness assessment of any control. The controls are derived logically from threat patterns and regulatory anchors; their effectiveness in live deployments remains empirically under-characterised, as the position paper acknowledges.

It does not deliver a turnkey implementation guide. Each control specifies what must be done; institutions implementing the methodology must adapt the test procedures, evidence artifacts, and ownership models to their internal structures.

It does not constitute formal attestation. The matrix produces assurance-ready evidence; formal attestation requires partnership with a qualified ISAE 3000 or AT-C 205 practitioner.

It is not exhaustive. The OWASP Top 10 for Agentic Applications taxonomy will evolve, threat patterns not yet documented will surface, and the regulatory landscape will continue to develop. The matrix is v1.0 of an ongoing artifact, and the methodology's discipline is to revise on the basis of what it encounters.
