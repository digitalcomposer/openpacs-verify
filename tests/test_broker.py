from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import unittest

from openpacs_verify.broker import DecisionBroker
from openpacs_verify.envelope import ActionEnvelope
from openpacs_verify.models import Action
from openpacs_verify.policy import Policy


SECRET = b"test-only-broker-secret-32-bytes!!"


def policy() -> Policy:
    return Policy.from_mapping(
        {
            "policy_id": "broker-test-policy",
            "allowed_kinds": ["observe", "validate"],
            "allowed_operations": ["health", "validate_configuration"],
            "allowed_networks": ["127.0.0.1/32", "::1/128"],
            "deny_state_change": True,
        }
    )


def allowed_action(**parameters: object) -> Action:
    return Action("observe", "127.0.0.1", "health", parameters)


class DecisionBrokerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.broker = DecisionBroker(policy(), secret=SECRET, ttl_seconds=10)

    def test_issues_and_consumes_one_grant(self) -> None:
        result = self.broker.authorize(allowed_action(sequence=1), now=100)
        self.assertTrue(result.decision.allowed)
        self.assertIsNotNone(result.envelope)
        self.assertIsNotNone(result.grant)

        decision = self.broker.verify_and_consume(
            result.grant, result.envelope, now=101  # type: ignore[arg-type]
        )
        self.assertTrue(decision.allowed)
        self.assertEqual(decision.reason_code, "GRANT_ACCEPTED")

    def test_rejects_replay(self) -> None:
        result = self.broker.authorize(allowed_action(), now=100)
        self.broker.verify_and_consume(
            result.grant, result.envelope, now=101  # type: ignore[arg-type]
        )
        replay = self.broker.verify_and_consume(
            result.grant, result.envelope, now=102  # type: ignore[arg-type]
        )
        self.assertFalse(replay.allowed)
        self.assertEqual(replay.reason_code, "GRANT_REPLAYED")

    def test_concurrent_consumption_accepts_exactly_once(self) -> None:
        result = self.broker.authorize(allowed_action(), now=100)

        def consume() -> str:
            decision = self.broker.verify_and_consume(
                result.grant, result.envelope, now=101  # type: ignore[arg-type]
            )
            return decision.reason_code

        with ThreadPoolExecutor(max_workers=2) as executor:
            reason_codes = list(executor.map(lambda _: consume(), range(2)))

        self.assertCountEqual(reason_codes, ["GRANT_ACCEPTED", "GRANT_REPLAYED"])

    def test_rejects_expired_grant(self) -> None:
        result = self.broker.authorize(allowed_action(), now=100)
        decision = self.broker.verify_and_consume(
            result.grant, result.envelope, now=110  # type: ignore[arg-type]
        )
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "GRANT_EXPIRED")

    def test_rejects_action_mutation(self) -> None:
        result = self.broker.authorize(allowed_action(sequence=1), now=100)
        mutated = ActionEnvelope.from_action(allowed_action(sequence=2))
        decision = self.broker.verify_and_consume(
            result.grant, mutated, now=101  # type: ignore[arg-type]
        )
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "ACTION_MUTATED")

    def test_rejects_target_and_operation_mutation(self) -> None:
        result = self.broker.authorize(allowed_action(), now=100)
        for mutated_action in (
            Action("observe", "::1", "health"),
            Action("observe", "127.0.0.1", "validate_configuration"),
        ):
            with self.subTest(action=mutated_action):
                decision = self.broker.verify_and_consume(
                    result.grant,  # type: ignore[arg-type]
                    ActionEnvelope.from_action(mutated_action),
                    now=101,
                )
                self.assertFalse(decision.allowed)
                self.assertEqual(decision.reason_code, "ACTION_MUTATED")

    def test_rejects_forged_grant(self) -> None:
        result = self.broker.authorize(allowed_action(), now=100)
        forged = replace(result.grant, expires_at=1000)  # type: ignore[arg-type]
        decision = self.broker.verify_and_consume(
            forged, result.envelope, now=101  # type: ignore[arg-type]
        )
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "GRANT_INVALID")

    def test_rejects_nonce_mutation(self) -> None:
        result = self.broker.authorize(allowed_action(), now=100)
        forged = replace(result.grant, nonce="00" * 16)  # type: ignore[arg-type]
        decision = self.broker.verify_and_consume(
            forged, result.envelope, now=101  # type: ignore[arg-type]
        )
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "GRANT_INVALID")

    def test_rejects_policy_mismatch(self) -> None:
        result = self.broker.authorize(allowed_action(), now=100)
        other_policy = Policy.from_mapping(
            {
                "policy_id": "changed-policy",
                "allowed_kinds": ["observe"],
                "allowed_operations": ["health"],
                "allowed_networks": ["127.0.0.1/32"],
                "deny_state_change": True,
            }
        )
        other_broker = DecisionBroker(other_policy, secret=SECRET, ttl_seconds=10)
        decision = other_broker.verify_and_consume(
            result.grant, result.envelope, now=101  # type: ignore[arg-type]
        )
        self.assertFalse(decision.allowed)
        self.assertEqual(decision.reason_code, "POLICY_MISMATCH")

    def test_denied_action_receives_no_grant(self) -> None:
        result = self.broker.authorize(
            Action("actuate", "127.0.0.1", "health"), now=100
        )
        self.assertFalse(result.decision.allowed)
        self.assertIsNone(result.grant)

    def test_rejects_noncanonical_float(self) -> None:
        result = self.broker.authorize(allowed_action(confidence=0.5), now=100)
        self.assertFalse(result.decision.allowed)
        self.assertEqual(result.decision.reason_code, "INVALID_ACTION_ENVELOPE")


if __name__ == "__main__":
    unittest.main()
