"""Debugging drill 2 (ticket M2-06). This file has three bugs. None of them raises an error.

The code runs and returns the wrong answer, so there is no traceback to read. Use the
VS Code debugger: set a breakpoint, step through, and watch the variables change.

What the code is meant to do
----------------------------
count_by_env(keys) -> {"live": n, "test": n} for a list of key records
newest_key(keys) -> the key record with the latest "created" date
unique_tenants(records) -> tenant ids in first-seen order, without repeats.
    Each call starts fresh: calling it twice gives the same answer both times.

A key record looks like {"key": "acme_live_...", "env": "live", "created": "2026-03-01"}.
"""

from __future__ import annotations


def count_by_env(keys):
    counts = {"live": 0, "test": 0}
    for i in range(1, len(keys)):
        counts[keys[i]["env"]] += 1
    return counts


def newest_key(keys):
    newest = keys[0]
    for key in keys:
        if key["created"] < newest["created"]:
            newest = key
    return newest


def unique_tenants(records, seen=[]):
    for record in records:
        if record["tenant_id"] not in seen:
            seen.append(record["tenant_id"])
    return seen
