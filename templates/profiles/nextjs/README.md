# Next.js Harness Profile

Use these snippets when the target project is a Next.js app, especially an App
Router project.

These files are agent reference material, not automatic transformations. Merge
only the pieces that fit the target project's existing tools.

## Recommended Checks

- `next build` for production build validation.
- `tsc --noEmit --incremental false` for a non-emitting TypeScript check.
- `scripts/check_docs_drift.py` for stale documentation references.
- `scripts/check_structure.py` for temporary or drift-prone files.

Expose a single local verification command in `package.json`:

```json
{
  "scripts": {
    "typecheck": "tsc --noEmit --incremental false",
    "check:harness": "npm run typecheck && npm run build && python scripts/check_docs_drift.py && python scripts/check_structure.py"
  }
}
```

Use `npm.cmd` instead of `npm` when running commands from Windows PowerShell if
script execution policy blocks `npm.ps1`.

## Next.js Notes

- Do not rely on `next lint` for current Next.js projects unless the target
  project already has a working lint command. Newer Next versions may not expose
  `next lint` as a valid command.
- `next build` may update `tsconfig.json` and `next-env.d.ts` during initial
  project setup. Review those changes instead of reverting them blindly.
- Ignore generated files and local reference clones: `.next/`, `node_modules/`,
  `tsconfig.tsbuildinfo`, and `harness-starter-kit/`.
- Do not commit the local `harness-starter-kit/` clone unless the target
  intentionally keeps it as a submodule or reference.
- Add a dedicated test runner only when build and typecheck no longer cover the
  user-facing behavior being changed.
