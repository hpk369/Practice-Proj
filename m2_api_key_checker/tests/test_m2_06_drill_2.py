"""Tests for M2-06, debugging drill 2. Fix the drill file until these pass. Don't edit the tests."""

import pytest

from m2_api_key_checker.drills import drill_2_key_tools as drill

pytestmark = pytest.mark.skip(reason="M2-06 not started. Delete this line when you begin the ticket.")

KEYS = [
    {"key": "acme_live_a", "env": "live", "created": "2026-03-01", "tenant_id": "fernhollow"},
    {"key": "acme_test_b", "env": "test", "created": "2026-09-15", "tenant_id": "fernhollow"},
    {"key": "acme_live_c", "env": "live", "created": "2026-06-30", "tenant_id": "cedarline"},
    {"key": "acme_live_d", "env": "live", "created": "2025-12-01", "tenant_id": "relaypoint"},
]


def test_count_by_env():
    assert drill.count_by_env(KEYS) == {"live": 3, "test": 1}


def test_count_by_env_single_key():
    assert drill.count_by_env(KEYS[:1]) == {"live": 1, "test": 0}


def test_newest_key():
    assert drill.newest_key(KEYS)["key"] == "acme_test_b"


def test_unique_tenants():
    assert drill.unique_tenants(KEYS) == ["fernhollow", "cedarline", "relaypoint"]


def test_unique_tenants_starts_fresh_on_every_call():
    drill.unique_tenants(KEYS)
    assert drill.unique_tenants(KEYS[:2]) == ["fernhollow"]
