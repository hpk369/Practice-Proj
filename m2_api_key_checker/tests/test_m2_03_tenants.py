"""Tests for M2-03. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m2_api_key_checker import checker

pytestmark = pytest.mark.skip(reason="M2-03 not started. Delete this line when you begin the ticket.")

TENANTS = Path(__file__).parent.parent / "data" / "tenants.json"
LIVE = "acme_live_00000000000000000000000000000f01"
TEST = "acme_test_00000000000000000000000000000f02"
UNKNOWN = "acme_live_ffffffffffffffffffffffffffffffff"


def test_api_key_holds_its_fields():
    key = checker.ApiKey(key=LIVE, env="live")
    assert key.key == LIVE
    assert key.env == "live"


def test_tenant_billing_status_defaults_to_active():
    tenant = checker.Tenant(tenant_id="t1", name="Tenant One", api_keys=[])
    assert tenant.billing_status == "active"


def test_two_api_keys_with_the_same_values_are_equal():
    assert checker.ApiKey(key=LIVE, env="live") == checker.ApiKey(key=LIVE, env="live")


def test_frozen_dataclass_cannot_be_changed():
    key = checker.ApiKey(key=LIVE, env="live")
    with pytest.raises(AttributeError):
        key.env = "test"


def test_load_tenants_returns_tenant_objects():
    tenants = checker.load_tenants(TENANTS)
    assert [t.tenant_id for t in tenants] == ["fernhollow", "cedarline", "relaypoint"]
    assert all(isinstance(t, checker.Tenant) for t in tenants)


def test_load_tenants_builds_api_key_objects():
    fernhollow = checker.load_tenants(TENANTS)[0]
    assert fernhollow.api_keys == [
        checker.ApiKey(key=LIVE, env="live"),
        checker.ApiKey(key=TEST, env="test"),
    ]


def test_billing_status_comes_from_the_file_or_the_default():
    tenants = checker.load_tenants(TENANTS)
    # cedarline has no billing_status in the file
    assert [t.billing_status for t in tenants] == ["active", "active", "suspended"]
