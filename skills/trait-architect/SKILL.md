---
name: trait-architect
description: Guide a contributor through a change or interview a maintainer about coding conventions. Inspect code, workflow DAGs and journeys to find review decisions and turn agreed patterns into proposed traits.
---

# Onboard someone to a project's conventions

Start with the change, workflow, journey or review decision the person named.
If they gave none, ask what they expect to work on first or often explain in
review. Use the answer to bound the interview. Someone asking for a walkthrough
can learn what the team already does without having to set policy.

## Choose the next decision

Read the project's guidance and applicable files in `traits/`. The catalogue
in `traits/README.md` can help find them. When the change touches a workflow
graph or a journey, follow the [inspection guide](inspection.md) to trace it
to code and order the sites. Otherwise use repo-relative path, then line
number. Use the consumer's files as evidence.

Take an explicitly requested decision first. At each site explain any applicable
trait. Show an example for a settled convention. Look for a choice the next
contributor will actually face, including any conflict with a written rule.
At that site, take a split between implementations before an undocumented
recurring shape. Break ties by source line, then symbol name. Discuss a shared
choice once and use the other sites as comparisons.
In new code, start with the first planned change and label examples hypothetical.

Keep the ordered topics, evidence and answers in the conversation. Return to
the next untouched topic after each decision. If the person changes the scope,
honor it and keep answers that still apply. A request to pause or finish takes
effect immediately, including in the middle of a topic.

## Interview one choice at a time

Show the exact line another contributor might write and ask **one question per
turn**. Start with the first unanswered point below. Use what the person already
told you, including answers they volunteered to later questions. Look up facts
the repository can answer. Ask the person for judgments.

| Order | What to establish | A question to adapt to the code |
| --- | --- | --- |
| 1 | Review decision | “Here the handler passes the caller's key. The other handler allocates one. What would you accept in the new handler?” |
| 2 | Applicability | “Which operations need to reuse the caller's key?” Get a condition someone can recognize in another file. |
| 3 | Boundary | Try the proposed rule on a second caller, the closest departure or an alternate path. “The replay worker has no caller. What should it do?” If only a hypothetical case exists, say so. |
| 4 | Reason and cost | “What goes wrong for the caller if the handler picks a fresh key?” Where two forms have real costs, ask which cost the team accepts. Keep the person's own reason, including an explicit “no particular reason”. |

Apply the answer to the original site and the boundary case. If two rules
still fit the answer, find the smallest change they would lead someone to
review differently. For a journey-backed choice, hold the outcome fixed.
Two adapters can both forward the original key while only one calls a shared
helper. Would the reviewer accept both? If the person wants your
recommendation, explain the tradeoff and let them choose.

“I usually do this” can describe a personal habit. Ask whether they would
request a change from someone who chose differently. “Either” closes the
choice as discretionary. When the choice or its scope remains disputed or
unknown, park the topic and advance. A bare “skip” also advances. If they
skip just the rationale, keep the agreed convention and leave its reason out.
Reopen a parked topic only when the person asks or supplies new evidence.

## Use the answer

For a walkthrough, leave files alone. When the person wants to encode a
convention, read back the code shape, scope and exceptions at the cited sites.
Carry their wording, reason and evidence to `trait-propose` for the code and
duplicate checks, proposal and index update. A maintainer ratifies by merging.
If a trait already covers the decision, show how to use it. Surface a conflict
with an existing trait for the person to resolve before editing.

Keep a one-off choice with its change. For a preference without supporting
code, give a candidate `description` and `when` in chat and name the first
change that could exercise it. Keep observable behavior with its journey.
When the area is covered or the person stops, recap what they can apply to
their change, any proposals written, and what remains open or unvisited.
For a pause, name the next topic or unanswered point so they can resume.
