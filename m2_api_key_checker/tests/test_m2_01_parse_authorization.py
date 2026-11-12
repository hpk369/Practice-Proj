"""Tests for M2-01. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m2_api_key_checker import checker

pytestmark = pytest.mark.skip(reason="M2-01 not started. Delete this line when you begin the ticket.")

TENANTS = Path(__file__).parent.parent / "data" / "tenants.json"
LIVE = "acme_live_00000000000000000000000000000f01"
TEST = "acme_test_00000000000000000000000000000f02"
UNKNOWN = "acme_live_ffffffffffffffffffffffffffffffff"


def test_bearer_header_returns_the_key():
    assert checker.parse_authorization(f"Bearer {LIVE}") == LIVE


@pytest.mark.parametrize("scheme", ["bearer", "BEARER", "BeArEr"])
def test_scheme_is_case_insensitive(scheme):
    assert checker.parse_authorization(f"{scheme} {LIVE}") == LIVE


def test_missing_header_returns_none():
    assert checker.parse_authorization(None) is None


def test_empty_header_returns_none():
    assert checker.parse_authorization("") is None


def test_wrong_scheme_returns_none():
    assert checker.parse_authorization(f"Token {LIVE}") is None


def test_bare_key_with_no_scheme_returns_none():
    assert checker.parse_authorization(LIVE) is None


@pytest.mark.parametrize("header", ["Bearer", "Bearer ", "Bearer    "])
def test_bearer_with_no_key_returns_none(header):
    assert checker.parse_authorization(header) is None


def test_extra_spaces_around_the_key_are_removed():
    assert checker.parse_authorization(f"Bearer   {LIVE}  ") == LIVE
