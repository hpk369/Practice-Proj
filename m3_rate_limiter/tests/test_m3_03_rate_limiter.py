"""Tests for M3-03. These define "done" for the ticket. Read them before you write code."""

import pytest

from m3_rate_limiter import limiter

pytestmark = pytest.mark.skip(reason="M3-03 not started. Delete this line when you begin the ticket.")


def test_first_request_is_allowed(clock):
    rl = limiter.FixedWindowRateLimiter(limit=3, clock=clock)
    decision = rl.check("key_a")
    assert decision == limiter.RateLimitDecision(
        allowed=True, limit=3, remaining=2, reset_after_s=60
    )


def test_remaining_counts_down_to_zero(clock):
    rl = limiter.FixedWindowRateLimiter(limit=3, clock=clock)
    assert [rl.check("key_a").remaining for _ in range(3)] == [2, 1, 0]


def test_the_request_at_the_limit_is_still_allowed(clock):
    rl = limiter.FixedWindowRateLimiter(limit=3, clock=clock)
    decisions = [rl.check("key_a") for _ in range(3)]
    assert all(d.allowed for d in decisions)


def test_the_request_over_the_limit_is_denied(clock):
    rl = limiter.FixedWindowRateLimiter(limit=3, clock=clock)
    for _ in range(3):
        rl.check("key_a")
    decision = rl.check("key_a")
    assert decision.allowed is False
    assert decision.remaining == 0


def test_remaining_never_goes_below_zero(clock):
    rl = limiter.FixedWindowRateLimiter(limit=1, clock=clock)
    for _ in range(5):
        decision = rl.check("key_a")
    assert decision.remaining == 0


def test_keys_have_separate_limits(clock):
    rl = limiter.FixedWindowRateLimiter(limit=1, clock=clock)
    rl.check("key_a")
    assert rl.check("key_a").allowed is False
    assert rl.check("key_b").allowed is True


def test_reset_after_follows_the_clock(clock):
    rl = limiter.FixedWindowRateLimiter(limit=3, clock=clock)
    clock.advance(45.5)
    assert rl.check("key_a").reset_after_s == 15


def test_a_new_window_starts_the_count_again(clock):
    rl = limiter.FixedWindowRateLimiter(limit=2, clock=clock)
    for _ in range(3):
        rl.check("key_a")
    clock.advance(60)
    decision = rl.check("key_a")
    assert decision.allowed is True
    assert decision.remaining == 1


def test_the_window_rolls_over_on_the_clock_not_on_first_use(clock):
    # First request arrives 50 seconds into the window. The window still ends at 180.
    rl = limiter.FixedWindowRateLimiter(limit=1, clock=clock)
    clock.advance(50)
    rl.check("key_a")
    clock.advance(10)
    assert rl.check("key_a").allowed is True


def test_the_limit_is_stored_on_the_decision(clock):
    assert limiter.FixedWindowRateLimiter(limit=7, clock=clock).check("key_a").limit == 7
