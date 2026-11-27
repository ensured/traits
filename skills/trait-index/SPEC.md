# Trait file specification

<!-- traits-format: 1 -->

A trait describes a recurring code pattern so a reader can predict how unseen code
is written. The pattern holds wherever it applies, subject to documented exceptions.

## Location and naming

- One trait per file, in a `traits/` directory at the root of the repository. The
  directory stays flat.
- The file name is a short, stable, lowercase kebab-case slug and is the trait's
  identifier. It does not change when the wording does.
- `traits/README.md` is the index of every trait's `description` and `when`. It is
  generated from the files and never edited by hand.
- `traits/SPEC.md` is a copy of this document, so the format travels with the project.

The `traits-format` marker identifies the format described by the spec. An unmarked
project copy uses format 1. Keep the marker with the spec when copying it into a
project.

## Frontmatter

| Field | Required | Meaning |
|---|---|---|
| `description` | Yes | One sentence stating what the code does. Positive, present tense and specific enough to check. |
| `when` | Yes | The situation in which the trait is relevant, described as an activity, independent of code layout. |
| `paths` | No | Globs for where the pattern lives. A hint for finding the pattern, not a limit on where violations are looked for. |
| `check.test` | No | A test that fails when the trait is broken. Its failure message names the trait file. |
| `check.covers` | With `check.test` | The part of the trait the test verifies, in one sentence. |

Start the file with frontmatter between two `---` lines. Put `description` and
`when` on separate lines with double-quoted values.

## Body

Every section is optional, and they appear in this order:

1. **Opening paragraph**: what the description leaves out, in a few sentences.
2. **Why**: the reason the trait exists, confirmed by a person. It is the grounds for
   applying, bending or retiring the trait. Leave it out sooner than guess.
3. **Pattern**: a minimal snippet showing the shape to follow, trimmed from real code
   and containing nothing unrelated to the trait.
4. **Exceptions**: the conditions under which code may depart from the trait, and where
   such departures are recorded.

## Example

`traits/feature-flags.md`:

````markdown
---
description: "Feature flags are read through flags.is_enabled"
when: "Making behaviour depend on a feature flag"
check:
  test: tests/architecture/test_flags.py::test_flags_are_read_through_is_enabled
  covers: "That no module outside flags/ reads the flag store"
---

Code that branches on a flag calls `flags.is_enabled(name, account)` for the current
account.

## Why

`is_enabled` records each evaluation so maintainers can measure usage when deciding
whether to retire a flag.

## Pattern

```python
if flags.is_enabled("bulk-export", account):
    return export_in_bulk(account)
```

## Exceptions

Start-up code that runs before the flag store is reachable reads `flags.DEFAULTS`.
````

## Rules

- **One prediction.** If two parts of a trait can be violated independently, they are
  two traits.
- **Shape only.** One-off decisions, environment facts and domain knowledge are not
  traits.
- **State what the code does**, not what is forbidden.
- **Ratified by merge.** A trait takes effect when a person merges its file, together
  with the changes that bring existing code into line. An agent proposes; it does not
  ratify.
- **Enforced by review.** Every trait is checked against each change by a reviewer,
  human or model, working from the file alone. `check` adds to that and does not
  replace it.
- **Retired by deletion.** When the why no longer holds, the file is removed.

## Lifecycle

Generate code, review and refine it, turn what the review established into traits,
ratify them, repeat.
