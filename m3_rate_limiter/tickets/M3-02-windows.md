# M3-02 · Window arithmetic

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sun Nov 22 | S | `window_start`, `reset_after` | `tests/test_m3_02_windows.py` (12) | 40 m / __ |

## Context
"Rate limited. Try again in 17 seconds" is far more useful to a customer than "rate
limited". To say that, the limiter needs to know when the current window ends.

## Requirements
Windows are 60 seconds long and start at multiples of 60 on the clock.
- `window_start(now)` returns the start of the window containing `now`: `150.5` gives `120.0`.
- `reset_after(now)` returns whole seconds until that window ends, rounded **up**, and never
  less than 1: at `150.5` there are 29.5 seconds left, so it returns `30`.

## Acceptance criteria
`tests/test_m3_02_windows.py` passes.

## Learn first (10 min)
- **Time as a number.** `time.time()` returns seconds since 1970 as a float, such as
  `1794300000.25`. The tests use small numbers like `120.0` so you can check by hand.
- **Floor division.** `//` divides and rounds down: `150.5 // 60` is `2.0`. Multiply back
  by 60 to get the window start.
- **Rounding up.** `import math`, then `math.ceil(29.5)` is `30`. It returns an int.
- **A lower bound.** `max(1, value)` never returns less than 1.
- **Use the constant.** `WINDOW_SECONDS` is defined at the top. Don't write `60` in your code.

## Try it by hand
Work out both answers on paper for `now = 179.999` before you run the tests.

## Explain-back (answer in the PR)
1. Why round up and not down? What happens to a customer who is told "retry in 0 seconds"?
2. Why does `WINDOW_SECONDS` exist as a name when it is just 60?
