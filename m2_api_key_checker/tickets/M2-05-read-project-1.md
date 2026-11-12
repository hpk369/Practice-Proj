# M2-05 · Reading: two files from Project-1

| Session | Size | Files | Output | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Fri Nov 20 | S | `acme_shield/tenants.py`, `acme_shield/errors.py` in Project-1 | answers in `LEARNING.md` | 60 m / __ |

## Context
You have now written a small version of both files. Go back to the originals and read
them. No code today. The skill is reading someone else's Python and saying what it does.

## Method
Read each file top to bottom, once, without running anything. For every line you can't
explain, write the line number down. Then answer the questions. Then look up only what
you still need.

## Questions on `tenants.py`
1. `KeyEnv = Literal["live", "test"]`. What is this line for? What would it stop someone doing?
2. `class ApiKey(BaseModel)` has the same two fields as your dataclass. What does
   `Tenant.model_validate(t)` do that you did by hand in `load_tenants`?
3. In `TenantStore.__init__`, find the line that does the job of your `build_key_index`.
   Rewrite it as an ordinary nested `for` loop.
4. What does the leading underscore in `self._by_key` tell another developer?
5. `@classmethod def from_yaml(cls, ...)`: how is it called, and what does it return?
6. `lookup_key` has the return type `tuple[Tenant, ApiKey] | None`. Say that in plain words.

## Questions on `errors.py`
7. `ApiError` and your `AuthError` are nearly the same class. Which attributes does `ApiError` add, and what are they for?
8. `self.headers = headers or {}`. What is `self.headers` when the caller passes nothing? Why not write `headers={}` as the default? (You'll meet that bug tomorrow.)
9. What does `error_body` return? Write out the dict for code `invalid_api_key`, message `No such key.`, request id `req_abc`.
10. `api_error_handler` starts with `async def`. You don't need to understand `async` yet. Ignoring that word, describe the three things the function does.

## Acceptance criteria
Ten answers in `LEARNING.md`, in your own words, plus the list of line numbers you couldn't
explain. Bring that list to chat.

## Explain-back (live in chat)
Explain `TenantStore` from top to bottom as if to a new teammate.
