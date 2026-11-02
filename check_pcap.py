"""Independent sanity check of sample_lab_capture.pcap: parses frames and verifies checksums."""
import struct, socket
def csum(d):
    if len(d) % 2: d += b"\x00"
    s = sum(struct.unpack("!%dH" % (len(d)//2), d))
    while s >> 16: s = (s & 0xFFFF) + (s >> 16)
    return (~s) & 0xFFFF
data = open("packet_analysis/sample_lab_capture.pcap","rb").read()
off, n, bad = 24, 0, 0
FL = {1:"FIN",2:"SYN",4:"RST",8:"PSH",16:"ACK"}
while off < len(data):
    sec, usec, cl, ol = struct.unpack("<IIII", data[off:off+16]); off += 16
    fr = data[off:off+cl]; off += cl; n += 1
    ip = fr[14:]; ihl = (ip[0] & 15)*4; proto = ip[9]
    src, dst = socket.inet_ntoa(ip[12:16]), socket.inet_ntoa(ip[16:20])
    ok_ip = csum(ip[:ihl]) == 0
    seg = ip[ihl:20+struct.unpack("!H", ip[2:4])[0]-20+0][:struct.unpack("!H", ip[2:4])[0]-ihl]
    ps = ip[12:20] + struct.pack("!BBH", 0, proto, len(seg))
    ok_l4 = csum(ps + seg) == 0
    if proto == 6:
        fl = struct.unpack("!B", seg[13:14])[0]
        info = "TCP " + "+".join(v for k,v in FL.items() if fl & k)
    else: info = "UDP"
    bad += (not ok_ip) + (not ok_l4)
    print(f"#{n:>2} {src:>13} -> {dst:<13} {info:<12} ip_csum={'ok' if ok_ip else 'BAD'} l4_csum={'ok' if ok_l4 else 'BAD'}")
print("RESULT:", "all checksums valid" if bad == 0 else f"{bad} bad checksums")
