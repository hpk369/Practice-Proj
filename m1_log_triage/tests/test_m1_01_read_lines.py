"""Tests for M1-01. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m1_log_triage import triage

# pytestmark = pytest.mark.skip(reason="M1-01 not started. Delete this line when you begin the ticket.")

LOG = Path(__file__).parent.parent / "data" / "access.log"


def test_returns_a_list_of_stripped_lines(tmp_path):
    f = tmp_path / "small.log"
    f.write_text("first\n  second  \nthird\n")
    assert triage.read_lines(f) == ["first", "second", "third"]


def test_skips_empty_and_whitespace_only_lines(tmp_path):
    f = tmp_path / "gaps.log"
    f.write_text("first\n\n   \nsecond\n")
    assert triage.read_lines(f) == ["first", "second"]


def test_empty_file_gives_empty_list(tmp_path):
    f = tmp_path / "empty.log"
    f.write_text("")
    assert triage.read_lines(f) == []


def test_real_log_has_241_non_empty_lines():
    # 243 lines in the file, 2 of them empty
    assert len(triage.read_lines(LOG)) == 241
