# M1-06 · Errors and error rate

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sat Nov 14 | S | `error_records`, `error_rate` | `tests/test_m1_06_errors.py` (6) | 45 m / __ |

## Context
"63 errors" means little on its own. Sixty-three out of 240 is an incident; 63 out of two
million is a normal Tuesday. Escalation write-ups quote a rate.

## Requirements
- `error_records(records)` returns a new list with only the records whose status is 400 or above.
- `error_rate(records)` returns the percentage of records that are errors, rounded to one
  decimal place. For an empty list it returns `0.0`.

## Acceptance criteria
`tests/test_m1_06_errors.py` passes.

## Learn first (5 min)
- **Filtering.** Loop, test with `if`, append the ones that pass. As a comprehension:
  `[r for r in records if r["status"] >= 400]`.
- **Division.** `/` always gives a float. Dividing by zero raises `ZeroDivisionError`, so
  deal with the empty list first.
- **Rounding.** `round(26.25, 1)`.
- **Reuse.** `error_rate` should call `error_records`. Don't write the filter twice.

## Explain-back (answer in the PR)
1. Why does the empty-list case need its own line?
2. The 403s here are `billing_suspended`. Should they count toward an "error rate" you'd put in an incident report? Argue one side.
