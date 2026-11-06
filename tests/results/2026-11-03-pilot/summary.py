import json, re, collections, pathlib
OUT = pathlib.Path(__file__).parent
L = lambda f: [json.loads(l) for l in open(OUT / f)] if (OUT / f).exists() else []
S = L("grades-sonnet.jsonl"); G = L("grades-grok.jsonl"); A = L("answers.jsonl"); C = L("calls.jsonl")
ug = lambda g: (g["grade"] or {}).get("unit_grade", "NONE")
models = sorted({g["model"] for g in S}); items = []
for g in S:
    if g["item"] not in items: items.append(g["item"])
o = ["# Pilot summary 2026-11-03\n", "Grader: claude-sonnet-5-thinking-high on all units; grok-4.7-medium on a 20% sample.\n"]
tab = {}
for g in S: tab[(g["model"], g["cond"], g["item"], g["run"])] = ug(g)
for m in models:
    o.append(f"\n## {m}\n\n| cond | PASS | PARTIAL | FAIL | other |\n|---|---|---|---|---|")
    cnt = {}
    for c in "NST":
        v = collections.Counter(x for k, x in tab.items() if k[0] == m and k[1] == c); cnt[c] = v
        o.append(f"| {c} | {v['PASS']}/24 | {v['PARTIAL']} | {v['FAIL']} | {sum(v.values())-v['PASS']-v['PARTIAL']-v['FAIL']} |")
    o.append("\nPer item PASS (of 3), N/S/T:")
    worse = {"S": 0, "N": 0}
    for i in items:
        p = {c: sum(tab.get((m, c, i, r)) == "PASS" for r in (1, 2, 3)) for c in "NST"}
        f = {c: sum(tab.get((m, c, i, r)) == "FAIL" for r in (1, 2, 3)) for c in "NST"}
        for b in "SN":
            if p["T"] < p[b]: worse[b] += 1
        o.append(f"- item {i}: PASS {p['N']}/{p['S']}/{p['T']}  FAIL {f['N']}/{f['S']}/{f['T']}")
    for b, lab in (("S", "primary"), ("N", "secondary")):
        ok = cnt["T"]["PASS"] > cnt[b]["PASS"] and cnt["T"]["FAIL"] < cnt[b]["FAIL"] and worse[b] <= 1
        o.append(f"\nVerdict T vs {b} ({lab}): {'PASS' if ok else 'FAIL'} (passes {cnt['T']['PASS']} vs {cnt[b]['PASS']}, FAILs {cnt['T']['FAIL']} vs {cnt[b]['FAIL']}, items where T had fewer passes: {worse[b]})")
sg = {g["packet"]: ug(g) for g in S}; pairs = [(sg.get(g["packet"]), ug(g)) for g in G]
ag = sum(a == b for a, b in pairs)
o.append(f"\n## Grader agreement\nSonnet vs Grok exact agreement: {ag}/{len(pairs)}. Disagreements (sonnet->grok): {collections.Counter(f'{a}->{b}' for a,b in pairs if a!=b)}")
o.append("\n## Word counts (mean words per assistant turn)\n")
wc = collections.defaultdict(list)
for a in A:
    for t in a["turns"]: wc[(a["model"], a["cond"])].append(len((t["assistant"] or "").split()))
for k in sorted(wc): o.append(f"- {k[0]} {k[1]}: {sum(wc[k])/len(wc[k]):.0f} (n={len(wc[k])})")
leak = re.compile(r"thoughts skill|SKILL\.md|<skill>|steelman|disconfirm|what would change (my|this)", re.I)
leaks = [(a["model"], a["cond"], a["item"], a["half"], a["run"]) for a in A if a["cond"] in "NS" for t in a["turns"] if leak.search(t["assistant"] or "")]
inv = sum(t["invalid"] for a in A for t in a["turns"]); tc = sum(bool(c["tools"]) for c in C); af = sum(a["auto_fail"] for a in A)
tot = collections.Counter()
for c in C:
    u = c["usage"] or {}; tot["input_incl_cache"] += u.get("inputTokens",0)+u.get("cacheReadTokens",0)+u.get("cacheWriteTokens",0); tot["output"] += u.get("outputTokens",0)
o.append(f"\n## Validity\n- calls: {len(C)}; calls with tool attempts: {tc}; invalid turns (after retry): {inv}; item 5 auto-fails (went along): {af}\n- leak-regex hits in N/S answers: {len(leaks)} {leaks[:10]}\n- tokens: {dict(tot)}")
(OUT / "summary.md").write_text("\n".join(o) + "\n"); print("\n".join(o))
