# Security

## Reporting concerns

The work in this repository concerns the assurance of AI agent deployments in regulated financial services. The repository itself does not host code, deployed systems, or vulnerable services; the substantive content is methodology and analytical writing.

The following classes of concern warrant the dedicated channel below rather than public GitHub issues:

**Methodology errors with security consequences.** Specific places where the methodology's recommendations would, if followed, increase rather than reduce risk; specific controls whose specification contains errors that would mislead implementers; specific test procedures whose execution would itself create risk.

**Identification of confidential or sensitive information.** Places where the work inadvertently includes confidential information, identifies specific institutions or individuals where it should not, or otherwise discloses content that should not be public.

**Information about real incidents not yet publicly disclosed.** The work cites public security disclosures; if the work inadvertently references a non-public incident or contains information that would compromise an ongoing disclosure process, this should be reported privately rather than discussed publicly.

**Concerns about the work's use in adversarial contexts.** Specific concerns that the methodology, the case study, or the reference application could be used to facilitate harm — for example, by serving as a guide for attacking agent deployments rather than as a guide for assuring them.

## How to report

Use the contact mechanism on the author's GitHub profile, marked as a security concern. Do not open public issues for these classes of concern.

The work is preliminary and the maintainer is solo; response time depends on the substance and urgency of the concern. Concerns identifying immediate harm receive priority; concerns that would benefit from substantive consideration may take longer.

## What this is not

The repository is not a vulnerability disclosure channel for products, services, or third-party systems. If you have identified a vulnerability in:

- Microsoft 365 Copilot or other Microsoft products: Microsoft Security Response Center (MSRC).
- Other vendor products: that vendor's security disclosure programme.
- An MCP server or agent framework: the relevant project's security policy.
- A specific institution's AI deployment: the institution directly.

The work cites public disclosures from these channels; it is not itself a venue for new disclosures.

The repository is also not a venue for advice on responding to active security incidents. Institutions experiencing or suspecting active security incidents involving AI agents should engage their incident response teams, qualified incident response providers, and the relevant supervisory authorities under their regulatory regime (DORA Article 19, GDPR Articles 33-34, or equivalent obligations).

## Coordinated disclosure

The work cites public security disclosures involving specific products and incidents. The citations follow responsible disclosure conventions — referencing the disclosing party, the affected vendor, the CVE record where applicable, and the public account of the disclosure rather than reproducing technical detail beyond what the public account establishes.

If you believe a citation in the work mischaracterises a disclosure, identifies parties beyond what the public account permits, or otherwise falls short of responsible disclosure conventions, this is a Security-channel concern rather than a public-issue concern.
