---
name: trait-propose
description: Turn a pattern a person has stated into a proposed trait, after checking how it fits the existing traits and how far the code already follows it. Use when the user says "we always", "we never", "this should be a rule" or "make this a trait", or names a convention they want written down.
argument-hint: "<the pattern, in a sentence>"
---

# Propose a trait from a stated pattern

Compare the stated convention with the project's traits and code before writing a
proposal. Run `trait-index --check-spec` first and stop if it fails. Read
`traits/SPEC.md`, or use the bundled
`${CLAUDE_SKILL_DIR}/../trait-index/SPEC.md` if the project has no copy. Read
`traits/README.md`, or read the trait files directly if the index is missing or stale.

The pattern is `$ARGUMENTS`. If none was given, ask for it in one sentence.

You propose. A person ratifies by merging, so write files but never commit them.

## 1. Restate it as a trait

Draft the `description` and `when` the statement implies, and test them against the
spec's rules:

- **Is it about shape?** A one-off decision, an environment fact or domain knowledge is
  worth writing down somewhere, but not here. Say where it belongs. If a rule about
  code follows from the fact, carry on with that rule and say that you did.
- **Is it one prediction?** If two parts could be broken separately, split it and treat
  each on its own.
- **Does it say what the code does?** Turn "never do X" into the thing done instead. If
  the statement gives no positive form, ask what it is.

A spoken statement is rarely exact about scope. State the scope you assumed, for
example "writes only, not lookups", so the user can correct it. Revise the wording
after step 3 if the code uses better terms than the statement did.

## 2. Fit with the existing traits

Compare it with every row of the index and open any trait that comes close.

| Finding | What to tell the user |
|---|---|
| Already covered | Which trait says it. Nothing to write, unless the wording there let a violation through |
| Narrower or wider than an existing trait | Whether to edit that trait or add a second one, and which you would do |
| Conflicts with an existing trait | Both traits, the code that could not satisfy both, and that one must give way |
| Sits beside related traits | Which ones, so its slug and wording match theirs |

Still do step 3 when the pattern is already covered: code that breaks an existing trait
is worth finding.

## 3. Fit with the existing code

Count where the code already follows the pattern and where it does not, with file and
line for both. Open the code; do not judge from search results alone. When there are
dozens of sites, open a sample and mark the counts as approximate.

| Finding | What it means |
|---|---|
| Holds everywhere, or bar a few | A trait. The few are violators |
| Holds, but one detail of it varies | A trait with a decision inside it. Settle the detail before choosing a pattern |
| Split between variants | A decision. There may be more than two variants |
| The code mostly does the opposite | The statement is a wish. Say so, and what adopting it would cost |
| Nothing in the code does this yet | Too early. There is no pattern to describe and no code to take one from |
| Already a trait, and some code breaks it | Either the code is fixed or the trait gains an exception. If the departure looks deliberate, say so |

The cost of a choice includes its callers. Changing which exception a function raises
also changes every place that catches it.

## 4. Give the feedback

Before writing anything, tell the user in a few lines:

- the trait as you would word it, and the scope you assumed;
- how it fits the existing traits;
- how far the code follows it, with the violators listed in one line;
- for each choice they need to make, the options, what each costs and which you
  recommend.

If the pattern holds and neither step 2 nor step 3 left a choice open, go on and write
it. Otherwise stop here and end with the question, phrased so it can be answered in a
word or two.

## 5. Write the proposal

One file in `traits/`, following the spec.

- **Why**: the user's own reason if they gave one. Ask for it if they did not; leave the
  section out if they have none.
- **Pattern**: trimmed from real code that follows the trait, never composed.
- **`check`**: only for a test that already exists.

Run `trait-index` to generate the index and install the specification if needed.
Report the file written and the departures to address before ratification.
