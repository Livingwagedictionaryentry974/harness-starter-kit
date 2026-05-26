# TypeScript Harness Profile

Use these snippets when the target project is JavaScript or TypeScript.

These files are agent reference material, not automatic transformations. Merge
only the pieces that fit the target project's existing tools.

## Recommended Checks

- ESLint for linting
- TypeScript compiler for type checking
- dependency boundary rules for architecture constraints
- unused export checks such as `ts-prune` or `knip`
- package scripts that expose one local verification command

## Integration Notes

Do not replace existing ESLint or package manager configuration blindly. Merge
the relevant rules into the target project.
