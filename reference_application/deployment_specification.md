# Deployment specification — claims-processing agent

*Reference deployment for the synthesis methodology demonstration in §5 of the position paper. This document specifies the deployment's architecture, tool inventory, principal model, and operational context in a form suitable as input to assurance engagement. The deployment is hypothetical but calibrated to patterns observable in production European insurer AI deployments as of early 2026; the configuration is illustrative of a stress case rather than a recommendation.*

## Institutional context

The deployment operates within a hypothetical Tier-2 European insurer offering motor and home insurance to retail customers across two member states. Claims volumes are in the low tens of thousands per month. The institution is subject to Solvency II oversight and falls within DORA's scope as a financial entity. The deployment has been in production for approximately six months at the point of the demonstration.

The institution's choice to deploy the agent reflects market conditions documented in EIOPA Opinion BoS-25-360 (claims management identified as a principal AI use case in the insurance value chain) and DNB's 2024 reporting (15 of 36 surveyed insurers had implemented AI in fraud detection and claim-amount estimation). The deployment is one configuration within a broader market trajectory rather than an outlier.

## Functional scope

The agent supports human claims adjusters by performing initial intake review, fact assembly, and recommendation drafting on incoming claims. The intended workflow is:

1. Claim submission arrives via the customer portal or call-centre intake system.
2. The agent retrieves the customer's policy details, claims history, and relevant supporting evidence (photographs, repair estimates, third-party reports).
3. The agent assesses the claim against policy terms and assembles a fact summary.
4. The agent drafts a recommendation (approve, request additional information, decline, or escalate to fraud review).
5. For claims under €2,500 with no fraud-risk indicators, the recommendation auto-approves and the customer is notified.
6. For claims above €2,500 or with risk flags, the recommendation is routed to a human adjuster with the agent's analysis attached. The adjuster reviews and either accepts the recommendation, modifies it, or returns the claim for further investigation.

The auto-approval threshold is the deployment's most consequential operational decision. The institution chose €2,500 as the boundary based on historical claims-cost analysis: roughly 60% of claims fall under this threshold, and pre-deployment historical data suggested the agent's recommendation accuracy on these claims exceeded the baseline of human adjuster decisions on comparable claims.

## Architecture

### Orchestration layer

The agent's orchestration is constructed in LangGraph, the LangChain Inc.-maintained open-source framework for building stateful, long-running agents (MIT-licensed; production users include Klarna, Replit, Elastic, Uber, J.P. Morgan, among others). LangGraph manages the agent's state machine, prompt construction, tool-invocation routing, and persistence of intermediate state across reasoning steps.

### Foundation model

Foundation-model reasoning is supplied by a frontier model accessed via API. Prompt construction is handled by the LangGraph orchestration layer; the model's outputs are parsed by orchestration-layer logic that determines tool-invocation routing. Model selection is treated as a configuration parameter; the deployment is calibrated to a single named model with documented version pinning, and model upgrades are subject to the institution's change-control discipline.

### Tool access layer

Tool access is implemented via the Model Context Protocol. The deployment connects to seven MCP servers, listed below by category:

