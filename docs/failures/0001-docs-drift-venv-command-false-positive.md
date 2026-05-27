# 0001. Docs Drift Treated Venv Python Commands As Missing Paths

## Date Tried

2026-05-27

## Goal

Document local verification commands for target repositories without making
cross-platform docs drift checks fail.

## What Was Tried

Target repositories documented virtual-environment commands as inline code, for
example:

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe scripts\check_harness.py
.venv/bin/python manage.py test
```

The docs drift checker treated inline code containing slashes or backslashes as
possible local file references.

## Why It Failed

Windows and POSIX virtual-environment Python paths are machine-local command
entrypoints. They may not exist in CI, on another operating system, or in a
fresh target repository checkout.

Treating these command strings as required documentation paths created a false
positive: useful verification commands could be reported as missing files.

## Current Replacement

`scripts/check_docs_drift.py` now recognizes virtual-environment Python
commands and local environment prefixes such as `.venv/`, `venv/`, and `env/`
without requiring those paths to exist.

Regression coverage lives in `tests/test_check_docs_drift.py` and includes both
Windows-style and POSIX-style venv Python command examples.

## Agent Guidance

Do not remove useful verification commands from docs to silence docs drift.
When an inline command is misclassified as a path, fix the classifier and add a
cross-platform regression test.
