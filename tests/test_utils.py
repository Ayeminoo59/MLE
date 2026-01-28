import pytest

from mle.utils import clamp, mean


def test_mean_basic() -> None:
    assert mean([1.0, 2.0, 3.0]) == pytest.approx(2.0)


def test_mean_empty_raises() -> None:
    with pytest.raises(ValueError):
        mean([])


def test_clamp_inside_range() -> None:
    assert clamp(5.0, low=0.0, high=10.0) == 5.0


def test_clamp_outside_range() -> None:
    assert clamp(-1.0, low=0.0, high=10.0) == 0.0
    assert clamp(99.0, low=0.0, high=10.0) == 10.0


def test_clamp_invalid_bounds_raises() -> None:
    with pytest.raises(ValueError):
        clamp(1.0, low=10.0, high=0.0)
