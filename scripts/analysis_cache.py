"""Content-addressed JSON cache for independent CAD analysis stages."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = Path(os.environ.get("CAD_ANALYSIS_CACHE_DIR", ROOT / ".cad-cache"))


def load_or_compute(*, stage: str, version: str, inputs: dict[str, Any], compute: Callable[[], Any]) -> Any:
    """Load a validated stage result or compute and atomically persist it.

    Callers must include every geometry/configuration dependency in inputs and
    bump version whenever the stage calculation semantics change.
    """
    if os.environ.get("CAD_ANALYSIS_CACHE_DISABLE") == "1":
        return compute()

    payload = {"stage": stage, "version": version, "inputs": inputs}
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    key = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    path = CACHE_DIR / stage / f"{key}.json"

    if path.is_file():
        try:
            envelope = json.loads(path.read_text(encoding="utf-8"))
            if envelope.get("key") == key and envelope.get("payload") == payload:
                print(f"CAD cache hit: {stage} ({key[:12]})")
                return envelope["result"]
        except (OSError, ValueError, KeyError, TypeError):
            pass

    result = compute()
    envelope = {"key": key, "payload": payload, "result": result}
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(envelope, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    temporary.replace(path)
    print(f"CAD cache stored: {stage} ({key[:12]})")
    return result
