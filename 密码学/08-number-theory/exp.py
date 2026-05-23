#!/usr/bin/env python3
"""Rabin cryptosystem: e=2, not coprime with phi(n).
Need to factor n, compute sqrt mod p and q, combine via CRT.
"""
import sys
from Crypto.Util.number import bytes_to_long, long_to_bytes

n = 7575902033426225167950043314332155258900663393486034928103860266410764626898791287984532785296011843379771469046029926050089616816195505504936668211640681
e = 2
c = 32748843439613104595061875650819304015632244700268333752918189942573734861014886982400317907840982929151143804326798262918937519997686914396514937609

# Step 1: factor n (use factordb or known factors)
p = 73773925003932958171463477312885203038886456623352755843730749682616333292719
q = 102690781777197656470432351840281521906544413527636318985325024278487016458599
assert p * q == n

# Step 2: compute sqrt mod p and sqrt mod q
def modular_sqrt(a, p):
    """Tonelli-Shanks algorithm for sqrt(a) mod p (p ≡ 3 mod 4 case)."""
    assert p % 4 == 3
    return pow(a, (p + 1) // 4, p)

# Step 3: compute square roots
mp = modular_sqrt(c, p)
mq = modular_sqrt(c, q)

# Step 4: combine with CRT
def crt(r1, m1, r2, m2):
    M = m1 * m2
    return (r1 * m2 * pow(m2, -1, m1) + r2 * m1 * pow(m1, -1, m2)) % M

r1 = crt(mp, p, mq, q)
r2 = crt(mp, p, -mq % q, q)
r3 = crt(-mp % p, p, mq, q)
r4 = crt(-mp % p, p, -mq % q, q)

for r in [r1, r2, r3, r4]:
    try:
        pt = long_to_bytes(r)
        if pt.startswith(b"flag{"):
            print(f"Flag: {pt.decode()}")
    except:
        pass
