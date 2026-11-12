# M1-02 · Turn a line into a record

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Thu Nov 12 | XS | `parse_line` | `tests/test_m1_02_parse_line.py` (4) | 25 m / __ |

## Context
Searching the log for the text `"status": 500` works until someone changes the spacing, or a
path happens to contain "500". Each line is JSON, so read it as data and ask for the field.

## Requirements
Implement `parse_line(line)`: take one line of text and return it as a dict.
Lines that aren't valid JSON are the next ticket. Don't handle them yet.

## Acceptance criteria
`tests/test_m1_02_parse_line.py` passes with its `pytestmark` line deleted.

## Learn first (5 min)
- **JSON** is text that describes data. `import json` at the top of the file, then
  `json.loads(text)` ("load string") turns that text into Python objects.
- **Dicts.** A JSON object becomes a dict: `record["status"]` gives the value stored under
  the key `"status"`. Numbers stay numbers, and JSON `null` becomes Python `None`.

## Try it by hand
Open a Python prompt (`python`) and run:
```python
from m1_log_triage import triage
lines = triage.read_lines("m1_log_triage/data/access.log")
record = triage.parse_line(lines[0])
record["status"], record["path"], record["tenant_id"]
for line in lines:
    triage.parse_line(line)
```
The loop crashes partway through. **Leave it broken.** Read the last line of the error and
find which line of the log caused it. That is M1-03.

## Explain-back (answer in the PR)
1. Why is `record["status"] == 500` more reliable than `'"status": 500' in line`?
2. Paste the last line of the error from the loop. What is it telling you?
