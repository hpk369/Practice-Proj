"""Tests for M2-04. These define "done" for the ticket. Read them before you write code."""

from pathlib import Path

import pytest

from m2_api_key_checker import checker

pytestmark = pytest.mark.skip(reason="M2-04 not started. Delete this line when you begin the ticket.")

TENANTS = Path(__file__).parent.parent / "data" / "tenants.json"
LIVE = "acme_live_00000000000000000000000000000f01"
TEST = "acme_test_00000000000000000000000000000f02"
UNKNOWN = "acme_live_ffffffffffffffffffffffffffffffff"


@pytest.fixture
def index():
    return checker.build_key_index(checker.load_tenants(TENANTS))


def test_index_has_every_key(index):
    assert len(index) == 4
    assert LIVE in index
    assert TEST in index


def test_index_maps_a_key_to_its_tenant_and_record(index):
    tenant, record = index[TEST]
    assert tenant.tenant_id == "fernhollow"
    assert record.env == "test"


def test_auth_error_carries_code_and_message():
    err = checker.AuthError("invalid_api_key", "No such key.")
    assert err.code == "invalid_api_key"
    assert err.message == "No such key."
    assert str(err) == "No such key."
    assert isinstance(err, Exception)


def test_known_live_key_returns_context(index):
    ctx = checker.authenticate(f"Bearer {LIVE}", index)
    assert isinstance(ctx, checker.AuthContext)
    assert ctx.tenant.tenant_id == "fernhollow"
    assert ctx.api_key == LIVE


@pytest.mark.parametrize(
    "header",
    [None, "", f"Token {LIVE}", LIVE, "Bearer ", f"Bearer {UNKNOWN}", "Bearer not-a-key"],
)
def test_bad_headers_and_unknown_keys_are_invalid_api_key(index, header):
    with pytest.raises(checker.AuthError) as excinfo:
        checker.authenticate(header, index)
    assert excinfo.value.code == "invalid_api_key"


def test_test_key_on_live_service_is_environment_mismatch(index):
    with pytest.raises(checker.AuthError) as excinfo:
        checker.authenticate(f"Bearer {TEST}", index)
    assert excinfo.value.code == "key_environment_mismatch"
    assert "test" in excinfo.value.message


def test_the_same_test_key_works_on_a_test_service(index):
    ctx = checker.authenticate(f"Bearer {TEST}", index, service_env="test")
    assert ctx.tenant.tenant_id == "fernhollow"


def test_a_suspended_tenant_still_authenticates(index):
    # Authentication answers "who are you?". Billing is a separate check (ACME-4 in Project-1).
    ctx = checker.authenticate("Bearer acme_live_00000000000000000000000000000a01", index)
    assert ctx.tenant.billing_status == "suspended"
