"""
Builds subnetting/subnetting_set.md.

Each problem has HAND-WORKED answers (written first, the way a student/AI would do it).
The script then re-computes every answer with Python's `ipaddress` module and
FAILS LOUDLY if a hand answer is wrong. This is the "verify all numeric answers" step.

Run from the repo root:  python subnetting/build_subnetting_set.py
"""
import ipaddress as ip


def mask_octet_info(p):
    m = str(ip.ip_network(f"0.0.0.0/{p}").netmask)
    idx = (p - 1) // 8
    mo = int(m.split(".")[idx])
    return m, idx, mo, 256 - mo


# (ip/prefix, network, broadcast, first, last, usable)  -- hand-worked
NET_PROBLEMS = [
    ("192.168.1.77/26", "192.168.1.64", "192.168.1.127", "192.168.1.65", "192.168.1.126", 62),
    ("172.16.45.200/20", "172.16.32.0", "172.16.47.255", "172.16.32.1", "172.16.47.254", 4094),
    ("10.5.130.9/17", "10.5.128.0", "10.5.255.255", "10.5.128.1", "10.5.255.254", 32766),
    ("192.168.100.200/27", "192.168.100.192", "192.168.100.223", "192.168.100.193", "192.168.100.222", 30),
    ("203.0.113.99/28", "203.0.113.96", "203.0.113.111", "203.0.113.97", "203.0.113.110", 14),
    ("172.31.200.17/22", "172.31.200.0", "172.31.203.255", "172.31.200.1", "172.31.203.254", 1022),
    ("192.168.5.130/30", "192.168.5.128", "192.168.5.131", "192.168.5.129", "192.168.5.130", 2),
    ("10.99.77.5/19", "10.99.64.0", "10.99.95.255", "10.99.64.1", "10.99.95.254", 8190),
]

out = [
    "# Subnetting Problem Set (15 problems, step-by-step, machine-verified)\n",
    "> **Method used throughout:** mask -> interesting octet -> block size (256 - mask octet) -> "
    "network = highest multiple of block <= host octet -> broadcast = next network - 1 -> "
    "usable hosts = 2^(32-p) - 2.\n",
    "> Every answer was first worked by hand and then checked by `build_subnetting_set.py` using Python's "
    "`ipaddress` module. Also cross-check with an online subnet calculator and record it in "
    "`verification/verification_report.md`.\n",
    "\n---\n## Part A - Network, broadcast, host range (Problems 1-8)\n",
]

