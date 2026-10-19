# Public source and provenance ledger

Only public sources may motivate the public project's requirements. Entries are
summaries and links, not copied content. Last checked 2026-10-19.

## Public vulnerability research motivating generic requirements

| ID | Source | Use in this project |
|---|---|---|
| SRC-PACS-01 | [SEC Consult: Multiple Critical Vulnerabilities in dormakaba Access Manager](https://sec-consult.com/vulnerability-lab/advisory/multiple-critical-vulnerabilities-in-dormakaba-access-manager/) | General failure classes: control-plane authentication, transport protection, sessions, secrets, diagnostics, privilege, platform and update security. No vendor implementation is reproduced. |
| SRC-PACS-02 | [SEC Consult: Hands-Free Lockpicking](https://sec-consult.com/blog/detail/hands-free-lockpicking-critical-vulnerabilities-in-dormakabas-physical-access-control-system/) | General PACS architecture, attack-precondition and segmentation lessons. No figures, code, tables or protocol details are copied. |
| SRC-PACS-03 | [dormakaba public security advisories](https://www.dormakabagroup.com/en/security-advisories) | Confirms public coordinated-disclosure and remediation context. Not used as product implementation input. |

## Law and official EU guidance

| ID | Source | Use in this project |
|---|---|---|
| SRC-EU-01 | [Artificial Intelligence Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | Primary AI legal reference. |
| SRC-EU-02 | [European Commission AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Current application timeline and official risk-classification overview. |
| SRC-EU-03 | [Cyber Resilience Act, Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) | Primary product-cybersecurity legal reference. |
| SRC-EU-04 | [Commission CRA implementation timeline](https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation) | Current reporting and full-application dates. |
| SRC-EU-05 | [Commission CRA open-source guidance](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source) | Initial non-commercial FOSS and steward applicability analysis. |
| SRC-EU-06 | [NIS2 Directive (EU) 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) | Operator risk-management, supply-chain, incident and vulnerability-handling context. |
| SRC-EU-07 | [Commission NIS2 overview](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) | Official scope summary and national-transposition context. |
| SRC-EU-08 | [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Personal-data governance baseline. |
| SRC-EU-09 | [ENISA multilayer cybersecurity framework for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai) | Baseline, AI-specific and sector-specific security structure. |
| SRC-EU-10 | [ENISA cybersecurity of AI and standardisation](https://www.enisa.europa.eu/publications/cybersecurity-of-ai-and-standardisation) | Standards landscape and gap-awareness input. |

## Security frameworks

| ID | Source | Use in this project |
|---|---|---|
| SRC-FW-01 | [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | OT definition, safety/reliability constraints and defensive architecture. |
| SRC-FW-02 | [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) | Govern, Map, Measure and Manage research lifecycle. |
| SRC-FW-03 | [MITRE ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) | Threat-behaviour mapping for synthetic scenarios. |
| SRC-FW-04 | [IEC 62443-4-1 public catalogue entry](https://webstore.iec.ch/en/publication/33615) | Secure development lifecycle scope. Normative content is not reproduced. |

## Program-alignment context

| ID | Source | Use in this project |
|---|---|---|
| SRC-AI-01 | [Anthropic Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program) | Public description of defensive access tiers and verification expectations; not a project endorsement. |
| SRC-AI-02 | [Anthropic Cyber Mission](https://www.anthropic.com/news/anthropic-cyber-mission) | Public critical-infrastructure and open-source defence priorities; not a project endorsement. |

## Excluded inputs

- non-public or NDA material;
- vendor firmware, binaries, schemas, source code and licensed tools;
- customer or installation documentation;
- captured production traffic;
- real badge, PIN, access-event, biometric or identity information;
- unpublished vulnerability details;
- remembered confidential facts, even if rewritten.

Any contributor uncertain about provenance must omit the material and request a
maintainer review without disclosing it in a public issue.
