---
name: trait-architect
description: Interview a contributor or maintainer about a project's coding conventions. Use for guided onboarding to a codebase or to help someone turn their design preferences into proposed traits.
---

# Onboard someone to a project's conventions

Start with a change the person expects to make or a choice they often explain
in review. If they gave you one, start there. For a newcomer without a task,
ask, "Which part of the project would you like to work on first?" For a
maintainer, try "What do you usually walk a new contributor through?"
Wait for their answer.

## Discuss one choice

Read the relevant project guidance and `traits/README.md` at the project
root, if present. Open any matching trait and a few files in the area the
person named. If the catalogue is missing or stale, read the trait files
directly. For someone learning an established convention, show where it
applies in their first change and explain the reason if one is documented.

Pick one decision a reviewer would care about. Show a real call site, or
two if the code uses competing approaches. Ask one question and wait for
the answer. If there is no example yet, ask how they want the first one
to work. For example, after showing a CLI command that receives an output
stream, ask, "If my next command called `print()` here, would you ask me to
change it in review?" Adapt the next question to what they say.

Find out when their preference applies, what prompted it, or which exception
matters. Ask only for what is still unclear. If they want your opinion, give
a recommendation and its tradeoff, then let them choose. "Either is fine",
"I don't know" and "skip" all let you move on. A newcomer can finish with
an explanation of the existing code and no proposed traits.

## Turn the answer into a trait

For a recurring choice the person wants contributors to follow, use
`trait-propose` with their wording, scope, reason and the sites you opened.
It checks the format and existing traits, compares the choice with the code,
and writes a proposal and refreshes the index when the evidence supports it.
Keep the person's reason in their own words. If an existing trait covers the
answer, show it. If the answer would change that trait, surface the conflict
before drafting an edit. A maintainer ratifies a proposal by merging it.

In a new project, or when the code has yet to adopt the preferred shape,
give the candidate `description` and `when` in the conversation. Include the
person's reason if supplied and name the first change where the team could
try the idea. A one-off decision can stay with that change. An answer about
what a user experiences over time can become a journey if the person wants
to explore it.

Follow the next topic the person raises. When they are done or the requested
area is covered, recap the existing traits worth reading, the proposals
written and any choices still open. Omit empty categories.
