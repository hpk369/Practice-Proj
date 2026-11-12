# M2-07 · Your own tests: fixtures and parametrize

| Session | Size | File | Estimate / Actual |
| --- | --- | --- | --- |
| Sat Nov 21 | S | `tests/test_m2_07_my_tests.py` | 60 m / __ |

## Context
A support engineer who can write a failing test for a customer's bug report hands
engineering something they can act on the same day.

## Requirements
Add a function `tenant_for_key(key, index)` to `checker.py`. It returns the `tenant_id` that
owns a key, or `None` if the key is unknown. Write the tests first.

In `tests/test_m2_07_my_tests.py`:
1. Write a **fixture** called `index` that builds the key index from `data/tenants.json`.
2. Write one **parametrized** test covering all four keys in the file, with the expected tenant for each.
3. Write a test for an unknown key.
4. Write a test that uses `pytest.raises`: calling `tenant_for_key(None, index)` should raise
   `TypeError` with a message you choose. Make the function do that.
5. Run the tests and watch them fail. Then write the function.

## Learn first (5 min)
- Reread the top of `tests/test_m2_04_authenticate.py` for the fixture pattern.
- Two values per case: `@pytest.mark.parametrize("key, expected", [(K1, "a"), (K2, "b")])`.
- **Red, green.** A test you have never seen fail might be testing nothing.

## Explain-back (answer in the PR)
1. Paste the failing output from step 5. What did the failure message tell you?
2. Why raise `TypeError` for `None` instead of returning `None`?
