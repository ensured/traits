---
name: trait-capture
description: Capture the reasoning when the user steers how code is written, so the preference is remembered as a trait instead of being lost at the end of the session. Use whenever the user corrects, redirects or rejects the shape of code you wrote or proposed, for example "not like that", "put it there instead", "we don't do it that way here", "use X for this", even if they never mention traits.
---

# Capture a preference when the user steers

A correction can reveal a code convention that applies beyond the current change.
Propose a trait when the correction identifies such a convention and the existing
code supports it.

## 1. Do what they asked first

Make the change. Never hold up the work to talk about traits.

## 2. Decide whether it was about shape

| The user was saying | Example | What to do |
|---|---|---|
| "This is wrong" | A bug, a wrong value, a missed case | Nothing more, unless the fix shows a convention you would break again elsewhere; then treat it as shape |
| "Not here, there" or "not like this, like that" | Where code lives, how it is named, how it fails, what it goes through | Carry on to step 3 |
| A better choice for this one piece | A clearer name for one variable | Nothing more |
| A preference about how you work | Shorter answers, fewer questions | Not a trait: traits describe code. Leave it to your own memory or instructions |

Use phrases like "this one" or "always" as clues to scope. If the correction could
apply either to this change or to a broader convention, follow step 4.

## 3. Check whether it is already written

Look in `traits/README.md` and the project's agent instructions or contributor
documentation. Read the trait files directly if their index is missing or stale.

| Finding | What to do |
|---|---|
| A trait covers it | Point to the existing trait |
| A trait covers part of it | Say which, and offer to tighten its wording to cover the rest. That offer is your one question |
| It is written somewhere other than `traits/` | Say where, in one line. Ask nothing. Keep any caveat written there |
| Nothing covers it | Carry on to step 4 |

## 4. Collect the reasoning

You need two things: whether this is a general rule or a one-off, and why. Take both
from what the user already said if you can.

If either is missing, ask once, briefly. For example: "Should handlers always go
through the service layer, or just this one? If always, what's the reason? I'll write
it down as a trait so it sticks."

Asking has a cost, so keep it low:

- **Wait for a natural pause**, such as the end of the task, and put everything you
  have collected into one question.
- **One question per correction at most**, and never about a pattern you already asked
  about or proposed in this session.
- **Drop the proposal if they describe a one-off or leave the question unanswered.**
- **Record the reason in their words.** Do not improve it or add to it.

## 5. Hand over to trait-propose

With the pattern and the reason in hand, follow the `trait-propose` skill: check how the
pattern fits the existing traits and how far the code already follows it, give that
feedback, and write the proposed file with the user's reason as its Why.

A preference the code does not follow yet is still worth reporting. Tell the user how
much code would have to change for it to hold, and let them decide.
