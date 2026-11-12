# M3-03 · The rate limiter

| Session | Size | Code | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sun Nov 22 | M | `FixedWindowRateLimiter` | `tests/test_m3_03_rate_limiter.py` (10) | 90 m / __ |

## Context
This is ticket ACME-3 from Project-1 with the same contract. When it passes here, you can
carry it across.

## Requirements
`check(key)` counts the request and returns a `RateLimitDecision`. The contract is in the
module docstring. In short:
- `allowed` is `True` while the key has made at most `limit` requests in the current window.
- `remaining` is what is left after this request, never below 0.
- `reset_after_s` comes from `reset_after`.
- When the clock moves into a new window, every key's count starts again.
- Read the time by calling `self._clock()`. Never call `time.time()` directly.

Use your `RequestCounter`, `window_start` and `reset_after`.

## Acceptance criteria
`tests/test_m3_03_rate_limiter.py` passes.

## Learn first (10 min)
- **Objects inside objects.** The limiter can own a counter: `self._counter = RequestCounter()`.
- **Remembering the window.** Store the start of the window you last saw. On each check,
  compare it with the current window start. If they differ, a new window has begun.
- **Passing the clock in.** `clock=time.time` in the signature stores the *function*, not a
  time. Production uses the real clock. Tests pass a `FakeClock` they can move forward, so
  a test about a 60-second window runs in a millisecond. Read `tests/conftest.py`.
- **`__call__`.** `FakeClock` defines `__call__`, which lets the object be used like a
  function: `clock()`.
- **Keyword arguments.** Build the decision with names so the order can't be mixed up:
  `RateLimitDecision(allowed=..., limit=..., remaining=..., reset_after_s=...)`.

<details><summary>Hint (direction)</summary>

In `check`: read the time once and keep it in a variable. Work out the window start. If it
differs from the one you stored, reset the counter and store the new one. Record the
request and keep the count. Everything in the decision follows from that count, the
limit and the time.
</details>

## Explain-back (answer in the PR)
1. A customer with a limit of 100 sends 100 requests at 12:00:59 and 100 more at 12:01:00. All 200 succeed. Is that a bug? Explain it to the customer in two sentences.
2. Why would a test that calls `time.sleep(60)` be a bad test?
