---
name: trait-derive
description: Survey existing code and propose traits it already follows, list the code that breaks them, and surface patterns too divided to be traits as decisions for the user. Use when adopting traits on a codebase or an area of it, or when asked what conventions the code already has.
argument-hint: "[path]"
---

# Derive traits from existing code

Find the shapes the code already repeats and write them down as proposed trait files.
Load `trait-index` and follow its `--check-spec` instructions first. Stop if
the check fails. Read `traits/SPEC.md`. If the project has no copy, read
`SPEC.md` from the base directory of the loaded `trait-index` skill. In
Claude Code, the bundled file is at `${CLAUDE_SKILL_DIR}/../trait-index/SPEC.md`.

Use the path from the request as the scope. With no path, cover the whole
repository. On a large codebase, work one area at a time.

You propose. A person ratifies by merging, so write files but never commit them.

## 1. Know what is already written

Read `traits/README.md` and the project's existing conventions in its agent
instructions, contributor documentation and linter configuration. Read the trait
files directly if their index is missing or stale.
Anything stated there is not a new finding. Code that breaks something already written,
whether a trait or a rule in those other documents, is drift, and is reported
separately in step 7.

## 2. Read the review history

The code shows what was written. Past reviews show what people asked for, which is the
better evidence of what the team wants. If the repository's pull requests are
reachable, use the repository host's tools to read reviews of recently merged changes
in scope. On GitHub, the following commands list recent merges and read the review of
pull request 123.

```bash
gh pr list --state merged --limit 100 --json number,title,files
gh pr view 123 --json reviews
gh api --paginate 'repos/{owner}/{repo}/pulls/123/comments'
```

Keep to pull requests that changed files in scope and had comments from human
reviewers. Ignore automated comments, and treat an automated code reviewer's remarks as
bug reports, never as statements about shape. Say how many pull requests you read.

Use what you find in three ways:

- **Candidates.** A remark that reviewers make more than once about the shape of code,
  such as "this belongs in…" or "we name these…", is a candidate even if the code
  counts alone would not have surfaced it.
- **Direction for a split.** When the code is divided between variants, the reviews
  often show which one people ask for, and commit dates show which is newer. That
  belongs in your recommendation for the decision.
- **Why.** A reason a human reviewer gave, quoted with the pull request number, is the
  best source for a Why section. A reason in the author's replies is weaker: a model
  may have written it.

A reviewer may cite a rule that is written nowhere and that the code only partly
follows. Report it as a decision and say that it was cited.

If the history cannot be reached, say so and carry on from the code alone.

## 3. Survey

For one package or directory, survey it yourself. For anything wider, split it into
areas that do not overlap, following the project's own boundaries (for example its
services, its layers, its tests), and give each to a read-only agent in parallel. Tell
every agent:

- Which conventions the project already documents.
- Which code follows each proposed pattern and which code departs from it, with
  counts and file and line references for both.
- Which generated and vendored code to exclude.
- Where to label estimated counts.

Look for what lets someone predict code without reading it: where a kind of thing lives,
how it is named, what it takes and returns, how it fails, how it is tested.

## 4. Sort the candidates

| Adherence | What it is | What to do |
|---|---|---|
| Holds across its scope with isolated departures | A candidate trait | Propose a file and list the departures |
| A clear majority with a real minority, or an even split | A decision | Put it to the user (step 7) |
| Too few occurrences to establish a convention | Insufficient evidence | Leave it out |

Use counts to describe the strength and limits of the evidence.

- **Count places the pattern could apply**, and say what you counted: call sites,
  functions or files give different ratios.
- **Leave out places it does not apply to**, such as empty stubs.
- **Check whether departures share a reason.** A small group may reflect a deliberate
  exception or a competing convention.

Then two tests of judgement:

- **Common is not the same as good.** If the majority variant looks like a mistake, say
  so and treat it as a decision.
- **Would knowing it change how someone writes or reviews code?** A pattern that holds
  but does not matter, such as a decorative habit, is not worth a file. Drop it.

## 5. Verify before writing

Agent reports arrive sounding certain. For every candidate you intend to write, rerun
the count yourself and open the code the pattern will be taken from. Drop a claim you
cannot reproduce.

## 6. Write the proposed traits

One file per trait in `traits/`, following the spec. In particular:

- **One prediction per file.** If two parts could be broken separately, write two files.
- **Name the slug for its area** when the trait is local to one, as in `cli-errors`,
  so related traits sort together in the index.
- **The pattern is trimmed from real code**, never composed. Do not invent a function
  name, a test name or a signature.
- **Never infer a Why.** Write one only when you have a source for it: a human
  reviewer's reason, a comment or docstring in the code, or behaviour you confirmed.
  Otherwise leave the section out. A plausible reason you made up reads as fact once
  merged.
- **Record `check` only for a test that exists**, and say in `covers` how much of the
  trait it verifies.

After writing proposals, run `trait-index` to generate the index and install the
specification if needed.

## 7. Report

Four parts, in this order.

**Proposed traits.** A table of slug, description and how many places follow and break
it. For each Why, say where it came from (a review, with its pull request number, or a
place in the code), so the person ratifying can confirm it; say which traits have none.
Say how many pull requests' reviews you read.

**Violators.** For each trait that does not yet hold everywhere, the files that break
it. This is the scrub that ratifying the trait requires.

**Drift.** Code that breaks a trait or a written rule that already existed before this
run.

**Decisions.** Every pattern too divided to be a trait, grouped by area and ordered
within each area by how many places the choice affects. Do not drop any to keep the
list short: on a large codebase the list is long because the work is. For each one give:

- the question, in one line;
- each variant with its count and one real example;
- how many places would change if that variant won;
- your recommendation and the reason.

A decision that is cosmetic, where either answer would do and few places change, gets
one line: the question, the counts and your recommendation.

Nothing is written for a decision until the user answers it. If they pick a variant,
write the trait and add the other sites to the violators. If they describe something
else, write that. Regenerate the index after writing either proposal. If they
decline, leave the decision open for a later run.

If the project has no standing instructions for reading traits, point the user to
the example instructions in `trait-index`.
