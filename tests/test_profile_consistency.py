from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROFILE_ROOT = REPO_ROOT / "templates" / "profiles"

REQUIRED_PHRASES = (
    "Apply this profile by priority",
    "In the final report, list which snippets were adopted, adapted, skipped, or",
)

DECISION_GUIDANCE_PHRASES = (
    "Consider a decision record",
    "no ADR guidance needed",
)

FORBIDDEN_PHRASES = (
    "Add a decision record when choosing",
    "Before feature implementation",
    "scenario test plan",
)


def profile_readmes() -> list[Path]:
    return sorted(PROFILE_ROOT.glob("*/README.md"))


class ProfileConsistencyTests(unittest.TestCase):
    def test_profile_readmes_exist(self) -> None:
        self.assertGreater(len(profile_readmes()), 0)

    def test_profile_readmes_use_conditional_guidance(self) -> None:
        for path in profile_readmes():
            with self.subTest(profile=path.parent.name):
                text = path.read_text(encoding="utf-8")
                for phrase in REQUIRED_PHRASES:
                    self.assertIn(phrase, text)
                self.assertTrue(
                    any(phrase in text for phrase in DECISION_GUIDANCE_PHRASES),
                    f"{path} needs conditional decision-record guidance",
                )

    def test_profile_readmes_avoid_overly_strict_phrases(self) -> None:
        for path in profile_readmes():
            with self.subTest(profile=path.parent.name):
                text = path.read_text(encoding="utf-8")
                for phrase in FORBIDDEN_PHRASES:
                    self.assertNotIn(phrase, text)

    def test_profile_template_documents_contract_phrases(self) -> None:
        template = REPO_ROOT / "docs" / "templates" / "profile-readme.md"
        text = template.read_text(encoding="utf-8")
        for phrase in REQUIRED_PHRASES:
            self.assertIn(phrase, text)
        self.assertIn("Consider a decision record", text)
        self.assertIn("narrow fix", text)
        self.assertIn("final report or check note", text)


if __name__ == "__main__":
    unittest.main()
