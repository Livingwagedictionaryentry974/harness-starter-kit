# Prompt: Apply harness-starter-kit To A Target Repository

Use this prompt after cloning or downloading `harness-starter-kit` inside the
target repository. Open the target repository root with your coding agent, not
the `harness-starter-kit` subdirectory.

```text
Read ./harness-starter-kit first, then apply the harness engineering starter kit
to this repository.

Treat the current working directory as the target repository. Treat
./harness-starter-kit as read-only reference material unless I explicitly ask
you to edit the kit itself.

Goal:
Make this repository easier and safer for coding agents to work in by adding
durable instructions, architecture constraints, feedback loops, knowledge
storage, and drift checks.

Adoption model:
This is prompt-first adoption. Do not treat ./harness-starter-kit as an
installer that knows this repository. Read it as reference material, inspect the
target repository, and adapt the harness pattern to the target's existing
architecture and tools.

Rules:
- Inspect this repository before editing.
- Identify the language, framework, package manager, test command, lint command,
  build command, CI provider, docs structure, and monorepo layout if present.
- Read existing AGENTS.md, CLAUDE.md, README, CONTRIBUTING, and CI configs if
  they exist.
- Preserve existing architecture, tools, naming, package managers, and test
  commands.
- Add the smallest useful harness rather than a large generic framework.
- Prefer updating existing docs/configs over duplicating them.
- Do not overwrite existing files without explaining why.
- Do not delete existing files unless I explicitly ask.
- Do not edit files under ./harness-starter-kit during adoption unless I
  explicitly ask.
- Treat any stack profile files as reference snippets for you to adapt, not as
  automatic changes that must be copied into the project.
- Before finishing, tell me whether ./harness-starter-kit should be removed,
  ignored, or kept intentionally as a submodule/reference before I commit.

Expected work:
- Add or update AGENTS.md with project-specific agent instructions.
- Add docs/decisions, docs/failures, docs/conventions, and docs/domain if no
  equivalent structure exists.
- Add lightweight drift checks under scripts/ when they reflect actual target
  repo rules. Generic doc-link and temporary-file checks are baseline hygiene;
  target-specific checks should enforce real project constraints.
- Add CI or pre-commit integration only when it fits the existing project and
  explain the tradeoff first.
- Add stack-specific lint/type/test recommendations based on the detected
  language.

Drift check examples:
- If AGENTS.md says routes must not access the database directly, add a check
  that fails on forbidden database imports in route files.
- If a decision record says Zustand is the chosen state library, add a check
  that fails when Redux dependencies are added.
- If generated files must live under one directory, add a structure check that
  rejects generated files elsewhere.

Finish by reporting:
- files added or changed
- checks I can run locally
- assumptions you made
- remaining manual steps
- what to do with ./harness-starter-kit before committing

Use ./harness-starter-kit/docs/templates/adoption-report.md as the report shape
if present.
```
