# M2-08 · Command line, logging and redaction

| Session | Size | Function | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Sat Nov 21 | M | `mask_key`, `main` | `tests/test_m2_08_cli.py` (8) | 75 m / __ |

## Context
Two audiences read what this tool produces. The person running it reads the printed
result. The person investigating later reads the log. And an API key must never appear
whole in a log, because logs get copied into tickets, chats and screenshots.

## Requirements
**`mask_key(key)`** returns the first 10 characters, then `...`, then the last 4:
`acme_live_...0f01`. A key of 14 characters or fewer returns just `...`, so a short value
is never shown whole.

**`main(argv=None)`** takes one argument, the header value.
- Load `data/tenants.json` (find it relative to `checker.py`, not the current folder),
  build the index, and authenticate.
- Success: print `OK tenant=<tenant_id>` and return `0`.
- `AuthError`: print `DENIED <code>: <message>`, log **one warning** that includes the code
  and the masked key, and return `1`.
- The full key must not appear in any log line at any level.

## Acceptance criteria
`tests/test_m2_08_cli.py` passes, and these work:
```bash
python -m m2_api_key_checker.checker "Bearer acme_live_00000000000000000000000000000f01"
python -m m2_api_key_checker.checker "Bearer acme_test_00000000000000000000000000000f02"
echo $?
```

## Learn first (10 min)
- **Slicing strings.** `text[:10]` is the first ten characters, `text[-4:]` the last four.
- **Catching your own exception.**
  ```python
  try:
      context = authenticate(header, index)
  except AuthError as err:
      ...  # err.code and err.message are available here
  ```
- **`logging`.** `import logging`, then once at module level
  `logger = logging.getLogger("m2_api_key_checker")`. Use `logger.warning("auth denied code=%s key=%s", code, masked)`.
  Levels, lowest to highest: DEBUG, INFO, WARNING, ERROR.
- **`print` or `logger`?** `print` is the program's output for the person running it.
  Logging is the record for whoever investigates afterwards, with a level and a name.
- **A path next to this file.** `Path(__file__).parent / "data" / "tenants.json"`.
- **`caplog`** is a pytest fixture that captures log records so a test can read them.

## Explain-back (answer in the PR)
1. Why keep the last four characters at all? What does support do with them?
2. Why is a denied key a WARNING and not an ERROR?
