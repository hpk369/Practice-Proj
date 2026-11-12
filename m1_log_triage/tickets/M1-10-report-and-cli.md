# M1-10 · The report and the command line

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sun Nov 15 | M | `format_report`, `main` | `tests/test_m1_10_report_and_cli.py` (6) | 75 m / __ |

## Context
Until now you've called functions from a Python prompt. A teammate needs one command that
prints something they can paste into a ticket.

## Requirements
**`format_report(records)`** returns one string in this layout:

```text
Acme Shield log triage
Period: 2026-11-10 09:00 to 2026-11-10 10:20
Total requests: 240
Error rate: 26.2%

By status
  200: 131
  201: 46
  ...

Top error codes
  billing_suspended: 32
  ...

Slowest requests
  2373.8 ms  GET /v1/alerts  req_d1c3a839eca22d9f
  ...
```
Statuses in ascending order. Error codes most common first, counted over error records
only. Five slowest requests. Two spaces of indent on the detail lines.

**`main(argv=None)`** is the command-line entry point:
- One required argument: the path to the log file.
- If the file doesn't exist: print `File not found: <path>` to standard error, print
  nothing to standard output, and return `1`.
- Otherwise print the report and return `0`.

## Acceptance criteria
`tests/test_m1_10_report_and_cli.py` passes, and this works:
```bash
python -m m1_log_triage.triage m1_log_triage/data/access.log
```

## Learn first (10 min)
- **f-strings.** `f"Total requests: {len(records)}"` puts values into text.
  `f"{first:%Y-%m-%d %H:%M}"` formats a datetime.
- **Building multi-line text.** Collect lines in a list, then `"\n".join(lines)`.
- **Sorting a dict.** `sorted(counts.items())` gives `(key, value)` pairs in key order.
- **`argparse`.** `import argparse`:
  ```python
  parser = argparse.ArgumentParser(description="...")
  parser.add_argument("logfile")
  args = parser.parse_args(argv)   # args.logfile holds the value
  ```
- **Exit codes.** A program returns 0 for success and non-zero for failure. Scripts and CI
  read that number. `print(message, file=sys.stderr)` sends errors to the error stream.
- **Does it exist?** `from pathlib import Path`, then `Path(args.logfile).exists()`.

<details><summary>Hint (direction)</summary>

`format_report` should call the functions you already wrote and do no counting of its own.
`main` is: parse arguments, check the file, load, print, return.
</details>

## Explain-back (answer in the PR)
1. Why does the error message go to stderr and the report to stdout?
2. `format_report` returns a string and `main` prints it. Why not print inside `format_report`?
