"""Tests for M3-06, debugging drill 3a. Fix the drill file until these pass. Don't edit the tests."""

import pytest

from m3_rate_limiter.drills.drill_3a_quota import DailyQuota

pytestmark = pytest.mark.skip(reason="M3-06 not started. Delete this line when you begin the ticket.")


@pytest.fixture
def quota():
    q = DailyQuota(limits={"fernhollow": 500}, default_limit=100)
    q.record("fernhollow", "2026-11-10", 120)
    q.record("cedarline", "2026-11-10", 30)
    q.record("relaypoint", "2026-11-10", 75)
    q.record("cedarline", "2026-11-11", 90)
    return q


def test_limit_for_uses_the_default_when_a_tenant_has_no_limit(quota):
    assert quota.limit_for("fernhollow") == 500
    assert quota.limit_for("cedarline") == 100


def test_record_returns_the_running_total(quota):
    assert quota.record("fernhollow", "2026-11-10", 30) == 150
    assert quota.record("fernhollow", "2026-11-10") == 151


def test_remaining_for_a_tenant_with_its_own_limit(quota):
    assert quota.remaining("fernhollow", "2026-11-10") == 380


def test_remaining_for_a_tenant_on_the_default_limit(quota):
    assert quota.remaining("cedarline", "2026-11-10") == 70


def test_remaining_never_goes_below_zero(quota):
    quota.record("relaypoint", "2026-11-10", 500)
    assert quota.remaining("relaypoint", "2026-11-10") == 0


def test_top_users_only_counts_the_day_asked_for(quota):
    assert quota.top_users("2026-11-10", n=2) == [("fernhollow", 120), ("relaypoint", 75)]


def test_top_users_on_a_quiet_day(quota):
    assert quota.top_users("2026-11-11") == [("cedarline", 90)]
