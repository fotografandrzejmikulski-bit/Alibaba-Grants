# Fixture Evidence CI Gate

A future CI workflow may enforce these checks automatically before an evidence commit is accepted.

## Required checks

- [ ] Fixture source is sanitized.
- [ ] No credentials, access keys, private endpoints, or customer identifiers are present.
- [ ] Validator exits with code `0`.
- [ ] Target artifact parses as JSON.
- [ ] Expected output remains non-deployable.
- [ ] Deployment gate remains human-approval dependent.
- [ ] SHA-256 manifest is regenerated.
- [ ] Evidence classification is explicitly stated.
- [ ] No benchmark percentage is presented without measured data.

## Evidence rule

A green fixture check demonstrates reproducibility of the fixture-level workflow only. It must never be represented as proof of live cloud execution, customer adoption, production readiness, or commercial performance.