log = []
n = 0
for (cidr, net, bc, first, last, usable) in NET_PROBLEMS:
    n += 1
    i = ip.ip_interface(cidr)
    p = i.network.prefixlen
    N = i.network
    calc = (str(N.network_address), str(N.broadcast_address),
            str(N.network_address + 1), str(N.broadcast_address - 1), N.num_addresses - 2)
    assert calc == (net, bc, first, last, usable), f"Problem {n} MISMATCH: hand={(net, bc, first, last, usable)} calc={calc}"
    log.append(f"Problem {n:>2}: {cidr:<20} OK  -> {net} .. {bc}  ({usable} hosts)")
    m, idx, mo, block = mask_octet_info(p)
    octet_val = int(str(i.ip).split(".")[idx])
    base = (octet_val // block) * block
    out.append(f"### Problem {n}\nFind the network address, broadcast address, usable host range and number of usable hosts for **{cidr}**.\n")
    out.append(
        f"**Solution**\n1. /{p} -> mask **{m}**.\n"
        f"2. Interesting octet = octet {idx + 1} (mask octet {mo}); block size = 256 - {mo} = **{block}**.\n"
        f"3. Host octet = {octet_val}. The block containing {octet_val} starts at **{base}** (next block starts at {base + block}).\n"
        f"4. Network = **{net}**; broadcast = **{bc}**.\n5. Host range = **{first} - {last}**.\n"
        f"6. Usable hosts = 2^{32 - p} - 2 = **{usable}**.\n"
    )

out.append("\n---\n## Part B - Masks, sizing, splitting, VLSM, summarisation, theory (Problems 9-15)\n")

# 9
assert str(ip.ip_network("10.0.0.0/29").netmask) == "255.255.255.248" and ip.ip_network("10.0.0.0/29").num_addresses - 2 == 6
log.append("Problem  9: 255.255.255.248 = /29, 6 hosts            OK")
out.append("### Problem 9\nConvert mask **255.255.255.248** to CIDR and state the usable hosts per subnet.\n\n**Solution**\n"
           "1. 248 = 11111000 -> 5 one-bits. 8+8+8+5 = **/29**.\n2. Host bits = 32 - 29 = 3 -> 2^3 - 2 = **6 usable hosts**.\n")

# 10
assert ip.ip_network("10.0.0.0/23").num_addresses - 2 == 510 and ip.ip_network("10.0.0.0/22").num_addresses - 2 == 1022
assert ip.ip_network("10.0.0.0/26").num_addresses - 2 == 62 and ip.ip_network("10.0.0.0/27").num_addresses - 2 == 30
assert ip.ip_network("10.0.0.0/24").num_addresses - 2 == 254
log.append("Problem 10: 500 hosts -> /23 (510); 60 hosts -> /26 (62) OK")
out.append("### Problem 10\nWhat is the smallest subnet (longest prefix) that fits **(a) 500 hosts** and **(b) 60 hosts**?\n\n**Solution**\n"
           "(a) Need 2^h - 2 >= 500 -> h = 9 (510) because h = 8 gives only 254. Prefix = 32 - 9 = **/23** (510 usable).\n\n"
           "(b) 2^h - 2 >= 60 -> h = 6 (62); h = 5 gives only 30. Prefix = 32 - 6 = **/26** (62 usable).\n")

# 11
parts = [str(s) for s in ip.ip_network("192.168.10.0/24").subnets(prefixlen_diff=2)]
hand = ["192.168.10.0/26", "192.168.10.64/26", "192.168.10.128/26", "192.168.10.192/26"]
assert parts == hand
log.append("Problem 11: 192.168.10.0/24 -> 4 x /26                OK")
out.append("### Problem 11\nSplit **192.168.10.0/24** into 4 equal subnets. List them.\n\n**Solution**\n"
           "1. 4 subnets = 2^2 -> borrow 2 bits -> /24 + 2 = **/26**.\n2. Block size = 256 - 192 = 64.\n"
           "3. Subnets: **" + "**, **".join(hand) + "**.\n4. Each has 62 usable hosts.\n")

# 12 VLSM
alloc = [("A", 100, "192.168.1.0/25"), ("B", 50, "192.168.1.128/26"),
         ("C", 25, "192.168.1.192/27"), ("D", 10, "192.168.1.224/28")]
pool = ip.ip_network("192.168.1.0/24")
cur = pool.network_address
for name, hosts, hand_net in alloc:
    h = 1
    while 2 ** h - 2 < hosts:
        h += 1
    net = ip.ip_network(f"{cur}/{32 - h}")
    assert str(net) == hand_net, (name, str(net), hand_net)
    cur = net.broadcast_address + 1
assert cur <= pool.broadcast_address + 1
log.append("Problem 12: VLSM 100/50/25/10 -> /25 /26 /27 /28        OK")
out.append("### Problem 12 (VLSM)\nSubnet **192.168.1.0/24** for four LANs needing **100, 50, 25 and 10** hosts. Allocate largest first.\n\n**Solution**\n\n"
           "| LAN | Hosts needed | Host bits | Prefix | Subnet |\n|---|---|---|---|---|\n"
           "| A | 100 | 7 (126 usable) | /25 | 192.168.1.0/25 (.0-.127) |\n"
           "| B | 50 | 6 (62 usable) | /26 | 192.168.1.128/26 (.128-.191) |\n"
           "| C | 25 | 5 (30 usable) | /27 | 192.168.1.192/27 (.192-.223) |\n"
           "| D | 10 | 4 (14 usable) | /28 | 192.168.1.224/28 (.224-.239) |\n\n"
           "Largest-first keeps blocks aligned; .240-.255 remains free for growth.\n")

# 13
a = ip.ip_interface("10.1.1.130/25"); b = ip.ip_interface("10.1.1.200/25")
c = ip.ip_interface("192.168.4.60/26"); d = ip.ip_interface("192.168.4.70/26")
assert a.network == b.network and c.network != d.network
log.append("Problem 13: same-subnet checks (yes / no)               OK")
out.append("### Problem 13\nAre these pairs in the same subnet? **(a)** 10.1.1.130/25 and 10.1.1.200/25  **(b)** 192.168.4.60/26 and 192.168.4.70/26\n\n**Solution**\n\n"
           "(a) /25 -> block 128. 130 and 200 both lie in 128-255 -> network 10.1.1.128 for both -> **Yes**.\n\n"
           "(b) /26 -> block 64. 60 lies in 0-63, 70 lies in 64-127 -> networks .0 and .64 -> **No** (a router is needed between them).\n")

# 14
nets = [ip.ip_network(f"172.16.{x}.0/24") for x in range(4, 8)]
assert [str(x) for x in ip.collapse_addresses(nets)] == ["172.16.4.0/22"]
log.append("Problem 14: 172.16.4-7.0/24 -> 172.16.4.0/22              OK")
out.append("### Problem 14\nSummarise 172.16.4.0/24, 172.16.5.0/24, 172.16.6.0/24 and 172.16.7.0/24 into one route.\n\n**Solution**\n"
           "1. Third octets 4-7 in binary: 00000100 ... 00000111. The first 6 bits (000001) are common.\n"
           "2. Common bits = 16 + 6 = **/22**.\n3. Summary route = **172.16.4.0/22** (covers 172.16.4.0 - 172.16.7.255).\n")

# 15
assert ip.ip_address("172.31.255.255").is_private and not ip.ip_address("172.32.5.1").is_private
log.append("Problem 15: 172.32.5.1 is public (outside 172.16/12)       OK")
out.append("### Problem 15\nIs **172.32.5.1** a private (RFC 1918) address?\n\n**Solution**\n"
           "RFC 1918 ranges: 10.0.0.0/8, 172.16.0.0/12 (172.16.0.0 - 172.31.255.255), 192.168.0.0/16. "
           "172.32.x.x is just outside 172.16.0.0/12 -> **public**.\n")

open("subnetting/subnetting_set.md", "w").write("\n".join(out))
open("verification/subnet_verification_log.txt", "w").write(
    "Hand-worked answers vs Python ipaddress module\n" + "=" * 50 + "\n" + "\n".join(log) +
    "\n\nRESULT: 15/15 hand answers match the computed values.\n")
print("\n".join(log))
print("\nAll 15 hand-worked answers VERIFIED. Wrote subnetting/subnetting_set.md")
