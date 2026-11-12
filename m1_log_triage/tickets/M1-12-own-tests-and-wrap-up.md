# M1-12 · Your own tests, and wrap-up

| Session | Size | File | Estimate / Actual |
| --- | --- | --- | --- |
| Sun Nov 15 | S | `tests/test_m1_12_my_tests.py`, `README.md`, `LEARNING.md` | 45 m / __ |

## Context
So far the tests were written for you. Reading them was half the lesson. Now write some.

## Requirements
1. **A new function with your own tests.** Add `requests_for_tenant(records, tenant_id)` to
   `triage.py`. It returns the records for one tenant. Write at least three tests for it in
   `tests/test_m1_12_my_tests.py`: a tenant with records, a tenant with none, and `None`
   as the tenant. Write the tests first, watch them fail, then write the function.
2. **Usage section.** Add a "Usage" section to `m1_log_triage/README.md` with the two
   commands and a sample of the output.
3. **Learning log.** Five lines in `LEARNING.md`.

## Learn first (5 min)
- A test is a function whose name starts with `test_`, containing `assert` statements.
- A parameter named `records` gets the six sample records from `tests/conftest.py`. That
  mechanism is called a fixture. You'll write your own in M2.
- Good tests cover the normal case, the empty case and the odd case.

## Explain-back (do this one live in chat)
Pick any function in `triage.py`. Explain it line by line, as if to a new teammate. Then
answer: which ticket took longest against its estimate, and why?
