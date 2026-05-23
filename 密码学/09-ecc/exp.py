#!/usr/bin/env python3
"""ECC small curve: brute-force discrete log."""
p = 97
a = 2
b = 3
G = (3, 6)
P = (80, 10)
flag_enc_hex = "363c31372b3533330f233d313c3c0f33252226350f39230f2735313b2d"
flag_enc = bytes.fromhex(flag_enc_hex)

def point_add(P1, P2):
    if P1 is None: return P2
    if P2 is None: return P1
    x1, y1 = P1
    x2, y2 = P2
    if x1 == x2 and y1 != y2: return None
    if P1 == P2:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def point_mul(k, P1):
    result = None
    addend = P1
    while k:
        if k & 1: result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result

# Brute-force discrete log: find k such that k*G = P
secret = None
cur = G
for k in range(1, 100):
    if cur == P:
        secret = k
        break
    cur = point_add(cur, G)

if secret:
    print(f"[+] Found secret = {secret}")
    key_byte = P[0] & 0xFF
    flag = bytes(c ^ key_byte for c in flag_enc)
    print(f"[+] Flag: {flag.decode()}")
else:
    print("[-] Secret not found")

# Alternative: since order of G is small, try all possible shared keys
print("\n[*] Alternative: try all order multiples:")
# Order of G on this curve was 5
for k in range(1, 10):
    Q = point_mul(k, G)
    if Q is not None:
        kb = Q[0] & 0xFF
        f = bytes(c ^ kb for c in flag_enc)
        print(f"  k={k}: {f}")
