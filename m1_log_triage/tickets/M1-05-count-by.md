# M1-05 · Count by any field

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sat Nov 14 | XS | `count_by` | `tests/test_m1_05_count_by.py` (5) | 30 m / __ |

## Context
After "how bad?" comes "who is affected, and by what?". That is the same counting again,
by tenant and by error code. Writing three near-identical functions is how bugs get copied.

## Requirements
Implement `count_by(records, field)`. It returns a `collections.Counter` of the values found
under `field`, for any field name: `"tenant_id"`, `"error_code"`, `"path"`, `"status"`.

## Acceptance criteria
`tests/test_m1_05_count_by.py` passes.

## Learn first (5 min)
- **A parameter makes a function general.** `record[field]` looks up whichever key the
  caller passed in.
- **`Counter`.** `from collections import Counter`. `Counter(a_list)` counts how often each
  item appears. It behaves like a dict, missing keys count as 0, and
  `counter.most_common(3)` returns the top three as `(value, count)` pairs.
- **Building the list to count.** You can use the loop-and-append pattern you know. The
  short form is a list comprehension: `[r["path"] for r in records]`.

## Try it by hand
```python
from m1_log_triage import triage
records = triage.load_records("m1_log_triage/data/access.log")
triage.count_by(records, "tenant_id").most_common()
triage.count_by(records, "error_code").most_common()
```

## Explain-back (answer in the PR)
1. Sixty-nine requests have a tenant of `None`: the 401s and the `/healthz` calls. Why can't the server name a tenant in each case?
2. `count_by(records, "status")` does the same job as `count_by_status`. Which would you keep in a real codebase, and why?
