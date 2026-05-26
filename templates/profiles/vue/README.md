# Vue Harness Profile

Use these snippets when the target project is a Vue 3 app such as Vite + Vue,
Nuxt, or a similar client-side project.

These files are agent reference material, not automatic transformations. Merge
only the pieces that fit the target project's existing tools.

## Recommended Checks

- `npm run lint` for ESLint including eslint-plugin-vue rules.
- `npm run typecheck` for TypeScript type checks via vue-tsc.
- `npm test` for unit and component tests.
- `npm run build` to confirm the production bundle compiles.
- `python scripts/check_docs_drift.py` for stale documentation references.
- `python scripts/check_structure.py` for temporary or drift-prone files.

## Suggested package.json Scripts

Merge the scripts from `package-scripts.harness.json` into the target
project's `package.json`.

## ESLint Config

Merge rules from `eslint.config.harness.mjs` into the target project's ESLint
config. The snippet enables `eslint-plugin-vue` with Vue 3 recommended rules.

## Vue Notes

- Prefer script setup syntax with the Composition API for new components.
- Name single-file components in PascalCase, and use PascalCase in templates.
- Keep component files in the target project's established component directory.
- Manage shared state with Pinia stores in Vue 3 projects unless the project
  already uses another state approach.
- Use `defineProps` and `defineEmits` with TypeScript generics for typed
  component contracts.
- Do not access `$parent` or mutate props directly; communicate via emits or
  shared stores.
- Do not edit or commit `dist/`, `node_modules/`, Vite cache directories, or
  the local `harness-starter-kit/` clone.
