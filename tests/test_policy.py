from __future__ import annotations

import unittest

from openpacs_verify.models import Action
from openpacs_verify.policy import Policy, PolicyError


def policy(**overrides: object) -> Policy:
    document: dict[str, object] = {
        "policy_id": "test-policy",
        "allowed_kinds": ["observe", "validate"],
        "allowed_operations": ["health", "validate_configuration"],
        "allowed_networks": ["127.0.0.1/32", "::1/128"],
        "deny_state_change": True,
    }
    document.update(overrides)
    return Policy.from_mapping(document)


class PolicyTests(unittest.TestCase):
    def test_allows_explicit_loopback_observation(self) -> None:
        decision = policy().authorize(Action("observe", "127.0.0.1", "health"))
        self.assertTrue(decision.allowed)
        self.assertEqual(decision.reason_code, "ALLOW")

    def test_denies_external_target(self) -> None:
        decision = policy().authorize(Action("observe", "192.0.2.10", "health"))
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "TARGET_OUT_OF_SCOPE")

    def test_denies_hostname_to_prevent_resolution_and_rebinding(self) -> None:
        decision = policy().authorize(Action("observe", "localhost", "health"))
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "IP_LITERAL_REQUIRED")

    def test_denies_actuation_even_on_loopback(self) -> None:
        decision = policy().authorize(Action("actuate", "127.0.0.1", "health"))
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "STATE_CHANGE_DENIED")

    def test_denies_unknown_operation(self) -> None:
        decision = policy().authorize(Action("observe", "127.0.0.1", "open_door"))
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "OPERATION_NOT_ALLOWED")

    def test_denies_sensitive_parameter_names(self) -> None:
        decision = policy().authorize(
            Action("validate", "127.0.0.1", "validate_configuration", {"pin": "synthetic"})
        )
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "SENSITIVE_PARAMETER_DENIED")

    def test_rejects_policy_that_allow_lists_state_change(self) -> None:
        with self.assertRaises(PolicyError):
            policy(allowed_kinds=["observe", "actuate"])

    def test_rejects_policy_that_disables_state_change_guard(self) -> None:
        with self.assertRaises(PolicyError):
            policy(deny_state_change=False)


if __name__ == "__main__":
    unittest.main()
