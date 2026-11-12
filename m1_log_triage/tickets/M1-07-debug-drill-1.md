# M1-07 · Debugging drill 1: read the traceback

| Session | Size | File | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sat Nov 14 | S | `drills/drill_1_tenant_summary.py` | `tests/test_m1_07_drill_1.py` (5) | 45 m / __ |

## Context
Most of the Python you touch at work will be code someone else wrote. This file was written
in a hurry and has four bugs. Every one of them raises an error, so the traceback points
at the line.

## Requirements
Make the five tests pass by fixing the drill file. Rules:
- Don't edit the tests.
- Don't rewrite the functions. Make the smallest change that fixes each bug.
- Fix one bug, run the tests, read the next traceback. One at a time.

## Method (use this every time something breaks)
1. Run `pytest m1_log_triage/tests/test_m1_07_drill_1.py -x`. `-x` stops at the first failure.
2. Read the **last line** first: the error type and message.
3. Find the line marked with `>` or the last line number inside the drill file. That is where it broke.
4. Say out loud what the line tried to do and why it couldn't.
5. Fix, rerun.

## Learn first (5 min)
The three errors you'll meet:
- `KeyError: 'x'`: you asked a dict for a key it doesn't have.
- `AttributeError: 'NoneType' object has no attribute ...`: you called a method on `None`.
- `ZeroDivisionError`: you divided by zero.

## Explain-back (answer in the PR)
For each bug, one line: the error type, the line number, and the cause in your own words.
