"""Tests for M1-07, debugging drill 1. Fix the drill file until these pass. Don't edit the tests."""

import pytest

from m1_log_triage.drills import drill_1_tenant_summary as drill

pytestmark = pytest.mark.skip(reason="M1-07 not started. Delete this line when you begin the ticket.")


def test_requests_per_tenant(records):
    assert drill.requests_per_tenant(records) == {"fernhollow": 2, "cedarline": 2, "unknown": 2}


def test_label_with_a_tenant(records):
    assert drill.label(records[0]) == "FERNHOLLOW /v1/scans"


def test_label_without_a_tenant(records):
    assert drill.label(records[2]) == "UNKNOWN /v1/scans"


def test_average_duration(records):
    assert drill.average_duration(records) == 484.89


def test_average_duration_of_nothing():
    assert drill.average_duration([]) == 0.0
