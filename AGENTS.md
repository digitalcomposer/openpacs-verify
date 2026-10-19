# Repository instructions

## Safety boundary

- Work only with synthetic fixtures, loopback services, documentation supplied
  under a compatible license, or systems for which written authorization is in
  the repository's private evidence record.
- Never add production targets, Internet scanning, real credentials, actuator
  operations, door-control commands, vendor firmware, proprietary binaries,
  confidential documents, customer data, or unpublished vulnerability details.
- The AI layer may propose declarative actions only. All execution must pass
  through the deterministic policy engine.
- A missing or ambiguous authorization condition must fail closed.

## Provenance

- Record every external source used to derive a requirement in
  `docs/source-ledger.md`.
- Paraphrase and cite. Do not copy diagrams, tables, exploit code, screenshots,
  protocol schemas or substantial text from third parties.
- Keep facts, assumptions and design decisions visibly separated.

## Engineering

- Python 3.11+ and standard library by default.
- Add tests for every policy decision and every denied safety case.
- Run `python3 -m unittest discover -s tests -v` before committing.
- Security-relevant changes require an updated threat model or an explicit note
  explaining why the model is unaffected.
