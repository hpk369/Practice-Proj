"""Tests for M3-05. These define "done" for the ticket. Read them before you write code."""

import pytest

from m3_rate_limiter import limiter

pytestmark = pytest.mark.skip(reason="M3-05 not started. Delete this line when you begin the ticket.")


def test_headers_for_an_allowed_request():
    decision = limiter.RateLimitDecision(allowed=True, limit=100, remaining=42, reset_after_s=17)
    assert limiter.rate_limit_headers(decision) == {
        "X-RateLimit-Limit": "100",
        "X-RateLimit-Remaining": "42",
        "X-RateLimit-Reset": "17",
    }


def test_denied_request_also_gets_retry_after():
    decision = limiter.RateLimitDecision(allowed=False, limit=100, remaining=0, reset_after_s=17)
    headers = limiter.rate_limit_headers(decision)
    assert headers["Retry-After"] == "17"
    assert headers["X-RateLimit-Remaining"] == "0"


def test_header_values_are_strings():
    decision = limiter.RateLimitDecision(allowed=False, limit=5, remaining=0, reset_after_s=9)
    assert all(isinstance(v, str) for v in limiter.rate_limit_headers(decision).values())


def test_allowed_requests_log_nothing(clock, caplog):
    rl = limiter.FixedWindowRateLimiter(limit=2, clock=clock)
    with caplog.at_level("WARNING"):
        rl.check("key_a")
        rl.check("key_a")
    assert caplog.records == []


def test_each_denied_request_logs_one_warning(clock, caplog):
    rl = limiter.FixedWindowRateLimiter(limit=1, clock=clock)
    with caplog.at_level("WARNING"):
        rl.check("key_a")
        rl.check("key_a")
        rl.check("key_a")
    assert len(caplog.records) == 2
    assert all(r.levelname == "WARNING" for r in caplog.records)
    assert "key_a" in caplog.text
