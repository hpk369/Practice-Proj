"""Tests for M2-02. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m2_api_key_checker import checker

pytestmark = pytest.mark.skip(reason="M2-02 not started. Delete this line when you begin the ticket.")

TENANTS = Path(__file__).parent.parent / "data" / "tenants.json"
LIVE = "acme_live_00000000000000000000000000000f01"
TEST = "acme_test_00000000000000000000000000000f02"
UNKNOWN = "acme_live_ffffffffffffffffffffffffffffffff"


@pytest.mark.parametrize("key", [LIVE, TEST, UNKNOWN])
def test_well_formed_keys(key):
    assert checker.is_well_formed(key) is True


@pytest.mark.parametrize(
    "key",
    [
        "",
        "acme_live_",
        "acme_prod_00000000000000000000000000000f01",  # no such environment
        "acme_live_00000000000000000000000000000f0",  # 31 hex characters
        "acme_live_00000000000000000000000000000f012",  # 33 hex characters
        "acme_live_0000000000000000000000000000zz01",  # z is not hex
        "ACME_LIVE_00000000000000000000000000000F01",  # wrong case
        "xacme_live_00000000000000000000000000000f01",  # junk in front
        "acme_live_00000000000000000000000000000f01\n",  # trailing newline
    ],
)
def test_malformed_keys(key):
    assert checker.is_well_formed(key) is False


def test_key_env_reads_the_environment_from_the_key():
    assert checker.key_env(LIVE) == "live"
    assert checker.key_env(TEST) == "test"


def test_key_env_of_a_malformed_key_is_none():
    assert checker.key_env("acme_prod_123") is None
