#!/usr/bin/env python3
import random

FLAG = b"flag{dh_small_subgroup_is_weak}"

p = 65537
g = 4096  # order of g mod p = 8

a = random.randint(1, 100000)
b = random.randint(1, 100000)
A = pow(g, a, p)
B = pow(g, b, p)

shared = pow(A, b, p)
assert shared == pow(B, a, p)

# Encrypt flag with shared secret
shared_bytes = shared.to_bytes((shared.bit_length() + 7) // 8, 'big')
flag_enc = bytes(c ^ shared_bytes[i % len(shared_bytes)] for i, c in enumerate(FLAG))

with open('transcript.txt', 'w') as f:
    f.write(f"p = {p}\n")
    f.write(f"g = {g}\n")
    f.write(f"A = {A}\n")
    f.write(f"B = {B}\n")
    f.write(f"flag_enc = {flag_enc.hex()}\n")

readme = f"""# 密钥交换的漏洞

**出题人：** KanaDE
**难度：** Hard
**方向：** Crypto

---

一个 Diffie-Hellman 密钥交换协议的实现。

但参数选得很糟糕——`g` 的阶太小，离散对数可以暴力求解。

恢复共享密钥，解密 flag。

---

**附件：** `transcript.txt`
"""

with open('README.md', 'w') as f:
    f.write(readme)

print(f"Flag: {FLAG.decode()}")
print(f"p = {p}, g = {g}")
print(f"A = {A}, B = {B}")
print(f"flag_enc = {flag_enc.hex()}")
