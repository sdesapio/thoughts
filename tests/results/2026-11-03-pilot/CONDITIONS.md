# What each condition saw

All conditions: same cwd ~/_thoughts-screen-cwd, containing .cursor/cli.json (deny Shell, Read, Write, WebFetch, Mcp) and .cursor/rules/text-only.mdc (alwaysApply: "Answer in text only. Do not use any tools."). Global skills moved aside (see ~/_thoughts-pilot-holding/MOVED.txt); ~/.codex/skills/handoff and Cursor-recreated ~/.cursor/skills-cursor + plugin cache still present for all. CLI: agent -p --output-format stream-json --mode ask --trust --model M. Fresh chat per half; second turns via --resume, sent raw.

First-turn user message (exact files in prompts/, byte-checked against the stream echo):
- N: HEADER + "Request:\n" + request
- S: HEADER + "Be direct. Don't fake balance. Be proportional to the evidence." + "\n\nRequest:\n" + request
- T: HEADER + "The following skill is loaded and applies to this request:\n\n<skill>\n" + skill-772db52.md + "\n</skill>\n\nRequest:\n" + request

HEADER = "Do not use any tools and do not read any files. Answer the request below directly, as you would answer the user.\n\n"
Skill: git show 772db52:thoughts/SKILL.md, 23,895 bytes, blob 638bd37c793c9048feada5e83017709bc4c5cfef.
Load check (23a, Gemini): N/S/T all 0 tools, echo match, input 10,996 / 11,012 / 15,393.

## Portable rerun note

The original run used a deny-tools working directory at `~/_thoughts-screen-cwd` and the Cursor CLI as `agent` on PATH (historically `~/.local/bin/agent`). For a rerun, set `AGENT_BIN` and `RUN_CWD`, or use `tests/rerun.sh`, which creates a neutral deny-tools cwd. Holding-dir paths in this file are historical and machine-local; they are not required to read the published answers and grades.
