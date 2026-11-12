"""Reading exercise for M3-04. `reading/retry.py` is correct. THREE OF THESE TESTS ARE WRONG.

Before you run anything, read retry.py and each test, and write down which three you
expect to fail and why. Then run them. Then fix the three tests (not the code).
"""

import pytest

from m3_rate_limiter.reading import retry

pytestmark = pytest.mark.skip(reason="M3-04 not started. Delete this line when you begin the ticket.")


class Flaky:
    """A fake service call that fails a set number of times, then succeeds."""

    def __init__(self, failures, error=ConnectionError):
        self.failures = failures
        self.error = error
        self.calls = 0

    def __call__(self):
        self.calls += 1
        if self.calls <= self.failures:
            raise self.error("temporary failure")
        return "ok"


def test_delays_double_each_time():
    assert retry.backoff_delays(4) == [1.0, 2.0, 4.0]


def test_three_attempts_means_three_waits():
    assert len(retry.backoff_delays(3)) == 3


def test_delays_are_capped():
    assert retry.backoff_delays(8, base=1.0, cap=30.0)[-1] == 30.0


def test_one_attempt_means_no_waiting():
    assert retry.backoff_delays(1) == []


def test_succeeds_first_time_without_sleeping():
    slept = []
    assert retry.call_with_retry(Flaky(failures=0), sleep=slept.append) == "ok"
    assert slept == []


def test_recovers_after_two_failures():
    slept = []
    service = Flaky(failures=2)
    assert retry.call_with_retry(service, attempts=3, sleep=slept.append) == "ok"
    assert service.calls == 3
    assert slept == [1.0, 2.0, 4.0]


def test_gives_up_after_all_attempts_fail():
    service = Flaky(failures=10)
    with pytest.raises(ConnectionError):
        retry.call_with_retry(service, attempts=3, sleep=lambda seconds: None)
    assert service.calls == 3


def test_other_errors_are_retried_too():
    service = Flaky(failures=1, error=ValueError)
    assert retry.call_with_retry(service, sleep=lambda seconds: None) == "ok"
