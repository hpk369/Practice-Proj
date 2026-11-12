"""API key checker for Acme Shield. Mini project M2 (yours).

Customers call the API with `Authorization: Bearer <key>`. Keys look like
`acme_live_<32 hex characters>` or `acme_test_<32 hex characters>`. This service is the
*live* environment, so a test key is recognised but refused, with its own error code:

| Situation                                  | Result                                  |
| ------------------------------------------ | --------------------------------------- |
| No header                                  | AuthError("invalid_api_key", ...)       |
| Scheme isn't Bearer (`Token x`, bare key)  | AuthError("invalid_api_key", ...)       |
| Bearer with no key, or an unknown key      | AuthError("invalid_api_key", ...)       |
| Known key, but its env is `test`           | AuthError("key_environment_mismatch", ...) |
| Known live key                             | returns AuthContext                     |

This is the logic of ticket ACME-2 in Project-1, without the web framework around it.
All tenants and keys are fictional placeholders.
"""

from __future__ import annotations

from dataclasses import dataclass

SERVICE_ENV = "live"


def parse_authorization(header):
    """M2-01. Return the key from an Authorization header value, or None if it isn't usable."""
    raise NotImplementedError("M2-01: implement parse_authorization")


def is_well_formed(key):
    """M2-02. Return True if the key has the shape acme_<live|test>_<32 hex characters>."""
    raise NotImplementedError("M2-02: implement is_well_formed")


def key_env(key):
    """M2-02. Return "live" or "test" for a well-formed key, or None for anything else."""
    raise NotImplementedError("M2-02: implement key_env")


@dataclass(frozen=True)
class ApiKey:
    """M2-03. Add the fields: key (str), env (str)."""


@dataclass(frozen=True)
class Tenant:
    """M2-03. Add the fields: tenant_id, name, api_keys, and billing_status (default "active")."""


def load_tenants(path):
    """M2-03. Read the tenants JSON file and return a list of Tenant objects."""
    raise NotImplementedError("M2-03: implement load_tenants")


def build_key_index(tenants):
    """M2-04. Return a dict of {key string: (Tenant, ApiKey)} covering every key of every tenant."""
    raise NotImplementedError("M2-04: implement build_key_index")


class AuthError(Exception):
    """M2-04. An authentication failure. Give it two attributes: code and message."""


@dataclass(frozen=True)
class AuthContext:
    """Who the caller is, once authentication has succeeded. (Written for you. Read it.)"""

    tenant: Tenant
    api_key: str


def authenticate(header, index, service_env=SERVICE_ENV):
    """M2-04. Return an AuthContext for a valid live key, or raise AuthError. See the table above."""
    raise NotImplementedError("M2-04: implement authenticate")


def mask_key(key):
    """M2-08. Return the key with its middle hidden: first 10 characters, "...", last 4."""
    raise NotImplementedError("M2-08: implement mask_key")


def main(argv=None):
    """M2-08. Command-line entry point. Return 0 if the header authenticates, 1 if not."""
    raise NotImplementedError("M2-08: implement main")


if __name__ == "__main__":
    raise SystemExit(main())
