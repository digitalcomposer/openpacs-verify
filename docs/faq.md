# Frequently asked questions

## What is OpenPACS Verify?

OpenPACS Verify is an open-source research project for safety-constrained,
AI-assisted security assurance of synthetic physical access control systems. It
combines a deterministic authorization boundary with evidence-based AI analysis.

## Is physical access control operational technology?

Yes. Physical access control systems can monitor or change the physical
environment through readers, controllers, alarms and locks. The project treats
them as cyber-physical OT and prioritizes safety, availability and human
oversight alongside confidentiality and integrity.

## Is this an OT vulnerability scanner?

No. The current Phase 0.5 release provides governance, a deny-by-default safety
kernel and decision-only authorization-binding semantics. It does not provide
process isolation, scan networks, discover Internet assets, execute exploits or
connect to production OT.

## Can OpenPACS Verify open doors or control locks?

No. The public architecture intentionally has no AI-to-actuator path. The policy
kernel rejects actuation, writes, exploitation and other state-changing action
types even if a policy file attempts to allow them.

## How is AI used safely?

The planned AI component receives synthetic or explicitly authorized evidence
and may propose structured findings or passive laboratory actions. Model output
is untrusted data. The implemented decision-only broker can bind a canonical
proposal to the complete policy with a short-lived, single-use grant. A future
separate broker process and adapter must independently verify that binding. No
AI component, execution adapter or OS isolation is implemented yet.

## What AI security risks are in scope?

The threat model includes prompt injection through logs or documentation,
unsafe tool use, scope escape, invented evidence, confidence miscalibration,
sensitive-data leakage, supply-chain compromise and automation bias.

## Which OT and AI security frameworks are considered?

The design draws on NIST SP 800-82, IEC 62443 concepts, MITRE ATT&CK for ICS,
NIST AI RMF, ENISA AI cybersecurity guidance, NIST SSDF and OWASP application
security guidance. Mappings express design intent; they are not certifications.

## Is the project compliant with the EU AI Act or Cyber Resilience Act?

The repository does not claim legal conformity or certification. It maintains a
dated applicability register for the EU AI Act, Cyber Resilience Act, GDPR,
NIS2 and related instruments. Legal duties depend on the actor, intended use,
data, market activity, jurisdiction and deployment context.

## Does the project reproduce vendor vulnerabilities or proprietary protocols?

No. Public research is used only to derive general security requirements. The
repository excludes vendor firmware, binaries, protocol schemas, confidential
documents, customer information, real credentials and unpublished findings.

## May I test a third-party access control system with it?

Not without explicit written authorization. The Apache-2.0 software license does
not grant permission to access or test any system. Production and real-actuator
testing are outside the public project's scope.

## What is PACS-SafetyBench?

PACS-SafetyBench is the planned synthetic evaluation corpus. It will contain
labelled benign, vulnerable, ambiguous and adversarial scenarios for measuring
finding precision, recall, evidence citation quality and prohibited-action
blocking.

## How can researchers contribute?

Start with `CONTRIBUTING.md` and the clean-room declaration. Contributions must
be original or compatibly licensed, synthetic, authorized and free of vendor,
customer, personal and confidential material.
