# OMEGA-X Alpha 0.4 — Real Artifact Record

## Evidence status

This record documents **repository-level artifacts that are actually present**. It does not claim that the source system has been executed by Alibaba Cloud, that a customer has used it, or that any performance percentage has been independently validated.

## Artifacts

| Artifact | Purpose | Evidence level |
|---|---|---|
| `fixtures/terraform-minimal/aws/main.tf` | Reproducible source Terraform fixture | E1 |
| `fixtures/terraform-minimal/expected-target-mapping.md` | Human-readable source-to-target mapping proposal | E1 |
| `fixtures/terraform-minimal/expected-target-artifact.json` | Machine-readable target artifact | E1 |
| `fixtures/terraform-minimal/validation-result.json` | Explicit validation/deployment gate record | E1 |
| `fixtures/terraform-minimal/runbook.md` | Reproducibility procedure | E1/E2 candidate |
| `fixtures/terraform-minimal/SHA256SUMS.txt` | Placeholder manifest requiring recomputation after final artifact freeze | E0 until recomputed |

## What can be claimed now

- A concrete, non-production fixture exists in the repository.
- The expected target mapping is explicit rather than implied.
- The target artifact is machine-readable.
- The fixture contains no production credentials.
- The deployment gate is intentionally blocked pending validation and authorization.

## What cannot be claimed yet

- Successful execution against Alibaba Cloud infrastructure.
- Customer production migration.
- 60% migration-cycle reduction.
- 70% audit-cost reduction.
- 40% AI-cost reduction.
- Any production conversion rate.

## Final evidence upgrade path

To upgrade this record from E1 to E2/E3:

1. Freeze the fixture commit.
2. Run the parser/translator locally.
3. Record tool and runtime versions.
4. Capture generated artifacts and validation output.
5. Recompute SHA-256 checksums.
6. Repeat the run from the same commit.
7. Compare outputs byte-for-byte or via canonical serialization.
8. For E3, run the workflow on an authorized Alibaba Cloud pilot and attach measured results.
