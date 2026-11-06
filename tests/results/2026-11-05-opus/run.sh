#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
export PAR=1
export PYTHONUNBUFFERED=1
PYTHON="$(command -v python3)"
echo "START $(date) — answers, then Grok 72, then GPT 72; no automatic restoration"
"$PYTHON" pilot.py answers
"$PYTHON" - <<'CHECK'
import json
from pathlib import Path
p=Path('answers.jsonl'); a=[json.loads(x) for x in p.read_text().splitlines()]
keys={(r['item'],r['half'],r['model'],r['cond'],r['run']) for r in a}
assert len(a)==len(keys)==144, (len(a),len(keys))
assert not any(t.get('invalid') or t.get('tools') or t.get('echo_ok') is not True for r in a for t in r['turns']), 'Invalid/contaminated answers; grading stopped'
print('ANSWERS VERIFIED: 144 half chats / 72 paired units')
CHECK
"$PYTHON" pilot.py grade grok
"$PYTHON" pilot.py grade gpt
"$PYTHON" - <<'CHECK'
import json
from pathlib import Path
for f in ['grades-grok.jsonl','grades-gpt.jsonl']:
 rows=[json.loads(x) for x in Path(f).read_text().splitlines()]
 assert len(rows)==72 and len({r['packet'] for r in rows})==72 and all(r['grade'] for r in rows), f
calls=[json.loads(x) for x in Path('calls.jsonl').read_text().splitlines()]
u=sum(sum((r.get('usage') or {}).get(k,0) for k in ['inputTokens','cacheReadTokens','cacheWriteTokens']) for r in calls)
assert u<=9000000, u
Path('COMPLETE.txt').write_text(f'Answers and both 72-unit grading passes complete. Input including cache: {u}. Skills remain in holding for deliberate restoration.\n')
print('COMPLETE',u)
CHECK
echo "FINISHED $(date) — restore skills only after reviewing COMPLETE.txt"
