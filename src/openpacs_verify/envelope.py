"""Canonical, bounded representation of an untrusted action proposal."""

from __future__ import annotations

import hashlib
import ipaddress
import json
from dataclasses import dataclass
from typing import Any, Mapping

from .models import Action

SCHEMA_VERSION = 1
MAX_ACTION_BYTES = 16_384
MAX_NESTING_DEPTH = 16


class EnvelopeError(ValueError):
    """Raised when an action cannot be represented without ambiguity."""


def _canonical_value(value: Any, *, depth: int = 0, seen: set[int] | None = None) -> Any:
    if depth > MAX_NESTING_DEPTH:
        raise EnvelopeError("parameters exceed maximum nesting depth")
    if seen is None:
        seen = set()

    if value is None or isinstance(value, (bool, str)):
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        if not -(2**63) <= value < 2**63:
            raise EnvelopeError("integer parameter is outside signed 64-bit range")
        return value
    if isinstance(value, float):
        raise EnvelopeError("floating-point parameters are not canonical")

    if isinstance(value, Mapping):
        identity = id(value)
        if identity in seen:
            raise EnvelopeError("parameters must not contain cycles")
        seen.add(identity)
        try:
            normalized: dict[str, Any] = {}
            for key, nested in value.items():
                if not isinstance(key, str) or not key:
                    raise EnvelopeError("parameter object keys must be non-empty strings")
                normalized[key] = _canonical_value(
                    nested, depth=depth + 1, seen=seen
                )
            return normalized
        finally:
            seen.remove(identity)

    if isinstance(value, (list, tuple)):
        identity = id(value)
        if identity in seen:
            raise EnvelopeError("parameters must not contain cycles")
        seen.add(identity)
        try:
            return [
                _canonical_value(item, depth=depth + 1, seen=seen)
                for item in value
            ]
        finally:
            seen.remove(identity)

    raise EnvelopeError(f"unsupported parameter type: {type(value).__name__}")


@dataclass(frozen=True, slots=True)
class ActionEnvelope:
    """Immutable canonical bytes and digest for one proposed action."""

    canonical_json: str
    digest: str

    @classmethod
    def from_action(cls, action: Action) -> "ActionEnvelope":
        try:
            target = str(ipaddress.ip_address(action.target.strip()))
        except ValueError as exc:
            raise EnvelopeError("target must be an IP literal") from exc

        document = {
            "kind": action.kind.strip().lower(),
            "operation": action.operation.strip().lower(),
            "parameters": _canonical_value(action.parameters),
            "schema_version": SCHEMA_VERSION,
            "target": target,
        }
        canonical_json = json.dumps(
            document, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        if len(canonical_json.encode("utf-8")) > MAX_ACTION_BYTES:
            raise EnvelopeError("canonical action exceeds maximum size")
        digest = hashlib.sha256(canonical_json.encode("utf-8")).hexdigest()
        return cls(canonical_json=canonical_json, digest=digest)

    def to_action(self) -> Action:
        document = json.loads(self.canonical_json)
        if document.get("schema_version") != SCHEMA_VERSION:
            raise EnvelopeError("unsupported action schema version")
        return Action(
            kind=document["kind"],
            target=document["target"],
            operation=document["operation"],
            parameters=document["parameters"],
        )
