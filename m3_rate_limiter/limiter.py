"""Per-key rate limiting for Acme Shield. Mini project M3 (yours).

Contract (the same as ticket ACME-3 in Project-1)
-------------------------------------------------
Fixed window of 60 seconds per API key. Windows start at multiples of 60 on the clock
(for example 120.0 to 179.999...), so every key's window rolls over at the same moment.

`check(key)` counts the request and returns a decision:
- allowed:        True while the key has made at most `limit` requests in this window
- limit:          the configured limit
- remaining:      requests left in this window after this one (never below 0)
- reset_after_s:  whole seconds until the window resets, rounded up, at least 1

The clock is passed in, so tests can move time without sleeping.
"""

from __future__ import annotations

import time
from dataclasses import dataclass

WINDOW_SECONDS = 60


class RequestCounter:
    """M3-01. Counts requests per key."""

    def __init__(self):
        # M3-01: create the state you need to remember a count for each key.
        pass

    def record(self, key):
        """Count one more request for `key`. Return the new count for that key."""
        raise NotImplementedError("M3-01: implement RequestCounter.record")

    def count(self, key):
        """Return how many requests `key` has made. A key never seen has made 0."""
        raise NotImplementedError("M3-01: implement RequestCounter.count")

    def reset(self):
        """Forget every count."""
        raise NotImplementedError("M3-01: implement RequestCounter.reset")


def window_start(now):
    """M3-02. Return the start of the 60-second window that contains `now`."""
    raise NotImplementedError("M3-02: implement window_start")


def reset_after(now):
    """M3-02. Return whole seconds until the current window ends, rounded up, at least 1."""
    raise NotImplementedError("M3-02: implement reset_after")


@dataclass(frozen=True)
class RateLimitDecision:
    """The answer to "may this request go ahead?". (Written for you. Read it.)"""

    allowed: bool
    limit: int
    remaining: int
    reset_after_s: int


class FixedWindowRateLimiter:
    """M3-03. Allows `limit` requests per key in each 60-second window."""

    def __init__(self, limit, clock=time.time):
        self.limit = limit
        self._clock = clock
        # M3-03: add the state you need to count requests per key in the current window.

    def check(self, key):
        """Count this request and return a RateLimitDecision."""
        raise NotImplementedError("M3-03: implement FixedWindowRateLimiter.check")


def rate_limit_headers(decision):
    """M3-05. Return the HTTP response headers for a decision, as a dict of str to str."""
    raise NotImplementedError("M3-05: implement rate_limit_headers")
