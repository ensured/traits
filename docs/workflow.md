# Write and review traits

## Onboard a contributor

Use `trait-architect` when someone wants to learn the codebase or has
opinions about its conventions but hasn't put them into words yet. Start
with their next change or something they often explain in review.

For a CLI change, the architect might open a command that takes an output
stream and ask whether a reviewer would accept a direct call to `print()`.
The answer might be that tests supply their own stream, or that either form
is fine. The architect follows up on the person's answer and uses
`trait-propose` to draft a supported convention. A preference that the
project has yet to try stays in the conversation with a suggested first use.

## Write a trait

1. Pick a recurring pattern and check where it applies in the code.
2. Add a file such as `traits/feature-flags.md` with a `description` of the
   pattern and a `when` field for the activity that calls for it.
3. Explain why the pattern exists and show a short snippet from the project.
   Bring existing code into line and document any allowed exceptions.
4. Regenerate `traits/README.md`. A maintainer ratifies the trait by merging it
   with the corresponding code changes.

Ask contributors and coding agents to read the index before changing code and
open each trait whose `when` field applies. Update or retire a trait when its
rationale changes. See the [file format](../skills/trait-index/SPEC.md) and
[worked examples](../examples/README.md).

## Review a change

Use `trait-check` with `main...HEAD` to check a branch against the ratified
traits at the merge base. Run `/traits:trait-check main...HEAD` in Claude Code
or ask OpenCode to load `trait-check` and review that range. The review uses
the rules at the start of the diff and reports proposed rule edits separately.
For a saved diff, run `/traits:trait-check change.diff --base <base-commit>`
in Claude Code or give OpenCode the file and its exact `--base <base-commit>`.

## Claude Code commands

| Command | Use it to |
| --- | --- |
| `/traits:trait-architect` | Walk through a contributor's first change and draw out conventions worth proposing. |
| `/traits:trait-derive` | Find recurring patterns in an area of the codebase. |
| `/traits:trait-capture` | Turn feedback about how code should be written into a proposal. |
| `/traits:trait-propose` | Check and draft a trait for a pattern you describe. |
| `/traits:trait-extract` | Find recurring conventions that surfaced in a code review. |
| `/traits:trait-check` | Review a diff against the applicable traits. |
| `/traits:trait-index` | Refresh the trait index. |
