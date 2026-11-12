# M2-01 · Read the Authorization header

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Mon Nov 16 | S | `parse_authorization` | `tests/test_m2_01_parse_authorization.py` (12) | 45 m / __ |

## Context
Support sees a steady stream of "401 but my key is right" tickets. Often the key is right
and the header is wrong: `Token <key>`, a bare key, or `Bearer` followed by nothing.
The first job is to pull the key out of the header, or decide there isn't one.

## Requirements
Implement `parse_authorization(header)` in `checker.py`.
- The header must be `<scheme> <key>`, where the scheme is `Bearer` in any letter case.
- Return the key, with surrounding spaces removed.
- Return `None` for a missing header (`None`), an empty one, a different scheme, a bare key,
  or `Bearer` with no key after it.

## Acceptance criteria
`pytest m2_api_key_checker/tests/test_m2_01_parse_authorization.py` passes.

## Learn first (10 min)
- **`str.partition(" ")`** splits a string at the first space and always returns three
  parts: before, the separator, after. Try these in a Python prompt and note each result:
  `"Bearer abc".partition(" ")`, `"Bearer".partition(" ")`, `"Bearer ".partition(" ")`.
- **Unpacking.** `scheme, _, key = header.partition(" ")`. The `_` is a name for "a value I
  don't need".
- **Case-insensitive comparison.** Compare `scheme.lower()` with `"bearer"`.
- **Early returns.** Deal with each bad case at the top and `return None` straight away.
  What is left at the bottom is the good case.
- **`None` first.** `None.partition(...)` raises `AttributeError`, so check for `None`
  before touching the string.
- **Parametrized tests.** `@pytest.mark.parametrize("scheme", [...])` runs one test function
  once per value. That is why this file reports 12 tests from 8 functions.

<details><summary>Hint (direction)</summary>

Three checks, in order: is the header None, is the scheme something other than bearer, is
the key empty after stripping. Then return the key.
</details>

## Explain-back (answer in the PR)
1. Why `partition(" ")` and not `split(" ")`? What does `"Bearer".split(" ")` give you, and what would unpacking it into two names do?
2. A customer sends `Authorization: bearer <key>` in lowercase. Should that work? Why did the ticket decide yes?
