---
name: trait-extract
description: Propose traits from a reviewed pull request by reading what the reviewers asked for and how the code changed in answer. Use after a pull request has been reviewed or merged, or when the user wants the lessons of a review written down as traits.
argument-hint: "<pull request number | base..head>"
---

# Extract traits from a reviewed pull request

Turn recurring conventions identified in a review into proposed trait files. Run
`trait-index --check-spec` first and stop if it fails. Read `traits/SPEC.md`, or use the bundled
`${CLAUDE_SKILL_DIR}/../trait-index/SPEC.md` if the project has no copy. Read
`traits/README.md`, or read the trait files directly if the index is missing or stale.

You propose. A person ratifies by merging, so write files but never commit them.

This pays off on a pull request where reviewers pushed on how the code was shaped. On
one where they only fixed substance, it finds nothing, and step 2 says to stop.

## 1. Find what the review changed

For a pull request number in `$ARGUMENTS`, use the repository host's tools to fetch
the commits, reviews, inline comments and diff. The following commands fetch them
for GitHub pull request 123.

```bash
gh pr view 123 --json title,body,commits,reviews
gh api --paginate 'repos/{owner}/{repo}/pulls/123/comments'
gh pr diff 123
```

For a `base..head` range with no review record, compare the two revisions and ask the
user what feedback led to the changes.

Walk the review threads in the order they happened, and pair each comment with the
commit that answered it. Authors often reply naming the commit.

- **Only comments from human reviewers are the signal.** Ignore automated comments such
  as coverage reports. Treat an automated code reviewer's comments as "this is wrong"
  at most, never as a statement about shape.
- **Later rounds can reverse earlier ones.** Read every round, and take the final
  position. A reversal is itself worth reporting.
- **Leave out changes that came from merging the base branch.** They were not asked for
  by the review.
- If the history was squashed and the intermediate commits are gone, work from the
  review comments and the final diff, and say so.

## 2. Separate shape from substance

Take each thing a reviewer asked for, and ask what kind of statement it is.

| The reviewer was saying | Example | Outcome |
|---|---|---|
| "This is wrong" or "this is missing" | A bug, a wrong unit, a missed case, a field to add | Not a trait |
| "Not here, there" or "not like this, like that" | Moving a query out of a request handler | Candidate |
| "We always…", "we never…" or "the policy is…" | Any remark phrased as a rule | Candidate |
| A preference with no reason given | A rename | Ask the user whether it is a rule; if you cannot ask, list it as an open question |

If there are no candidates, say so and stop. Do not go looking for traits the review
did not raise.

## 3. Test each candidate

Assess each candidate the way `trait-propose` assesses a stated pattern: restate it as
a trait, compare it with the existing traits, and count the code.

| Finding | Outcome |
|---|---|
| An existing trait covers it | The change broke a trait and review caught it. Report it; propose an edit only if the trait's wording let it through |
| It overlaps or conflicts with a trait | Name the trait and say which should give way or be edited |
| The reviewed shape already holds widely | Propose a trait; the rest are violators |
| Both shapes are common | A decision for the user, with counts and one example of each |
| The reviewer cites a rule the code does not follow | A decision. Say where the rule is written, or that you could not find it written anywhere |
| This is the first time it has come up | Mention it; write nothing |

If the count depends on information outside the code, report it as unknown and name
the evidence needed to establish it.

## 4. Write the proposals

One file per trait, following the spec.

- **Why**: the reviewer's own reason, quoted, where they gave one. Otherwise leave the
  section out. Do not take the reason from the pull request author's replies or from
  comments in the code under review: those may have been written by a model.
- **Pattern**: trim it from the final, reviewed code.
- **One prediction per file.**

After writing proposals, run `trait-index` to generate the index and install the
specification if needed.

## 5. Report

- **Proposed traits**, each with the review comment it came from.
- **Violators**: existing code each new trait would require changing.
- **Broken traits**: existing traits the change violated, both those review caught and
  any still broken in the merged result.
- **Decisions**, **open questions** and **first sightings**, as above.
