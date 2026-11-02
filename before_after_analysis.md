# Before / After Analysis

## A. Prompt improvement (before vs after)

| | Before (weak prompt) | After (engineered prompt) |
|---|---|---|
| Prompt | "Explain subnetting." | "You are a networking tutor for third-year CSE students. Explain subnetting using the block-size method with ONE worked example (192.168.1.77/26). Show each step: mask, block size, network, broadcast, host range, usable hosts. Then give 3 practice problems and list any assumptions. If unsure, say UNSURE." |
| Typical weakness / strength | Long generic definition, no worked example, no check possible | Structured, checkable steps, right level, practice included |
| Hallucination risk | Higher (no constraints, no uncertainty rule) | Lower (explicit steps + "UNSURE" rule + external verification) |
| Verifiability | Hard | Easy (every number can be re-run in Python) |

**Scoring rubric (1-5):** Accuracy - Level fit - Structure - Verifiability. *Run both prompts in your chosen tool, paste the real outputs into `verification/screenshots/`, and fill your scores:*

| Criterion | Before | After |
|---|---|---|
| Accuracy | _/5 | _/5 |
| Level fit | _/5 | _/5 |
| Structure | _/5 | _/5 |
| Verifiability | _/5 | _/5 |

## B. Content improvement (AI draft vs verified final) - changes actually made in this project

| Artifact | Before (first draft) | After (verified) |
|---|---|---|
| Subnetting set | Answers worked by hand only | Every answer asserted against `ipaddress`; log saved |
| Quiz key | 9 of 15 correct answers were "B" | Evenly distributed; key re-checked against option text |
| DNS diagram | Real-looking public IP in example | Neutral wording; documentation address used elsewhere |
| TCP reference | Risk of citing RFC 793 | RFC 9293 cited as current |
| Packet analysis | Descriptive text only | Real `.pcap` created, structure and checksums validated, frame sizes reconciled (909 bytes total) |
| Generator | Hand-computed answers possible | Answers computed by `ipaddress`, private ranges only |

## C. Learning impact
Using the generator + quiz, a student can self-test in minutes, find weak spots (e.g. block-boundary mistakes), and re-test. *(Optional: measure your own score on Q1-Q15 before and after studying the notes and record it here.)*

| Attempt | Score /15 | Weak topics |
|---|---|---|
| Before notes | | |
| After notes | | |
