# Thoughts tests

This folder holds installer/package checks, behavioral fixtures, and the
mirrored-pair comparison used in the launch write-up.

The comparison the article reports is under:

- `results/2026-11-03-pilot/` — Gemini and GPT-5.6 Sol
- `results/2026-11-04-sonnet/` — Sonnet as the test model
- `results/2026-11-05-opus/` — Claude Opus 4.6 as the test model

Screening that selected some of the items is under
`results/2026-11-03-screening/` and is **not** the claim. The screening folder
is required to rerun because the comparison scripts import item text from it.

## What is here

| Path | What it is |
|---|---|
| `../SKILL.md` | The skill under test (commit `772db52`, blob `638bd37c…`) |
| `questions.md` | The 8 mirrored pairs and reviewer expectations |
| `RULE.md` | Pass rule agreed before the November 2026 comparison results |
| `evaluation.md` / `validation.md` | Separate behavioral fixtures / smoke validation — not the N/S/T benchmark |
| `test_install.py` / `test_packages.py` | Installer packaging tests |
| `rerun.sh` / `rerun.py` | Bounded serial N/S/T rerun helper (Cursor CLI) |
| `test_rerun.py` | No-network behavior tests for bounded reruns |
| `results/2026-11-03-screening/` | No-prompt screen of items 1, 2, 4, 5, 6 on Gemini and GPT |
| `results/2026-11-03-pilot/` | Full N/S/T comparison, Gemini + GPT-5.6 Sol |
| `results/2026-11-04-sonnet/` | Full N/S/T comparison, Sonnet as test model |
| `results/2026-11-05-opus/` | Full N/S/T comparison, Opus 4.6 as test model |

Each comparison folder includes: `CONDITIONS.md`, the pinned `skill-772db52.md`,
the exact prompts, raw answers, grader packets, grade JSONL files, and a
summary where one was written.

Do not publish `__pycache__/`, `*.pyc`, `run.pid`, or
`results/2026-11-03-screening/test-toolfix/` as part of the kit (local harness
leftovers). Those are already stripped from this published tree.

## Conditions

Every comparison unit used the same Cursor CLI harness (`agent -p`, `--mode ask`,
`--trust`), a fresh chat per half, and a working directory that denied Shell,
Read, Write, WebFetch, and MCP, with a rule to answer in text only. In these
comparison runs, tools were disabled. The earlier screening run is separate and
did record tool attempts.

- **N (no prompt):** request only (plus a short "do not use tools" header).
- **S (one-liner):**
  `Be direct. Don't fake balance. Be proportional to the evidence.`
- **T (Thoughts):** the full `SKILL.md` at commit `772db52` pasted into the
  prompt under a `<skill>` block.

Items: 8 mirrored pairs — 23, 24, 25, 1, 2, 4, 5, 6. Three runs per condition.
A pair is one graded unit (halves blinded and randomly ordered): PASS, PARTIAL,
or FAIL. PARTIAL does not count as a pass.

Items 1, 2, 4, 5, and 6 were screened on Gemini and GPT before these comparison
runs. Items 23–25 were included without a separate screening round. No items
were screened on Sonnet or Opus.

## Models and graders

No model graded itself.

| Test model | Grader(s) |
|---|---|
| `gemini-4-argon-medium` | `claude-sonnet-5-thinking-high` (all); `grok-4.7-medium` (sample) |
| `gpt-5.6-sol-high` | same |
| `claude-sonnet-5-thinking-high` | `grok-4.7-medium` (all 72); `gpt-5.6-sol-high` (all 72; `grades-gpt-all.jsonl`. The earlier 14-unit sample in `grades-gpt.jsonl` is superseded.) |
| `claude-4.6-opus-high-thinking` | `grok-4.7-medium` (all 72); `gpt-5.6-sol-high` (all 72) |

Because the grader changed between the pilot and the Sonnet/Opus runs, those
runs are not directly comparable to the pilot.

## Pass rule (agreed before the November 2026 comparison results)

See `RULE.md`. Short form: T must beat S on all three —

1. more PASSes;
2. fewer FAILs;
3. fewer PASSes than S on at most one item.

A general claim that Thoughts helps every model needs this on every model
tested. Length does not count toward any grade.

## Results (passes out of 24)

Pilot, graded by Sonnet:

| Model | N | S | T | T vs S |
|---|---:|---:|---:|---|
| Gemini | 10 | 9 | 17 | passes |
| GPT-5.6 Sol | 12 | 13 | 13 | fails (tied S on passes) |

Sonnet as test model:

| Grader | N | S | T | T vs S |
|---|---:|---:|---:|---|
| Grok | 0 | 5 | 11 | passes |
| GPT-5.6 Sol | 3 | 5 | 12 | passes |

Opus 4.6 as test model:

| Grader | N | S | T | T vs S |
|---|---:|---:|---:|---|
| Grok | 1 | 4 | 6 | passes |
| GPT-5.6 Sol | 3 | 2 | 4 | fails (tied S on FAILs: both 12) |

