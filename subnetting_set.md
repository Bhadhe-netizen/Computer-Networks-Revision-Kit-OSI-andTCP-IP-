# Subnetting Problem Set (15 problems, step-by-step, machine-verified)

> **Method used throughout:** mask -> interesting octet -> block size (256 - mask octet) -> network = highest multiple of block <= host octet -> broadcast = next network - 1 -> usable hosts = 2^(32-p) - 2.

> Every answer was first worked by hand and then checked by `build_subnetting_set.py` using Python's `ipaddress` module. Also cross-check with an online subnet calculator and record it in `verification/verification_report.md`.


---
## Part A - Network, broadcast, host range (Problems 1-8)

### Problem 1
Find the network address, broadcast address, usable host range and number of usable hosts for **192.168.1.77/26**.

**Solution**
1. /26 -> mask **255.255.255.192**.
2. Interesting octet = octet 4 (mask octet 192); block size = 256 - 192 = **64**.
3. Host octet = 77. The block containing 77 starts at **64** (next block starts at 128).
4. Network = **192.168.1.64**; broadcast = **192.168.1.127**.
5. Host range = **192.168.1.65 - 192.168.1.126**.
6. Usable hosts = 2^6 - 2 = **62**.

### Problem 2
Find the network address, broadcast address, usable host range and number of usable hosts for **172.16.45.200/20**.

**Solution**
1. /20 -> mask **255.255.240.0**.
2. Interesting octet = octet 3 (mask octet 240); block size = 256 - 240 = **16**.
3. Host octet = 45. The block containing 45 starts at **32** (next block starts at 48).
4. Network = **172.16.32.0**; broadcast = **172.16.47.255**.
5. Host range = **172.16.32.1 - 172.16.47.254**.
6. Usable hosts = 2^12 - 2 = **4094**.

### Problem 3
Find the network address, broadcast address, usable host range and number of usable hosts for **10.5.130.9/17**.

**Solution**
1. /17 -> mask **255.255.128.0**.
2. Interesting octet = octet 3 (mask octet 128); block size = 256 - 128 = **128**.
3. Host octet = 130. The block containing 130 starts at **128** (next block starts at 256).
4. Network = **10.5.128.0**; broadcast = **10.5.255.255**.
5. Host range = **10.5.128.1 - 10.5.255.254**.
6. Usable hosts = 2^15 - 2 = **32766**.

### Problem 4
Find the network address, broadcast address, usable host range and number of usable hosts for **192.168.100.200/27**.

**Solution**
1. /27 -> mask **255.255.255.224**.
2. Interesting octet = octet 4 (mask octet 224); block size = 256 - 224 = **32**.
3. Host octet = 200. The block containing 200 starts at **192** (next block starts at 224).
4. Network = **192.168.100.192**; broadcast = **192.168.100.223**.
5. Host range = **192.168.100.193 - 192.168.100.222**.
6. Usable hosts = 2^5 - 2 = **30**.

### Problem 5
Find the network address, broadcast address, usable host range and number of usable hosts for **203.0.113.99/28**.

**Solution**
1. /28 -> mask **255.255.255.240**.
2. Interesting octet = octet 4 (mask octet 240); block size = 256 - 240 = **16**.
3. Host octet = 99. The block containing 99 starts at **96** (next block starts at 112).
4. Network = **203.0.113.96**; broadcast = **203.0.113.111**.
5. Host range = **203.0.113.97 - 203.0.113.110**.
6. Usable hosts = 2^4 - 2 = **14**.

### Problem 6
Find the network address, broadcast address, usable host range and number of usable hosts for **172.31.200.17/22**.

**Solution**
1. /22 -> mask **255.255.252.0**.
2. Interesting octet = octet 3 (mask octet 252); block size = 256 - 252 = **4**.
3. Host octet = 200. The block containing 200 starts at **200** (next block starts at 204).
4. Network = **172.31.200.0**; broadcast = **172.31.203.255**.
5. Host range = **172.31.200.1 - 172.31.203.254**.
6. Usable hosts = 2^10 - 2 = **1022**.

### Problem 7
Find the network address, broadcast address, usable host range and number of usable hosts for **192.168.5.130/30**.

