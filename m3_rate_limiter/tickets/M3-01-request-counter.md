# M3-01 · A class that counts

| Session | Size | Code | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sun Nov 22 | S | `RequestCounter` | `tests/test_m3_01_request_counter.py` (6) | 40 m / __ |

## Context
A rate limiter has to remember things between calls: how many requests each key has made.
A function forgets everything when it returns. An object keeps its own state, which is
what a class is for.

## Requirements
Fill in `RequestCounter` in `limiter.py`:
- `record(key)` counts one more request for that key and returns the new count.
- `count(key)` returns the count without changing it. An unseen key has a count of 0.
- `reset()` forgets every count.
- Two separate counters must not share counts.

## Acceptance criteria
`pytest m3_rate_limiter/tests/test_m3_01_request_counter.py` passes.

## Learn first (10 min)
- **Class and object.** The class is the blueprint. `RequestCounter()` builds one object
  from it. Each object has its own data.
- **`__init__`** runs once when the object is built. Set up the starting state there.
- **`self`** is the object the method was called on. `self._counts = {}` stores a dict on
  this particular object. Every method takes `self` first, and Python passes it for you:
  `counter.record("a")` calls `record(self=counter, key="a")`.
- **The underscore** in `_counts` says "internal, don't touch from outside".
- **`defaultdict`.** `from collections import defaultdict`. `defaultdict(int)` is a dict that
  gives 0 for a missing key, so `d[key] += 1` works first time. One catch: reading
  `d[key]` for a new key *adds* it. Use `d.get(key, 0)` when you only want to look.
- You wrote one class already: `AuthError` in M2-04. This is the same idea with more methods.

## Explain-back (answer in the PR)
1. What goes wrong if you write `counts = {}` directly under `class RequestCounter:` instead of `self._counts = {}` inside `__init__`? Which test catches it?
2. Why does `count` use `.get` and not `self._counts[key]`?
