# Case studies

Public cases test the methodology against different failure modes. Each analysis distinguishes what the sources establish, what the methodology can assess, and what remains unknown. Retrospective analysis does not establish that the framework would have prevented an incident.

## Choose a case

| Case | Evidence status | Assurance question | Start here |
|---|---|---|---|
| **OpenAI–Hugging Face, July 2026** | Documented intrusion; first-party accounts and an independent investigation with a bounded scope | Does the deployment boundary include shared infrastructure, unexpected communication, and trustworthy execution evidence? | [Case study](openai_huggingface.md); [control-gap assessment and reusable scenario](openai_huggingface_control_assessment.md) |
| **EchoLeak, CVE-2025-32711, June 2025 disclosure** | Research demonstration of a vulnerability; the cited disclosures report no known in-the-wild exploitation | Can untrusted retrieved content compose with sensitive-data access and response-rendering egress? | [Case study](echoleak.md); [worked finding](echoleak.md#7-the-supervisory-engageable-finding) |

The OpenAI–Hugging Face case tests the framework's limits, including the matrix's acknowledged code-execution gap. EchoLeak demonstrates the methodology's application to a compositional exfiltration path. The [reference application](../reference_application/README.md) supplies a separate, prospective example against a hypothetical insurance deployment.

## How to use the analyses

1. Read the case summary and evidence limits before drawing comparisons with your deployment.
2. Identify the relevant trust boundaries and controls in the [published matrix](../paper/control_matrix.md).
3. Turn the comparison into an assessment scenario with expected behaviour, required evidence, an owner, and acceptance criteria.
4. Record findings and unresolved questions using the [assurance kit](../assurance_kit/README.md). Record an untested control as untested; absence of public evidence does not establish absence of a vendor control.

The [OpenAI–Hugging Face assessment](openai_huggingface_control_assessment.md#reusable-assessment-scenario) provides a ready-to-adapt scenario. It is an assessment specification; no deployment tests have been executed for this repository.

## Evidence and contribution standard

Use distinct labels for a confirmed intrusion, a demonstrated vulnerability, and a hypothetical application. Attribute vendor statements and independent findings separately, date the evidence reviewed, and identify investigation limits. Separate control applicability from evidence of implementation and effectiveness.

New cases should contribute a different deployment context, failure mode, or methodology gap. Contributions should include a sourced account, a control assessment, a worked finding or reusable assessment scenario, and explicit limits on counterfactual claims. Follow the [contribution process](../CONTRIBUTING.md) for substantive additions.

[Repository overview](../README.md) · [Project roadmap](../ROADMAP.md)
