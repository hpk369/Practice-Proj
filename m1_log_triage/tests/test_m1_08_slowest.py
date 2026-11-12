"""Tests for M1-08. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-08 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_slowest_first(records):
    result = triage.slowest(records, 2)
    assert [r["request_id"] for r in result] == ["req_4", "req_5"]


def test_default_is_five(records):
    assert len(triage.slowest(records)) == 5


def test_asking_for_more_than_exist(records):
    assert len(triage.slowest(records, 50)) == 6


def test_input_order_is_left_alone(records):
    triage.slowest(records, 2)
    assert records[0]["request_id"] == "req_1"


def test_real_log():
    top = triage.slowest(triage.load_records(LOG), 3)
    assert [r["request_id"] for r in top] == [
        "req_d1c3a839eca22d9f",
        "req_947cff7c4992ab85",
        "req_69092ddee7745df1",
    ]
