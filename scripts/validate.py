#!/usr/bin/env python3
"""Self-contained structural validation for the public QuantSonar Skill."""
from __future__ import annotations

import json
import re
from pathlib import Path

from metrics import calculate

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_WORKFLOWS = {
    "stock-research",
    "market-brief",
    "stock-screening",
    "quant-data-prep",
    "direct-data",
}


def validate_frontmatter() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    assert match, "SKILL.md frontmatter is missing"
    keys = {
        line.split(":", 1)[0]
        for line in match.group(1).splitlines()
        if line and not line.startswith(" ")
    }
    assert keys == {"name", "description"}, f"unexpected frontmatter keys: {keys}"
    assert "name: quantsonar" in match.group(1)


def validate_links() -> None:
    markdown_files = [ROOT / "SKILL.md", *sorted((ROOT / "references").rglob("*.md"))]
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", text):
            resolved = (source.parent / target).resolve()
            assert resolved.is_relative_to(ROOT), f"link escapes package: {source} -> {target}"
            assert resolved.exists(), f"broken link: {source.relative_to(ROOT)} -> {target}"


def validate_golden_prompts() -> None:
    cases = json.loads((ROOT / "tests" / "golden-prompts.json").read_text(encoding="utf-8"))
    workflows = {case["workflow"] for case in cases}
    assert workflows == REQUIRED_WORKFLOWS, (
        f"golden prompts missing routes: {REQUIRED_WORKFLOWS - workflows}"
    )
    assert all(case["prompt"].strip() for case in cases)
    assert any(
        case["workflow"] == "stock-research" and len(case.get("guardrails", [])) >= 3
        for case in cases
    ), "missing adversarial investment-decision case"


def validate_metrics() -> None:
    result = calculate(
        {
            "prices": [10, 12, 9, 15],
            "current_valuation": 12,
            "valuation_history": [8, 10, 12, 14],
        }
    )
    assert result["total_return"] == 0.5
    assert result["maximum_drawdown"] == -0.25
    assert result["valuation_percentile"] == 0.625


def main() -> None:
    validate_frontmatter()
    validate_links()
    validate_golden_prompts()
    validate_metrics()
    print("QuantSonar Skill validation passed")


if __name__ == "__main__":
    main()
