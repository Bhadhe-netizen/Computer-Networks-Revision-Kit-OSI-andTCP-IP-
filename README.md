# Computer Networks Revision Kit (OSI and TCP/IP)

**Capstone 14 - CSE Capstone Projects, Free AI Tools Edition**

> **Project question:** How can AI help students master networking layers, addressing and protocols through examples and labs?

**Target audience:** third-year CSE students revising for Computer Networks exams and labs.
**Author:** _<your name, roll no., college>_  |  **Date:** October 2026

---

## What is in this repo (maps 1-to-1 to the "Final submission" list)

| # | Required deliverable | File / folder |
|---|---|---|
| 1 | Research report | [`docs/01_research_report.md`](docs/01_research_report.md) |
| 2 | Layer-by-layer protocol checklist | [`docs/02_protocol_checklist.md`](docs/02_protocol_checklist.md) |
| 3 | Layer notes (with courier/post-office analogy) | [`docs/03_layer_notes.md`](docs/03_layer_notes.md), diagrams in [`diagrams/diagrams.md`](diagrams/diagrams.md) |
| 4 | Subnetting set (15 problems) | [`subnetting/subnetting_set.md`](subnetting/subnetting_set.md) |
| 5 | Packet analysis (Wireshark) | [`packet_analysis/packet_analysis.md`](packet_analysis/packet_analysis.md) + `sample_lab_capture.pcap` |
| 6 | Quiz (15 Qs) and answer key | [`quiz/quiz_and_answer_key.md`](quiz/quiz_and_answer_key.md) |
| 7 | Presentation (7 slides) | [`presentation/OSI_TCPIP_Revision_Kit.pptx`](presentation/OSI_TCPIP_Revision_Kit.pptx) |
| 8 | Python generator | [`python/subnet_practice_generator.py`](python/subnet_practice_generator.py) |
| 9 | Prompt library | [`prompts/prompt_library.md`](prompts/prompt_library.md) |
| 10 | Verification report | [`verification/verification_report.md`](verification/verification_report.md) |
| 11 | Before/after analysis | [`verification/before_after_analysis.md`](verification/before_after_analysis.md) |
| 12 | Ethics statement | [`docs/ethics.md`](docs/ethics.md) |
| 13 | Final demo script | [`DEMO.md`](DEMO.md) |

## Quick start

```bash
git clone <your-repo-url> && cd osi-tcpip-revision-kit
python3 --version                       # Python 3.8+ ; no external packages needed

# 1. Re-verify all 15 subnetting answers (fails loudly if any is wrong)
python3 subnetting/build_subnetting_set.py

# 2. Practice with random problems
python3 python/subnet_practice_generator.py -n 5 --level medium --answers
python3 python/subnet_practice_generator.py --quiz -n 5

# 3. Rebuild the sample capture and open it in Wireshark
python3 packet_analysis/make_sample_pcap.py
python3 packet_analysis/check_pcap.py
```

## AI skills demonstrated (required: at least 6 of Topics 1-9)

Prompting - technical explanation - calculation verification - quiz design - presentation design - code generation / automation - research with source checking - hallucination testing - responsible AI.

## AI tools used (required: at least 4 free tools)

| Tool | Used for |
|---|---|
| Claude | drafting notes, subnetting solutions, quiz, Python generator, slide deck |
| _ChatGPT / Gemini / DeepSeek_ | cross-checking answers and hallucination tests (see verification report) |
| _NotebookLM_ | summarising RFC/Cisco/Mozilla sources into the research summary |
| _Gamma / Leonardo.ai_ | optional deck polish / analogy illustrations |
| Wireshark + Python | packet capture analysis, `ipaddress` verification |

## Honest-use note
AI produced first drafts. Numeric answers were verified with Python's `ipaddress` module and a subnet calculator; protocol facts were checked against RFCs and vendor/MDN documentation. See `verification/` and `docs/ethics.md`.

---

## Before you submit - things only YOU can do (about 1-2 hours)

- [ ] Put your name, roll number and college in this README and on slide 1 (`presentation/build_deck.js`, then `node presentation/build_deck.js`, or edit the .pptx directly).
- [ ] Run the 12 tests in `verification/verification_report.md` on **at least 4 free AI tools**; fill the table and add screenshots in `verification/screenshots/`. Do not alter outputs.
- [ ] Run the before/after prompts in `verification/before_after_analysis.md` and fill in your scores.
- [ ] Open every RFC/Cisco/MDN/Wireshark link and tick the source checklist.
- [ ] Open `sample_lab_capture.pcap` in Wireshark and take 3 screenshots (DNS, handshake, HTTP stream) into `packet_analysis/screenshots/`. Optionally capture your own lab traffic.
- [ ] Generate the analogy illustration with Leonardo.ai or Gemini (prompt P11) and save it in `diagrams/`.
- [ ] Try NotebookLM or Gamma if you list them under tools - only list tools you really used.
- [ ] Record the 5-7 minute demo following `DEMO.md` and add the link here.
- [ ] Read everything once so you can explain it in the viva.

## Publishing to GitHub
```bash
git init && git add . && git commit -m "Capstone 14: Computer Networks Revision Kit"
git branch -M main
git remote add origin https://github.com/<username>/osi-tcpip-revision-kit.git
git push -u origin main
```
