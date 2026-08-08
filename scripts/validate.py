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
    "sector-research",
    "research-mandate",
    "market-brief",
    "stock-screening",
    "technical-analysis",
    "capital-behavior",
    "etf-research",
    "dividend-research",
    "event-monitor",
    "index-research",
    "investment-lifecycle",
    "thesis-review",
    "research-review",
    "market-feasibility",
    "quant-data-prep",
    "direct-data",
}

REQUIRED_METHODS = {
    "daily", "fundamentals", "adj_factor", "technical_factors",
    "technical_factors_pro", "margin", "block_trade", "top_list", "top_inst",
    "shareholders", "holder_trade", "limit_list", "concepts", "concept_members",
    "moneyflow", "moneyflow_hsgt", "northbound_holdings", "southbound_holdings",
    "distribution", "fx_daily", "index_daily", "index_weight", "basic",
    "etf_daily", "etf_adj_factor", "nav", "portfolio", "share_size",
    "tracking_indices", "indicators", "income", "balance_sheet", "cash_flow",
    "forecast", "express", "analyst_reports", "audit", "main_business",
    "disclosure_date", "dividend", "stocks", "industries", "trade_calendar",
    "realtime", "news_flash",
}

SYSTEM_WORKFLOW_FILES = {
    "research-mandate", "market-brief", "stock-screening", "stock-research",
    "sector-research",
    "technical-analysis", "capital-behavior", "etf-research", "dividend-research",
    "event-monitor", "index-research", "quant-data-prep", "thesis-review",
    "market-feasibility", "research-review",
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


def validate_matrix_coverage() -> None:
    text = (ROOT / "references" / "skill-matrix.md").read_text(encoding="utf-8")
    covered = set(re.findall(r"`([a-z][a-z0-9_]*)`", text))
    assert REQUIRED_METHODS <= covered, (
        f"skill matrix missing methods: {sorted(REQUIRED_METHODS - covered)}"
    )


def validate_research_system() -> None:
    text = (ROOT / "references" / "research-system.md").read_text(encoding="utf-8")
    artifacts = {
        "research_mandate", "market_context", "candidate_pool", "evidence_pack",
        "thesis_card", "feasibility_card", "change_log", "research_review",
    }
    for artifact in artifacts:
        assert f"`{artifact}`" in text, f"research system missing artifact: {artifact}"
    for gate in range(8):
        assert f"G{gate}" in text, f"research system missing gate: G{gate}"
    assert "Individual-stock research" in text, "research system missing stock entrance"
    assert "Sector research" in text, "research system missing sector entrance"

    for name in SYSTEM_WORKFLOW_FILES:
        workflow = (ROOT / "references" / f"{name}.md").read_text(encoding="utf-8")
        assert "## System contract" in workflow, f"workflow missing system contract: {name}"
        assert "research-system.md" in workflow, f"workflow not linked to system: {name}"


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
    validate_matrix_coverage()
    validate_research_system()
    validate_metrics()
    print("QuantSonar Skill validation passed")


if __name__ == "__main__":
    main()
