# M1 · Log triage CLI

Read an Acme Shield access log and print a triage summary: how many requests, how many
failed, who was affected, and which requests were slowest.

**Dates:** Nov 12 to 15 · **Budget:** 10 hours · **Libraries:** `json`, `collections`,
`datetime`, `csv`, `argparse`, `pathlib`, `pytest`

## Tickets

| Ticket | Day | What you build | New Python |
| --- | --- | --- | --- |
| [M1-01](tickets/M1-01-read-lines.md) | Thu | Read the file | `open`, loops, strings, lists, `return` |
| [M1-02](tickets/M1-02-parse-line.md) | Thu | Line to dict | `json`, dicts |
| [M1-03](tickets/M1-03-load-records.md) | Fri | Survive a bad line | tracebacks, `try`/`except`, `None` |
| [M1-04](tickets/M1-04-count-by-status.md) | Fri | Count per status | building a dict |
| [M1-05](tickets/M1-05-count-by.md) | Sat | Count by any field | parameters, `Counter`, comprehensions |
| [M1-06](tickets/M1-06-errors.md) | Sat | Errors and error rate | filtering, division, reuse |
| [M1-07](tickets/M1-07-debug-drill-1.md) | Sat | Debugging drill | reading tracebacks |
| [M1-08](tickets/M1-08-slowest.md) | Sat | Slowest requests | `sorted`, `key`, `lambda`, slicing |
| [M1-09](tickets/M1-09-time-range.md) | Sun | Time range | `datetime`, tuples |
| [M1-10](tickets/M1-10-report-and-cli.md) | Sun | Report and CLI | f-strings, `argparse`, exit codes |
| [M1-11](tickets/M1-11-write-csv.md) | Sun | CSV export | `csv`, optional arguments |
| [M1-12](tickets/M1-12-own-tests-and-wrap-up.md) | Sun | Your own tests | writing tests |

## Files
- `triage.py`: the module you fill in, one function per ticket
- `data/access.log`: 243 lines of sample log, including two empty lines and one cut-off line
- `tests/`: one test file per ticket, skipped until you start that ticket
- `drills/`: broken code for the debugging ticket
