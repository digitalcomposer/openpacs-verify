from __future__ import annotations

import unittest

from openpacs_verify.cli import _parse_action


class CliParsingTests(unittest.TestCase):
    def test_rejects_duplicate_keys(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate object key"):
            _parse_action(
                '{"kind":"observe","kind":"actuate",'
                '"target":"127.0.0.1","operation":"health"}'
            )


if __name__ == "__main__":
    unittest.main()
