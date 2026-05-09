# Source Status

*Companion to the position paper. Catalogues the load-bearing sources by evidentiary status so the reader can see, at a glance, which kinds of evidence underlie which kinds of claim.*

## Convention

The paper makes claims of varying evidentiary status. This document sorts the load-bearing sources and claims into four buckets:

- **Primary regulatory and standards documents** — official sources whose authority derives from the issuing institution. Cited as the institution states them; no inference beyond document content.
- **Direct technical disclosures** — first-party security disclosures (CVE records, vendor advisories, researcher-disclosed incidents with vendor confirmation). Time-stamped, attributable, reproducibly cited.
- **Secondary technical analyses** — academic papers, security-firm analyses, attribution claims that synthesise primary technical material into named patterns or threats.
- **Inferential or generalised claims** — places where the paper makes claims that depend on inference from available evidence rather than direct primary verification. The paper text marks these explicitly where they occur.

Verification of each source's identifier, date, and substantive content was performed in v0.7 (four high-priority citations) and v0.8 (batch resolution of all remaining markers); the full audit trail is in `verification_log.md`.

## Bucket 1 — Primary regulatory and standards documents

### EU regulation
- AI Act (Regulation (EU) 2024/1689) — entered into force 1 August 2024; articles 6, 12, 14, 15 cited; Annex III sections 5(b) and 5(c) cited
- Digital Omnibus on AI proposal (COM(2025) 836, 19 November 2025) — proposes deferral of high-risk obligations to 2 December 2027 (stand-alone) and 2 August 2028 (product-embedded)
- DORA (Regulation (EU) 2022/2554) — articles 9, 17–18, 24–27, 28 cited
- DORA RTS — 2024/1774 (ICT risk management), 2025/532 (subcontracting), 2025/1190 (threat-led penetration testing)
- GDPR (Regulation (EU) 2016/679) — articles 25, 33, 34 cited

### International standards
- ISO/IEC 42001:2023 (AI Management System) — December 2023
- ISO/IEC 27001:2022 (Information Security Management System) — October 2022
- ISO/IEC 23894:2023 (AI Risk Management Guidance)

### NIST publications
- NIST AI Risk Management Framework 1.0 — January 2023
- NIST AI 600-1 (Generative AI Profile) — July 2024
- NIST Cybersecurity Framework 2.0 — 26 February 2024
- NIST SP 800-207 (Zero Trust Architecture) — August 2020

### Audit and assurance standards
- ISAE 3000 (Revised) — IAASB (assurance engagements other than audits or reviews of historical financial information)
- AT-C 205 — AICPA (examination engagements)

### Supervisory communications and guidance
- Federal Reserve SR 26-2 — 17 April 2026 (jointly issued with OCC and FDIC; supersedes SR 11-7 and SR 21-8; explicitly excludes generative AI and agentic AI from MRM scope)
- PRA SS1/23 (Model Risk Management Principles for Banks) — 17 May 2023, effective 17 May 2024
- ECB SSM Supervisory Priorities 2026–2028 — 18 November 2025
- BaFin *Guidance on ICT Risks in the Use of AI at Financial Entities* — 18 December 2025 (German); 30 January 2026 (English)
- ACPR Beau Lisbon speech ("A compass to guide us toward intelligent AI supervision") — 27 October 2025; corresponding article in *Archives de philosophie du droit* Tome 66 (November 2025)
- DNB *AI bij verzekeraars / AI at Insurers: opportunities and risks* — 27 March 2025
- CSSF (with Banque centrale du Luxembourg) *Second Thematic Review on the use of Artificial Intelligence in the Luxembourg Financial Sector* — 16 May 2025
- EIOPA Opinion BoS-25-360 (Opinion on AI Governance and Risk Management) — 6 August 2025
- BoE Financial Policy Committee *Financial Stability in Focus: AI in the financial system* — 9 April 2025
- EBA AI Act mapping — factsheet 21 November 2025; full annex letter to Berrigan/Viola 17 December 2025
- FSB *The Financial Stability Implications of Artificial Intelligence* — 14 November 2024

### Frameworks and protocols cited as regulatory or standards anchors
- CBEST framework — Bank of England, 2014
- TIBER-EU framework — ECB, May 2018
- Model Context Protocol specification — Anthropic launch 25 November 2024; specification revision 18 June 2025 (OAuth 2.0 Resource Server classification, RFC 9728 Protected Resource Metadata, RFC 8707 Resource Indicators); donation to Linux Foundation AAIF 9 December 2025

## Bucket 2 — Direct technical disclosures

