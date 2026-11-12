"""Tests for M2-08. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m2_api_key_checker import checker

pytestmark = pytest.mark.skip(reason="M2-08 not started. Delete this line when you begin the ticket.")

TENANTS = Path(__file__).parent.parent / "data" / "tenants.json"
LIVE = "acme_live_00000000000000000000000000000f01"
TEST = "acme_test_00000000000000000000000000000f02"
UNKNOWN = "acme_live_ffffffffffffffffffffffffffffffff"


def test_mask_key_keeps_the_prefix_and_last_four():
    assert checker.mask_key(LIVE) == "acme_live_...0f01"


def test_mask_key_never_shows_a_short_value_in_full():
    assert checker.mask_key("short") == "..."
    assert checker.mask_key("exactly14chars") == "..."


def test_valid_key_prints_ok_and_returns_0(capsys):
    exit_code = checker.main([f"Bearer {LIVE}"])
    assert exit_code == 0
    assert capsys.readouterr().out.strip() == "OK tenant=fernhollow"


def test_test_key_prints_denied_and_returns_1(capsys):
    exit_code = checker.main([f"Bearer {TEST}"])
    assert exit_code == 1
    assert capsys.readouterr().out.startswith("DENIED key_environment_mismatch: ")


def test_wrong_scheme_prints_denied_and_returns_1(capsys):
    exit_code = checker.main([f"Token {LIVE}"])
    assert exit_code == 1
    assert capsys.readouterr().out.startswith("DENIED invalid_api_key: ")


def test_denial_is_logged_as_a_warning_with_the_code(caplog, capsys):
    with caplog.at_level("WARNING"):
        checker.main([f"Bearer {UNKNOWN}"])
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
    assert "invalid_api_key" in caplog.text


def test_the_full_key_never_reaches_the_log(caplog, capsys):
    with caplog.at_level("DEBUG"):
        checker.main([f"Bearer {UNKNOWN}"])
        checker.main([f"Bearer {TEST}"])
    assert UNKNOWN not in caplog.text
    assert TEST not in caplog.text
    assert "acme_live_...ffff" in caplog.text


def test_success_logs_nothing_at_warning_level(caplog, capsys):
    with caplog.at_level("WARNING"):
        checker.main([f"Bearer {LIVE}"])
    assert caplog.records == []
