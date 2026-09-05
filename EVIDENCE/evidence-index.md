# OMEGA-X — Evidence Index

## Evidence hierarchy

- **E0** — assertion / narrative only
- **E1** — concrete repository artifact
- **E2** — reproducible execution
- **E3** — real pilot measurement
- **E4** — independent corroboration

## Current artifact set

| ID | Artifact | Evidence level | Status |
|---|---|---:|---|
| EV-001 | `fixtures/terraform-minimal/aws/main.tf` | E1 | Present |
| EV-002 | `fixtures/terraform-minimal/expected-target-mapping.md` | E1 | Present |
| EV-003 | `fixtures/terraform-minimal/expected-target-artifact.json` | E1 | Present |
| EV-004 | `fixtures/terraform-minimal/validation-result.json` | E1 | Present |
| EV-005 | `fixtures/terraform-minimal/validator.py` | E1 / E2-ready | Present |
| EV-006 | `fixtures/terraform-minimal/validate_schema.py` | E1 / E2-ready | Present |
| EV-007 | `fixtures/terraform-minimal/run-fixture.sh` | E1 / E2-ready | Present |
| EV-008 | `fixtures/terraform-minimal/runbook.md` | E1 / E2-ready | Present |
| EV-009 | `fixtures/terraform-minimal/CI-CHECKLIST.md` | E1 | Present |
| EV-010 | `fixtures/terraform-minimal/generate-evidence-manifest.py` | E1 / E2-ready | Present |
| EV-011 | `claim-evidence-matrix.md` | E1 | Present |

## Evidence that is deliberately not claimed yet

The following require actual execution or external records before they can be represented as completed evidence:

- live Alibaba Cloud execution,
- production deployment,
- customer traction,
- pilot KPI measurements,
- benchmarked percentage improvements,
- independently corroborated results.

## Interpretation

The repository now contains real artifacts demonstrating a controlled, non-production, fixture-level workflow. The fixture's machine-readable validation record keeps deployment blocked pending human approval and explicitly states that it is not evidence of cloud execution.

## Promotion rule

An item may be promoted from E1/E2 to E3 only after execution in a real or formally representative pilot has been captured with timestamp, environment, inputs, outputs, metrics, and reproducible references.

Do not manufacture evidence to fill a checklist gap.
