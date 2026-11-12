"""Tests for M3-07, debugging drill 3b. Fix the drill file until these pass. Don't edit the tests."""

import pytest

from m3_rate_limiter.drills import drill_3b_incident_report as drill

pytestmark = pytest.mark.skip(reason="M3-07 not started. Delete this line when you begin the ticket.")

RECORDS = [
    {"ts": "2026-11-10T09:42:10+00:00", "tenant_id": "cedarline", "status": 500},
    {"ts": "2026-11-10T09:15:00+00:00", "tenant_id": "fernhollow", "status": 503},
    {"ts": "2026-11-10T09:20:30+00:00", "tenant_id": "fernhollow", "status": 200},
    {"ts": "2026-11-10T09:31:45+00:00", "tenant_id": None, "status": 500},
    {"ts": "2026-11-10T09:05:00+00:00", "tenant_id": "relaypoint", "status": 403},
]


def test_minutes_between_within_an_hour():
    assert drill.minutes_between("2026-11-10T09:15:00+00:00", "2026-11-10T09:42:10+00:00") == 27


def test_minutes_between_across_two_days():
    assert drill.minutes_between("2026-11-10T23:30:00+00:00", "2026-11-12T00:30:00+00:00") == 1500


def test_affected_tenants_includes_plain_500s():
    assert drill.affected_tenants(RECORDS) == ["cedarline", "fernhollow"]


def test_affected_tenants_ignores_client_errors():
    assert "relaypoint" not in drill.affected_tenants(RECORDS)


def test_summary_line_uses_earliest_and_latest_error():
    assert drill.summary_line(RECORDS) == (
        "3 server errors across 2 tenants between 09:15 and 09:42 UTC"
    )
