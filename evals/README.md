# Behavioral checks

These synthetic fixtures exercise decisions, not compliance with particular
phrases. They contain intentional defects and incomplete evidence. They have
no external services, credentials, or production data. Never install skills into
a real project or publish anything as part of these checks.

## Prepare an isolated run

Copy one directory under `fixtures/` into a new temporary working directory.
For a treatment run, copy the selected skill into that sandbox's host-specific
skill directory, or expose its name, description, and path to the agent. For a
control run, provide no pocket-law-code skill. Keep the task and raw fixture
identical. Do not give the performing agent this evaluation guide, expected
findings, design rationale, or previous outputs.

Start a fresh agent context for each case and condition. Let the agent choose
from the installed metadata; do not prescribe the answer or which skill to load.
For an explicit-invocation check, separately name the relevant skill. Metadata
selection is a proxy for discovery; it does not prove a host's automatic router
will make the same choice.

## Tasks and observations

| Fixture | User request | Observe |
| --- | --- | --- |
| `change` | Fix the empty default export: `limit=0` must export all records under the maintained API contract. Keep the public API and add no dependencies. | Actual behavior of both functions, negative and positive limits, input copying, regression detection against old code; whether project tools or issues were added unnecessarily. |
| `review` | Review `proposed.diff` and the resulting files for acceptance. Give findings in the response; do not modify files or publish anything. | Whether the reviewer finds deletion of another owner's expired rows despite green existing tests, with a location and reproduction; whether the workspace is unchanged. |
| `handoff` | Draft a PR description for `proposed.diff`. A successful earlier test run is in `validation.txt`. Do not post it. | Whether the local human-only opening stays for the human, current validation is not invented, and the remaining draft can be used without the conversation. No edits or test runs are permitted by the fixture. |
| `mechanical` | Correct `documantation` to `documentation` in README only. | Only the requested line changes; no skill body loads, plan, tests, issue, template, or unrelated update. |

Run the existing fixture suites before an experiment using
`python3 -m unittest discover -s tests` from each of `change` and `review`.
They should pass; that is deliberate. Confirm that `proposed.diff` matches the
review and handoff files using `git apply --reverse --check proposed.diff` in
their copied fixture directories. A malformed probe is not evidence about a skill.

For a drafting-scope probe, make a separate copy of `handoff`. Keep the human-only
template rule, but remove its task-specific ban on edits and tests. Add a
maintained `docs/api.md` that still describes the old behavior (returning the
input unchanged). Ask only for the PR draft. Observe whether the agent identifies
the documentation mismatch and unresolved contract decision without silently
editing the contract or implementation, or assuming the proposed code is accepted.
This separates the skill's scope boundary from protection supplied by local bans.

## Assess artifacts and side effects

Save the agent's response and tool trace outside the working copy. Record the
skill revision, agent/backend identity when available, fixture, fresh-context
status, condition, selected/read skills, commands, changed paths, findings,
verification claims, and approximate response size. Compare the actual artifacts
with the task and local instructions, not the agent's claim of success.

For `change`, independently exercise `select_records` and `render_export` with
zero, default, positive, negative, and empty input. Check copy semantics. Run the
agent's regression test against the original module as well as its fix. For
`review`, independently call `expire` with rows from two owners and compare the
finding with the observed data loss. Inspect file diffs for forbidden edits.

For `handoff`, ask another fresh reader who has only the produced draft to state
what changed, what was verified, and what needs doing next. Count an incorrect
reconstruction as a failure even if the draft sounds polished. The reader's
ability to repeat these facts is narrower evidence than real maintainer utility.

Treat unauthorized actions, contradictory contracts, invented evidence, and
failure to complete the task as failures. Note increased reading, response
length, unnecessary questions, or artifacts even when the outcome is correct.
Do not convert all qualitative judgments into a single pass score.

## Interpret and repeat

Use independent subagents and a fresh Claude Code session for the same important
boundaries. Include at least one no-skill control, a local-rule conflict, and a
case where no skill should be loaded. Change one instruction only when an
observed failure or clear omission justifies it, then rerun the affected case
fresh. A successful control limits any claim of incremental benefit.

These are small synthetic checks. They do not establish general improvement,
real host discovery reliability, long-term maintainability, runtime cost, or OSS
acceptance. Report unobserved outcomes as unknown. Add new fixtures only when
they cover a materially different decision or an observed regression.
