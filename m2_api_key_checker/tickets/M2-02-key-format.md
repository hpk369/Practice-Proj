# M2-02 · Check the shape of a key

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Tue Nov 17 | S | `is_well_formed`, `key_env` | `tests/test_m2_02_key_format.py` (14) | 50 m / __ |

## Context
Customers paste keys with a missing character, a trailing newline, or a key from another
product. You can tell a key is malformed, and which environment it is for, without
looking it up anywhere.

## Requirements
A well-formed key is exactly `acme_`, then `live` or `test`, then `_`, then 32 lowercase
hex characters (`0-9`, `a-f`). Nothing before, nothing after.
- `is_well_formed(key)` returns `True` or `False`.
- `key_env(key)` returns `"live"` or `"test"` for a well-formed key, and `None` otherwise.

## Acceptance criteria
`tests/test_m2_02_key_format.py` passes.

## Learn first (15 min)
- **Regular expressions** describe the shape of text. `import re`.
- The pieces you need:
  - literal text matches itself: `acme_`
  - `(live|test)` matches either word, and the brackets make it a *group* you can read back
  - `[0-9a-f]` matches one character from that set
  - `{32}` means "exactly 32 of the previous thing"
- **`re.fullmatch(pattern, text)`** succeeds only if the whole text fits. It returns a match
  object, or `None`. (`re.search` finds the pattern anywhere inside, and `re.match` only
  anchors the start. Both let junk through. Several tests are there to catch that.)
- **Reading a group.** `match.group(1)` is whatever the first bracketed group matched.
- **Compile once.** `KEY_PATTERN = re.compile(r"...")` at module level, then
  `KEY_PATTERN.fullmatch(key)`. The `r` prefix keeps backslashes literal.

## Try it by hand
Build the pattern step by step in a Python prompt. Start with `r"acme_"` against `"acme_"`,
then add one piece at a time and test again after each.

## Explain-back (answer in the PR)
1. Which test fails if you use `re.match` instead of `re.fullmatch`? Why?
2. A customer's key fails `is_well_formed`. Write the one-sentence reply you'd send them.