### Disclosed incidents with vendor confirmation
- **EchoLeak** — CVE-2025-32711 (Microsoft as CNA, 11 June 2025; CVSS 9.3 Critical via Microsoft, 7.5 High via NVD enrichment); discloser Aim Labs (Aim Security)
- **SpAIware** — Johann Rehberger, disclosed at BSides Vancouver Island 20 September 2024
- **AgentFlayer** — Zenity Labs (Michael Bargury, Tamir Ishay Sharbat), Black Hat USA 6 August 2025
- **Shadow Escape** — Operant AI, 22 October 2025
- **Asana MCP incident** — 4–17 June 2025; ~1,000 customers affected; tenant-isolation logic flaw confirmed by Asana spokesperson
- **Invariant Labs GitHub MCP disclosure** — 26 May 2025; vector via issue body, exfiltration via public PR
- **General Analysis Supabase/Cursor disclosure** — 6 July 2025; PoC on synthetic data with corroboration by Simon Willison and Supabase security team
- **Snyk × Invariant acquisition and Snyk Agent Scan launch** — 24 June 2025; toxic-flow detection rule TF001
- **Month of AI Bugs** — Johann Rehberger, August 2025; 20+ daily disclosures across ChatGPT, Codex, Anthropic MCPs, Cursor, Amp, Devin, OpenHands, Claude Code, GitHub Copilot, Google Jules

### Vendor security advisories and changelogs cited
- Microsoft Security Response Center records for AI assistant vulnerabilities
- Anthropic, OpenAI, Google MCP and agent-tooling security advisories (where referenced)
- GitHub MCP server documentation and security responses

## Bucket 3 — Secondary technical analyses

### Frameworks, taxonomies, benchmarks
- **OWASP Top 10 for Agentic Applications** — released 9 December 2025 at London Agentic Security Summit / Black Hat Europe 2025; categories ASI01–ASI10
- **MCPTox benchmark** — arXiv:2508.14925 (August 2025); AAAI 2026 proceedings
- **AgentDojo benchmark** — Debenedetti et al., NeurIPS 2024 Datasets and Benchmarks Track (arXiv:2406.13352); maintained by ETH Zurich SPY Lab; extended through joint UK/US AI Safety Institute red-teaming exercise
- **LangGraph** — LangChain Inc., MIT-licensed framework; production users including Klarna, Replit, Elastic, Uber, J.P. Morgan

### Attributions and named patterns
- **Lethal trifecta** — coined by Simon Willison, blog post 16 June 2025 ("The lethal trifecta for AI agents: private data, untrusted content, external communication")
- **Toxic flow analysis** — methodology synthesised from Snyk × Invariant work; the paper's compositional framing distinct from the methodology itself
- Tool poisoning (metadata-layer) — distinguished in §3.2.1 with MCPTox as canonical example; the paper applies a strict metadata-only definition

### Security-firm and researcher analyses
- Aim Labs, Zenity Labs, Operant AI, General Analysis, Invariant Labs, Embrace The Red, Snyk — cited where they provide direct analyses or disclosures
- Academic papers on prompt injection, agent security, and adversarial attacks (cited where directly relevant to specific claims)

## Bucket 4 — Inferential or generalised claims

These places acknowledge in the paper text that the claim depends on inference or available evidence rather than direct primary verification.

- **Reference deployment configuration (§5).** Described in §5.2 as "plausible as a representative pattern, not that any specific institution operates exactly this configuration." Inference rests on publicly disclosed deployment patterns rather than direct observation of any institution's configuration.

- **Macroprudential references (§3.3).** BoE FPC, ECB FSR, IMF GFSR, and BIS publications referenced in generalised form. The body text was deliberately generalised away from specific publication identifiers (e.g., BIS Papers 154, IMF GFSR Chapter 3 specifics, ECB FSR Leitner et al., Lopez-Lira NBER WP 34054) where primary-source verification of those identifiers was not feasible within scope. The substantive claim — that concentration and correlation are flagged macroprudential concerns — is supported by the FSB report (Bucket 1) and the broader regulatory record.

- **Deployment-pace characterisations (§1.3, §6).** Based on supervisory communications, vendor disclosures, and public reporting rather than direct industry-survey data. Framed as "as of early 2026"; the paper does not claim direct measurement.

- **Tier-2 EU financial-services market characterisation.** Based on aggregate statistics from EIOPA, DNB, and CSSF supervisory publications (Bucket 1), not on direct market research by the paper's author.

- **AI Board Subgroup on Financial Services framing (§1.3).** Refers to the EU AI Board's structure rather than an ECB-internal body; the paper's framing was softened in v0.8 to reflect institutional engagement signalling rather than a specific structural commitment by the ECB.

- **Regulator-legibility design principle as a discrete claim.** The principle's status as discrete from framework-anchoring is an analytical claim made by the paper rather than a finding from external evidence. The paper presents the argument; the reader assesses it.

## Reading guidance

A reader assessing the paper's evidentiary discipline can use this document in two ways. First, to spot-check any claim against the source bucket it draws from: a Bucket 1 claim should be reproducible by reading the cited document; a Bucket 4 claim should be read with the explicit caveat the paper attaches to it. Second, to assess where the paper's confidence is concentrated: most load-bearing claims sit in Buckets 1 and 2; the architectural argument and the design principles in §4 are analytical contributions of the paper itself, supported by but not derived from the bucketed sources.

The verification log documents the audit trail for each marker resolved during paper preparation; this document sits alongside it as the publication-level evidentiary map.
