# Expected Source-to-Target Mapping

Fixture: `EVIDENCE/fixtures/terraform-minimal/aws/main.tf`

| Source resource | Target proposal | Confidence | Manual review |
|---|---|---:|---|
| `aws_instance.web` | Alibaba Cloud ECS instance | High | Required before deployment |
| `aws_db_instance.app` | Alibaba Cloud managed PostgreSQL-compatible database service | Medium | Required; engine/version/HA/storage must be confirmed |

## Validation requirements

The mapping is a **proposal**, not an executable migration plan. A production workflow must verify:

- target region and service availability,
- engine/version compatibility,
- network topology,
- identity and access requirements,
- storage and performance characteristics,
- backup/restore requirements,
- security policies,
- total cost assumptions.

No credential, secret, or production endpoint is contained in this artifact.
