"""Tests for M1-02. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_returns_a_dict():
    record = triage.parse_line('{"status": 200, "path": "/v1/scans"}')
    assert record == {"status": 200, "path": "/v1/scans"}


def test_numbers_stay_numbers():
    record = triage.parse_line('{"status": 500, "duration_ms": 12.5}')
    assert record["status"] == 500
    assert isinstance(record["status"], int)
    assert isinstance(record["duration_ms"], float)


def test_json_null_becomes_python_none():
    record = triage.parse_line('{"tenant_id": null}')
    assert record["tenant_id"] is None


def test_first_line_of_the_real_log():
    first = triage.read_lines(LOG)[0]
    record = triage.parse_line(first)
    assert record["tenant_id"] == "fernhollow"
    assert record["path"] == "/v1/alerts"
    assert record["status"] == 200
