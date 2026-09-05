# OMEGA-X — Data Flow

```text
Customer-approved source artifacts
        │
        ▼
[Ingestion]
  parse + validate
        │
        ▼
[Canonical Model]
  resource graph + metadata
        │
        ├──────────────► [Residency / sensitivity classification]
        │                               │
        ▼                               ▼
[Coordinator] ◄────────────────── policy constraints
        │
        ├──► Architect ──► target architecture
        ├──► Developer ──► IaC artifacts
        └──► Security  ──► security findings
                 │
                 ▼
        [Deterministic Validator]
                 │
          ┌──────┴──────┐
          │             │
        FAIL           PASS
          │             │
   bounded repair      ▼
      loop        [Evidence Package]
          │             │
          └──────┐      ├──► TCO/ROI report
                 │      ├──► migration report
                 │      ├──► audit record
                 │      └──► pilot deployment (authorized)
                 │
                 ▼
           [Termination]
```

## Data classes

| Class | Examples | Control principle |
|---|---|---|
| Source infrastructure | Terraform, architecture metadata | customer authorization, least privilege |
| Derived model | normalized resource graph | access-controlled, traceable to source |
| AI context | prompt/context fragments | minimize, redact where required, bounded retention |
| Generated artifact | IaC, plans, reports | validation + hash + versioning |
| Audit evidence | findings, approvals, timestamps | immutable/append-oriented record where practical |

## Context caching

Repeatedly supplied architecture context can be represented using context-cache mechanisms where supported by the selected Model Studio models. Cache usage must be evaluated against data sensitivity, retention requirements, pricing, and regional constraints.

## No implicit data export

OMEGA-X should not silently move customer data between regions. Cross-region transfer requires a policy decision, customer authorization, and an audit record.
