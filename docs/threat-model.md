# Threat model

## Scope and audience

This model covers the public OpenPACS Verify repository, its future synthetic
digital twin, evidence pipeline, AI analysis workflow, policy broker and
read-only adapters. It is for maintainers and security reviewers.

## Facts, assumptions and exclusions

### Observed facts

- The implemented policy kernel accepts declarative actions and performs no
  network or process execution.
- The decision-only broker binds an authorization grant to canonical action and
  policy digests and rejects expiry, mutation, forgery and replay.
- The broker is currently an in-process reference implementation, not process
  isolation or an OS sandbox.
- The default policy permits only loopback observations and validation.
- The public repository prohibits real PACS and confidential data.

### Assumptions

- AI models and imported evidence may be malicious or compromised.
- Contributors may make mistakes or attempt to weaken safeguards.
- A future digital twin will run on a workstation or CI runner with isolation.

### Exclusions

- Production deployment and real actuators.
- Vendor-specific vulnerability validation.
- Safety certification or legal conformity assessment.

## Abuse cases and STRIDE analysis

| ID | Threat | STRIDE | Primary control | Residual risk |
|---|---|---|---|---|
| TM-01 | Evidence contains instructions that hijack the AI planner | T/E | Treat evidence as quoted data; schema output; policy broker | Model may still produce misleading findings |
| TM-02 | Model proposes an operational or external target | E | IP literals, scoped networks, action allow-list | Policy defect or unsafe future adapter |
| TM-03 | Contributor adds an actuator operation | T/E | Invariant tests, review, protected branches | Maintainer collusion or compromised account |
| TM-04 | DNS rebinding redirects an allowed hostname | S/T | Hostnames prohibited at the policy boundary | Unsafe resolver added later |
| TM-05 | Findings invent evidence or severity | R | Evidence IDs, confidence, abstention, human review | Reviewer automation bias |
| TM-06 | Logs disclose PINs, credentials or access events | I | Synthetic data; parameter denial; structured redaction | Novel sensitive fields not classified |
| TM-07 | Crafted evidence exhausts parser/model resources | D | Size/time limits, bounded schemas, isolation | Complex decompression/parser attacks |
| TM-08 | Compromised dependency or CI modifies release | T | Minimal dependencies, pinned actions, provenance | Upstream CI compromise |
| TM-09 | Hosted model retains confidential evidence | I | Public/synthetic data only; provider review | User bypasses project rules |
| TM-10 | Lab network is bridged to production | S/E | Loopback default, no external route, preflight checks | Host misconfiguration |
| TM-11 | A denial is interpreted as proof of safety | R | Explicit scope and evidence status | User overconfidence |
| TM-12 | Framework mapping is represented as certification | R | Disclaimer, traceable controls, review dates | Downstream marketing misuse |
| TM-13 | Action fields are mutated after authorization | T/E | Canonical digest binding and adapter-side verification contract | Future adapter not yet implemented |
| TM-14 | A valid authorization is replayed | S/E | Expiring single-use nonce and bounded replay cache | Multi-process persistence not yet implemented |
| TM-15 | In-process caller bypasses broker semantics | E | Planned separate broker process and OS sandbox | Current Phase 0.5 is not isolated |

## Highest-priority risks

1. An execution path bypasses the deterministic policy broker.
2. The laboratory becomes connected to a real access-control environment.
3. Confidential or personal data is submitted to the repository or a model.
4. AI-generated claims are published without evidence and human verification.
5. Users treat research-framework mappings as legal conformity.

## Mitigation roadmap

- Keep architecture tests that reject network/process authority in the
  decision-only package.
- Move grant issuance and consumption into a separate least-privilege broker
  process with bounded local protocol messages.
- Add an operating-system sandbox and no-default-route preflight.
- Define signed authorization manifests with expiry and purpose.
- Add evidence object hashes and structured finding schemas.
- Add prompt-injection and data-exfiltration benchmark cases.
- Introduce release provenance, dependency review and protected branches.

## Residual risk decision

Phase 0.5 is acceptable for local policy and authorization-binding evaluation
only. Its grants do not prove runtime isolation. Network collection,
model-provider integration, adapters and any external pilot remain **not
approved** until the separate broker, sandbox, controls and adversarial tests
are implemented and reviewed.

## Review triggers

- new tool adapter or network capability;
- model/provider integration;
- processing of non-synthetic evidence;
- change to policy schema or safety invariants;
- public release, commercialization or an authorized external pilot.
