# Final Demo Script (5-7 minutes)

Record as a screen-capture video (e.g. OBS / phone screen recorder) and add the link to the README.

| Time | What to show | What to say |
|---|---|---|
| 0:00 | README on GitHub | Problem question and target audience (third-year CSE). |
| 0:30 | `docs/03_layer_notes.md` + courier analogy | "Each layer adds an envelope; IP is the destination city, MAC is the next stop." |
| 1:30 | Terminal: `python3 python/subnet_practice_generator.py -n 5 --level medium --answers` | Generator creates random problems; answers computed with `ipaddress`. |
| 2:30 | Terminal: `python3 subnetting/build_subnetting_set.py` | All 15 hand answers verified - "this is how I caught AI mistakes". |
| 3:30 | Wireshark: open `sample_lab_capture.pcap`, filter `dns`, then `tcp.flags.syn==1`, then Follow TCP Stream | Map packets to layers: DNS over UDP/53, handshake, HTTP, teardown. |
| 5:00 | `verification/verification_report.md` | Hallucination tests, issues found, scores per tool. |
| 6:00 | Presentation slide 6-7 | Workflow and ethics. Close with what you learned. |

**Viva-ready questions:** why MAC changes per hop; difference between segment/packet/frame; how /26 block size is found; why DNS uses UDP; what RFC 9293 replaced.
