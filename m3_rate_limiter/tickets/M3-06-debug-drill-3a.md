# M3-06 · Debugging drill 3a: planted bugs in a class

| Session | Size | File | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Tue Nov 24 | S | `drills/drill_3a_quota.py` | `tests/test_m3_06_drill_3a.py` (7) | 45 m / __ |

## Context
Three bugs in a small class. Some crash, some return the wrong answer. Nobody tells you
which. This is the format of the Nov 27 check.

## Requirements
Make the seven tests pass with the smallest fix for each bug. Don't edit the tests.
Don't rewrite methods.

## Method
1. Read the docstring: what is each method **meant** to do?
2. Run the tests. Sort the failures: which crash, which give a wrong value?
3. Several failing tests can share one cause. Pick the simplest failing test first.
4. Crash: read the traceback from the bottom. Wrong value: use the debugger, or work it out by hand.
5. Fix one thing. Rerun everything. Repeat.

## Explain-back (answer in the PR)
A three-row table: the bug, how you found it (traceback, debugger or reading), and the fix.
Then: how many minutes did it take? The target for Friday is three bugs in 30.
