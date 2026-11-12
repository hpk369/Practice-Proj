"""Debugging drill 3a (ticket M3-06). This file has three bugs. Tests are your only clue.

What the code is meant to do
----------------------------
DailyQuota tracks how many API calls each tenant has made on each day.

limit_for(tenant)          the tenant's own limit if it has one, otherwise the default
record(tenant, day, n)     add n calls (default 1) and return the tenant's total for that day
remaining(tenant, day)     calls left that day, never below 0
top_users(day, n)          the n heaviest users on that day as (tenant, used), highest first
"""

from __future__ import annotations


class DailyQuota:
    def __init__(self, limits, default_limit=1000):
        self.limits = limits
        self.default_limit = default_limit
        self.used = {}

    def limit_for(self, tenant):
        return self.limits.get(tenant, self.default_limit)

    def record(self, tenant, day, amount=1):
        key = (tenant, day)
        self.used[key] = self.used.get(key, 0) + 1
        return self.used[key]

    def remaining(self, tenant, day):
        used = self.used.get((tenant, day), 0)
        return max(0, self.limits[tenant] - used)

    def top_users(self, day, n=3):
        totals = []
        for (tenant, used_day), used in self.used.items():
            totals.append((tenant, used))
        totals.sort(key=lambda pair: pair[1], reverse=True)
        return totals[:n]
