# Claude Opus 4.6 comparison — 2026-11-05

- Answer model: `claude-4.6-opus-high-thinking` only.
- Same 8 mirrored pairs, N/S/T conditions, 3 runs: 72 paired units / 144 half-chat records, plus follow-up turns and item-5 correction checks as specified by the original harness.
- Same ITEMS, ORDER, CONDS, ONELINER, HEADER and prompt builders as the Sonnet runner. Tested skill: `skill-772db52.md`, copied unchanged from Sonnet.
- Primary blind grader: `grok-4.7-medium`, all 72 units after answers; also original item-5 correction checks during answers. Second blind grader: `gpt-5.6-sol-high`, all 72 after primary grading. No Opus grading.
- Same cwd `~/_thoughts-screen-cwd`: deny Shell(*), Read(**), Write(**), WebFetch(*), Mcp(*:*); always-applied rule: “Answer in text only. Do not use any tools.” Tools disabled in comparison runs. CLI flags: `agent -p --output-format stream-json --mode ask --trust --model MODEL`; resumed follow-up sessions unchanged.
- Global skills/rules/plugin cache moved, not copied, to `~/_thoughts-opus-holding/`; restoration manifest `MOVED.txt`. Do not restore before answers AND grading finish (unless explicitly stopped). Recreated cache/skills directories will be noted, not repeatedly removed.
- Hard input cap: 9,000,000 including inputTokens + cacheReadTokens + cacheWriteTokens, accumulated across all logged calls (load check, answers, correction checks, grading, retries). Single-call execution (`PAR=1`), 500,000-token admission headroom: no new call admitted after 8,500,000 used. Stop rather than extend the approved budget. CLI usage arrives after each call; the headroom guards in-flight usage.
- Load check: item 23a, N/S/T; require zero tool attempts, exact prompt echo, valid answer.
- No commits, pushes, or publication. October folders excluded and untouched.

## Load-check result
23a N/S/T passed: zero tool attempts, exact echo, valid answers. Input including cache respectively: 11935, 11951, 16691. Total 40577. See loadcheck.log and calls.jsonl.

## Portable rerun note

The original run used a deny-tools working directory at `~/_thoughts-screen-cwd` and the Cursor CLI as `agent` on PATH (historically `~/.local/bin/agent`). For a rerun, set `AGENT_BIN` and `RUN_CWD`, or use `tests/rerun.sh`, which creates a neutral deny-tools cwd. Holding-dir paths in this file are historical and machine-local; they are not required to read the published answers and grades.
