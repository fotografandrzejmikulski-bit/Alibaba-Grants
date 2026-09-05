# OMEGA-X — System Architecture

## Design objective

Provide a controlled pipeline that turns approved AWS infrastructure descriptors into an evidence-backed Alibaba Cloud migration proposal and, where authorized, a bounded pilot deployment.

## Logical layers

```text
┌─────────────────────────────────────────────────────────────┐
│ Enterprise Input Layer                                      │
│ Terraform / architecture metadata / policies / constraints │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Ingestion & Normalization                                   │
│ parser → canonical resource graph → dependency model       │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Agent Orchestration                                         │
│ Coordinator                                                  │
│   ├── Architect                                             │
│   ├── Developer                                             │
│   └── Security                                              │
└─────────────────────────────┬───────────────────────────────┘
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
┌──────────────────────────┐   ┌──────────────────────────────┐
│ Model Studio / Qwen      │   │ Deterministic Validation     │
│ inference + agent tasks  │   │ schema / policy / hash / TTL │
└─────────────┬────────────┘   └──────────────┬───────────────┘
              │                                │
              └────────────────┬───────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Evidence & Context Layer                                    │
│ audit records / embeddings / cache / generated artifacts    │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Pilot Execution Layer                                       │
│ Alibaba Cloud ECS / database / network / security services  │
└─────────────────────────────────────────────────────────────┘
```

## Trust boundaries

1. **Untrusted input boundary** — customer-provided configuration is treated as data, not executable instructions.
2. **Model boundary** — LLM output is untrusted until deterministic validation completes.
3. **Deployment boundary** — consequential actions require policy checks and explicit authorization.
4. **Customer boundary** — access to customer environments is scoped and logged.

## Agent execution rules

Each agent execution should be bounded by:

- maximum wall-clock time,
- maximum model calls,
- maximum context size,
- maximum retry count,
- explicit termination condition,
- validation checkpoint before promotion.

## Infrastructure principle

Use Alibaba Cloud native services wherever practical, but do not hard-code a particular GPU SKU or region into the grant narrative. Capacity and service availability must be validated during onboarding. Model Studio Token Plan is currently documented as available in Singapore; other Model Studio/API deployment choices should be validated against the selected region and account configuration before implementation.
