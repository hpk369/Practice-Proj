# M2 · API key checker

Decide whether an `Authorization` header holds a valid Acme Shield key, and say why not
when it doesn't. This is the logic of ticket ACME-2 from Project-1 as plain Python.

**Dates:** Nov 16 to 21 · **Budget:** 9 hours · **Libraries:** `re`, `dataclasses`, `json`,
`pathlib`, `logging`, `argparse`, `pytest` (fixtures, parametrize, raises, caplog)

## Tickets

| Ticket | Day | What you build | New Python |
| --- | --- | --- | --- |
| [M2-01](tickets/M2-01-parse-authorization.md) | Mon | Read the header | `partition`, unpacking, early returns |
| [M2-02](tickets/M2-02-key-format.md) | Tue | Check a key's shape | regular expressions |
| [M2-03](tickets/M2-03-tenants.md) | Wed | Tenants as data classes | `dataclass`, type hints, nested data |
| [M2-04](tickets/M2-04-authenticate.md) | Thu | Authenticate | dict index, custom exceptions, `raise` |
| [M2-05](tickets/M2-05-read-project-1.md) | Fri | Read two Project-1 files | reading code |
| [M2-06](tickets/M2-06-debug-drill-2.md) | Sat | Debugger drill | breakpoints, stepping, watch |
| [M2-07](tickets/M2-07-own-tests.md) | Sat | Your own tests | fixtures, parametrize |
| [M2-08](tickets/M2-08-cli-and-logging.md) | Sat | CLI, logging, redaction | `logging`, slicing, `try`/`except` on your own error |
| [M2-09](tickets/M2-09-wrap-up.md) | Sat | Map back to ACME-2 | |

## Files
- `checker.py`: the module you fill in
- `data/tenants.json`: three fictional tenants with placeholder keys
- `tests/`: one test file per ticket, skipped until you start that ticket
- `drills/`: code with silent bugs for the debugger ticket
