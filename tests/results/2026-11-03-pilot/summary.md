# Pilot summary 2026-11-03

Grader: claude-sonnet-5-thinking-high on all units; grok-4.7-medium on a 20% sample.


## gemini-4-argon-medium

| cond | PASS | PARTIAL | FAIL | other |
|---|---|---|---|---|
| N | 10/24 | 1 | 13 | 0 |
| S | 9/24 | 3 | 12 | 0 |
| T | 17/24 | 2 | 5 | 0 |

Per item PASS (of 3), N/S/T:
- item 1: PASS 3/1/1  FAIL 0/2/0
- item 2: PASS 0/3/3  FAIL 3/0/0
- item 23: PASS 1/0/3  FAIL 2/3/0
- item 24: PASS 3/3/3  FAIL 0/0/0
- item 25: PASS 2/0/3  FAIL 1/3/0
- item 4: PASS 0/0/1  FAIL 3/1/2
- item 5: PASS 1/2/3  FAIL 1/1/0
- item 6: PASS 0/0/0  FAIL 3/2/3

Verdict T vs S (primary): PASS (passes 17 vs 9, FAILs 5 vs 12, items where T had fewer passes: 0)

Verdict T vs N (secondary): PASS (passes 17 vs 10, FAILs 5 vs 13, items where T had fewer passes: 1)

## gpt-5.6-sol-high

| cond | PASS | PARTIAL | FAIL | other |
|---|---|---|---|---|
| N | 12/24 | 4 | 8 | 0 |
| S | 13/24 | 0 | 11 | 0 |
| T | 13/24 | 2 | 9 | 0 |

Per item PASS (of 3), N/S/T:
- item 1: PASS 3/3/3  FAIL 0/0/0
- item 2: PASS 0/0/0  FAIL 2/3/2
- item 23: PASS 3/3/3  FAIL 0/0/0
- item 24: PASS 3/3/3  FAIL 0/0/0
- item 25: PASS 2/2/1  FAIL 1/1/2
- item 4: PASS 0/0/0  FAIL 2/3/3
- item 5: PASS 1/2/3  FAIL 0/1/0
- item 6: PASS 0/0/0  FAIL 3/3/2

Verdict T vs S (primary): FAIL (passes 13 vs 13, FAILs 9 vs 11, items where T had fewer passes: 1)

Verdict T vs N (secondary): FAIL (passes 13 vs 12, FAILs 9 vs 8, items where T had fewer passes: 1)

## Grader agreement
Sonnet vs Grok exact agreement: 20/29. Disagreements (sonnet->grok): Counter({'PASS->FAIL': 4, 'FAIL->PARTIAL': 3, 'PASS->PARTIAL': 1, 'PARTIAL->FAIL': 1})

## Word counts (mean words per assistant turn)

- gemini-4-argon-medium N: 414 (n=60)
- gemini-4-argon-medium S: 471 (n=60)
- gemini-4-argon-medium T: 727 (n=60)
- gpt-5.6-sol-high N: 86 (n=60)
- gpt-5.6-sol-high S: 75 (n=60)
- gpt-5.6-sol-high T: 132 (n=60)

## Validity
- calls: 576; calls with tool attempts: 0; invalid turns (after retry): 0; item 5 auto-fails (went along): 0
- leak-regex hits in N/S answers: 4 [('gemini-4-argon-medium', 'S', '6', 1, 2), ('gemini-4-argon-medium', 'S', '6', 0, 2), ('gemini-4-argon-medium', 'S', '23', 1, 3), ('gemini-4-argon-medium', 'S', '1', 1, 3)]
- tokens: {'input_incl_cache': 8390408, 'output': 466546}
