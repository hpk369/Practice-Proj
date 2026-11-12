# M1-04 · Count requests per status

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Fri Nov 13 | XS | `count_by_status` | `tests/test_m1_04_count_by_status.py` (3) | 25 m / __ |

## Context
The first question in any triage is "how bad is it?". A count of responses per status code
answers it: mostly 200s with a few 401s is a customer problem, a wall of 500s is ours.

## Requirements
Implement `count_by_status(records)`. Return a plain dict such as `{200: 131, 401: 23}`.
Build it by hand with a loop. You'll replace it with a library tool tomorrow, and you'll
appreciate that tool more for having written this once.

## Acceptance criteria
`tests/test_m1_04_count_by_status.py` passes.

## Learn first (5 min)
- **Adding to a dict.** `counts[key] = 1` creates or overwrites. `counts[key] += 1` only
  works if the key is already there, otherwise it raises `KeyError`.
- **Checking for a key.** `if key in counts:` is true when the key exists.
- **Or in one step.** `counts.get(key, 0)` returns the value, or 0 if the key is missing.

## Try it by hand
```python
from m1_log_triage import triage
triage.count_by_status(triage.load_records("m1_log_triage/data/access.log"))
```

## Explain-back (answer in the PR)
1. Looking at the real counts: is this mostly a customer-side problem or a server-side one? Why?
2. What error do you get from `counts[status] += 1` on an empty dict, and why?
