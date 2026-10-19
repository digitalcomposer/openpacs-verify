"""Command-line interface for inspecting policy decisions."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .models import Action
from .policy import Policy, PolicyError


def _parse_action(raw: str) -> Action:
    try:
        value: Any = json.loads(raw)
        if not isinstance(value, dict):
            raise ValueError("action root must be an object")
        parameters = value.get("parameters", {})
        if not isinstance(parameters, dict):
            raise ValueError("parameters must be an object")
        return Action(
            kind=str(value["kind"]),
            target=str(value["target"]),
            operation=str(value["operation"]),
            parameters=parameters,
        )
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid action: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate an OpenPACS lab action")
    parser.add_argument("--policy", required=True, help="path to JSON policy")
    parser.add_argument("--action", required=True, help="declarative action as JSON")
    args = parser.parse_args()

    try:
        policy = Policy.load(args.policy)
        decision = policy.authorize(_parse_action(args.action))
    except (PolicyError, ValueError) as exc:
        print(json.dumps({"allowed": False, "reason_code": "INVALID_INPUT", "explanation": str(exc)}))
        return 2

    print(
        json.dumps(
            {
                "allowed": decision.allowed,
                "reason_code": decision.reason_code,
                "explanation": decision.explanation,
                "policy_id": policy.policy_id,
            },
            sort_keys=True,
        )
    )
    return 0 if decision.allowed else 2


if __name__ == "__main__":
    sys.exit(main())
