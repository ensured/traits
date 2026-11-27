---
name: trait-check
description: Check a diff against the traits at its comparison base. Use before asking for review, when reviewing a change, or when asked whether code follows the project's traits.
argument-hint: "[pull request number | Git range | diff file [--base <ref>]]"
---

# Check a change against the traits

Report where a change follows or breaks ratified traits and where it introduces
a pattern they do not cover.

## Who runs this

If this session wrote the change and an independent agent is available, give it this
skill, the diff, the base commit ID and the traits from that commit. Otherwise,
review the change directly.

## 1. Pin the comparison

Resolve refs to commit IDs before reading the diff or traits. Use the same base
commit for both.

- For a pull request number in `$ARGUMENTS`, get the target and head commit IDs
  from the repository host. For example, use `gh pr view 123 --json baseRefOid,headRefOid`
  on GitHub. Use the merge base for those commits as the comparison base and
  the pinned head as the endpoint. If the host supplies the diff, verify it is
  for those commits and that comparison base.
- For `A..B`, use `A` as the base and `B` as the endpoint. For `A...B`, use
  the merge base of `A` and `B` as the base and `B` as the endpoint.
- For a saved diff, use `--base <ref>` or trusted metadata that identifies the
  exact comparison commit. Check for inconsistencies between that commit and
  the diff's recorded base or preimage. Ask for the base if it is missing or unclear.
- With no argument, compare the working tree with the merge base of `HEAD` and
  the repository's default branch. Include untracked source files that belong to
  the change. Ask for the comparison base if the default branch is unknown.

With local Git objects, use `git merge-base --all` to find the merge base and
`git diff <base> <head> --` for committed endpoints. For a working-tree review,
use `git diff <base> --` for tracked files. If there are multiple merge bases,
establish which one the comparison uses before judging it. If the exact base
or its tree is unavailable, report the review as unavailable. If the diff is
incomplete, report the scope you could inspect and withhold an overall verdict.

Check whether the working tree matches the code under review before relying on any
local test result. For a remote pull request or a saved diff, verify the match
explicitly.

## 2. Read the ratified traits at the base

List the direct children of `traits/` in the base tree and read each trait's
frontmatter from its committed file. Use regular Markdown files other than
`README.md` and `SPEC.md`. With local Git, list entries with
`git ls-tree --full-tree -r <base> -- traits/` and read files with
`git show <base>:traits/<slug>.md`. Treat a committed index as a navigation aid.
Use the base tree even for a working-tree review.

Read the format marker from the base's `traits/SPEC.md` as a regular file.
The marker `<!-- traits-format: 1 -->`, an unmarked spec, and an absent spec
all use format 1. If the spec is unreadable or declares an unsupported or
invalid format, report the problem and withhold trait verdicts. If the base
contains no trait files, report that and suggest `trait-derive` for adoption.

Use each trait's `when` to decide whether the change does that activity. Using
something already in the code counts. For example, calling an existing client
is still calling an external provider. Read the body of each applicable trait
and any whose scope is unclear.

`paths` says where a pattern usually lives. It is not a filter: code that does a
trait's activity somewhere outside its paths is often the violation.

## 3. Judge each one

Hold the change to what the trait states in its description and opening paragraph, and
to nothing more. Read the Pattern for the shape and the Exceptions for what is allowed.

| Verdict | Meaning |
|---|---|
| Follows | The change does what the trait says |
| Breaks | It does not; cite the file and line and say what the trait expects there |
| Excepted | It departs in a way the trait's Exceptions section allows |
| Unclear | The trait's wording does not settle it; say what is ambiguous |

Prefer Unclear to a guess. A reviewer that flags things the trait does not say stops
being read, and an unclear verdict tells the team which trait needs tightening.

An Exceptions section states a condition. If the change meets the condition, it is
Excepted, even when the section also names existing examples and this is not one of
them. Report the trait as stale (step 4) so the list gets updated.

Use `check.test` as a test identifier for the project's normal test runner. Run
the test only when the checkout matches the change and its code and test runner
are trusted for execution. If the diff changes a linked test, confirm it still
verifies `check.covers` before using a pass as evidence. Judge the rest by reading.
When execution is unavailable or the code is untrusted, say "check not run" and
judge by reading. Report a test that no longer exists as a stale check.

## 4. Report

State the comparison base commit and the head commit or working-tree scope.
Cite line numbers from the changed file. List findings in this order.

1. **Breaks**, each with file, line, the trait's slug and the fix the trait implies.
   When the same lines break two traits, report them together with one fix.
2. **Unclear**, each with the question that would settle it.
3. **Stale traits**: trait text this change makes out of date, such as an exception
   list that no longer names every case, or a `check` that no longer exists.
4. **Proposed trait changes**: additions, edits and deletions in `traits/`, including
   changes to the spec. Omit generated index changes. These proposals have no bearing
   on the current verdict.
5. **Uncovered**: anything in the diff that sets a new shape no trait describes, such
   as a new kind of module or a second way of doing something the code does one way.
   Leave out anything too small to recur. These are candidates for `trait-propose`.
6. **Follows** and **Excepted**, as a list of slugs with a few words each.

Do not list the traits that did not apply.

This is a check against traits, not a full code review. If you notice a defect that no
trait concerns, such as a call to a function that does not exist, mention it in one
line under **Other** and do not investigate further.

Do not change the code unless asked.
