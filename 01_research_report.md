# Research Report - OSI, TCP/IP, Addressing, DNS, HTTP and TCP

## 1. Purpose and audience
Third-year CSE students need to connect *theory* (layers) to *practice* (packets, subnets, DNS lookups). This report summarises what reliable sources say and how AI tools can speed up revision **if** their output is verified.

## 2. Method
1. Used AI research assistants (Claude, NotebookLM, plus at least two others) to summarise topics.
2. Collected primary sources (RFCs, Cisco Networking Academy free pages, MDN, Wireshark docs).
3. Checked each AI claim against a primary source; numeric claims checked with Python `ipaddress`.
4. Recorded errors and prompt improvements in `verification/`.

## 3. Findings by topic

### 3.1 OSI vs TCP/IP
- **OSI (ISO/IEC 7498-1)** is a 7-layer *reference model*: Physical, Data Link, Network, Transport, Session, Presentation, Application.
- **TCP/IP** is the *implemented* suite. RFC 1122 describes four layers (Link, Internet, Transport, Application); many textbooks teach a 5-layer hybrid by splitting Link into Data Link + Physical.
- OSI Session + Presentation + Application roughly map to TCP/IP **Application**.
- Each layer adds a header on the sender (**encapsulation**) and removes it at the receiver (**decapsulation**). PDU names: data -> segment (TCP) / datagram (UDP) -> packet -> frame -> bits.

### 3.2 IP addressing and subnetting
- IPv4 = 32 bits (RFC 791); IPv6 = 128 bits (RFC 8200).
- Classless addressing (CIDR, RFC 4632) uses a prefix length (/n). Usable hosts = 2^(32-n) - 2 (network and broadcast excluded; /31 and /32 are special cases).
- Private ranges (RFC 1918): 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. Loopback 127.0.0.0/8. Link-local 169.254.0.0/16. Documentation ranges (RFC 5737): 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24.
- Techniques: block-size method, VLSM (allocate largest subnet first), route summarisation.

### 3.3 DNS
- Hierarchical, distributed database (RFC 1034/1035). Resolution path: stub resolver -> recursive resolver -> root -> TLD -> authoritative server.
- Common records: A, AAAA, CNAME, MX, NS, TXT, PTR. Uses port 53 (UDP normally; TCP for large responses/zone transfers). Responses carry a TTL for caching.

### 3.4 HTTP
- Application-layer request/response protocol (RFC 9110 semantics, RFC 9112 HTTP/1.1). Methods: GET, POST, PUT, DELETE, HEAD, OPTIONS. Status classes: 1xx info, 2xx success, 3xx redirect, 4xx client error, 5xx server error.
- HTTP/1.1 and HTTP/2 run over TCP; HTTP/3 runs over QUIC (UDP). HTTPS = HTTP inside TLS (port 443).

### 3.5 TCP (and UDP)
- Connection-oriented, reliable, ordered byte stream (RFC 9293, which replaces RFC 793). Three-way handshake (SYN, SYN-ACK, ACK), sequence/ack numbers, sliding-window flow control, retransmission, congestion control, four-way close (FIN/ACK).
- UDP (RFC 768): connectionless, 8-byte header, no reliability - used by DNS queries, DHCP, streaming, QUIC.

## 4. Source list and reliability

| Source | Type | Used for | Reliability |
|---|---|---|---|
| RFC 791 (IP), RFC 792 (ICMP), RFC 826 (ARP) | IETF standard | addressing, ICMP, ARP | Primary / high |
| RFC 768 (UDP), RFC 9293 (TCP) | IETF standard | transport | Primary / high |
| RFC 1034, RFC 1035 (DNS) | IETF standard | DNS | Primary / high |
| RFC 9110, RFC 9112 (HTTP) | IETF standard | HTTP | Primary / high |
| RFC 1918, RFC 4632, RFC 5737, RFC 8200 | IETF standard | private ranges, CIDR, doc ranges, IPv6 | Primary / high |
| RFC 1122 | IETF standard | TCP/IP layer model | Primary / high |
| Cisco Networking Academy free learning pages | Vendor education | layer/subnetting explanations | Secondary / high |
| MDN Web Docs - "HTTP" and "How the web works" | Mozilla docs | HTTP | Secondary / high |
| Wireshark User's Guide + sample captures wiki | Official tool docs | packet analysis | Secondary / high |
| AI chat answers (any) | Generated | drafts only | **Unverified until checked** |

RFCs are at `https://www.rfc-editor.org/rfc/rfcNNNN`. *(Open each link yourself before submission and tick it in the verification report.)*

## 5. How AI helped, and where it needs supervision

| Helpful | Risky |
|---|---|
| Explaining layers with analogies at the right level | Confidently wrong subnet arithmetic (off-by-one on usable hosts, wrong block boundary) |
| Generating many practice problems quickly | Mixing OSI and TCP/IP layer counts or putting protocols in the wrong layer |
| Writing code (generator) and quiz distractors | Outdated facts (RFC 793 vs 9293, HTTP/3, deprecated TLS versions) |
| Summarising long documents (NotebookLM) | Invented RFC numbers, port numbers or flags |

## 6. Conclusion
AI is an excellent *tutor and drafter* for networking revision when combined with (1) primary sources, (2) deterministic tools (Python/subnet calculators/Wireshark) and (3) a documented verification step.
