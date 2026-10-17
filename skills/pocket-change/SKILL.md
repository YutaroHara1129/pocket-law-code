---
name: pocket-change
description: Plan and implement features, bug fixes, or refactors when contracts, affected callers, or verification need judgment. Skip mechanical edits and read-only reviews.
license: MIT
---

# Make a change others can continue

Use the project's contracts and contribution rules within the governing
instruction hierarchy, safety constraints, and granted permissions. This skill
fills gaps; it neither replaces project policy nor grants authority. Treat
inferred needs as hypotheses, not additional requirements.

## Establish what must work

Identify the requested outcome, constraints, and evidence that would demonstrate
completion. Consider who will use, review, operate, or later change the result;
investigate only needs that could change today's implementation or handoff.

Read applicable local instructions and the code, callers, tests, and maintained
documentation relevant to the change. Distinguish intended contracts from current
behavior: a passing test or an existing implementation can preserve a bug. When
sources disagree, use their role, authority, and evidence; do not automatically
prefer code, the newest text, or a fixed list of filenames.

Resolve material uncertainty from available evidence first. Ask for a decision
only if an unresolved choice changes the requested outcome, compatibility, or
authority; continue independent authorized work. Do not turn routine choices
into approvals or expand scope to satisfy a hypothetical future need.

## Keep the change coherent

Trace the effect through affected callers, data, error paths, configuration, and
public contracts. Include the tests and documentation necessary to keep those
parts consistent. Reuse the project's existing design and tools where they fit.

Prefer the smallest complete solution with understandable dependencies. Split
unrelated outcomes when they can be evaluated and integrated independently;
keep prerequisites and compatibility updates together when splitting would leave
a broken intermediate state. Line counts and file counts do not decide this.

Leave recoverable intent in the code's structure. Add a nearby reason or
constraint only when a future maintainer cannot infer it and needs it to change
the code safely. Use the project's existing record for broader decisions; do
not create a parallel documentation or issue system.

If new evidence changes the scope, risk, or contract, revisit the affected
decision rather than restarting all investigation or silently broadening work.

## Establish and hand over evidence

Choose checks for the behavior that could break, including relevant failures and
boundaries. Prefer the cheapest check that can detect that failure; a unit test
cannot establish an integration contract it never exercises. For a bug, check
that the regression test fails against the old behavior and passes with the fix
when practical. Do not test internal call sequences unless those are the contract.

Use existing required checks. Add tooling or CI only when the task requires it
or a demonstrated gap justifies it within scope. Do not weaken checks to get a
green result. Coverage and CI success show what was exercised, not correctness
outside that scope. Distinguish failures caused by the change, pre-existing
failures, and checks you could not run.

Before declaring completion, compare the actual result with the requested
outcome and affected contracts. Briefly hand over the changed behavior and its
reason, meaningful verification and its limits, and any remaining decision or
action the recipient needs. Use existing project formats; omit empty sections
and routine process narration. Readiness alone does not authorize publication,
merge, or deployment.
