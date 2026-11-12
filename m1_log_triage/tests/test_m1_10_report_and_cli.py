"""Tests for M1-10. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-10 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_report_has_the_headline_numbers(records):
    report = triage.format_report(records)
    assert "Total requests: 6" in report
    assert "Error rate: 50.0%" in report
    assert "Period: 2026-11-10 08:59 to 2026-11-10 09:04" in report


def test_report_lists_statuses_in_ascending_order(records):
    lines = triage.format_report(records).splitlines()
    status_lines = [line for line in lines if line.startswith("  ") and line.strip()[:3].isdigit()]
    assert status_lines[:4] == ["  200: 2", "  201: 1", "  401: 2", "  500: 1"]


def test_report_lists_error_codes_most_common_first(records):
    report = triage.format_report(records)
    assert "  invalid_api_key: 2" in report
    assert report.index("invalid_api_key: 2") < report.index("internal_error: 1")


def test_report_names_the_slowest_request(records):
    assert "req_4" in triage.format_report(records)


def test_main_prints_the_report_and_returns_0(capsys):
    exit_code = triage.main([str(LOG)])
    out = capsys.readouterr().out
    assert exit_code == 0
    assert "Total requests: 240" in out
    assert "Error rate: 26.2%" in out


def test_main_returns_1_for_a_missing_file(capsys):
    exit_code = triage.main(["no-such-file.log"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "File not found" in captured.err
    assert captured.out == ""
