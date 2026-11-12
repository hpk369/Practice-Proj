# M1-03 · Survive a bad line

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Fri Nov 13 | S | `parse_line`, `load_records` | `tests/test_m1_03_load_records.py` (5) | 30 m / __ |

## Context
One line in the log was cut off mid-write, which happens whenever a server restarts. A
triage tool that crashes on line 144 of 243 is no use during an incident. It should skip
what it can't read and carry on.

## Requirements
- Change `parse_line` so that a line that isn't valid JSON returns `None` instead of crashing.
- Implement `load_records(path)`: read the lines, parse each one, and return a list of the
  records that parsed. Use the two functions you already have.

## Acceptance criteria
`tests/test_m1_03_load_records.py` passes, and M1-01 and M1-02 tests still pass.

## Learn first (5 min)
- **Reading a traceback.** Read it from the bottom. The last line is the error type and
  message. The lines above it are the path the program took to get there, most recent last.
- **`try` / `except`.** Code that might fail goes under `try:`. If it raises the error you
  name, Python jumps to the `except` block instead of stopping:
  ```python
  try:
      number = int(text)
  except ValueError:
      number = 0
  ```
- **Name the error.** Catch the specific error you saw in M1-02
  (`json.JSONDecodeError`). A bare `except:` would also hide your own typos.
- **`None`** means "no value". Check for it with `is None` or `is not None`.

<details><summary>Hint (direction)</summary>

`parse_line` needs four lines: try, return the parsed dict, except the JSON error, return
None. `load_records` is a loop like the one in `read_lines`, with an `if` that keeps a
record only when it is not None.
</details>

## Try it by hand
```bash
python -c "from m1_log_triage import triage; print(len(triage.load_records('m1_log_triage/data/access.log')))"
```
240 records: 241 non-empty lines minus the one that was cut off.

## Explain-back (answer in the PR)
1. Why return `None` for a bad line instead of an empty dict `{}`?
2. In a real incident, would you want to know how many lines were skipped? Where would you report it?
