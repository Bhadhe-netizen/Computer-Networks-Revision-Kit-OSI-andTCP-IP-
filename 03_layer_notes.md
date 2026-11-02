# Layer Notes - with a Courier / Post-Office Analogy

**The analogy:** You (an application) want to send a parcel (your data) to a friend in another city.

| Layer | What it does (tech) | Courier / post-office analogy | Example |
|---|---|---|---|
| **7 Application** | Gives programs network services; defines message formats | *You decide what to send and write the letter* ("Please send me the notes") | HTTP GET, DNS query |
| **6 Presentation** | Encoding, compression, encryption | *You write in a language both understand and seal it in a tamper-proof envelope* | UTF-8, TLS |
| **5 Session** | Starts, maintains, ends dialogues | *You and your friend agree on a phone call: start, pauses, end* | TLS session, RPC |
| **4 Transport** | End-to-end delivery between processes; reliability (TCP) or speed (UDP); ports | *Registered post vs ordinary post.* Big parcels are split into numbered boxes; the **port** is the person/flat number inside the building | TCP seq numbers, UDP datagram |
| **3 Network** | Logical addressing and routing across networks | *The PIN code and city on the address; sorting offices choose the best route* | IP, ICMP, routers |
| **2 Data Link** | Delivery between neighbouring devices on one link; MAC addresses; error detection | *The local delivery van going from one sorting office to the next, using the street/door number of the next stop only* | Ethernet frame, switch |
| **1 Physical** | Sends raw bits as signals | *The actual roads, trucks and aeroplanes* | cable, Wi-Fi radio |

**Key idea - encapsulation:** each layer puts the parcel inside another envelope with its own label (header). The receiver opens envelopes in reverse order (decapsulation).
**Why IP and MAC both exist:** the IP address is the *final destination* (the friend's address); the MAC address is the *next stop* (the next sorting office). IP stays the same end to end; MAC changes at every hop.

---

## Layer 7/6/5 - Application (TCP/IP: Application)
- Protocols decide the *meaning* of messages. **HTTP** requests a resource; **DNS** converts names to IPs; **DHCP** hands out IP settings.
- In TCP/IP these three OSI layers are merged: the application itself handles formatting, encryption (TLS library) and sessions.
- *Exam tip:* "Which layer does TLS belong to?" - TCP/IP: application; OSI: usually described as presentation (it is a classic grey area; say so).

## Layer 4 - Transport
- **TCP**: connection-oriented, reliable, ordered, flow and congestion control. Handshake: `SYN -> SYN+ACK -> ACK`.
- **UDP**: connectionless, minimal overhead, no guarantee. Good for DNS queries, VoIP, gaming.
- **Ports** (16-bit, 0-65535): well-known 0-1023, registered 1024-49151, dynamic/ephemeral 49152-65535.
- PDU: *segment* (TCP) / *datagram* (UDP).

## Layer 3 - Network
- **IP** gives every interface a logical address and forwards packets hop by hop using routing tables (longest-prefix match).
- **TTL** (hop limit) decreases at every router and stops loops; **ICMP** reports errors (used by `ping`, `traceroute`).
- **Subnetting** divides an address block: `mask -> block size -> network -> broadcast -> hosts`.

## Layer 2 - Data Link
- **Ethernet frame:** Dst MAC (6) | Src MAC (6) | EtherType (2) | Payload (46-1500) | FCS (4).
- **Switches** learn which MAC is on which port. **ARP** asks "who has IP x?" and learns the MAC.

## Layer 1 - Physical
- Bits as electrical, optical or radio signals; defines cables, connectors, voltage/frequency.

---

## Encapsulation example (HTTP request over Ethernet)
```
HTTP data  ->  [TCP hdr | HTTP data]  ->  [IP hdr | TCP seg]  ->  [Eth hdr | IP pkt | FCS]  ->  bits
 App           Segment (port)            Packet (IP)               Frame (MAC)                 Physical
```
Typical minimum header sizes: Ethernet 14 B (+4 FCS), IPv4 20 B, TCP 20 B, UDP 8 B.

## One-page memory aids
- **OSI top-down:** *All People Seem To Need Data Processing* (Application, Presentation, Session, Transport, Network, Data link, Physical).
- **OSI bottom-up:** *Please Do Not Throw Sausage Pizza Away.*
- **PDUs:** *Data - Segment - Packet - Frame - Bits.*
