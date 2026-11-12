# Practice-Proj

Python practice built the way a support engineering team builds: small tickets, a branch
per ticket, tests that define "done", CI on every pull request. Everything is set around
**Acme Shield**, a fictional SaaS. All tenants, keys and logs are made up.

The aim by **Nov 27**: read Python, understand it, and debug it.

## The three projects

| Project | Dates | What it is | Tickets |
| --- | --- | --- | --- |
| [M1 Log triage CLI](m1_log_triage/README.md) | Nov 12 to 15 | Summarise an access log for a ticket | 12 |
| [M2 API key checker](m2_api_key_checker/README.md) | Nov 16 to 21 | Decide whether an API key is valid, and say why not | 9 |
| [M3 Rate limiter](m3_rate_limiter/README.md) | Nov 22 to 27 | Limit requests per key per minute | 8 |

M4 (HTTP and real APIs) and M5 (a small web service with SQL) are added after the Nov 27
checkpoint.

## One-time setup

```bash
git clone https://github.com/hpk369/Practice-Proj.git
cd Practice-Proj
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```

You should see every test reported as skipped. That is the starting state.

Each time you open a new terminal, run `source .venv/bin/activate` again.

## How to work a ticket

1. **Read the ticket** in the project's `tickets/` folder, including "Learn first".
2. **Branch:** `git switch -c m1-01-read-lines`
3. **Un-skip the tests:** open the ticket's test file and delete the line that starts with
   `pytestmark =`. Read the tests. They are the specification.
4. **Run them and watch them fail:** `pytest m1_log_triage/tests/test_m1_01_read_lines.py`
5. **Write the code** in the stub. Replace the `raise NotImplementedError` line.
6. **Run until green.** Then run everything: `pytest` and `ruff check .`
7. **Commit and push:**
   ```bash
   git add -A
   git commit -m "M1-01: read log lines"
   git push -u origin m1-01-read-lines
   ```
8. **Open a pull request** on GitHub. Fill in the template, including the explain-back answers.
9. **Wait for CI** to go green, then paste the PR link in chat for review.
10. **Merge**, then `git switch main && git pull` before the next ticket.

## Rules

- Stuck for 15 minutes on one thing: open the hint in the ticket. Still stuck after
  another 10: send what you have and the error message. That is how it works on a team too.
- The solutions are not in this repo. Ask in chat if you need one to move on.
- Don't edit a test to make it pass (except in M3-04, where that is the task).
- Files under `drills/` are broken on purpose, and are left out of linting.
- Five lines in `LEARNING.md` at the end of each day.

## Useful commands

| Command | What it does |
| --- | --- |
| `pytest` | Run every test |
| `pytest path/to/test_file.py` | Run one file |
| `pytest -x` | Stop at the first failure |
| `pytest -k "name"` | Run tests whose name contains the text |
| `pytest -rs` | List skipped tests with the reason |
| `ruff check .` | Lint: unused imports, undefined names and similar |
| `git status` | What has changed |
| `git diff` | Show the changes line by line |
