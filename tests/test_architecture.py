from __future__ import annotations

import ast
from pathlib import Path
import unittest


FORBIDDEN_AUTHORITY_MODULES = {"socket", "subprocess"}


class ArchitectureTests(unittest.TestCase):
    def test_decision_only_package_has_no_network_or_process_imports(self) -> None:
        violations: list[str] = []
        for path in sorted(Path("src/openpacs_verify").rglob("*.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                imported: list[str] = []
                if isinstance(node, ast.Import):
                    imported = [alias.name.split(".", 1)[0] for alias in node.names]
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported = [node.module.split(".", 1)[0]]
                for module in imported:
                    if module in FORBIDDEN_AUTHORITY_MODULES:
                        violations.append(f"{path}:{node.lineno}: import {module}")

        self.assertEqual(violations, [], "decision-only authority violation")


if __name__ == "__main__":
    unittest.main()
