# M1-09 · Time range of the log

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sun Nov 15 | S | `time_range` | `tests/test_m1_09_time_range.py` (3) | 40 m / __ |

## Context
Every escalation states the window it covers. Log lines are not guaranteed to be in time
order, so "first line to last line" is not good enough.

## Requirements
Implement `time_range(records)`: return a tuple `(first, last)` holding the earliest and
latest `ts` values as `datetime` objects.

## Acceptance criteria
`tests/test_m1_09_time_range.py` passes.

## Learn first (10 min)
- **Text is not time.** `"2026-11-10T09:00:19.000+00:00"` is a string. To compare or
  subtract times, convert it: `from datetime import datetime`, then
  `datetime.fromisoformat(text)`.
- **`min` and `max`** work on a list of datetimes.
- **Subtracting** two datetimes gives a `timedelta`; `.total_seconds()` turns it into a number.
- **Tuples.** `return first, last` returns two values as a tuple. The caller unpacks them:
  `first, last = time_range(records)`.
- **Time zones.** The `+00:00` at the end means UTC. Logs are almost always UTC; customers
  almost never are. Always say which one you mean in a ticket.

## Explain-back (answer in the PR)
1. A customer in Toronto says "it broke at 4:15 this morning". What UTC time do you search for in November?
2. Why can't you compare the `ts` strings directly? (They happen to sort correctly here. When wouldn't they?)
