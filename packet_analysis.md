# Packet Analysis - Matching Packets to Layers

**Capture:** `sample_lab_capture.pcap` (12 packets). It is **synthetic lab traffic** produced by `make_sample_pcap.py` using the documentation address 203.0.113.80 and private addresses - no real user data. Open it in Wireshark (*File -> Open*). Checksums are valid (`check_pcap.py`).
*Optional stronger evidence:* capture your own traffic on a lab machine/VM (`ping`, `nslookup`, `curl http://...`), keep only lab traffic, and repeat the table below with real values.

## Scenario
Client **192.168.1.10** resolves `lab.example` using DNS server **192.168.1.1**, opens TCP port 80 on **203.0.113.80**, sends `GET /`, receives `200 OK`, closes.

## Packet-by-packet table

| # | Frame length | Source -> Destination | Protocol | What it is | Layer 2 | Layer 3 | Layer 4 | Layer 7 |
|---|---|---|---|---|---|---|---|---|
| 1 | 71 B | 192.168.1.10 -> 192.168.1.1 | DNS | Query: A record for `lab.example` | Eth: aa:bb:cc:00:00:01 -> aa:bb:cc:00:00:02 | IPv4, proto 17 (UDP) | UDP 53124 -> 53 | DNS, ID 0x1a2b, RD=1 |
| 2 | 87 B | 192.168.1.1 -> 192.168.1.10 | DNS | Response: A = 203.0.113.80, TTL 300 | Eth (reversed) | IPv4, proto 17 | UDP 53 -> 53124 | DNS answer, same ID 0x1a2b |
| 3 | 54 B | 192.168.1.10 -> 203.0.113.80 | TCP | **SYN** (handshake step 1) | Eth -> gateway MAC | IPv4, proto 6 (TCP) | TCP 49152 -> 80, SYN | none (no payload) |
| 4 | 54 B | 203.0.113.80 -> 192.168.1.10 | TCP | **SYN, ACK** (step 2) | Eth | IPv4 | TCP 80 -> 49152, SYN+ACK | none |
| 5 | 54 B | 192.168.1.10 -> 203.0.113.80 | TCP | **ACK** (step 3) - connection established | Eth | IPv4 | TCP ACK | none |
| 6 | 138 B | client -> server | HTTP | `GET / HTTP/1.1`, Host: lab.example | Eth | IPv4 | TCP PSH+ACK, 84 B payload | HTTP request |
| 7 | 54 B | server -> client | TCP | ACK of the request | Eth | IPv4 | TCP ACK | none |
| 8 | 181 B | server -> client | HTTP | `HTTP/1.1 200 OK`, 44-byte HTML body | Eth | IPv4 | TCP PSH+ACK, 127 B payload | HTTP response |
| 9 | 54 B | client -> server | TCP | ACK of the response | Eth | IPv4 | TCP ACK | none |
| 10 | 54 B | server -> client | TCP | **FIN, ACK** (server closes) | Eth | IPv4 | TCP FIN+ACK | none |
| 11 | 54 B | client -> server | TCP | **FIN, ACK** | Eth | IPv4 | TCP FIN+ACK | none |
| 12 | 54 B | server -> client | TCP | final **ACK** | Eth | IPv4 | TCP ACK | none |

## Layer-by-layer walk-through of packet 3 (TCP SYN, 54 bytes)
| Layer | Bytes | Fields |
|---|---|---|
| Layer 1 | - | Not visible in a capture (bits on the wire; frame arrives after preamble) |
| Layer 2 - Ethernet II | 14 | Dst MAC aa:bb:cc:00:00:02 (default gateway), Src MAC aa:bb:cc:00:00:01, EtherType 0x0800 = IPv4 |
| Layer 3 - IPv4 | 20 | Version 4, IHL 5 (20 B), TTL 64, Protocol 6 = TCP, Src 192.168.1.10, Dst 203.0.113.80, header checksum |
| Layer 4 - TCP | 20 | Src port 49152 (ephemeral), Dst port 80 (HTTP), flags = SYN, window 64240, no payload |
| Layer 7 | 0 | Nothing yet - handshake only |
Total = 14 + 20 + 20 = **54 bytes** (matches the capture).

## Observations to point out in the demo
1. **MAC vs IP:** the destination MAC in packets 3, 6 etc. is the *gateway's*, while the destination IP is the *remote server's* - MAC is per hop, IP is end to end.
2. **DNS before TCP:** the client needs the IP before it can connect. DNS uses **UDP/53**; the web connection uses **TCP/80**.
3. **Port roles:** client uses an ephemeral port (49152); the server listens on a well-known port (80).
4. **Handshake:** Wireshark's *Statistics -> Flow Graph* shows SYN, SYN-ACK, ACK. By default Wireshark displays **relative** sequence numbers (starting at 0); raw ISNs in this file are 1000 (client) and 5000 (server).
5. **Encapsulation sizes:** packets 3-5, 7, 9-12 are 54 B = headers only; packets 6 and 8 add HTTP payload.
6. **Useful Wireshark steps:** display filters `dns`, `tcp.flags.syn==1`, `http`, `ip.addr==203.0.113.80`; *Follow -> TCP Stream* shows the HTTP text; expand *Frame / Ethernet II / Internet Protocol / TCP / HTTP* in the Packet Details pane to see the layer stack.

## Practice questions on this capture
1. Which packet completes the TCP handshake? *(5)*
2. Why does the first packet use UDP? *(DNS queries are small, single request/response; UDP avoids handshake cost.)*
3. What is the TTL in packet 3? *(64)*
4. Which field tells the receiving host that the payload is TCP? *(IPv4 Protocol = 6)*
5. Which field tells the NIC that the payload is IPv4? *(EtherType 0x0800)*