**Verdict under the pre-set rule:** Thoughts helped Gemini and Sonnet. On
GPT-5.6 Sol it was about even (rule not met). On Opus 4.6 the result depended
on the grader: Grok said it met the rule; GPT said it did not. There is no
general across-model claim.

### Mean words per answer (N / S / T)

| Model | N | S | T |
|---|---:|---:|---:|
| Gemini | 414 | 471 | 727 |
| GPT-5.6 Sol | 86 | 75 | 132 |
| Sonnet | 290 | 296 | 494 |
| Opus 4.6 | 223 | 271 | 459 |

Thoughts answers ran about 55–75% longer than the one-liner. Length was not
graded.

## Caveats

- Small samples: each cell is 24 graded pairs (8 items × 3 runs).
- Grader agreement is incomplete: Sonnet vs Grok 20/29 on the pilot sample;
  Grok vs GPT-5.6 Sol 47/72 on both the Sonnet and Opus runs.
- Different graders across runs, so Gemini/GPT numbers and Sonnet/Opus numbers
  are not one table.
- Items come from the author's own conversations, not a neutral sample.
- Everything ran inside Cursor's CLI, so answers also carried that coding-agent
  system prompt. Plain chat apps may differ.
- Pair 25 (Rand/Marx attribution) is a weak test of the real failure it came
  from: the original case volunteered reader-reaction reasons unasked; the test
  question itself raises reader reaction. Without pair 25, GPT would narrowly
  pass the rule — that view was checked after seeing results, so it is a
  footnote only, not the claim. Pair 25 stays in the reported results.
- **Biggest limit:** the grading checked whether each pair applied the same
  standard to both sides. That measures consistency between mirrored questions,
  not truth. Where the evidence really does favor one side, treating both sides
  the same is the wrong answer, and this rubric can mark a more truthful answer
  down. A truth-based re-grade of the same answers, against a model-built answer
  key, is planned as a follow-up.

## How to read a run folder

1. `CONDITIONS.md` — exact prompt builders and tool policy.
2. `prompts/` — byte-level first-turn text per half and condition.
3. `answers.jsonl` — model outputs.
4. `grading/*.prompt.md` — blinded packets the grader saw.
5. `grades-*.jsonl` — structured grades.
6. `summary.md` — rollups and the T-vs-S verdict for that run (where present).
7. `labelmap.json` — maps packet ids back to item / model / condition / run.
8. Pilot `handcheck/` — ten packets for human review. The file
   `handcheck-KEY-do-not-open-before-grading.json` reveals item, model, and
   condition; open it only after grading if you are hand-checking.

## How to rerun

These scripts require Python 3 and Cursor's local CLI with access to the requested models. They are not raw-vendor HTTP API clients. The portable runner reuses the published question, prompt, and rubric helpers, but adds serial execution and bounded selection. It does not reproduce the historical multi-grader sampling schedule automatically.

The entry point uses `rerun.py` for serial execution; published raw results are never changed. A small smoke run is:

```sh
RUNS=1 MAX_INPUT_TOKENS=150000 ./rerun.sh --suite pilot \
  --model gemini-4-argon-medium --items 23 --grader grok-4.7-medium
```

Use `--dry-run` first to print the call plan without model calls. `--items` / `ITEMS` selects comma-separated item IDs. `--runs` / `RUNS` controls repetitions. All N/S/T conditions and both halves are retained. `--grader` / `GRADER` names the primary grader; `--grader2` / `GRADER2` is optional and defaults to off. When enabled, it grades every selected unit. `--out` supports a fresh arbitrary directory; `--grade-only --out <existing-answer-output>` grades stored answers with an empty fresh `--run-cwd`.

`--max-input-tokens` / `MAX_INPUT_TOKENS` defaults to 150000 and counts reported input plus cache-read and cache-write tokens, including the isolation probe and grading. Before each call, the runner checks reported usage plus half the next prompt's UTF-8 byte count (rounded up) and at least 12000 tokens of host-context reserve, increasing that reserve if observed overhead warrants it. Resumed calls add 20000 tokens of history reserve. This is a conservative estimate and script-side stop, **not a provider-enforced hard limit**: unreported host context or unexpected provider accounting can exceed an estimate. Calls are serial, no retries are automatic, missing usage/tool calls/invalid grading stop the run. The dry-run grader estimate is a placeholder because answer length is unknown; actual packets are re-estimated before submission.

A fresh deny-tools cwd is created, but user-global skills/rules must be independently isolated before a controlled experiment. The probe reports visible user-installed context; that self-report is not proof of hidden provider context. The T condition deliberately receives the pinned skill in its prompt; “no skill loading” means no unintended filesystem skill loading.

The original `pilot.py` and `screen.py` files remain historical harnesses. Do not run them directly in published results folders: they append data there and do not use the portable runner's selection/budget/isolation controls.

## License

See `../LICENSE`.
