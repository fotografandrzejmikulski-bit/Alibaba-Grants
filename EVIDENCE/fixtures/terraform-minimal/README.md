# OMEGA-X Minimal Terraform Evidence Fixture

This fixture is a **sanitized, non-production, offline demonstration** of the OMEGA-X source-to-target evidence workflow.

## What it proves

It provides a repeatable test object containing:

- a minimal AWS Terraform source descriptor,
- an expected source-to-target mapping,
- a machine-readable target artifact,
- deterministic validation rules,
- SHA-256 checksums,
- a runbook.

## What it does not prove

It does **not** prove:

- live AWS execution,
- live Alibaba Cloud execution,
- production readiness,
- customer adoption,
- benchmarked percentage improvements,
- commercial conversion.

Those claims require separately captured evidence.

## Run

```bash
python3 validator.py
```

The validator is deliberately offline. It never contacts a cloud provider and never applies infrastructure.
