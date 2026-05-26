# Example Adoption Report: Node JavaScript Target

## Target

`sample-task-tracker`, a tiny JavaScript ES module project using Node's built-in
test runner.

## Files Added Or Changed

- Added `AGENTS.md` with project commands, source boundaries, forbidden actions,
  and completion criteria.
- Added `.harness/structure-rules.json`.
- Added `scripts/check_docs_drift.py` and `scripts/check_structure.py`.
- Added `docs/conventions/coding.md`, `docs/domain/glossary.md`,
  `docs/decisions/001-adopt-agent-harness.md`, and failure/decision templates.
- Added TypeScript profile snippets under `docs/harness/profiles/typescript/`.
- Added `check:harness` to `package.json`.
- Added `.gitignore` entries for generated files and the local
  `harness-starter-kit/` clone.

## Checks Run

```powershell
npm.cmd run check:harness
```

The command ran syntax checks, `node --test`, document drift checks, and
structure drift checks successfully.

## Assumptions

- Windows PowerShell users should run `npm.cmd` if `npm.ps1` is blocked by
  execution policy.
- The local `harness-starter-kit/` clone is adoption reference material, not
  target project source.

## Remaining Manual Steps

- Remove, ignore, or intentionally keep `harness-starter-kit/` before committing
  adoption changes.
- Add CI only after choosing the target repository's CI provider.
