# Gap Analysis — [Agent ID]

*Control-by-control evaluation of the deployment specified in `deployment_specification.md` against the v1.0 control matrix at `paper/control_matrix.md`. Mirrors the structure of `reference_application/gap_analysis.md`.*

## Conventions

Each control from the matrix is evaluated against four possible states. *Present* means the control's substantive requirements are implemented in the current deployment, possibly with operational refinements still useful but not addressing material gaps. *Partially present* means some elements of the control's requirements are implemented, but material gaps remain. *Absent* means the control's substantive requirements are not implemented. *Not applicable* means the control does not apply to the current deployment configuration (recorded explicitly so the evaluation status is visible rather than implicit).

For each Partially-present and Absent control, the gap analysis specifies the gap, the operational consequence, and the recommended remediation. The gap analysis does not estimate implementation cost or timeline; those are properly the institution's operational decisions.

## Controls

### Tool poisoning (TP)

**TP-01 — Tool metadata integrity verification — [Present / Partially present / Absent / Not applicable]**

[If Partial or Absent: describe the gap, operational consequence, and remediation. If Present: brief confirmation of how the substantive requirements are met.]

**TP-02 — Third-party MCP server qualification — [state]**

[...]

**TP-03 — First-party tool change control — [state]**

[...]

### Identity and privilege abuse (IA)

**IA-01 — Principal propagation through tool chains — [state]**

[...]

**IA-02 — Service-account authority limitation — [state]**

[...]

**IA-03 — Authentication strength for high-authority actions — [state]**

[...]

### Lethal trifecta (LT)

**LT-01 — Lethal trifecta architectural review — [state]**

[...]

**LT-02 — Egress-channel inventory and control — [state]**

[...]

### Toxic flows (TF)

**TF-01 — Toxic-flow analysis of authorised tool inventory — [state]**

[...]

**TF-02 — Cross-deployment flow review — [state]**

[...]

### Zero-click exfiltration (ZC)

**ZC-01 — Asynchronous-processing risk gating — [state]**

[...]

**ZC-02 — Content-source provenance preservation — [state]**

[...]

### Memory and context poisoning (MC)

**MC-01 — Retrieval-context integrity — [state]**

[...]

**MC-02 — Memory-poisoning detection and response — [state]**

[...]

### Resource overload (RO)

**RO-01 — Resource-consumption limits and degradation behaviour — [state]**

[...]

### Evidence and audit (AT)

**AT-01 — Runtime evidence capture — [state]**

[Cross-reference `evidence_capture_checklist.md` for the operational specification.]

**AT-02 — Evidence-capture privacy controls — [state]**

[...]

**AT-03 — Evidence-store reconstruction queryability — [state]**

[...]

### Supervisory readiness (HC)

**HC-01 — Supervisory-engagement repository — [state]**

[Cross-reference `supervisory_engagement_pack_template.md` for the consolidating artifact.]

**HC-02 — Second-line review cadence — [state]**

[...]

### Governance process (GP)

**GP-01 — Deployment authorisation — [state]**

[Cross-reference the agent inventory entry and the deployment specification's authorisation record.]

**GP-02 — Adversarial testing programme — [state]**

[...]

**GP-03 — Methodology revision and learning — [state]**

[...]

### Inter-agent communication (IC)

**IC-01 — Inter-agent message authentication and policy enforcement — [state]**

[For multi-agent deployments — where the agent communicates directly with other agents — evaluate against the control's substantive requirements. For single-agent deployments, mark *Not applicable in current configuration* explicitly, and note that cross-deployment shared-infrastructure concerns belong under TF-02 (cross-deployment flow review) and CF-01 (failure-domain isolation) rather than under IC-01.]

### Cascading failures (CF)

**CF-01 — Failure-domain isolation and cascade prevention — [state]**

[...]

### Rogue agent / behavioural drift (RA)

**RA-01 — Agent-behaviour drift detection and response — [state]**

[...]

## Aggregate gap assessment

[Total counts: X Present / X Partially present / X Absent / X Not applicable. Cross-reference the threat register's aggregate severity. Note: counts should sum to twenty-six.]

## Priority remediation guidance

The methodology does not specify priority order; remediation prioritisation is properly the institution's decision based on risk appetite, operational constraints, and regulatory exposure. The following observations may inform prioritisation:

- The principal-model gap (IA-01), if Absent, underlies multiple downstream controls and is usually the highest-leverage remediation.
- The runtime evidence-capture gap (AT-01), if Absent, is the precondition for after-the-fact reconstruction of any incident.
- The supervisory-engagement repository gap (HC-01), if Absent, is the gap most visible to a supervisory reviewer.
- The lethal-trifecta and toxic-flow analyses (LT-01, TF-01), if Absent, are the methodology's most visible analytical gaps.

`MINIMUM_VIABLE_ASSURANCE.md` at the repository root selects ten of the twenty-six controls as a first-pass adoption subset; absent any prior prioritisation, that subset is a defensible starting point.

## See also

- `finding_template.md` — finding format per gap requiring documentation
- `paper/control_matrix.md` — the full matrix
- `reference_application/gap_analysis.md` — worked example
- `MINIMUM_VIABLE_ASSURANCE.md` — ten-control subset for first-pass adoption
