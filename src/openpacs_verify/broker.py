"""Decision-only authorization broker semantics.

This module deliberately performs no network, subprocess, or adapter execution.
It defines the grant binding that a future isolated broker must enforce.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import secrets
import threading
import time
from dataclasses import dataclass

from .envelope import ActionEnvelope, EnvelopeError
from .models import Action, Decision
from .policy import Policy


@dataclass(frozen=True, slots=True)
class AuthorizationGrant:
    """A short-lived, single-use authorization bound to action and policy."""

    action_digest: str
    policy_digest: str
    issued_at: int
    expires_at: int
    nonce: str
    mac: str

    def signed_fields(self) -> dict[str, str | int]:
        return {
            "action_digest": self.action_digest,
            "expires_at": self.expires_at,
            "issued_at": self.issued_at,
            "nonce": self.nonce,
            "policy_digest": self.policy_digest,
        }


@dataclass(frozen=True, slots=True)
class AuthorizationResult:
    decision: Decision
    envelope: ActionEnvelope | None = None
    grant: AuthorizationGrant | None = None


class DecisionBroker:
    """Issue and consume grants without executing the authorized action."""

    def __init__(
        self, policy: Policy, secret: bytes | None = None, ttl_seconds: int = 30
    ):
        if not 1 <= ttl_seconds <= 300:
            raise ValueError("ttl_seconds must be between 1 and 300")
        key = secret if secret is not None else secrets.token_bytes(32)
        if len(key) < 32:
            raise ValueError("broker secret must contain at least 32 bytes")
        self._policy = policy
        self._secret = bytes(key)
        self._ttl_seconds = ttl_seconds
        self._consumed_nonces: dict[str, int] = {}
        self._consume_lock = threading.Lock()

    @staticmethod
    def _encoded(fields: dict[str, str | int]) -> bytes:
        return json.dumps(fields, sort_keys=True, separators=(",", ":")).encode()

    def _mac(self, fields: dict[str, str | int]) -> str:
        return hmac.new(self._secret, self._encoded(fields), hashlib.sha256).hexdigest()

    def authorize(self, action: Action, *, now: int | None = None) -> AuthorizationResult:
        try:
            envelope = ActionEnvelope.from_action(action)
        except EnvelopeError as exc:
            return AuthorizationResult(
                Decision(False, "INVALID_ACTION_ENVELOPE", str(exc))
            )

        decision = self._policy.authorize(envelope.to_action())
        if not decision.allowed:
            return AuthorizationResult(decision=decision, envelope=envelope)

        issued_at = int(time.time()) if now is None else now
        fields: dict[str, str | int] = {
            "action_digest": envelope.digest,
            "policy_digest": self._policy.digest(),
            "issued_at": issued_at,
            "expires_at": issued_at + self._ttl_seconds,
            "nonce": secrets.token_hex(16),
        }
        grant = AuthorizationGrant(**fields, mac=self._mac(fields))
        return AuthorizationResult(decision=decision, envelope=envelope, grant=grant)

    def verify_and_consume(
        self,
        grant: AuthorizationGrant,
        envelope: ActionEnvelope,
        *,
        now: int | None = None,
    ) -> Decision:
        current_time = int(time.time()) if now is None else now
        expected_mac = self._mac(grant.signed_fields())
        if not hmac.compare_digest(grant.mac, expected_mac):
            return Decision(
                False, "GRANT_INVALID", "authorization grant signature is invalid"
            )
        if grant.policy_digest != self._policy.digest():
            return Decision(False, "POLICY_MISMATCH", "authorization policy has changed")
        if grant.action_digest != envelope.digest:
            return Decision(
                False, "ACTION_MUTATED", "action differs from authorized envelope"
            )
        if current_time < grant.issued_at or current_time >= grant.expires_at:
            return Decision(
                False,
                "GRANT_EXPIRED",
                "authorization grant is not currently valid",
            )
        with self._consume_lock:
            self._consumed_nonces = {
                nonce: expiry
                for nonce, expiry in self._consumed_nonces.items()
                if expiry > current_time
            }
            if grant.nonce in self._consumed_nonces:
                return Decision(
                    False,
                    "GRANT_REPLAYED",
                    "authorization grant was already consumed",
                )
            self._consumed_nonces[grant.nonce] = grant.expires_at
        return Decision(
            True, "GRANT_ACCEPTED", "authorization grant is valid and consumed"
        )
