# M3-04 · Reading: predict the tests

| Session | Size | Files | Estimate / Actual |
| --- | --- | --- | --- |
| Sun Nov 22 | S | `reading/retry.py`, `tests/test_m3_04_predict.py` | 60 m / __ |

## Context
`reading/retry.py` is a small, correct retry helper, the kind found in every codebase that
calls another service. Someone wrote eight tests for it without reading it carefully.
Three of the tests expect the wrong thing.

## Requirements
1. **Read** `reading/retry.py`. Don't run it.
2. **Trace by hand.** On paper, work out what `backoff_delays(4)` returns, one pass of the
   loop at a time.
3. **Predict.** Read each of the eight tests. In `LEARNING.md`, write pass or fail for each,
   with one line of reasoning.
4. **Run.** Delete the `pytestmark` line and run the tests. Score your predictions out of eight.
5. **Fix the three wrong tests** so they describe what the code does. Don't change `retry.py`.
   Rename a test if its name is now untrue.

## Acceptance criteria
All eight tests pass, `retry.py` is unchanged, and your predictions are in `LEARNING.md`.

## Learn first (5 min)
- **`range(n)`** produces `0, 1, ..., n-1`. `range(attempts - 1)` produces one fewer.
- **`2**i`** is 2 to the power of `i`.
- **Functions as arguments.** `sleep=time.sleep` is the same idea as the injected clock.
  The tests pass `slept.append`, so each "sleep" is recorded in a list instead of waiting.
- **A bare `raise`** inside `except` re-raises the error that was just caught.
- **`except retry_on:`** catches only the error types in that tuple.

## Explain-back (live in chat)
Walk through `call_with_retry` for a service that fails twice and then succeeds, saying the
value of `attempt` and what happens on each pass.
