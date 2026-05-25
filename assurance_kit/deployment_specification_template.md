# Deployment Specification — [Agent ID]

*Per-deployment specification capturing architecture, tools, principal model, and authority surface in the detail downstream methodology work requires. Mirrors the structure of `reference_application/deployment_specification.md` for the hypothetical insurance claims-processing agent; adapt to the specific deployment.*

## 1. Deployment overview

[One paragraph: business function, deployment date, scope, business owner.]

## 2. Architecture

[High-level architecture: orchestration framework, foundation model, retrieval substrate, evidence-capture infrastructure, integration points with other systems. Note any shared infrastructure with other agent deployments — shared foundation-model APIs, shared orchestration frameworks, shared retrieval stores, shared evidence-capture infrastructure — and reference TF-02 and CF-01 for the cross-deployment concerns those shares raise.]

## 3. Foundation-model layer

[Model identifier, provider, version pinning policy, fall-back behaviour, monitoring for model deprecation or behaviour drift. Note any model-routing or model-selection logic.]

## 4. Tool inventory

| Tool | Provider | Read / Write | Sensitive-data access | Change-control discipline | Qualification status |
|---|---|---|---|---|---|
| [tool name] | [first-party / vendor / community MCP server] | [R / RW] | [Y / N / Conditional] | [vendor change-control / internal change-control / community-maintained / unmanaged] | [qualified / pending qualification / N/A] |
| | | | | | |

[For each non-first-party tool, note the change-control discipline its operator follows and the qualification status against the institution's third-party risk management process. The methodology's TP-01, TP-02, and TP-03 controls address tool inventory's assurance posture.]

## 5. Principal model

[Describe the identity-and-authority architecture: how the agent authenticates, what principal it operates under, whether identity propagates through tool calls, what authorisation is checked at each interaction layer.]

**Service-account vs propagated-identity?** [single service account / propagated user identity / hybrid]

**Scope of authority granted to the service account (if applicable).** [List the data classes and actions the service account is authorised for. The gap between this scope and any specific requesting principal's authority is the methodology's primary identity-and-privilege-abuse concern; see IA-01.]

## 6. Decision authority and escalation

[Auto-approve thresholds and the criteria they apply to; routing logic to human reviewers; escalation paths; fallback behaviour on tool errors or low-confidence outputs. Auto-approval is the highest-consequence authority surface in most deployments; document it explicitly.]

## 7. Data flows

[The data the agent retrieves from each source, the data the agent produces, the data persisted in memory or context. Note flows from untrusted sources to sensitive data and to egress channels — this informs the lethal-trifecta analysis (LT-01) and the toxic-flow analysis (TF-01) downstream.]

**Untrusted-input sources.** [List: customer-submitted claims, externally-originated email, third-party tool outputs, web-scraping outputs, community-MCP-server returns, etc.]

**Sensitive-data destinations.** [List: customer records, policy administration, payment systems, internal reporting, etc.]

**Egress channels.** [List: customer notifications, payment instructions, recommendation routing, audit log outputs, integration outputs to other systems, etc. Note explicitly whether each egress is internal-only or has external destinations.]

## 8. Evidence-capture infrastructure

[What runtime evidence is captured, with what retention, with what access control, with what privacy treatment under GDPR Article 25. Gaps belong in the threat register and gap analysis downstream; the high-level picture belongs here. Cross-reference `evidence_capture_checklist.md`.]

## 9. Regulatory anchoring

[Which regulatory regimes apply to this deployment specifically. AI Act Annex III classification (if any); DORA scope; Solvency II or CRR / CRD as applicable; GDPR special-category data flags; institution-internal model-risk tier; AI Office or supervisory examination contact (where known).]

## 10. Boundary acknowledgements

[Explicit limits of the specification: what is not specified, what is presumed, what depends on operational decisions made elsewhere. Honest framing of the specification's coverage matters for the downstream threat register.]

## See also

- `agent_inventory_template.md` — institution-wide inventory; the specification expands one entry from the inventory
- `threat_register_template.md` — threat enumeration against this specification
- `paper/full.md` §5 — the reference deployment specification's structure
- `reference_application/deployment_specification.md` — worked example
