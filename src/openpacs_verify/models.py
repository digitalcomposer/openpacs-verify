"""Typed inputs and outputs for the deterministic safety boundary."""

from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class Action:
    """A proposed laboratory action.

    Model-generated content must be parsed into this small declarative shape.
    No command string or executable callback is accepted.
    """

    kind: str
    target: str
    operation: str
    parameters: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "parameters", MappingProxyType(dict(self.parameters)))


@dataclass(frozen=True, slots=True)
class Decision:
    """An auditable authorization result."""

    allowed: bool
    reason_code: str
    explanation: str
