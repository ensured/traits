---
name: trait-index
description: Regenerate traits/README.md, the index of every trait's description and when, and set up the traits/ directory on first use. Use after adding, rewording, renaming or deleting a trait file, when the index looks out of date, or when a project has no traits/ directory yet.
argument-hint: "[--check-spec]"
allowed-tools:
  - Bash(${CLAUDE_SKILL_DIR}/generate.sh)
  - Bash(${CLAUDE_SKILL_DIR}/generate.sh --check-spec)
---

# Regenerate the trait index

If `$ARGUMENTS` is `--check-spec`, run the compatibility check from inside the
target project, report its result, and stop.

```bash
"${CLAUDE_SKILL_DIR}/generate.sh" --check-spec
```

`traits/README.md` is built from the frontmatter of the trait files. It is never edited
by hand, because a hand-edited index drifts from the files it lists.

From inside the target project, run the bundled script. It requires Bash and Awk.

```bash
"${CLAUDE_SKILL_DIR}/generate.sh"
```

The script writes `traits/README.md` at the Git repository root, or in the current
directory when run outside Git. It creates `traits/` and installs `traits/SPEC.md`
when those paths are missing. Keep `traits/` and the generated files within the
project as a directory and regular files.

The project spec must match the bundled format. Unmarked copies use format 1.
For a mismatch, use a matching Traits release or migrate the project traits and
spec together.

If a trait lacks fenced frontmatter, `description`, or `when`, the script names
the file and exits before replacing the index. Fix the trait file and rerun the
script.

Report the number of indexed traits and summarize any changed rows.

If the project's agent instructions do not already mention traits, suggest adding
the following guidance.

> Before writing code, read `traits/README.md` and open every trait whose `when`
> matches the work.
>
> When the user corrects the shape of code you wrote, finish the work, then find out
> whether it is a general rule and why, and propose it as a trait.
