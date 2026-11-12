# M2-03 · Tenants and keys as data classes

| Session | Size | Code | Tests | Estimate / Actual |
| --- | --- | --- | --- | --- |
| Wed Nov 18 | S | `ApiKey`, `Tenant`, `load_tenants` | `tests/test_m2_03_tenants.py` (7) | 50 m / __ |

## Context
In M1 every record was a dict, and a typo like `record["tenant"]` only failed when that
line ran. For data with a known shape, a class with named fields catches the typo earlier
and tells the reader what a tenant is.

## Requirements
- Give `ApiKey` two fields: `key` and `env`, both `str`.
- Give `Tenant` four fields: `tenant_id`, `name`, `api_keys` (a list of `ApiKey`), and
  `billing_status` with a default of `"active"`.
- Implement `load_tenants(path)`: read `data/tenants.json` and return a list of `Tenant`
  objects, each holding `ApiKey` objects. A tenant with no `billing_status` in the file
  gets the default.

## Acceptance criteria
`tests/test_m2_03_tenants.py` passes.

## Learn first (10 min)
- **A dataclass** is a class that mostly holds data. You list the fields with their types
  and Python writes the rest:
  ```python
  @dataclass(frozen=True)
  class Point:
      x: int
      y: int
      label: str = "origin"
  ```
  `Point(x=1, y=2)` creates one. `p.x` reads a field. Two points with the same values are equal.
- **`frozen=True`** means a field can't be reassigned after creation. Data that can't change
  can't be changed by accident.
- **Defaults go last.** A field with a default can't come before a field without one.
- **Type hints** (`x: int`) document what is expected. Python doesn't enforce them at run
  time; tools and readers use them.
- **Reading a whole JSON file.** `json.loads(Path(path).read_text())`.
- **Nested loops.** For each tenant in the file, build its list of `ApiKey` objects first,
  then build the `Tenant`.

<details><summary>Hint (direction)</summary>

`raw["tenants"]` is a list of dicts. For the optional field use
`t.get("billing_status", "active")`.
</details>

## Explain-back (answer in the PR)
1. What does `tenant.nmae` do on a dataclass, compared with `record["nmae"]` on a dict? When does each fail?
2. Open `acme_shield/tenants.py` in Project-1. It uses pydantic's `BaseModel` instead of a dataclass. Name one thing that looks the same and one that looks different.
