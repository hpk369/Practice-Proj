# M1-11 · Export to CSV

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sun Nov 15 | S | `write_csv`, `main` | `tests/test_m1_11_write_csv.py` (3) | 40 m / __ |

## Context
The account manager wants the numbers in a spreadsheet for the customer call.

## Requirements
- `write_csv(counts, path, header)` writes a header row, then one row per item in `counts`,
  highest count first.
- Add an optional `--csv PATH` argument to `main`. When given, write the status counts there
  with the header `status,count`.

## Acceptance criteria
`tests/test_m1_11_write_csv.py` passes, and this produces a file you can open in a spreadsheet:
```bash
python -m m1_log_triage.triage m1_log_triage/data/access.log --csv out/status.csv
```
(`out/` is in `.gitignore`. Create the folder first.)

## Learn first (5 min)
- **Use the `csv` module**, not string joins with commas. It quotes values that contain
  commas, which one of the tests checks.
  ```python
  with open(path, "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["a", "b"])
  ```
- **Sort by count.** `sorted(counts.items(), key=lambda pair: pair[1], reverse=True)`.
- **Optional arguments** start with `--`: `parser.add_argument("--csv")`. The value is
  `None` when the flag isn't used.

## Explain-back (answer in the PR)
1. What would `",".join(...)` get wrong for a path like `/v1/scans, v2`?
