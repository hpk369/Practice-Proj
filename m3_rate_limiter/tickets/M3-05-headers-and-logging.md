# M3-05 · Tell the customer and tell the log

| Session | Size | Code | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Mon Nov 23 | S | `rate_limit_headers`, `check` | `tests/test_m3_05_headers_and_logging.py` (5) | 50 m / __ |

## Context
When a customer writes "your API is returning 429", the first thing you ask for is the
response headers, because they say what the limit is and when to retry. Someone has to
produce those headers. The server-side log should also show who was limited.

## Requirements
**`rate_limit_headers(decision)`** returns a dict of header name to string value:
- always `X-RateLimit-Limit`, `X-RateLimit-Remaining` and `X-RateLimit-Reset` (the
  seconds until reset)
- `Retry-After`, with the same number of seconds, **only** when the request was denied

**Logging.** Change `check` so that each denied request logs one warning that includes the
key. Allowed requests log nothing.

## Acceptance criteria
`tests/test_m3_05_headers_and_logging.py` passes, and the M3-03 tests still pass.

## Learn first (5 min)
- **Header values are text.** Convert numbers with `str(...)`.
- **Adding a key conditionally.** Build the dict, then `if not decision.allowed:` add one more.
- **Logging** works as it did in M2-08: a module-level
  `logger = logging.getLogger("m3_rate_limiter")` and `logger.warning(...)`.

## Explain-back (answer in the PR)
1. A customer's script retries immediately on every 429 in a tight loop. Which header should it have read, and what should it have done?
2. In M2 you masked the key before logging it. This ticket logs the key as given. In a real service, what would you log instead?
