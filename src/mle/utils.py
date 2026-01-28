from __future__ import annotations

from collections.abc import Iterable


def mean(values: Iterable[float]) -> float:
    vals = list(values)
    if not vals:
        raise ValueError("mean() requires at least one value")
    return sum(vals) / len(vals)


def clamp(x: float, *, low: float, high: float) -> float:
    if low > high:
        raise ValueError("low must be <= high")
    if x < low:
        return low
    if x > high:
        return high
    return x
