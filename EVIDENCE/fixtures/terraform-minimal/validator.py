#!/usr/bin/env python3
"""Deterministic, offline validator for the OMEGA-X minimal Terraform fixture.

This is a fixture-level evidence harness. It never contacts AWS or Alibaba Cloud,
does not execute Terraform, and does not perform infrastructure changes.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "aws" / "main.tf"
TARGET = ROOT / "expected-target-artifact.json"
RESULT = ROOT / "validation-result.json"

REQUIRED_SOURCE_PATTERNS = [
    r'resource\s+"aws_instance"\s+"web"',
    r'resource\s+"aws_db_instance"\s+"app"',
    r'provider\s+"aws"\s*\{',
]

FORBIDDEN_DEPLOYMENT_PATTERNS = [
    r'password\s*=\s*"[^"$]+"',
    r'aws_access_key',
    r'aws_secret_key',
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not SOURCE.exists() or not TARGET.exists():
        print("FAIL: required fixture file is missing", file=sys.stderr)
        return 2

    source_text = SOURCE.read_text(encoding="utf-8")
    for pattern in REQUIRED_SOURCE_PATTERNS:
        if not re.search(pattern, source_text):
            print(f"FAIL: missing expected source pattern: {pattern}", file=sys.stderr)
            return 3

    secrets = [p for p in FORBIDDEN_DEPLOYMENT_PATTERNS if re.search(p, source_text, re.I)]
    target = json.loads(TARGET.read_text(encoding="utf-8"))
    required_target_keys = {"schema_version", "fixture", "resources", "assumptions"}
    missing = required_target_keys - set(target)
    if missing:
        print(f"FAIL: target artifact missing keys: {sorted(missing)}", file=sys.stderr)
        return 4

    if secrets:
        print("FAIL: possible secret pattern detected", file=sys.stderr)
        return 5

    expected = json.loads(RESULT.read_text(encoding="utf-8")) if RESULT.exists() else {}
    print(json.dumps({
        "status": "PASS",
        "fixture": "terraform-minimal",
        "source_sha256": sha256(SOURCE),
        "target_sha256": sha256(TARGET),
        "deployment": expected.get("validation", {}).get("deployment_gate", "BLOCKED_UNTIL_HUMAN_APPROVAL"),
        "evidence_class": "fixture-level_demonstration",
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
