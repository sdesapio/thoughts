# What each condition saw (2026-11-04 Sonnet run)

Identical to ../2026-11-03-pilot/CONDITIONS.md except: test model claude-sonnet-5-thinking-high only; primary grader grok-4.7-medium on all 72 units (also runs the item-5 correction check); second grader gpt-5.6-sol-high initially on a 20% sample (14 units, rng seed 20261103; see grades-gpt.jsonl), then extended to all 72 units (grades-gpt-all.jsonl; gpt-summary.txt). Sonnet graded nothing.
Same cwd ~/_thoughts-screen-cwd (deny Shell, Read, Write, WebFetch, Mcp; rule "Answer in text only. Do not use any tools."), same CLI flags (agent -p --output-format stream-json --mode ask --trust), same HEADER/N/S/T builders. prompts/ is byte-identical to the pilot's prompts/ (diff -r clean). Skill: skill-772db52.md copied from the pilot.
Load check (23a, Sonnet): N/S/T all 0 tools, echo match, input incl. cache 16,236 / 16,261 / 23,453.
Hard cap 6.6M input incl. cache in script (Scott's hard stop 7M).

## Portable rerun note

The original run used a deny-tools working directory at `~/_thoughts-screen-cwd` and the Cursor CLI as `agent` on PATH (historically `~/.local/bin/agent`). For a rerun, set `AGENT_BIN` and `RUN_CWD`, or use `tests/rerun.sh`, which creates a neutral deny-tools cwd. Holding-dir paths in this file are historical and machine-local; they are not required to read the published answers and grades.
