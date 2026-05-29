# 0001. Keep Harness Adoption Prompt-First

## Status

Accepted

## Date

2026-05-29

## Context

This starter kit helps coding agents add durable instructions, constraints,
feedback loops, knowledge storage, and drift checks to target repositories.

The target repository is always the source of truth. Target repositories vary by
language, framework, package manager, CI provider, local runtime dependencies,
existing docs, and team conventions. A generic installer cannot reliably infer
which rules should become real project constraints, which snippets should remain
reference material, or which existing files should be patched instead of left
alone.

The kit still needs a low-friction path for users who want a starter skeleton,
but that path must not replace repository inspection or project-specific agent
judgment.

## Decision

Keep prompt-first adoption as the primary workflow.

The expected adoption flow is:

1. The user opens the target repository with an agent.
2. The user gives the agent the kit Git URL.
3. The agent clones the kit into `./harness-starter-kit`, reads the docs,
   commands, templates, and scripts, then adapts the harness pattern to the
   target repository.

Keep `scripts/apply_harness.py` as an optional skeleton bootstrapper only. It may
copy conservative generic files, copy profile snippets into
`docs/harness/profiles/<profile>/`, and skip existing files by default. It must
not become the authoritative adoption mechanism for target repositories.

## Rationale

- Prompt-first adoption forces the agent to inspect the target repository before
  changing it.
- Target-specific harness rules are only useful when they match the target's
  real architecture, commands, generated files, and maintenance expectations.
- Existing project docs, CI, package scripts, and conventions should be reused
  rather than shadowed by starter-kit defaults.
- Conservative skeleton files are still useful when a repository has no durable
  harness yet, as long as they remain a starting point for adaptation.
- Keeping the installer narrow lowers the risk of overwriting target files,
  introducing the wrong tooling, or making generic checks look more authoritative
  than local project knowledge.

## Alternatives Considered

- Installer-first adoption: rejected because it would push the kit toward
  guessing target architecture, package manager behavior, CI wiring, and
  project-specific boundaries. That would make adoption faster in the simplest
  cases but more dangerous and less trustworthy in real repositories.
- Profile-first adoption: rejected because stack profiles are useful reference
  material, not complete policy. A Django, FastAPI, React, or Android project
  can still have very different local commands, generated files, deployment
  paths, and review expectations.
- Documentation-only adoption: rejected because durable instructions without
  checks, report templates, and drift sensors do not create enough feedback for
  future agent sessions.

## Consequences

- Adoption remains slower than a one-command installer, but it is safer and more
  faithful to the target repository.
- The optional installer must stay conservative, non-destructive by default, and
  clearly documented as a bootstrap tool rather than a full adoption engine.
- Profile snippets should continue to land as reviewable reference material
  instead of replacing existing target configuration.
- Command workflows such as `/harness doctor`, `/harness update`, and
  `/harness refresh` must preserve the rule that the target repository is the
  source of truth.
- Future work should improve prompts, templates, diagnostics, examples, and
  safe patch guidance before adding broad automatic mutation behavior.

## Agent Guidance

When applying this kit to a target repository, inspect the target first and adapt
the smallest useful harness pieces. Do not treat profile snippets or installer
output as mandatory target changes.

When changing this starter kit, preserve the prompt-first model unless a new
decision record explicitly supersedes this one. If a proposed change makes
`scripts/apply_harness.py` more automatic or more willing to modify existing
target files, evaluate it against this decision and document the tradeoff before
implementation.
