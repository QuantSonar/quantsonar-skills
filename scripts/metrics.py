#!/usr/bin/env python3
"""Deterministic market metrics for QuantSonar workflows.

Read a JSON object from stdin:
{"prices": [10, 11, 9], "current_valuation": 12, "valuation_history": [8, 10, 12]}
"""
from __future__ import annotations

import json
import math
import statistics
import sys
from collections.abc import Iterable


def clean_numbers(values: Iterable[object], *, positive_only: bool = False) -> list[float]:
    cleaned: list[float] = []
    for value in values:
        if value is None or isinstance(value, bool):
            continue
        try:
            number = float(value)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(number) or (positive_only and number <= 0):
            continue
        cleaned.append(number)
    return cleaned


def total_return(prices: Iterable[object]) -> float | None:
    values = clean_numbers(prices, positive_only=True)
    if len(values) < 2:
        return None
    return values[-1] / values[0] - 1


def maximum_drawdown(prices: Iterable[object]) -> float | None:
    values = clean_numbers(prices, positive_only=True)
    if not values:
        return None
    peak = values[0]
    worst = 0.0
    for value in values:
        peak = max(peak, value)
        worst = min(worst, value / peak - 1)
    return worst


def annualized_volatility(prices: Iterable[object], periods: int = 252) -> float | None:
    values = clean_numbers(prices, positive_only=True)
    if len(values) < 3:
        return None
    returns = [values[i] / values[i - 1] - 1 for i in range(1, len(values))]
    return statistics.stdev(returns) * math.sqrt(periods)


def percentile_rank(
    current: object,
    history: Iterable[object],
    *,
    positive_only: bool = False,
) -> float | None:
    values = clean_numbers(history, positive_only=positive_only)
    current_values = clean_numbers([current], positive_only=positive_only)
    if not values or not current_values:
        return None
    point = current_values[0]
    below = sum(value < point for value in values)
    equal = sum(value == point for value in values)
    return (below + 0.5 * equal) / len(values)


def calculate(payload: dict) -> dict:
    prices = payload.get("prices", [])
    result = {
        "total_return": total_return(prices),
        "annualized_volatility": annualized_volatility(
            prices, int(payload.get("periods", 252))
        ),
        "maximum_drawdown": maximum_drawdown(prices),
    }
    if "current_valuation" in payload:
        result["valuation_percentile"] = percentile_rank(
            payload["current_valuation"],
            payload.get("valuation_history", []),
            positive_only=bool(payload.get("positive_valuation_only", True)),
        )
    return result


def main() -> None:
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict):
            raise ValueError("input must be a JSON object")
        print(json.dumps(calculate(payload), ensure_ascii=False, allow_nan=False))
    except (ValueError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
