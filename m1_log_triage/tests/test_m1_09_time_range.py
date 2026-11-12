"""Tests for M1-09. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-09 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_returns_datetimes(records):
    from datetime import datetime

    first, last = triage.time_range(records)
    assert isinstance(first, datetime)
    assert isinstance(last, datetime)


def test_finds_earliest_and_latest_even_when_out_of_order(records):
    # req_6 is last in the list but earliest in time
    first, last = triage.time_range(records)
    assert (first.hour, first.minute) == (8, 59)
    assert (last.hour, last.minute) == (9, 4)


def test_real_log_covers_80_minutes():
    first, last = triage.time_range(triage.load_records(LOG))
    minutes = (last - first).total_seconds() / 60
    assert 80 < minutes < 81
