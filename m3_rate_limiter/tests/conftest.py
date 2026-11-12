"""Shared fixtures for M3."""

import pytest


class FakeClock:
    """A clock the test controls. Call it to read the time; use advance() to move it."""

    def __init__(self, now=120.0):
        self.now = now

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


@pytest.fixture
def clock():
    return FakeClock(now=120.0)
