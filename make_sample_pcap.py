#!/usr/bin/env python3
"""
Creates packet_analysis/sample_lab_capture.pcap  (SYNTHETIC lab traffic, no real users).

Scenario: client 192.168.1.10 looks up "lab.example" via DNS (192.168.1.1),
then opens a TCP connection to 203.0.113.80:80 (TEST-NET-3 documentation address),
sends an HTTP GET, receives 200 OK, and closes the connection.

Open the .pcap in Wireshark.  Checksums are correctly computed.
Only the Python standard library is used.
"""
import struct
import socket

CLIENT_MAC = bytes.fromhex("aabbcc000001")
GW_MAC = bytes.fromhex("aabbcc000002")
CLIENT_IP, DNS_IP, WEB_IP = "192.168.1.10", "192.168.1.1", "203.0.113.80"
CPORT, DPORT = 49152, 80

packets = []   # (timestamp, bytes)
t = [1.000000]


def ip_bytes(a):
    return socket.inet_aton(a)


def csum(data):
    if len(data) % 2:
        data += b"\x00"
    s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    return (~s) & 0xFFFF


ip_id = [0x1000]


def ipv4(src, dst, proto, payload):
    ip_id[0] += 1
    hdr = struct.pack("!BBHHHBBH4s4s", 0x45, 0, 20 + len(payload), ip_id[0], 0x4000, 64, proto, 0,
                      ip_bytes(src), ip_bytes(dst))
    hdr = hdr[:10] + struct.pack("!H", csum(hdr)) + hdr[12:]
    return hdr + payload


def pseudo(src, dst, proto, length):
    return ip_bytes(src) + ip_bytes(dst) + struct.pack("!BBH", 0, proto, length)


def udp(src, dst, sport, dport, data):
    length = 8 + len(data)
    h = struct.pack("!HHHH", sport, dport, length, 0)
    c = csum(pseudo(src, dst, 17, length) + h + data) or 0xFFFF
    return struct.pack("!HHHH", sport, dport, length, c) + data


def tcp(src, dst, sport, dport, seq, ack, flags, data=b"", window=64240):
    h = struct.pack("!HHIIBBHHH", sport, dport, seq, ack, 5 << 4, flags, window, 0, 0)
    c = csum(pseudo(src, dst, 6, len(h) + len(data)) + h + data)
    h = h[:16] + struct.pack("!H", c) + h[18:]
    return h + data


def eth(dst_mac, src_mac, payload):
    return dst_mac + src_mac + struct.pack("!H", 0x0800) + payload


def add(frame, dt=0.001):
    t[0] += dt
    packets.append((t[0], frame))


def dns_query(name, txid=0x1A2B):
    q = b"".join(bytes([len(p)]) + p.encode() for p in name.split(".")) + b"\x00"
    return struct.pack("!HHHHHH", txid, 0x0100, 1, 0, 0, 0) + q + struct.pack("!HH", 1, 1), q


FIN, SYN, RST, PSH, ACK = 0x01, 0x02, 0x04, 0x08, 0x10

# 1-2  DNS ---------------------------------------------------------------
qmsg, qname = dns_query("lab.example")
add(eth(GW_MAC, CLIENT_MAC, ipv4(CLIENT_IP, DNS_IP, 17, udp(CLIENT_IP, DNS_IP, 53124, 53, qmsg))))
resp = (struct.pack("!HHHHHH", 0x1A2B, 0x8180, 1, 1, 0, 0) + qname + struct.pack("!HH", 1, 1)
        + b"\xc0\x0c" + struct.pack("!HHIH", 1, 1, 300, 4) + ip_bytes(WEB_IP))
add(eth(CLIENT_MAC, GW_MAC, ipv4(DNS_IP, CLIENT_IP, 17, udp(DNS_IP, CLIENT_IP, 53, 53124, resp))), 0.012)


def seg_c(seq, ack, flags, data=b"", dt=0.001):
    add(eth(GW_MAC, CLIENT_MAC, ipv4(CLIENT_IP, WEB_IP, 6, tcp(CLIENT_IP, WEB_IP, CPORT, DPORT, seq, ack, flags, data))), dt)


def seg_s(seq, ack, flags, data=b"", dt=0.001):
    add(eth(CLIENT_MAC, GW_MAC, ipv4(WEB_IP, CLIENT_IP, 6, tcp(WEB_IP, CLIENT_IP, DPORT, CPORT, seq, ack, flags, data))), dt)


c_isn, s_isn = 1000, 5000
# 3-5  three-way handshake ------------------------------------------------
seg_c(c_isn, 0, SYN, dt=0.020)
seg_s(s_isn, c_isn + 1, SYN | ACK, dt=0.030)
seg_c(c_isn + 1, s_isn + 1, ACK, dt=0.001)
# 6-9  HTTP --------------------------------------------------------------
req = b"GET / HTTP/1.1\r\nHost: lab.example\r\nUser-Agent: lab-client/1.0\r\nConnection: close\r\n\r\n"
body = b"<html><body>Hello from the lab</body></html>"
rsp = (b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + str(len(body)).encode()
       + b"\r\nConnection: close\r\n\r\n" + body)
seg_c(c_isn + 1, s_isn + 1, PSH | ACK, req)
seg_s(s_isn + 1, c_isn + 1 + len(req), ACK, dt=0.030)
seg_s(s_isn + 1, c_isn + 1 + len(req), PSH | ACK, rsp, dt=0.010)
seg_c(c_isn + 1 + len(req), s_isn + 1 + len(rsp), ACK, dt=0.001)
# 10-12 teardown ------------------------------------------------------------
seg_s(s_isn + 1 + len(rsp), c_isn + 1 + len(req), FIN | ACK, dt=0.002)
seg_c(c_isn + 1 + len(req), s_isn + 2 + len(rsp), FIN | ACK, dt=0.001)
seg_s(s_isn + 2 + len(rsp), c_isn + 2 + len(req), ACK, dt=0.030)

with open("packet_analysis/sample_lab_capture.pcap", "wb") as f:
    f.write(struct.pack("<IHHiIII", 0xA1B2C3D4, 2, 4, 0, 0, 65535, 1))
    for ts, fr in packets:
        sec, usec = int(ts), int((ts % 1) * 1_000_000)
        f.write(struct.pack("<IIII", sec, usec, len(fr), len(fr)) + fr)
print(f"Wrote {len(packets)} packets to packet_analysis/sample_lab_capture.pcap")
