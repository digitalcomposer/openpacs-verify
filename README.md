# OpenPACS Verify

[![CI](https://github.com/digitalcomposer/openpacs-verify/actions/workflows/ci.yml/badge.svg)](https://github.com/digitalcomposer/openpacs-verify/actions/workflows/ci.yml)

Open-source, safety-constrained and vendor-neutral assurance tooling for
AI-assisted security research on physical access control systems (PACS),
operational technology (OT) and cyber-physical systems.

OpenPACS Verify combines OT security, AI agent safety, LLM security, threat
modeling and evidence-based verification. It is designed as a reproducible
research platform for defensive analysis—not as a production scanner or door
control system.

> [!IMPORTANT]
> OpenPACS Verify is for synthetic environments and systems you own or are
> explicitly authorized to test. It must never be connected to a production
> access-control network or a real actuator.

## Why this project exists

Physical access control is operational technology: a software decision can
change physical state. OpenPACS Verify explores whether an AI-assisted analyst
can turn evidence into reproducible defensive findings while a deterministic
policy layer prevents out-of-scope or state-changing actions.

The project is vendor-neutral. Public vulnerability research motivates generic
assurance requirements, but this repository contains no vendor firmware,
software, protocol implementation, confidential material, customer data, or
real credentials.

## Research question

Can a safety-constrained AI workflow identify and explain PACS security
weaknesses from synthetic evidence while technically preventing commands that
could change real physical state?

## Who this is for

- OT, ICS and cyber-physical security researchers;
- physical access control and building-security engineers;
- AI security, LLM security and agent-safety evaluators;
- universities and maintainers building synthetic security benchmarks;
- defenders studying IEC 62443, NIST SP 800-82 or NIST AI RMF workflows.

See the [frequently asked questions](docs/faq.md) for concise explanations of
the project scope, terminology, AI safety model and legal limitations.

## Current status

**Phase 0.5: decision-only broker semantics.** The repository currently provides:

- a deny-by-default action authorization kernel;
- canonical action envelopes and short-lived, policy-bound, single-use grants;
- mutation, expiry, forgery, replay and duplicate-key rejection tests;
- an executable CLI and unit tests;
- the initial security architecture and STRIDE threat model;
- a clean-room and coordinated-disclosure policy;
- an EU legal and standards applicability register;
- an evidence-source ledger and research roadmap.

It does **not** yet provide process isolation, an OS sandbox, an execution
adapter, an AI model integration, a controller emulator, scanner, exploit
modules, or production integration. The implemented broker module defines and
tests authorization semantics only; it must not be described as an isolation
boundary.

## Safety kernel quick start

Requires Python 3.11 or newer and has no runtime dependencies.

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m openpacs_verify.cli \
  --policy policies/lab-policy.json \
  --action '{"kind":"observe","target":"127.0.0.1","operation":"health"}'
```

The default policy permits passive observations against `127.0.0.1` only. It
denies hostnames, external addresses, nested credential-bearing parameters and
every state-changing or actuator action. The decision-only broker additionally
binds an authorization grant to the canonical action and complete policy,
expires it, and accepts it once. It performs no network or process execution.

## Design principles

1. **No direct AI-to-actuator path.** Model output is untrusted input.
2. **Deny by default.** A deterministic policy engine makes every authorization
   decision.
3. **Evidence before conclusions.** Findings must reference reproducible,
   integrity-protected evidence.
4. **Synthetic data by default.** Personal, customer and confidential data are
   outside the public project's scope.
5. **Human accountability.** AI proposes; authorized humans approve higher-risk
   laboratory work and own all published conclusions.
6. **Safe failure.** Ambiguity, malformed input or missing policy produces a
   denial, never an operational action.

## Documentation

- [Research plan](docs/research-plan.md)
- [Architecture](docs/architecture.md)
- [Threat model](docs/threat-model.md)
- [Security controls](docs/security-controls.md)
- [EU legal and framework register](docs/eu-legal-framework.md)
- [Public source ledger](docs/source-ledger.md)
- [Frequently asked questions](docs/faq.md)
- [Security and disclosure policy](SECURITY.md)
- [Contributing and clean-room rules](CONTRIBUTING.md)
- [AI-readable project index](llms.txt) — experimental community convention

## Research metadata

- [`CITATION.cff`](CITATION.cff) provides GitHub-readable citation metadata.
- [`codemeta.json`](codemeta.json) provides machine-readable research-software
  metadata.
- [`llms.txt`](llms.txt) is a curated project index for AI retrieval systems.
  It is an experimental convention and does not grant crawler permission or
  guarantee inclusion in any AI search engine.

## Legal position

This repository is research software, not a compliance certification or legal
opinion. Applicability of the EU AI Act, Cyber Resilience Act, GDPR, NIS2 and
sector-specific law depends on the actor, deployment, market activity, data,
jurisdiction and whether the system can influence safety or access decisions.
See the maintained [applicability register](docs/eu-legal-framework.md).

## License

Apache License 2.0. Documentation and source citations remain subject to their
respective authors' rights. The license does not grant permission to test any
third-party system.
