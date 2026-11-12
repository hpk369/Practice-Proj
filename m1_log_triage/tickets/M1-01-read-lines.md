# M1-01 · Read the log file

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Thu Nov 12 | XS | `read_lines` | `tests/test_m1_01_read_lines.py` (4) | 25 m / __ |

## Context
A customer says "we saw errors yesterday morning". Support exports the access log for that
window. Before anything can be counted, the tool has to read the file and throw away the
empty lines that the log shipper leaves behind.

## Requirements
Implement `read_lines(path)` in `triage.py`.
- Open the file and go through it line by line.
- Remove the whitespace around each line (including the newline at the end).
- Leave out lines that are empty after that.
- Return the remaining lines as a list of strings.

## Acceptance criteria
Delete the `pytestmark` line in the test file, then `pytest m1_log_triage/tests/test_m1_01_read_lines.py` passes.

## Learn first (5 min)
- **Opening a file.** `with open(path) as f:` opens it and closes it for you when the
  indented block ends. `for line in f:` gives you one line at a time.
- **Strings.** `line.strip()` returns a new string without leading and trailing whitespace.
  An empty string counts as false in an `if`, so `if line:` means "if it isn't empty".
- **Lists.** `lines = []` makes an empty list. `lines.append(x)` adds to the end.
- **`return`.** A function hands its result back with `return`. Printing shows something on
  screen; returning gives the value to whoever called the function. Tests need the return.

<details><summary>Hint (direction)</summary>

Four steps, in this order: make an empty list, loop over the file, strip each line, append
it if anything is left. Return the list after the loop, not inside it.
</details>

## Try it by hand
```bash
python -c "from m1_log_triage import triage; print(len(triage.read_lines('m1_log_triage/data/access.log')))"
```
You should see 241. The file has 243 lines, so two were empty.

## Explain-back (answer in the PR)
1. What would go wrong later if you kept the newline on the end of each line?
2. What is the difference between `print(lines)` and `return lines`?
