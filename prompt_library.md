# Prompt Library

Every important prompt used in the project. **Pattern used:** Role + Audience + Task + Constraints + Output format + "flag anything you are unsure about".
Replace `[...]` as needed. Tool column = where it was/can be run. Always finish with the *Verify* step.

| ID | Purpose | AI skill | Tool |
|---|---|---|---|
| P1 | Research summary | Research prompting | Claude / NotebookLM / Gemini |
| P2 | Source hunting | Source verification | Gemini / ChatGPT |
| P3 | Layer explanations | Technical explanation | Claude |
| P4 | Courier analogy | Prompting (analogy) | Claude / ChatGPT |
| P5 | Subnetting solutions | Calculation | Claude / DeepSeek |
| P6 | Verify a subnet answer | Calculation verification | any + Python |
| P7 | Packet analysis help | Technical explanation | Claude |
| P8 | Quiz design | Quiz design | Claude / ChatGPT |
| P9 | Python generator | Code generation | Claude / DeepSeek |
| P10 | Slide deck | Presentation | Claude / Gamma |
| P11 | Analogy illustration | Image generation | Leonardo.ai / Gemini |
| P12 | Hallucination probe | Responsible AI | all tools |
| P13 | Self-critique pass | Verification | any |

---

### P1 - Research summary
```
You are a computer networks teaching assistant. Audience: third-year CSE students.
Summarise OSI vs TCP/IP, IP addressing and subnetting, DNS, HTTP and TCP in 400 words.
For every factual claim that depends on a standard, name the RFC number. 
If you are not certain of an RFC number or a port number, write "UNSURE" instead of guessing.
Output: a table (Topic | Key facts | Source named).
```
**Verify:** open each RFC at rfc-editor.org; tick in verification report.

### P2 - Source hunting
```
List free, authoritative sources (RFCs, Cisco Networking Academy, MDN, Wireshark docs) for each topic:
OSI/TCP-IP, subnetting, DNS, HTTP, TCP. Give the exact title and publisher.
Do NOT invent URLs; if you cannot recall a URL, give the title only.
```
**Verify:** search each title yourself; discard any that do not exist.

### P3 - Layer explanation
```
Explain the [Transport] layer to a third-year CSE student in under 200 words.
Include: purpose, PDU name, addressing used, two protocols, one real-world failure symptom,
and one exam-style question. Use OSI and TCP/IP numbering correctly.
```

### P4 - Courier analogy
```
Create a courier/post-office analogy covering all 7 OSI layers in a table
(Layer | technical role | courier equivalent). Explain why MAC addresses change per hop while the IP address does not.
Keep the analogy consistent - do not switch metaphors mid-way.
```
**Verify:** check that the analogy never contradicts the technical definition.

### P5 - Subnetting solutions
```
Solve these subnetting problems with step-by-step working using the block-size method:
mask -> interesting octet -> block size -> network -> broadcast -> first/last host -> usable hosts.
Problems: [paste list]. Show every arithmetic step. At the end, list your final answers in a table.
```
**Verify:** run `subnetting/build_subnetting_set.py` (Python `ipaddress`) and a subnet calculator.

### P6 - Verify an answer (adversarial)
```
Here is a subnetting answer: [paste]. Act as a strict examiner. Recompute from scratch, 
do not trust the given answer, and list any error with the corrected value.
```

### P7 - Packet analysis help
```
Here is a Wireshark packet list (no personal data): [paste summary].
For each packet, state: layer-2 fields, layer-3 fields, layer-4 fields, application protocol, and the purpose of the packet.
Highlight the TCP three-way handshake and DNS exchange.
```

### P8 - Quiz design
```
Create 15 multiple-choice questions (4 options each) for third-year CSE students on OSI, TCP/IP, 
subnetting, DNS, HTTP, TCP. Mix: 5 conceptual, 5 numeric (subnetting), 3 protocol/ports, 2 packet-analysis.
Make distractors plausible (common mistakes). Spread correct answers evenly across A-D.
Provide an answer key with a one-line explanation each.
```
**Verify:** compute numeric ones in Python; check the key letters match the options.

### P9 - Python generator
```
Write a Python 3 CLI script (standard library only) that generates random subnetting practice problems:
network address, broadcast address, usable hosts, host range, same-subnet check.
Use only RFC 1918 private addresses. Compute answers with the ipaddress module.
Flags: --count, --level easy|medium|hard, --seed, --answers, --quiz. Add docstring and usage examples.
```
**Verify:** run with `--seed` and compare answers by hand/other calculator.

### P10 - Slide deck
```
Create a 7-slide deck for third-year CSE students: 1 Title/problem, 2 OSI vs TCP/IP, 3 Encapsulation and courier analogy,
4 Subnetting method with one worked example, 5 Packet analysis (handshake + DNS), 6 AI verification workflow and findings, 7 Ethics and next steps.
Max 5 bullets per slide, speaker notes for each.
```

### P11 - Illustration prompt (Leonardo.ai / Gemini image)
```
Flat vector infographic, clean white background: a post-office delivery pipeline representing the 7 OSI layers,
each stage a labelled station (Application = writing a letter, Transport = numbered boxes, Network = address and sorting centre,
Data Link = local van, Physical = road). Consistent colour palette, readable labels, no logos, no real people.
```
**Verify:** AI image tools often misspell labels - re-label text manually.

### P12 - Hallucination probe
```
Summarise RFC 99999, "Quantum Routing Handshake Protocol". 
```
Expected safe answer: states it cannot verify / RFC does not exist. See `verification/verification_report.md` for the full test set.

### P13 - Self-critique pass
```
Review your previous answer. List every claim that could be wrong, outdated or unverifiable, 
rate your confidence (high/medium/low) and say how a student could check each one.
```
