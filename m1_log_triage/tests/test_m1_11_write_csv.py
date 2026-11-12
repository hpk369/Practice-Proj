"""Tests for M1-11. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

pytestmark = pytest.mark.skip(reason="M1-11 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_writes_header_then_rows_highest_count_first(tmp_path):
    out = tmp_path / "status.csv"
    triage.write_csv({200: 2, 401: 5, 500: 1}, out, ["status", "count"])
    assert out.read_text().splitlines() == ["status,count", "401,5", "200,2", "500,1"]


def test_values_with_commas_are_quoted(tmp_path):
    out = tmp_path / "paths.csv"
    triage.write_csv({"/v1/scans, v2": 3}, out, ["path", "count"])
    assert out.read_text().splitlines()[1] == '"/v1/scans, v2",3'


def test_cli_writes_a_csv_when_asked(tmp_path, capsys):
    out = tmp_path / "status.csv"
    exit_code = triage.main([str(LOG), "--csv", str(out)])
    capsys.readouterr()
    assert exit_code == 0
    rows = out.read_text().splitlines()
    assert rows[0] == "status,count"
    assert rows[1] == "200,131"
    assert len(rows) == 7
