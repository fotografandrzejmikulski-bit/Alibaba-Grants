# OMEGA-X — TCO / ROI Measurement Model

## Purpose

Generate a transparent migration business case that distinguishes model estimates from measured customer costs.

## Cost model

For each pilot calculate:

**Source annual cost** = compute + storage + database + network + security + managed-service charges + relevant operational labor.

**Target annual cost** = equivalent Alibaba Cloud resources + managed-service charges + migration-specific operational assumptions.

**Migration cost** = engineering labor + testing + temporary dual-run infrastructure + OMEGA-X/implementation cost.

**First-year migration economics** = source cost − target cost − migration cost.

## Assumptions register

Every TCO report must expose:

- source pricing date,
- source region,
- target region,
- committed-use assumptions,
- instance sizes,
- data transfer assumptions,
- storage growth,
- database capacity,
- staffing assumptions,
- excluded costs.

## ROI treatment

Do not present a guaranteed ROI. Present a scenario range based on explicit assumptions.

Example:

| Scenario | Target annual run-rate | Migration cost | Year-1 net impact |
|---|---:|---:|---:|
| Conservative | customer input | customer input | calculated |
| Base | customer input | customer input | calculated |
| Optimistic | customer input | customer input | calculated |

## Alibaba Cloud value linkage

The report should additionally estimate potential recurring Alibaba Cloud consumption associated with workloads that proceed to production, without representing that estimate as guaranteed revenue.
