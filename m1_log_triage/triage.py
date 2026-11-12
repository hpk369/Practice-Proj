"""Log triage for Acme Shield access logs. Mini project M1 (yours).

Each line of the log is one request, written as JSON:

    {"ts": "2026-11-10T09:00:19.000+00:00", "level": "info", "request_id": "req_b9f7...",
     "tenant_id": "fernhollow", "method": "GET", "path": "/v1/alerts", "status": 200,
     "duration_ms": 32.98, "error_code": null}

`tenant_id` and `error_code` can be null. A real log is never perfectly clean: this one has
empty lines and one line that was cut off mid-write.

Every function below belongs to one ticket in `tickets/`. Replace the `raise` line with
your code. Add the imports you need at the top as you go.
"""

from __future__ import annotations


def read_lines(path):
    #M1-01. Return the non-empty lines of the file, each with surrounding whitespace removed.
    f = open(path) 
    lines = []
    for line in f:
        line = line.strip()
        if line:
            lines.append(line)
    return lines
    #raise NotImplementedError("M1-01: implement read_lines")


def parse_line(line):
    """M1-02 and M1-03. Turn one log line into a dict. Return None if it isn't valid JSON."""
    raise NotImplementedError("M1-02: implement parse_line")


def load_records(path):
    """M1-03. Return every valid record in the file as a list of dicts. Skip bad lines."""
    raise NotImplementedError("M1-03: implement load_records")


def count_by_status(records):
    """M1-04. Return a plain dict of {status: number of requests}."""
    raise NotImplementedError("M1-04: implement count_by_status")


def count_by(records, field):
    """M1-05. Return a collections.Counter of the values of `field` across the records."""
    raise NotImplementedError("M1-05: implement count_by")


def error_records(records):
    """M1-06. Return only the records whose status is 400 or above."""
    raise NotImplementedError("M1-06: implement error_records")


def error_rate(records):
    """M1-06. Return the percentage of records that are errors, rounded to 1 decimal place.

    An empty list has an error rate of 0.0.
    """
    raise NotImplementedError("M1-06: implement error_rate")


def slowest(records, n=5):
    """M1-08. Return the n records with the highest duration_ms, slowest first."""
    raise NotImplementedError("M1-08: implement slowest")


def time_range(records):
    """M1-09. Return (first, last): the earliest and latest `ts` as datetime objects."""
    raise NotImplementedError("M1-09: implement time_range")


def format_report(records):
    """M1-10. Return the triage report as one string. The format is in the ticket."""
    raise NotImplementedError("M1-10: implement format_report")


def write_csv(counts, path, header):
    """M1-11. Write `counts` (a dict or Counter) to a CSV file, highest count first."""
    raise NotImplementedError("M1-11: implement write_csv")


def main(argv=None):
    """M1-10. Command-line entry point. Return 0 on success, 1 if the file doesn't exist."""
    raise NotImplementedError("M1-10: implement main")


if __name__ == "__main__":
    raise SystemExit(main())
