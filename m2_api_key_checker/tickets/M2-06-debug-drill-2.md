# M2-06 · Debugging drill 2: the VS Code debugger

| Session | Size | File | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sat Nov 21 | S | `drills/drill_2_key_tools.py` | `tests/test_m2_06_drill_2.py` (5) | 60 m / __ |

## Context
The bugs in drill 1 crashed, so the traceback told you where to look. These three don't.
The code runs and returns a wrong answer. To find that kind of bug you watch the program
run, one line at a time.

## Set up the debugger (10 min)
1. Install the **Python** extension in VS Code if you haven't.
2. Open the **Testing** panel (the flask icon). Choose pytest, with the repo root as the folder.
3. Delete the `pytestmark` line in `tests/test_m2_06_drill_2.py`.
4. In the drill file, click to the left of a line number to set a **breakpoint** (a red dot).
5. In the Testing panel, right-click a test and choose **Debug Test**.

## The controls
| Key | Name | What it does |
| --- | --- | --- |
| F10 | Step over | Run this line, stop at the next |
| F11 | Step into | Go inside the function this line calls |
| Shift+F11 | Step out | Finish this function, return to the caller |
| F5 | Continue | Run to the next breakpoint |

While stopped, the **Variables** panel shows every value. Add an expression such as
`counts` or `len(keys)` to the **Watch** panel to follow it.

## Requirements
Make the five tests pass with the smallest fix for each bug. Don't edit the tests. For
each bug, find it with the debugger before you change anything.

## Method
1. Before running: read the function and predict the value of each variable after the first pass through the loop.
2. Step through and compare. The first line where the real value differs from your prediction is the bug, or is just after it.

## Learn first (5 min)
One of these bugs is famous. A default argument value is created **once**, when the
function is defined, not on every call. If that default is a list, every call shares the
same list. Watch `seen` at the start of the second call.

## Explain-back (answer in the PR)
For each bug: the line, what you expected the variable to hold, what it held, and the fix.
Then: one of the tests passes even with the bug in place. Which one, and why is that a problem?
