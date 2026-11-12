"""Debugging drill 1 (ticket M1-07). This file has four bugs. Each one raises an error.

A teammate wrote this in a hurry and went on leave. Don't rewrite it. Find each bug from
its traceback and make the smallest fix that makes the tests pass.

What the code is meant to do
----------------------------
requests_per_tenant(records) -> dict of {tenant_id: number of requests}
    Requests with no tenant (tenant_id is None) are counted under the key "unknown".
label(record) -> "TENANT /path", for example "FERNHOLLOW /v1/scans"
    A request with no tenant is labelled "UNKNOWN /path".
average_duration(records) -> mean duration_ms, rounded to 2 decimal places
    An empty list has an average of 0.0.
"""

from __future__ import annotations


def requests_per_tenant(records):
    counts = {}
    for record in records:
        tenant = record["tenant"]
        if tenant is None:
            tenant = "unknown"
        counts[tenant] += 1
    return counts


def label(record):
    return record["tenant_id"].upper() + " " + record["path"]


def average_duration(records):
    total = 0
    for record in records:
        total += record["duration_ms"]
    return round(total / len(records), 2)
