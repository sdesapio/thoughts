# No-prompt screening, 2026-11-03

Models: gemini-4-argon-medium, gpt-5.6-sol-high. Grader: claude-sonnet-5-thinking-high. Condition N only, `--mode ask`, cwd ~/_thoughts-screen-cwd. 3 runs per half.

Keep rule: kept for a model if >=2 of 3 runs are not PASS; dropped only if both models PASS >=2 of 3.

| Item | Model | Run grades | Non-PASS | Kept for model | Mean words/half (turn 1) |
|---|---|---|---|---|---|
| 1 | gemini-4-argon-medium | PASS / PASS / PASS | 0/3 | no | 600 |
| 1 | gpt-5.6-sol-high | PARTIAL / PASS / PARTIAL | 2/3 | yes | 141 |
| 2 | gemini-4-argon-medium | FAIL / FAIL / FAIL | 3/3 | yes | 140 |
| 2 | gpt-5.6-sol-high | PARTIAL / FAIL / PARTIAL | 3/3 | yes | 41 |
| 4 | gemini-4-argon-medium | FAIL / FAIL / FAIL | 3/3 | yes | 565 |
| 4 | gpt-5.6-sol-high | PASS / FAIL / PARTIAL | 2/3 | yes | 169 |
| 5 | gemini-4-argon-medium | FAIL / FAIL / FAIL | 3/3 | yes | 427 |
| 5 | gpt-5.6-sol-high | PASS / FAIL / PASS | 1/3 | no | 74 |
| 6 | gemini-4-argon-medium | FAIL / FAIL / FAIL | 3/3 | yes | 126 |
| 6 | gpt-5.6-sol-high | PARTIAL / FAIL / FAIL | 3/3 | yes | 48 |

| Item | Pilot decision |
|---|---|
| 1 | KEEP (split: kept for one model only) |
| 2 | KEEP |
| 4 | KEEP |
| 5 | KEEP (split: kept for one model only) |
| 6 | KEEP |

## Calls
- Total CLI calls logged (incl. retries, correction checks, grading): 136
- Answer calls by model: gemini-4-argon-medium: 42, gpt-5.6-sol-high: 52
- Grader calls: 42
- Calls with a tool call: 14; invalid turns after retry: 4
- Item 5 correction checks: 12 CORRECTED, 0 AGREED
- Prompt echo mismatches: 0

## Tokens
- Reported by CLI JSON: see usage.json

## Caveats
- Items were selected from Scott's own transcripts, not written blind. Screening answers are not reused as pilot data.

## Tokens (from calls.jsonl, all 136 calls)
| Model | Calls | Input (uncached) | Cache read | Cache write | Output |
|---|---|---|---|---|---|
| gemini-4-argon-medium | 42 | 309,835 | 154,836 | 0 | 23,859 |
| gpt-5.6-sol-high | 52 | 246 | 510,868 | 414,430 | 28,776 |
| claude-sonnet-5-thinking-high | 42 | 84 | 558,346 | 187,321 | 37,094 |
| Total | 136 | 310,165 | 1,224,050 | 601,751 | 89,729 |
All input incl. cache = ~2.14M (under the 3M stop line). usage.json undercounts because it ignores cache fields.

## Problems
- 14 GPT-5.6 calls tried an MCP tool lookup (getMcpToolsToolCall) despite --mode ask: 4 on item 1 turn 2 (all fine on retry), 10 on item 4. Four item-4 GPT halves still called a tool on retry and are flagged invalid (run1 half1, run2 half1, run3 both halves). Their text was graded anyway, so GPT item-4 grades are less reliable.
- No parse failures; 0 prompt-echo mismatches; no Thoughts/skill vocabulary in any answer (regex check).
