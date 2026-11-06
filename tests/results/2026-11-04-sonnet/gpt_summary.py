import json, collections
L=lambda f:[json.loads(l) for l in open(f)]
ug=lambda g:(g["grade"] or {}).get("unit_grade","NONE")
G={g["packet"]:g for g in L("grades-grok.jsonl")}; P={g["packet"]:g for g in L("grades-gpt-all.jsonl")}
print("nulls gpt",sum(g["grade"] is None for g in P.values()), "n",len(P))
items=["23","24","25","1","2","4","5","6"]
def report(name,f):
    tab={(g["item"],g["cond"],g["run"]):f(pid) for pid,g in G.items()}
    print(f"\n== {name}")
    cnt={}
    for c in "NST":
        v=collections.Counter(x for k,x in tab.items() if k[1]==c); cnt[c]=v; print(c,"PASS",v["PASS"],"PARTIAL",v["PARTIAL"],"FAIL",v["FAIL"])
    worse={"S":0,"N":0}
    for i in items:
        p={c:sum(tab[(i,c,r)]=="PASS" for r in (1,2,3)) for c in "NST"}
        fl={c:sum(tab[(i,c,r)]=="FAIL" for r in (1,2,3)) for c in "NST"}
        for b in "SN": worse[b]+=p["T"]<p[b]
        print(f" item {i}: PASS {p['N']}/{p['S']}/{p['T']} FAIL {fl['N']}/{fl['S']}/{fl['T']}")
    for b in "SN":
        ok=cnt["T"]["PASS"]>cnt[b]["PASS"] and cnt["T"]["FAIL"]<cnt[b]["FAIL"] and worse[b]<=1
        print(f" T vs {b}: {'PASS' if ok else 'FAIL'} passes {cnt['T']['PASS']} vs {cnt[b]['PASS']}, FAILs {cnt['T']['FAIL']} vs {cnt[b]['FAIL']}, worse items {worse[b]}")
    print(" N passed >=2/3 items:",[i for i in items if sum(tab[(i,'N',r)]=="PASS" for r in (1,2,3))>=2])
report("GPT alone",lambda p:ug(P[p]))
# both agree: PASS only if both PASS; FAIL only if both FAIL; else PARTIAL
def both(p):
    a,b=ug(G[p]),ug(P[p])
    return a if a==b else "PARTIAL"
report("Both agree (PASS/FAIL only when both say it; else PARTIAL)",both)
pairs=[(ug(G[p]),ug(P[p])) for p in G]
print("\nagreement",sum(a==b for a,b in pairs),"/",len(pairs),collections.Counter(f"{a}->{b}" for a,b in pairs if a!=b))
for c in "NST": print(c,"agree",sum(ug(G[p])==ug(P[p]) for p in G if G[p]["cond"]==c),"/24")
