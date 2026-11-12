"""Tests for M3-01. These define "done" for the ticket. Read them before you write code."""

import pytest

from m3_rate_limiter import limiter

pytestmark = pytest.mark.skip(reason="M3-01 not started. Delete this line when you begin the ticket.")


def test_a_new_counter_has_seen_nothing():
    counter = limiter.RequestCounter()
    assert counter.count("key_a") == 0


def test_record_returns_the_new_count():
    counter = limiter.RequestCounter()
    assert counter.record("key_a") == 1
    assert counter.record("key_a") == 2
    assert counter.record("key_a") == 3


def test_keys_are_counted_separately():
    counter = limiter.RequestCounter()
    counter.record("key_a")
    counter.record("key_a")
    counter.record("key_b")
    assert counter.count("key_a") == 2
    assert counter.count("key_b") == 1


def test_asking_for_a_count_does_not_change_it():
    counter = limiter.RequestCounter()
    counter.record("key_a")
    counter.count("key_a")
    counter.count("key_a")
    assert counter.count("key_a") == 1


def test_reset_forgets_everything():
    counter = limiter.RequestCounter()
    counter.record("key_a")
    counter.record("key_b")
    counter.reset()
    assert counter.count("key_a") == 0
    assert counter.count("key_b") == 0


def test_two_counters_do_not_share_state():
    first = limiter.RequestCounter()
    second = limiter.RequestCounter()
    first.record("key_a")
    assert second.count("key_a") == 0
