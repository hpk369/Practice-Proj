"""Retry with backoff. Reading exercise for ticket M3-04.

THIS FILE IS CORRECT. Don't change it. Read it, then predict the tests.

When a call to another service fails for a passing reason (a dropped connection, a
timeout), the usual response is to wait a little and try again, waiting longer each time
so a struggling service isn't flooded.
"""

from __future__ import annotations

import time


def backoff_delays(attempts, base=1.0, cap=30.0):
    """Return the waits, in seconds, between `attempts` tries.

    The wait doubles each time, starting at `base`, and never exceeds `cap`.
    """
    delays = []
    for i in range(attempts - 1):
        delays.append(min(cap, base * 2**i))
    return delays


def call_with_retry(func, attempts=3, base=1.0, sleep=time.sleep, retry_on=(ConnectionError,)):
    """Call `func()` until it succeeds or `attempts` tries have been made.

    Only the error types in `retry_on` are retried. Anything else is raised straight away.
    If every try fails, the last error is raised.
    """
    delays = backoff_delays(attempts, base)
    for attempt in range(attempts):
        try:
            return func()
        except retry_on:
            if attempt == attempts - 1:
                raise
            sleep(delays[attempt])
