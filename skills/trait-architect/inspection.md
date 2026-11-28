# Trace a change to code

Work from the consumer project's declared dependencies and journey files.
Start at the named node, step or property when the person gives one. For a
broader change, visit workflow nodes first, then journey steps with additional
sites, then remaining scoped source locations by path and line. Attach related
journey evidence to a node as soon as you inspect it.

## Workflow DAGs

Read the relevant workflow definition or use the project's read-only graph
listing. Locate the task definitions and the dependencies they declare. For a
handoff, open the producer and the consumer. Look at what crosses the edge,
who owns it, and where failures or cleanup change that choice.

Within the scoped graph, visit prerequisites before dependents. Each time
several nodes are ready, take the lexically first node ID. Order separate
graphs by repo-relative definition path, then graph ID. This orders the interview even when
the scheduler can run tasks concurrently. Cite the definition path, node IDs
and the implementation site. If an edge is generated and cannot be resolved,
or a cycle prevents further ordering, identify the gap and continue from the
available source sites.

## Journeys

Read the project's `journeys/SPEC.md` when present. Open matching
`journeys/<slug>.md` files directly, even if the catalogue is missing.
Match the requested actor, trigger, outcome or changed operation. Visit
matching slugs in lexical order and steps in the order written. Inspect each
relevant alternative at its point of divergence. Active property IDs come
from `## Properties`. If several apply to one step, take them in numeric order.
Retired IDs stay in the history. A retry can revisit a step, and successive
steps alone establish no dependency edge.

Follow references in the evidence section to the implementation or test. If a
previous journey inspection is available, reuse findings for the same property,
revision and path. A property about rejected input may say nothing about a
worker that crashes after writing half its output.

Identify the site that carries out the step and read a comparable caller when
one exists. Cite the journey step and the applicable property separately
(for example, `retry-purchase` step 3 and `retry-purchase/P1`) alongside the
source location. Distinguish what a trace observed, what a model covered and
what the journey asks for.
Leave an unlocated implementation open.

For example, a buyer seeing the original receipt on retry is observable
behavior. Two adapters forwarding the stored purchase key give you a question
about code shape. Ask how the contributor would review a third adapter that
allocates a key. If either implementation is acceptable as long as the receipt
is recovered, the decision stays with the journey. For a requested behavior
review, use `journey-check` when available.
