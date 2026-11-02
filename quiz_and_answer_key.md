# 15-Question Quiz - OSI, TCP/IP, Addressing, DNS, HTTP, TCP

Answer first, then check the key at the bottom. (Numeric answers verified with Python `ipaddress`.)

---

**Q1.** Which OSI layer is responsible for logical addressing and routing?
A) Data Link  B) Network  C) Transport  D) Session

**Q2.** The PDU at the Transport layer for TCP is called a:
A) Frame  B) Packet  C) Segment  D) Bit

**Q3.** How many layers are in the TCP/IP model as defined in RFC 1122?
A) 4  B) 3  C) 5  D) 7

**Q4.** A switch primarily makes forwarding decisions using:
A) IP addresses  B) Port numbers  C) DNS names  D) MAC addresses

**Q5.** Which is the correct order of the TCP three-way handshake?
A) SYN, ACK, SYN-ACK  B) SYN, SYN-ACK, ACK  C) ACK, SYN, SYN-ACK  D) SYN-ACK, SYN, ACK

**Q6.** DNS normally uses which transport and port for ordinary queries?
A) UDP 53  B) TCP 80  C) TCP 443  D) UDP 67

**Q7.** In the courier analogy, what best represents a TCP *port number*?
A) The city PIN code  B) The delivery van  C) The recipient's flat/door number inside the building  D) The road

**Q8.** What is the network address of **192.168.1.77/26**?
A) 192.168.1.0  B) 192.168.1.96  C) 192.168.1.76  D) 192.168.1.64

**Q9.** How many usable host addresses are in a **/27** subnet?
A) 32  B) 30  C) 62  D) 28

**Q10.** What is the broadcast address of **172.16.45.200/20**?
A) 172.16.47.255  B) 172.16.45.255  C) 172.16.63.255  D) 172.16.32.255

**Q11.** Which address is **private** under RFC 1918?
A) 172.32.5.1  B) 192.169.1.1  C) 11.0.0.1  D) 172.20.5.1

**Q12.** Which HTTP status code means "Not Found"?
A) 200  B) 301  C) 404  D) 500

**Q13.** Which field in the IPv4 header is decremented by each router to prevent endless loops?
A) TTL  B) Protocol  C) Checksum  D) IHL

**Q14.** Which protocol maps an IPv4 address to a MAC address on a local network?
A) DNS  B) DHCP  C) ICMP  D) ARP

**Q15.** What single summary route covers 172.16.4.0/24 through 172.16.7.0/24?
A) 172.16.4.0/23  B) 172.16.4.0/22  C) 172.16.0.0/16  D) 172.16.4.0/21

---

## Answer key

| Q | Ans | Explanation |
|---|---|---|
| 1 | B | Network layer (IP) does logical addressing and routing. |
| 2 | C | TCP -> segment (UDP -> datagram); IP -> packet; Ethernet -> frame. |
| 3 | A | RFC 1122: Link, Internet, Transport, Application. (5-layer is a teaching variant.) |
| 4 | D | Layer-2 devices learn source MACs and forward by destination MAC. |
| 5 | B | SYN -> SYN-ACK -> ACK. |
| 6 | A | DNS queries use UDP/53 (TCP/53 for large responses and zone transfers). |
| 7 | C | The IP is the building; the port picks the right "flat" (process). |
| 8 | D | /26 -> block 64; 77 lies in 64-127; network = .64. |
| 9 | B | 2^5 - 2 = 30. |
| 10 | A | /20 -> block 16 in 3rd octet; 45 lies in 32-47; broadcast 172.16.47.255. |
| 11 | D | Private 172 range is 172.16.0.0-172.31.255.255. |
| 12 | C | 404 Not Found. |
| 13 | A | Time To Live; at 0 the router drops the packet and sends ICMP Time Exceeded. |
| 14 | D | ARP resolves IP to MAC (RFC 826). |
| 15 | B | Four /24s = 2 bits borrowed back from /24 -> /22: 172.16.4.0/22. |
