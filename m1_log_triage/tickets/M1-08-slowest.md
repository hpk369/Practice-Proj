# M1-08 · Slowest requests

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sat Nov 14 | S | `slowest` | `tests/test_m1_08_slowest.py` (5) | 45 m / __ |

## Context
"The API feels slow" is the hardest ticket to act on. A list of the slowest requests with
their request IDs gives engineering something to look up.

## Requirements
Implement `slowest(records, n=5)`: return the `n` records with the highest `duration_ms`,
slowest first. Don't change the order of the list you were given.

## Acceptance criteria
`tests/test_m1_08_slowest.py` passes.

## Learn first (10 min)
- **`sorted`** returns a new sorted list and leaves the original alone. (`a_list.sort()`
  changes the list in place. That is the bug one of the tests looks for.)
- **`key=`** tells `sorted` what to compare. It takes a function that receives one item and
  returns the value to sort by. You can define one with `def`, or write it inline:
  `key=lambda r: r["duration_ms"]`. A lambda is a one-line function without a name.
- **`reverse=True`** sorts highest first.
- **Slicing.** `a_list[:n]` is the first `n` items. It doesn't fail if the list is shorter.
- **Default arguments.** `n=5` in the signature means callers may leave `n` out.

## Try it by hand
```python
from m1_log_triage import triage
for r in triage.slowest(triage.load_records("m1_log_triage/data/access.log")):
    print(r["duration_ms"], r["status"], r["path"], r["request_id"])
```

## Explain-back (answer in the PR)
1. Look at the statuses of the five slowest. Which are failures and which are slow successes? Which worries you more?
2. Why hand engineering a `request_id` and not a timestamp?
