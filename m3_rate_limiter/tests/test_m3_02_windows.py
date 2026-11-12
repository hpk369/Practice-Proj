"""Tests for M3-02. These define "done" for the ticket. Read them before you write code."""

import pytest

from m3_rate_limiter import limiter

pytestmark = pytest.mark.skip(reason="M3-02 not started. Delete this line when you begin the ticket.")


@pytest.mark.parametrize(
    "now, expected",
    [(0.0, 0.0), (59.999, 0.0), (60.0, 60.0), (120.0, 120.0), (150.5, 120.0), (179.999, 120.0)],
)
def test_window_start(now, expected):
    assert limiter.window_start(now) == expected


@pytest.mark.parametrize(
    "now, expected",
    [
        (120.0, 60),  # a full window left
        (150.0, 30),
        (150.5, 30),  # 29.5 seconds left rounds up
        (179.0, 1),
        (179.999, 1),  # never 0
    ],
)
def test_reset_after(now, expected):
    assert limiter.reset_after(now) == expected


def test_reset_after_returns_a_whole_number():
    assert isinstance(limiter.reset_after(150.5), int)
