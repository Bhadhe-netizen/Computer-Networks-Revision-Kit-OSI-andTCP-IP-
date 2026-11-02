# Diagrams (Mermaid - render automatically on GitHub)

## 1. OSI vs TCP/IP mapping
```mermaid
flowchart LR
  subgraph OSI
    A7[7 Application]:::o --> A6[6 Presentation]:::o --> A5[5 Session]:::o --> A4[4 Transport]:::o --> A3[3 Network]:::o --> A2[2 Data Link]:::o --> A1[1 Physical]:::o
  end
  subgraph TCPIP[TCP/IP]
    T4[Application]:::t --> T3[Transport]:::t --> T2[Internet]:::t --> T1[Link]:::t
  end
  A7 -.-> T4
  A6 -.-> T4
  A5 -.-> T4
  A4 -.-> T3
  A3 -.-> T2
  A2 -.-> T1
  A1 -.-> T1
  classDef o fill:#dbeafe,stroke:#1d4ed8,color:#0f172a;
  classDef t fill:#dcfce7,stroke:#15803d,color:#0f172a;
```

## 2. Encapsulation
```mermaid
flowchart TB
  D[Application data<br/>HTTP GET /] --> S[TCP segment<br/>+ TCP header: ports, seq, flags]
  S --> P[IP packet<br/>+ IP header: src/dst IP, TTL]
  P --> F[Ethernet frame<br/>+ Eth header: src/dst MAC, + FCS]
  F --> B[Bits on the wire]
```

## 3. TCP three-way handshake and HTTP exchange (matches sample capture)
```mermaid
sequenceDiagram
  participant C as Client 192.168.1.10
  participant S as Server 203.0.113.80
  C->>S: SYN (seq=x)
  S->>C: SYN+ACK (seq=y, ack=x+1)
  C->>S: ACK (ack=y+1)
  C->>S: HTTP GET / (PSH,ACK)
  S->>C: ACK
  S->>C: HTTP 200 OK (PSH,ACK)
  C->>S: ACK
  S->>C: FIN,ACK
  C->>S: FIN,ACK
  S->>C: ACK
```

## 4. DNS resolution
```mermaid
sequenceDiagram
  participant B as Browser/stub resolver
  participant R as Recursive resolver
  participant Root as Root server
  participant TLD as TLD server (.com)
  participant Auth as Authoritative server
  B->>R: A record for www.example.com?
  R->>Root: where is .com?
  Root-->>R: TLD servers
  R->>TLD: where is example.com?
  TLD-->>R: authoritative servers
  R->>Auth: A record for www.example.com?
  Auth-->>R: IP address + TTL
  R-->>B: answer (cached by TTL)
```
