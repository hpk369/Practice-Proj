# M3 · Rate limiter

A fixed-window rate limiter as a class, with the clock passed in so it can be tested
without waiting. Same contract as ticket ACME-3 in Project-1.

**Dates:** Nov 22 to 27 · **Budget:** 9 hours · **Libraries:** `time`, `math`,
`collections.defaultdict`, `dataclasses`, `logging`, `pytest` (fixtures, fake clock, caplog)

## Tickets

| Ticket | Day | What you build | New Python |
| --- | --- | --- | --- |
| [M3-01](tickets/M3-01-request-counter.md) | Sun | A class that counts | classes, `__init__`, `self`, `defaultdict` |
| [M3-02](tickets/M3-02-windows.md) | Sun | Window arithmetic | floor division, `math.ceil`, constants |
| [M3-03](tickets/M3-03-rate-limiter.md) | Sun | The rate limiter | objects owning objects, injected clock |
| [M3-04](tickets/M3-04-read-and-predict.md) | Sun | Read and predict tests | reading code, functions as arguments |
| [M3-05](tickets/M3-05-headers-and-logging.md) | Mon | Headers and logging | building dicts, logging |
| [M3-06](tickets/M3-06-debug-drill-3a.md) | Tue | Planted bugs, round 1 | debugging a class |
| [M3-07](tickets/M3-07-debug-drill-3b.md) | Wed | Planted bugs, timed | debugging silent bugs |
| [M3-08](tickets/M3-08-dry-run-and-checkpoint.md) | Thu, Fri | Dry run and checkpoint | |

## Files
- `limiter.py`: the module you fill in
- `reading/retry.py`: correct code to read for M3-04
- `tests/`: one test file per ticket, skipped until you start that ticket
- `drills/`: two files with planted bugs
