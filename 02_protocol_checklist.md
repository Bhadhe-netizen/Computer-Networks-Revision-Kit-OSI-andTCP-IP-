# Layer-by-Layer Protocol Checklist

Tick each item when you can explain it **and** find it in a packet or lab. (`- [ ]` boxes render as check-boxes on GitHub.)

| OSI # | OSI layer | TCP/IP layer | PDU | Addressing | Key protocols / standards | Devices |
|---|---|---|---|---|---|---|
| 7 | Application | Application | Data | - (ports identify services) | HTTP/HTTPS, DNS, DHCP, SMTP, IMAP, FTP, SSH, Telnet | - |
| 6 | Presentation | Application | Data | - | TLS/SSL, character encodings (UTF-8), MIME, compression | - |
| 5 | Session | Application | Data | - | Session handling in TLS/RPC/NetBIOS | - |
| 4 | Transport | Transport | Segment / Datagram | Port numbers | TCP, UDP, (QUIC over UDP) | Firewalls (L4), load balancers |
| 3 | Network | Internet | Packet | IP address | IPv4, IPv6, ICMP, (ARP sits between 2 and 3), OSPF/BGP | Router, L3 switch |
| 2 | Data Link | Link | Frame | MAC address | Ethernet (802.3), Wi-Fi (802.11), ARP, VLAN (802.1Q), PPP | Switch, bridge, access point |
| 1 | Physical | Link | Bits | - | Cables, fibre, radio, signalling | Hub, repeater, NIC, cable |

## Checklist per layer

### Application layer (7/6/5)
- [ ] Explain client-server request/response.
- [ ] HTTP: methods (GET/POST/PUT/DELETE), status classes (1xx-5xx), headers (`Host`, `Content-Type`).
- [ ] DNS: record types A, AAAA, CNAME, MX, NS, TXT, PTR; recursive vs authoritative.
- [ ] DHCP: DORA (Discover, Offer, Request, Ack), UDP 67/68.
- [ ] Well-known ports: HTTP 80, HTTPS 443, DNS 53, SSH 22, FTP 21, SMTP 25, DHCP 67/68.
- [ ] TLS provides encryption/authentication (Presentation-like role).

### Transport layer (4)
- [ ] TCP vs UDP comparison (reliability, ordering, header size 20+ vs 8 bytes).
- [ ] TCP three-way handshake and four-way close; flags SYN, ACK, FIN, RST, PSH.
- [ ] Sequence and acknowledgement numbers; window size (flow control).
- [ ] Congestion control idea (slow start, congestion avoidance).
- [ ] Ports: source (ephemeral) vs destination (well-known); socket = IP:port.

### Network layer (3)
- [ ] IPv4 header fields: version, IHL, TTL, protocol, source/destination, checksum.
- [ ] IPv4 vs IPv6 (32 vs 128 bits).
- [ ] Subnet mask, CIDR, network/broadcast/host range, VLSM, summarisation.
- [ ] Private vs public (RFC 1918), NAT, default gateway.
- [ ] ICMP: ping (echo), traceroute (TTL exceeded), destination unreachable.
- [ ] Routing basics: routing table, longest-prefix match.

### Data Link layer (2)
- [ ] Ethernet frame: dst MAC, src MAC, EtherType, payload (46-1500 B), FCS.
- [ ] MAC address (48 bits) vs IP address.
- [ ] ARP: IP -> MAC on the local network.
- [ ] Switch learns MACs (CAM table); VLAN idea.
- [ ] MTU 1500 bytes for Ethernet.

### Physical layer (1)
- [ ] Media: twisted pair, fibre, wireless; bit encoding; bandwidth vs throughput vs latency.

## End-to-end flow checklist ("what happens when I open a website?")
- [ ] 1. Browser checks cache -> DNS lookup (UDP 53).
- [ ] 2. ARP for the default gateway's MAC (if not cached).
- [ ] 3. TCP three-way handshake to port 80/443.
- [ ] 4. (HTTPS) TLS handshake.
- [ ] 5. HTTP request -> response.
- [ ] 6. TCP close (FIN/ACK).
