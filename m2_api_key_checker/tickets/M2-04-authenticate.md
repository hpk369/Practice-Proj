# M2-04 · Authenticate

| Session | Size | Code | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Thu Nov 19 | M | `build_key_index`, `AuthError`, `authenticate` | `tests/test_m2_04_authenticate.py` (14) | 60 m / __ |

## Context
This is the ticket that felt too hard in Project-1, without FastAPI around it. A test key
on the live API and an unknown key are both refused, but they get different error codes,
because the customer fixes them in different ways.

## Requirements
1. **`build_key_index(tenants)`** returns a dict from key string to a `(Tenant, ApiKey)` pair,
   for every key of every tenant.
2. **`AuthError`** is an exception with two attributes, `code` and `message`.
   `str(error)` gives the message.
3. **`authenticate(header, index, service_env=SERVICE_ENV)`** follows the table in the module
   docstring:
   - no usable key in the header, or a key that isn't in the index: raise
     `AuthError("invalid_api_key", <message>)`
   - a known key whose `env` differs from `service_env`: raise
     `AuthError("key_environment_mismatch", <message>)`. The message must say which
     environment the key is for.
   - otherwise return `AuthContext(tenant=..., api_key=...)`

Write messages a customer could act on without opening a ticket.

## Acceptance criteria
`tests/test_m2_04_authenticate.py` passes.

## Learn first (10 min)
- **Why an index.** Searching every tenant's key list on each request is slow and fiddly.
  Build a dict once, then `index.get(key)` answers in one step and returns `None` for a
  key it doesn't know.
- **Your own exception.**
  ```python
  class QuotaError(Exception):
      def __init__(self, limit, message):
          super().__init__(message)
          self.limit = limit
          self.message = message
  ```
  `__init__` runs when the object is created. `self` is the object being built.
  `super().__init__(message)` lets the built-in `Exception` do its normal setup.
- **`raise`** stops the function and hands the error to the caller:
  `raise QuotaError(100, "Over the limit.")`.
- **Testing for an error.** `with pytest.raises(checker.AuthError) as excinfo:` passes only
  if the block raises that error. `excinfo.value` is the error object.
- **Fixtures.** The `index` function at the top of the test file is marked
  `@pytest.fixture`. Any test with a parameter named `index` receives its return value.

<details><summary>Hint (direction)</summary>

Handle the cases in the same order as the table and leave each one early. Call
`parse_authorization` first: you already wrote and tested the header rules.
`tenant, record = found` unpacks the pair from the index.
</details>

## Explain-back (answer in the PR)
1. Why is a test key on the live API a different `code` from an unknown key? How does that change what support says to the customer?
2. A suspended tenant still authenticates here. Why is "who are you?" kept separate from "are you allowed?"
