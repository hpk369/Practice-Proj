"""Tests for M1-03. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-03 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_cut_off_line_returns_none():
    assert triage.parse_line('{"ts": "2026-11-10T09:4') is None


def test_plain_text_returns_none():
    assert triage.parse_line("server restarting") is None


def test_valid_line_still_returns_a_dict():
    assert triage.parse_line('{"status": 200}') == {"status": 200}


def test_load_records_skips_bad_lines(tmp_path):
    f = tmp_path / "mixed.log"
    f.write_text('{"status": 200}\n\n{"status": 5\n{"status": 404}\n')
    assert triage.load_records(f) == [{"status": 200}, {"status": 404}]


def test_real_log_has_240_valid_records():
    records = triage.load_records(LOG)
    assert len(records) == 240
    assert all(isinstance(r, dict) for r in records)
