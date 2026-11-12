"""Tests for M1-06. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-06 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_error_records_keeps_400_and_above(records):
    errors = triage.error_records(records)
    assert [r["request_id"] for r in errors] == ["req_3", "req_4", "req_6"]


def test_error_records_does_not_change_the_input(records):
    triage.error_records(records)
    assert len(records) == 6


def test_error_rate_small_list(records):
    # 3 errors out of 6
    assert triage.error_rate(records) == 50.0


def test_error_rate_of_nothing_is_zero():
    assert triage.error_rate([]) == 0.0


def test_error_rate_is_rounded_to_one_decimal():
    three = [{"status": 200}, {"status": 200}, {"status": 500}]
    assert triage.error_rate(three) == 33.3


def test_real_log():
    records = triage.load_records(LOG)
    assert len(triage.error_records(records)) == 63
    assert triage.error_rate(records) == 26.2
