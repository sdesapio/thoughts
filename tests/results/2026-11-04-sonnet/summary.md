# Sonnet run summary 2026-11-04

Test model: claude-sonnet-5-thinking-high. Grader: grok-4.7-medium on all units; gpt-5.6-sol-high on a 20% sample. Sonnet did not grade.


## claude-sonnet-5-thinking-high

| cond | PASS | PARTIAL | FAIL | other |
|---|---|---|---|---|
| N | 0/24 | 10 | 14 | 0 |
| S | 5/24 | 8 | 11 | 0 |
| T | 11/24 | 6 | 7 | 0 |

Per item PASS (of 3), N/S/T:
- item 1: PASS 0/0/2  FAIL 1/2/1
- item 2: PASS 0/0/0  FAIL 3/1/1
- item 23: PASS 0/0/2  FAIL 3/3/1
- item 24: PASS 0/3/3  FAIL 3/0/0
- item 25: PASS 0/0/0  FAIL 0/1/3
- item 4: PASS 0/0/0  FAIL 0/1/0
- item 5: PASS 0/2/3  FAIL 1/0/0
- item 6: PASS 0/0/1  FAIL 3/3/1

Verdict T vs S (primary): PASS (passes 11 vs 5, FAILs 7 vs 11, items where T had fewer passes: 0)

Verdict T vs N (secondary): PASS (passes 11 vs 0, FAILs 7 vs 14, items where T had fewer passes: 0)

## Grader agreement
Grok vs GPT exact agreement: 7/14. Disagreements (grok->gpt): Counter({'FAIL->PARTIAL': 3, 'FAIL->PASS': 2, 'PARTIAL->PASS': 1, 'PARTIAL->FAIL': 1})

## Word counts (mean words per assistant turn)

- claude-sonnet-5-thinking-high N: 290 (n=60)
- claude-sonnet-5-thinking-high S: 296 (n=60)
- claude-sonnet-5-thinking-high T: 494 (n=60)

## Validity
- calls: 290; calls with tool attempts: 0; invalid turns (after retry): 0; item 5 auto-fails (went along): 0
- leak-regex hits in N/S answers: 3 [('claude-sonnet-5-thinking-high', 'N', '1', 1, 2), ('claude-sonnet-5-thinking-high', 'S', '1', 0, 3), ('claude-sonnet-5-thinking-high', 'S', '1', 1, 3)]
- tokens: {'input_incl_cache': 5052619, 'output': 671007}
