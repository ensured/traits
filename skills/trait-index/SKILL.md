---
name: trait-index
description: Regenerate traits/README.md, the index of every trait's description and when, and set up the traits/ directory on first use. Use after adding, rewording, renaming or deleting a trait file, when the index looks out of date, or when a project has no traits/ directory yet.
argument-hint: "[--check-spec]"
allowed-tools:
  - Bash(${CLAUDE_SKILL_DIR}/generate.sh)
  - Bash(${CLAUDE_SKILL_DIR}/generate.sh --check-spec)
---

# Regenerate the trait index

Run the bundled script from inside the target project with Bash and Awk.
In OpenCode, use the base directory reported by the `skill` tool and run
`bash` with the absolute path to `generate.sh` and the arguments shown below.

If the user requests `--check-spec`, run the compatibility check, report its
result, and stop.

```bash
"${CLAUDE_SKILL_DIR}/generate.sh" --check-spec
```

`traits/README.md` is built from the frontmatter of the trait files. It is never edited
by hand, because a hand-edited index drifts from the files it lists.

To refresh the index, run the script without arguments.

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
