# Toxic-Flow Analysis — [Agent ID]

*Compositional analysis of the deployment's authorised tool inventory, identifying paths from untrusted-input sources through privileged-data access to egress channels. Operationalises TF-01 from the v1.0 control matrix. Mirrors the analytical content in `reference_application/findings/tf_01_01_toxic_flow.md` and feeds into the threat register's *Toxic flows* cross-cutting section.*

## How to use

Run after the deployment specification is complete (the tool inventory and data-flows sections are the analysis's inputs). The outputs feed into the threat register (specifically the *Toxic flows* cross-cutting section) and the gap analysis (specifically TF-01). Each identified flow becomes either a *remediated* path (after configuration change), a *gated* path (with documented compensating controls and named assumptions), or an *accepted-residual* path (with explicit residual-risk acceptance by an accountable executive).

## Identified flows

| Flow ID | Untrusted-input source | Sensitive-data access | Egress channel | Path narrative | Classification |
|---|---|---|---|---|---|
| TF-001 | [e.g., customer-submitted claims] | [e.g., policy-admin system via claims-agent service account] | [e.g., customer notification via outbound email] | [e.g., claim submission → RAG retrieval over claims history → recommendation drafted → outbound notification with embedded URL] | [remediated / gated / accepted] |
| | | | | | |

[Add a row per identified flow. The path-narrative column should be specific enough that a reviewer can trace the flow through the deployment specification's data-flows section.]

## Per-flow gating analysis

For each *gated* flow above, the analysis specifies the compensating controls and the assumptions on which gating rests.

### Flow TF-001 — [short title]

**Compensating controls in current configuration.** [List of controls that gate the flow.]

**Assumptions named.** [Each control's effectiveness depends on assumptions; the assumptions are the load-bearing element of the gating. Examples:

- "The XPIA classifier remains effective against current variants of indirect prompt injection."
- "The outbound notification system's URL allowlist remains complete and current."
- "The retrieval store's content provenance is preserved through indexing and retrieval."]

**Probeable assumptions.** [Which assumptions could plausibly be probed by an adversary and how. The methodology's *evidence-first* discipline applied to compositional risk: gating assumptions that cannot be empirically tested are weaker than gating assumptions that can.]

**Severity if gating fails.** [Critical / High / Medium / Low.]

### Flow TF-002 — [...]

[...]

## Per-flow accepted-residual analysis

For each *accepted* flow, reference the residual-risk-acceptance artifact.

### Flow TF-XXX

- **Residual-risk acceptance reference:** see `residual_risk_acceptance_template.md` for [finding ID, e.g., TF-01-01].
- **Accountable executive:** [name, role].
- **Acceptance date:** [YYYY-MM-DD].
- **Review cadence:** [annual / quarterly / per material change to tool inventory].

## Aggregate

[Total counts: X remediated / X gated / X accepted-residual. Brief commentary on whether the gating-heavy or accepted-heavy aggregate reflects a stress-case configuration or a more conservative one.]

## Cross-deployment scope (TF-02)

[Where the deployment shares infrastructure with other agent deployments — shared retrieval stores, shared evidence-capture infrastructure, shared foundation-model API — the toxic-flow analysis extends to cross-deployment compositional paths. Reference TF-02 (Cross-deployment flow review) for the institutional discipline; document any cross-deployment flows surfaced here. The single-deployment analysis above does not cover cross-deployment composition.]

## See also

- `threat_register_template.md` — the *Toxic flows* cross-cutting section feeds from this analysis
- `gap_analysis_template.md` — TF-01 evaluation feeds from this analysis
- `finding_template.md` — engagement-style finding (TF-01-NN) per identified flow warranting documentation
- `paper/control_matrix.md` TF-01 — the matrix specification
- `paper/full.md` §3.2.4 — toxic-flow methodology
- `paper/full.md` §5.3 — application of toxic-flow analysis to the reference deployment
- `reference_application/findings/tf_01_01_toxic_flow.md` — worked example