**First-party MCP servers (operated by the insurer's IT function).**

1. *Policy administration MCP server.* Read access to policy records — coverage terms, premiums, exclusions, endorsements, customer relationship history.
2. *Claims database MCP server.* Read access to historical claims for any policy and write access to claims-status updates for claims under the agent's authority.
3. *Document management MCP server.* Read access to documents uploaded by customers (photographs, repair estimates, medical reports for personal-injury claims, third-party reports).

**Vendor-supplied MCP servers (operated by named third parties).**

4. *Fraud-detection scoring MCP server.* Provided by a specialised fraud-detection vendor under contract; receives anonymised claim attributes and returns a fraud-risk score.
5. *Repair-shop estimate MCP server.* Provided by a vehicle-repair-network vendor under contract; receives vehicle details and damage descriptions and returns repair-cost estimates.

**Community-maintained MCP servers (operated by community contributors).**

6. *Regional vehicle-data registry MCP server.* Community-maintained MCP server providing access to public vehicle-registration data across the two member states.
7. *Document parsing MCP server.* Community-maintained MCP server for general document parsing (PDF text extraction, image OCR, form-field extraction).

The mix of server provenance is deliberate. Three first-party servers carry the institution's full change-control discipline; two vendor servers carry contractual obligations on the vendors but require third-party-risk-management oversight; two community servers carry no contractual relationship and the institution's exposure depends on the community's maintenance discipline.

### Persistent context layer

Persistent memory is implemented via a vector store of past claim summaries. At session initialisation for each new claim, the orchestration layer retrieves summaries of past claims from the same customer, claims of similar type, and claims with similar fact patterns, and includes the retrieved summaries in the agent's reasoning context. Tool outputs from individual sessions are not persisted in memory across sessions by default; only the structured claim summaries the orchestration layer commits to the vector store at session close are retained.

The vector store's content is derived from the agent's own past reasoning. The summaries written at session close reflect the agent's interpretation of each claim's facts; if those interpretations are flawed, the flaws propagate forward into future reasoning over related claims.

## Principal model

The deployment's principal model is the source of its most significant assurance challenge.

The agent operates with a single set of service credentials — a `claims_agent` service account holding read access to:

- The policy-administration system (all policies, all customers).
- The claims database (all historical claims).
- The customer-record system (all customer profiles).
- The fraud-detection vendor's scoring API (any claim).
- The document-management system (any uploaded document).

Plus write access to:

- Claims-status updates (any claim within the agent's authority).
- Recommendation drafts (any claim).

The same service-account credentials are used for every claim the agent processes, regardless of which customer the claim concerns.

Customer identity is communicated to the agent through the claim payload at session initialisation. The agent's reasoning is conditioned on the customer's identity; the prompt the model receives includes the customer's name, policy number, and claim details. The orchestration layer's reasoning over the customer's identity is not, however, propagated to the tool-invocation layer. Downstream tool calls — to the policy-administration system, the claims database, the customer-record system — are authenticated against the `claims_agent` service account, not against the requesting customer's identity.

Operationally, the configuration permits the agent to retrieve any customer's records when processing a specific customer's claim. The deployment's intended workflow constrains the agent to retrieve only the requesting customer's records, and the orchestration layer's prompts encourage this discipline. The architectural authority to retrieve other customers' records is present and is exercised at the agent's discretion, based on the model's reasoning over the runtime context.

When a claim is routed to a human adjuster (claims above €2,500 or with risk flags), the adjuster is identified at routing time and the claim is assigned via the claims-management system. The adjuster's downstream actions on the claim are performed under the adjuster's own credentials. The agent's pre-routing actions, however, are performed under the service account.

## Auto-approval boundary conditions

For claims under €2,500 with no fraud-risk indicators, the agent's recommendation auto-approves the claim. Auto-approval triggers the following downstream actions, all performed under the `claims_agent` service account:

1. The claim status is updated to "approved."
2. A payment instruction is generated and submitted to the institution's payment system.
3. A notification is sent to the customer via the channel they provided at submission.

No human is in the loop between the agent's recommendation and the payment instruction for auto-approved claims.

## Evidence-capture posture (current state)

The deployment captures the following evidence at runtime:

- LangGraph orchestration logs: state machine transitions, tool invocations and responses, errors and retries.
- Foundation-model API logs: per-invocation request and response.
- MCP-server access logs (per server): tool invocations and responses, scoped to the server's own tooling.
- Claims-database audit logs: read and write operations by service account.

The captured evidence is sufficient to reconstruct the agent's tool invocations and the responses it received, but is *not* structured to support reconstruction of the agent's reasoning context — specifically, the assembled prompt the model received at each invocation, including the retrieved vector-store content. The orchestration logs note *that* retrieval occurred but do not preserve *what* was retrieved.

This is the configuration's most consequential evidence gap. After-the-fact reconstruction of any specific recommendation can establish what the agent did but not why the model produced the recommendation it did.

## Configuration risk surfaces

The deployment is calibrated to exhibit several risk surfaces deliberately, as the methodology demonstration's purpose is to show the framework's response to a configuration with non-trivial residual risk. Specifically:

**Two community-maintained MCP servers** (regional vehicle-data registry, document parsing) carry the broadest supply-chain attack surface in the deployment. Neither has contractual obligations on the maintainer, neither has been qualified through the institution's third-party-risk-management process to the standard the methodology recommends, and both expose the deployment to metadata-layer tool poisoning risks.

**The service-account principal model** for all customer interactions creates the structural authority gap the IA-01 finding addresses.

**The auto-approval threshold at €2,500** with the agent's actions taken under the service account compounds the principal-model gap with consequential downstream effects: a successful manipulation of the agent's reasoning at a low-value claim produces a payment instruction with no human review.

**The vector-store retrieval** at session initialisation introduces past claim summaries into reasoning context with no integrity verification beyond the orchestration layer's own write discipline. Corrupted historical entries propagate forward; a successful attack at one session could shape the agent's reasoning across subsequent related sessions.

**The foundation model and orchestration layer** have shared infrastructure across multiple deployments within the institution. The agent shares the model API, the orchestration framework, and parts of the evidence-capture infrastructure with two other internal agent deployments (a customer-service triage agent and an internal-operations workflow agent). Cross-deployment compositional risks are present but not analysed in current configuration.

## Configuration anchor points

This specification serves as the input to the methodology's threat register, gap analysis, and findings. Subsequent documents in the `reference_application/` directory derive their analysis from the configuration described here.

The configuration represents a snapshot at the point of the demonstration. In an actual engagement, configuration changes between assessment and remediation would be tracked through change-control records that the methodology's evidence-first principle would require. For the demonstration, the configuration is treated as static.
