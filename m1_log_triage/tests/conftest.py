"""Shared test data for M1. pytest finds fixtures in this file automatically."""

import pytest


@pytest.fixture
def records():
    """Six hand-written records, small enough to check by eye."""
    return [
        {"ts": "2026-11-10T09:00:00.000+00:00", "request_id": "req_1", "tenant_id": "fernhollow",
         "method": "GET", "path": "/v1/scans", "status": 200, "duration_ms": 12.5, "error_code": None},
        {"ts": "2026-11-10T09:01:00.000+00:00", "request_id": "req_2", "tenant_id": "fernhollow",
         "method": "POST", "path": "/v1/scans", "status": 201, "duration_ms": 40.0, "error_code": None},
        {"ts": "2026-11-10T09:02:30.000+00:00", "request_id": "req_3", "tenant_id": None,
         "method": "GET", "path": "/v1/scans", "status": 401, "duration_ms": 3.2,
         "error_code": "invalid_api_key"},
        {"ts": "2026-11-10T09:03:00.000+00:00", "request_id": "req_4", "tenant_id": "cedarline",
         "method": "GET", "path": "/v1/alerts", "status": 500, "duration_ms": 1900.0,
         "error_code": "internal_error"},
        {"ts": "2026-11-10T09:04:00.000+00:00", "request_id": "req_5", "tenant_id": "cedarline",
         "method": "GET", "path": "/v1/alerts", "status": 200, "duration_ms": 950.75, "error_code": None},
        {"ts": "2026-11-10T08:59:00.000+00:00", "request_id": "req_6", "tenant_id": None,
         "method": "GET", "path": "/v1/scans", "status": 401, "duration_ms": 2.9,
         "error_code": "invalid_api_key"},
    ]
