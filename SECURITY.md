# Security and coordinated disclosure policy

## Supported versions

The project is pre-alpha. Only the latest commit on the default branch is
maintained. It must not be used in production.

## Report a vulnerability

Use GitHub private vulnerability reporting when it is enabled for this
repository. If it is unavailable, open a non-sensitive issue requesting a
private contact channel; do not include vulnerability details, credentials,
personal data, target information or proof-of-concept material in that issue.

Reports should include:

- affected commit and component;
- safety or security invariant that fails;
- minimal reproduction using synthetic/loopback targets only;
- expected and observed result;
- potential impact and suggested remediation;
- whether information has been shared elsewhere.

Do not test this software against third-party or production PACS. A project bug
does not authorize access to any external system.

## Disclosure process

Maintainers will acknowledge, triage, reproduce in an isolated synthetic lab,
develop a fix and coordinate publication. Timelines depend on safety impact and
downstream coordination. We will credit reporters who request credit and whose
reports comply with authorization and safety requirements.

## Safety-critical classes

Treat the following as confidential until remediation and coordination:

- bypass of the deterministic policy decision point;
- ability to enable state-changing actions through configuration;
- target-scope bypass, SSRF, DNS rebinding or sandbox escape;
- leakage of model-provider credentials or private evidence;
- supply-chain compromise of a release;
- a feature that can interact with a real actuator or production PACS.

## Confidentiality boundary

Do not submit dormakaba or any other vendor's confidential information. Public
project maintainers cannot accept NDA material, customer configurations,
credentials, proprietary firmware, or unpublished third-party findings.
