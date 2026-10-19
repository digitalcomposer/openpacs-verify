"""Deny-by-default authorization for proposed PACS laboratory actions."""

from __future__ import annotations

import ipaddress
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .models import Action, Decision


class PolicyError(ValueError):
    """Raised when policy cannot be loaded safely."""


_STATE_CHANGING_KINDS = frozenset({"state_change", "actuate", "write", "exploit"})
_SENSITIVE_PARAMETER_NAMES = frozenset(
    {"password", "passwd", "secret", "token", "api_key", "private_key", "pin"}
)


@dataclass(frozen=True, slots=True)
class Policy:
    """Immutable policy evaluated before any action reaches a tool adapter."""

    policy_id: str
    allowed_kinds: frozenset[str]
    allowed_operations: frozenset[str]
    allowed_networks: tuple[ipaddress.IPv4Network | ipaddress.IPv6Network, ...]
    deny_state_change: bool = True

    @classmethod
    def from_mapping(cls, document: Mapping[str, Any]) -> "Policy":
        try:
            policy_id = str(document["policy_id"]).strip()
            allowed_kinds = frozenset(str(value) for value in document["allowed_kinds"])
            allowed_operations = frozenset(
                str(value) for value in document["allowed_operations"]
            )
            allowed_networks = tuple(
                ipaddress.ip_network(str(value), strict=True)
                for value in document["allowed_networks"]
            )
            deny_state_change = document.get("deny_state_change", True)
        except (KeyError, TypeError, ValueError) as exc:
            raise PolicyError(f"invalid policy document: {exc}") from exc

        if not policy_id:
            raise PolicyError("policy_id must not be empty")
        if not allowed_kinds or not allowed_operations or not allowed_networks:
            raise PolicyError("allow lists must not be empty")
        if not isinstance(deny_state_change, bool):
            raise PolicyError("deny_state_change must be a boolean")
        if allowed_kinds & _STATE_CHANGING_KINDS:
            raise PolicyError("state-changing action kinds cannot be allow-listed")
        if not deny_state_change:
            raise PolicyError("the public safety kernel requires deny_state_change=true")

        return cls(
            policy_id=policy_id,
            allowed_kinds=allowed_kinds,
            allowed_operations=allowed_operations,
            allowed_networks=allowed_networks,
            deny_state_change=deny_state_change,
        )

    @classmethod
    def load(cls, path: str | Path) -> "Policy":
        try:
            document = json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise PolicyError(f"cannot load policy: {exc}") from exc
        if not isinstance(document, dict):
            raise PolicyError("policy root must be an object")
        return cls.from_mapping(document)

    def authorize(self, action: Action) -> Decision:
        """Return a stable decision without causing network or process activity."""

        kind = action.kind.strip().lower()
        operation = action.operation.strip().lower()

        if kind in _STATE_CHANGING_KINDS:
            return Decision(False, "STATE_CHANGE_DENIED", "state-changing actions are prohibited")
        if kind not in self.allowed_kinds:
            return Decision(False, "KIND_NOT_ALLOWED", "action kind is not allow-listed")
        if operation not in self.allowed_operations:
            return Decision(False, "OPERATION_NOT_ALLOWED", "operation is not allow-listed")

        try:
            target = ipaddress.ip_address(action.target.strip())
        except ValueError:
            return Decision(False, "IP_LITERAL_REQUIRED", "target must be an IP literal")

        if not any(target in network for network in self.allowed_networks):
            return Decision(False, "TARGET_OUT_OF_SCOPE", "target is outside laboratory scope")

        parameter_names = {str(name).strip().lower() for name in action.parameters}
        if parameter_names & _SENSITIVE_PARAMETER_NAMES:
            return Decision(
                False,
                "SENSITIVE_PARAMETER_DENIED",
                "credential or personal access data is not accepted",
            )

        return Decision(True, "ALLOW", "action satisfies the laboratory policy")