**Solution**
1. /30 -> mask **255.255.255.252**.
2. Interesting octet = octet 4 (mask octet 252); block size = 256 - 252 = **4**.
3. Host octet = 130. The block containing 130 starts at **128** (next block starts at 132).
4. Network = **192.168.5.128**; broadcast = **192.168.5.131**.
5. Host range = **192.168.5.129 - 192.168.5.130**.
6. Usable hosts = 2^2 - 2 = **2**.

### Problem 8
Find the network address, broadcast address, usable host range and number of usable hosts for **10.99.77.5/19**.

**Solution**
1. /19 -> mask **255.255.224.0**.
2. Interesting octet = octet 3 (mask octet 224); block size = 256 - 224 = **32**.
3. Host octet = 77. The block containing 77 starts at **64** (next block starts at 96).
4. Network = **10.99.64.0**; broadcast = **10.99.95.255**.
5. Host range = **10.99.64.1 - 10.99.95.254**.
6. Usable hosts = 2^13 - 2 = **8190**.


---
## Part B - Masks, sizing, splitting, VLSM, summarisation, theory (Problems 9-15)

### Problem 9
Convert mask **255.255.255.248** to CIDR and state the usable hosts per subnet.

**Solution**
1. 248 = 11111000 -> 5 one-bits. 8+8+8+5 = **/29**.
2. Host bits = 32 - 29 = 3 -> 2^3 - 2 = **6 usable hosts**.

### Problem 10
What is the smallest subnet (longest prefix) that fits **(a) 500 hosts** and **(b) 60 hosts**?

**Solution**
(a) Need 2^h - 2 >= 500 -> h = 9 (510) because h = 8 gives only 254. Prefix = 32 - 9 = **/23** (510 usable).

(b) 2^h - 2 >= 60 -> h = 6 (62); h = 5 gives only 30. Prefix = 32 - 6 = **/26** (62 usable).

### Problem 11
Split **192.168.10.0/24** into 4 equal subnets. List them.

**Solution**
1. 4 subnets = 2^2 -> borrow 2 bits -> /24 + 2 = **/26**.
2. Block size = 256 - 192 = 64.
3. Subnets: **192.168.10.0/26**, **192.168.10.64/26**, **192.168.10.128/26**, **192.168.10.192/26**.
4. Each has 62 usable hosts.

### Problem 12 (VLSM)
Subnet **192.168.1.0/24** for four LANs needing **100, 50, 25 and 10** hosts. Allocate largest first.

**Solution**

| LAN | Hosts needed | Host bits | Prefix | Subnet |
|---|---|---|---|---|
| A | 100 | 7 (126 usable) | /25 | 192.168.1.0/25 (.0-.127) |
| B | 50 | 6 (62 usable) | /26 | 192.168.1.128/26 (.128-.191) |
| C | 25 | 5 (30 usable) | /27 | 192.168.1.192/27 (.192-.223) |
| D | 10 | 4 (14 usable) | /28 | 192.168.1.224/28 (.224-.239) |

Largest-first keeps blocks aligned; .240-.255 remains free for growth.

### Problem 13
Are these pairs in the same subnet? **(a)** 10.1.1.130/25 and 10.1.1.200/25  **(b)** 192.168.4.60/26 and 192.168.4.70/26

**Solution**

(a) /25 -> block 128. 130 and 200 both lie in 128-255 -> network 10.1.1.128 for both -> **Yes**.

(b) /26 -> block 64. 60 lies in 0-63, 70 lies in 64-127 -> networks .0 and .64 -> **No** (a router is needed between them).

### Problem 14
Summarise 172.16.4.0/24, 172.16.5.0/24, 172.16.6.0/24 and 172.16.7.0/24 into one route.

**Solution**
1. Third octets 4-7 in binary: 00000100 ... 00000111. The first 6 bits (000001) are common.
2. Common bits = 16 + 6 = **/22**.
3. Summary route = **172.16.4.0/22** (covers 172.16.4.0 - 172.16.7.255).

### Problem 15
Is **172.32.5.1** a private (RFC 1918) address?

**Solution**
RFC 1918 ranges: 10.0.0.0/8, 172.16.0.0/12 (172.16.0.0 - 172.31.255.255), 192.168.0.0/16. 172.32.x.x is just outside 172.16.0.0/12 -> **public**.
