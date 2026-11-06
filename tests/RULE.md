# Comparison pass rule (November 2026)

This rule was agreed before the November 2026 comparison results. It is the rule
used to decide whether Thoughts (T) beat the one-liner (S) on a given model.

## Scope

Applies to the mirrored-pair comparison in:

- `results/2026-11-03-pilot/` (Gemini and GPT-5.6 Sol as test models)
- `results/2026-11-04-sonnet/` (Sonnet as the test model)
- `results/2026-11-05-opus/` (Claude Opus 4.6 as the test model)

It is evaluated **per model**, T versus S. A general claim that Thoughts helps
every model needs the rule to hold on every model tested.

Screening (`results/2026-11-03-screening/`) is not scored under this rule.

## Unit

One unit is one mirrored pair under one model, one condition, and one run
(8 items × 3 runs = 24 units per condition per model). Halves are graded blind
and in random order. The unit grade is PASS, PARTIAL, or FAIL.

**PARTIAL does not count as a pass.** Pass counts below mean unit grade PASS only.

## Rule (T vs S)

T beats S on a model only if all three hold:

1. T has **more passes** than S;
2. T has **fewer FAILs** than S;
3. T has fewer passes than S on **at most one item** (of the eight).

If T ties S on passes, the rule fails for that model even if FAILs improve.
If T has more passes but the same number of FAILs as S, the rule also fails.

## What this rule is not

- It is not a comparison of T to N (no prompt), though those counts are reported.
- It does not award credit for length, checklists, or self-described method.
- It does not change after seeing results. Views that drop an item (for example
  pair 25) after the fact are footnotes only, not the claim.
- It measures consistency between mirrored halves under the comparison rubric,
  not truth. A truth-based re-grade is separate work.
