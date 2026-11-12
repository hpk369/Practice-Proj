"""Debugging drill 3b (ticket M3-07). This file has three bugs. Tests are your only clue.

Time yourself: the Nov 27 check gives you 30 minutes for three bugs.

What the code is meant to do
----------------------------
minutes_between(start, end)   whole minutes between two ISO timestamps, however far apart
affected_tenants(records)     sorted tenant ids that received a server error (status 500 or above)
summary_line(records)         "<n> server errors across <t> tenants between HH:MM and HH:MM UTC",
                              using the earliest and latest error times, whatever order the
                              records arrive in
"""

from __future__ import annotations

from datetime import datetime


def minutes_between(start, end):
    delta = datetime.fromisoformat(end) - datetime.fromisoformat(start)
    return delta.seconds // 60


def affected_tenants(records):
    tenants = set()
    for record in records:
        if record["status"] > 500 and record["tenant_id"] is not None:
            tenants.add(record["tenant_id"])
    return sorted(tenants)


def summary_line(records):
    errors = [r for r in records if r["status"] >= 500]
    first = datetime.fromisoformat(errors[0]["ts"])
    last = datetime.fromisoformat(errors[-1]["ts"])
    tenants = affected_tenants(records)
    return (
        f"{len(errors)} server errors across {len(tenants)} tenants "
        f"between {first:%H:%M} and {last:%H:%M} UTC"
    )
