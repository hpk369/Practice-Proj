"""Tests for M1-05. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-05 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_returns_a_counter(records):
    from collections import Counter

    assert isinstance(triage.count_by(records, "path"), Counter)


def test_counts_by_path(records):
    assert triage.count_by(records, "path") == {"/v1/scans": 4, "/v1/alerts": 2}


def test_none_is_counted_as_its_own_value(records):
    counts = triage.count_by(records, "tenant_id")
    assert counts[None] == 2
    assert counts["fernhollow"] == 2


def test_most_common_on_the_real_log():
    counts = triage.count_by(triage.load_records(LOG), "tenant_id")
    assert counts.most_common(1) == [("fernhollow", 78)]
    assert counts["relaypoint"] == 32


def test_same_answer_as_count_by_status(records):
    assert triage.count_by(records, "status") == triage.count_by_status(records)
