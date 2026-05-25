# Minimum Viable Assurance

*Ten controls every regulated agent deployment should have evidence of before production. A tractable entry point for first adoption of the synthesis methodology; the full v1.0 control matrix at `paper/control_matrix.md` carries the comprehensive twenty-six-control set.*

## Selection rationale

The full control matrix populates the methodology's framework across all ten OWASP Top 10 for Agentic Applications categories, the five cross-cutting threat patterns of §3.2, and additional governance and evidence-capture areas. The matrix's depth supports comprehensive assurance posture; its depth is also a barrier to first adoption.

The Minimum Viable Assurance (MVA) subset below selects ten controls whose absence indicates the deployment has not been seriously assessed against the methodology's architectural concerns. The MVA is not a substitute for the full matrix; it is the first-pass set after which the full matrix populates the assurance posture.

The selection criterion was simple: a control belongs in the MVA if its absence would be the first thing a serious second-line or supervisory reviewer would identify as a gap.

## The ten controls

### Threat-pattern controls

**1. LT-01 — Lethal trifecta architectural review.** Configurations exhibiting the three architectural conditions (sensitive data access, untrusted input exposure, egress capability) require explicit architectural review with accountable-executive sign-off on the residual risk. The methodology's flagship analytical exercise.

**2. TF-01 — Toxic-flow analysis of authorised tool inventory.** Static analysis of the tool inventory identifying compositional paths from untrusted-input sources through privileged-data access to egress, with each path classified as remediated, gated, or accepted residual.

**3. IA-01 — Principal propagation through tool chains.** The identity of the requesting principal must propagate through the agent's tool invocations, or scope-narrowing controls must compensate for absent propagation. The deployment's structural authority concern.

### Identity and authority

**4. IA-03 — Authentication strength for high-authority actions.** Where the agent takes consequential action (auto-approval, payment instructions, decision routing), authentication and authorisation must be calibrated to the action's consequence.

### Tool inventory

**5. TP-01 — Tool metadata integrity verification.** Tools the agent can invoke must be qualified against an internal registry, with metadata pinning at session initialisation to detect tampering.

### Memory and context

**6. MC-01 — Retrieval-context integrity.** Where the agent's reasoning depends on retrieved context (RAG, vector store, memory), integrity controls verify that retrieved content has not been adversarially manipulated.

### Asynchronous processing

**7. ZC-01 — Asynchronous-processing risk gating.** Where the agent processes content without a human-in-the-loop at the moment of action (background indexing, queue-driven workflows), runtime policy gates control outbound actions triggered by background content.

### Evidence

**8. AT-01 — Runtime evidence capture.** Per-invocation capture of the assembled prompt, retrieved context, tool definitions, tool calls and outputs, model response, and final action, supporting after-the-fact reconstruction.

### Institutional infrastructure

**9. GP-01 — Deployment authorisation.** The deployment must have an authorisation record documenting its intended function, principal model, threat surface, and accountable executive — and the authorisation preconditions must have been completed (notably LT-01 and TF-01).

**10. HC-01 — Supervisory-engagement repository.** A consolidated, retrievable repository of the deployment's assurance artifacts (inventory, threat register, gap analysis, findings, evidence references), structured for supervisory dialogue without translation work.

## Sequencing for first adoption

For a deployment without prior assurance work, the methodology's *evidence-first* and *framework-anchored* principles suggest the following sequence:

1. **GP-01 first** (deployment authorisation) — the authorisation record forces the institution to specify the deployment's intended function, principal model, and accountable executive. Without this, the remaining controls have no clear referent.
2. **Then LT-01 and TF-01** — the architectural analyses. Their outputs inform the remaining controls' priority and shape the threat register and gap analysis downstream.
3. **Then AT-01** — runtime evidence capture is the precondition for after-the-fact reconstruction of any incident; it should be in place before consequential actions are authorised in production.
4. **Then IA-01 and IA-03** — principal propagation and authentication strength. Address the deployment's structural authority concerns.
5. **Then TP-01 and MC-01** — tool inventory integrity and retrieval-context integrity. Address the supply-chain and context-substrate concerns.
6. **Then ZC-01** — where the deployment is asynchronous-processing, the runtime gating.
7. **Then HC-01** — the supervisory-engagement repository consolidates the outputs from the above and is the artifact most visible to second-line and supervisory audiences.

The sequence is not a hard ordering — many of these controls are properly addressed in parallel — but the dependency structure is real, and starting with GP-01 plus LT-01 + TF-01 is the defensible entry point.

## What the MVA does not establish

- **MVA presence is not equivalent to full-matrix coverage.** The remaining sixteen controls of the v1.0 matrix address concerns the MVA does not surface — including evidence-capture privacy (AT-02), evidence reconstruction queryability (AT-03), second-line review cadence (HC-02), adversarial testing programme (GP-02), methodology revision (GP-03), inter-agent communication (IC-01), cascade prevention (CF-01), behavioural drift (RA-01), resource overload (RO-01), supply-chain qualification (TP-02, TP-03), egress inventory (LT-02), cross-deployment flow review (TF-02), content-source provenance (ZC-02), memory-poisoning detection (MC-02), and service-account authority limitation (IA-02).

- **MVA presence is not residual-risk acceptance.** Each MVA control's presence in an "implemented" state still requires the institution to articulate the residual risk that remains after implementation, and to accept that residual risk through the accountable executive.

- **MVA is not formal attestation.** ISAE 3000 / AT-C 205 attestation pathways require qualified-practitioner partnership and sit outside the methodology's scope.

## See also

- `paper/control_matrix.md` — the full v1.0 control matrix (twenty-six controls)
- `paper/full.md` §4 — methodology design principles and matrix structure
- `assurance_kit/` — templates for applying the methodology to a specific deployment
- `reference_application/` — worked example showing full-matrix application to a hypothetical deployment
- `CONTRIBUTING.md` — engagement channels for corrections, extensions, and engagement experience
