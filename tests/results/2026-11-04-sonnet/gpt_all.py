"""Grade remaining Sonnet units with gpt-5.6-sol-high; same packets (grading/*.prompt.md), blinding and order from labelmap.json."""
import json, os
from concurrent.futures import ThreadPoolExecutor
import pilot
base = pilot.tok["all_input"]; pilot.CAP = base + 1_900_000  # hard stop 2M new
lm = json.load(open(pilot.OUT / "labelmap.json"))
out = pilot.OUT / "grades-gpt-all.jsonl"
have = {json.loads(l)["packet"] for l in open(out)} if out.exists() else set()
if not have:
    with open(out, "w") as f:
        for l in open(pilot.OUT / "grades-gpt.jsonl"): f.write(json.dumps({**json.loads(l), "reused": True}) + "\n")
    have = {json.loads(l)["packet"] for l in open(out)}
jobs = []
for pid, m in lm.items():
    if pid in have: continue
    meta = {k: m[k] for k in ("item", "model", "cond", "run", "A", "B")}
    jobs.append((pid, pilot.GRADER2, (pilot.OUT / "grading" / f"{pid}.prompt.md").read_text(), meta, "gpt-all"))
print("to grade", len(jobs), "base", base, flush=True)
with ThreadPoolExecutor(6) as ex: list(ex.map(pilot.grade_one, jobs))
print("new input", pilot.tok["all_input"] - base)
