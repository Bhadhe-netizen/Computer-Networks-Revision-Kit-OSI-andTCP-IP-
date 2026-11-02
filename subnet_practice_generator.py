#!/usr/bin/env python3
"""
Subnet Practice Generator  (Capstone 14 - automation step)

Generates random subnetting problems whose answers are computed with Python's
`ipaddress` module, so the answer key is always correct.
Only PRIVATE (RFC 1918) addresses are used, so no real/public hosts are referenced.

Examples:
  python subnet_practice_generator.py -n 5 --level easy
  python subnet_practice_generator.py -n 10 --level hard --seed 42 --answers
  python subnet_practice_generator.py --quiz -n 5        # interactive mode
"""
import argparse
import ipaddress as ip
import random

LEVELS = {"easy": (24, 30), "medium": (16, 30), "hard": (9, 30)}


def rand_private_ip():
    base = random.choice(["10", f"172.{random.randint(16, 31)}", "192.168"])
    parts = base.split(".")
    while len(parts) < 4:
        parts.append(str(random.randint(0, 255)))
    return ".".join(parts)


def make_problem(level):
    lo, hi = LEVELS[level]
    p = random.randint(lo, hi)
    iface = ip.ip_interface(f"{rand_private_ip()}/{p}")
    net = iface.network
    kind = random.choice(["network", "broadcast", "hosts", "range", "same"])
    if kind == "network":
        return f"Network address of {iface}?", str(net.network_address)
    if kind == "broadcast":
        return f"Broadcast address of {iface}?", str(net.broadcast_address)
    if kind == "hosts":
        return f"How many usable hosts in a /{p} subnet?", str(net.num_addresses - 2)
    if kind == "range":
        return (f"First and last usable host for {iface}? (format: first - last)",
                f"{net.network_address + 1} - {net.broadcast_address - 1}")
    offset = random.choice([-70, -3, 5, 40, 200])
    other = ip.ip_address((int(iface.ip) + offset) % 2 ** 32)
    return (f"Is {other} in the same subnet as {iface}? (Yes/No)",
            "Yes" if other in net else "No")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-n", "--count", type=int, default=5, help="number of problems")
    ap.add_argument("--level", choices=LEVELS, default="medium")
    ap.add_argument("--seed", type=int, help="repeatable output")
    ap.add_argument("--answers", action="store_true", help="print the answer key")
    ap.add_argument("--quiz", action="store_true", help="interactive mode")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)
    problems = [make_problem(args.level) for _ in range(args.count)]

    if args.quiz:
        score = 0
        for i, (q, ans) in enumerate(problems, 1):
            reply = input(f"Q{i}. {q}\n> ").strip()
            ok = reply.replace(" ", "").lower() == ans.replace(" ", "").lower()
            score += ok
            print("Correct!\n" if ok else f"Answer: {ans}\n")
        print(f"Score: {score}/{len(problems)}")
        return

    for i, (q, _) in enumerate(problems, 1):
        print(f"Q{i}. {q}")
    if args.answers:
        print("\n--- ANSWER KEY ---")
        for i, (_, ans) in enumerate(problems, 1):
            print(f"Q{i}. {ans}")


if __name__ == "__main__":
    main()
