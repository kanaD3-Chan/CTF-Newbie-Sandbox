#!/usr/bin/env python3
import os

FLAG = b"flag{ecc_small_curve_is_weak}"

# Small elliptic curve: y^2 = x^3 + ax + b (mod p)
# The curve is small enough to brute-force the discrete log
p = 97
a = 2
b = 3
G = (3, 6)  # base point on the curve, order = 5

def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 != y2:
        return None
    if P == Q:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def point_mul(k, P):
    result = None
    addend = P
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result

# Compute order of G
order = 1
cur = G
while True:
    cur = point_add(cur, G)
    order += 1
    if cur is None:  # reached point at infinity
        break

print(f"Order of G: {order}")

# Generate ECDH keypair
secret = 2  # small enough to brute-force
P = point_mul(secret, G)

# Encrypt flag: use P's x-coordinate as XOR key
key_byte = P[0] & 0xFF
flag_enc = bytes(c ^ key_byte for c in FLAG)

readme = f"""# 椭圆曲线上的秘密

**出题人：** KanaDE
**难度：** Hard
**方向：** Crypto

---

椭圆曲线密码学。

曲线参数有问题——阶太小，可以暴力破解离散对数。

---

**曲线参数：**
```
y^2 = x^3 + {a}x + {b} (mod {p})
G = {G}
```

**公钥：**
```
P = {P}
```

**密文：**
```
flag_enc = {flag_enc.hex()}
```

**附件：** `params.txt`
"""

with open('README.md', 'w') as f:
    f.write(readme)

with open('params.txt', 'w') as f:
    f.write(f"p = {p}\n")
    f.write(f"a = {a}\n")
    f.write(f"b = {b}\n")
    f.write(f"G = {G}\n")
    f.write(f"P = {P}\n")
    f.write(f"flag_enc = {flag_enc.hex()}\n")

print(f"Flag: {FLAG.decode()}")
print(f"G = {G}, order = {order}")
print(f"secret = {secret}, P = {P}")
print(f"flag_enc = {flag_enc.hex()}")
