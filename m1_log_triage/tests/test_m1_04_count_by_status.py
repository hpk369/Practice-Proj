"""Tests for M1-04. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-04 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_counts_small_list(records):
    assert triage.count_by_status(records) == {200: 2, 201: 1, 401: 2, 500: 1}


def test_empty_list_gives_empty_dict():
    assert triage.count_by_status([]) == {}


def test_real_log():
    counts = triage.count_by_status(triage.load_records(LOG))
    assert counts == {200: 131, 201: 46, 401: 23, 403: 32, 429: 2, 500: 6}
