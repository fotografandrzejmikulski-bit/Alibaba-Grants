#!/usr/bin/env python3
"""Generate a deterministic SHA-256 manifest for fixture files."""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = [
    ROOT / "aws" / "main.tf",
    ROOT / "expected-target-artifact.json",
    ROOT / "expected-target-mapping.md",
    ROOT / "validation-result.json",
    ROOT / "runbook.md",
    ROOT / "validator.py",
]
OUT = ROOT / "SHA256SUMS.generated.txt"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


lines = [f"{digest(path)}  {path.relative_to(ROOT)}" for path in sorted(FILES)]
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {OUT.name}")
