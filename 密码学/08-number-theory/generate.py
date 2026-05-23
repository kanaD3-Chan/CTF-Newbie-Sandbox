#!/usr/bin/env python3
from Crypto.Util.number import getPrime, bytes_to_long

FLAG = "flag{rabin_crypto_is_quadratic}"

# Rabin cryptosystem: e = 2
# e and phi(n) are not coprime (share factor 2)
# Cannot compute d = inverse(e, phi(n)) directly
# Need to factor n and compute square roots mod p and mod q

# Need p, q ≡ 3 (mod 4) for simple sqrt formula
while True:
    p = getPrime(256)
    q = getPrime(256)
    if p % 4 == 3 and q % 4 == 3:
        break
n = p * q
e = 2
m = bytes_to_long(FLAG.encode())
c = pow(m, e, n)

readme = f"""# 数论基础

**出题人：** KanaDE
**难度：** Hard
**方向：** Crypto

---

一道 RSA 变体题。

`e` 和 `phi(n)` 不互素，普通的求逆元方法不管用。

需要用到一些数论知识——Rabin 密码体制。

---

**参数：**

```
n = {n}
e = {e}
c = {c}
```

**附件：** `params.txt`
"""

with open('README.md', 'w') as f:
    f.write(readme)

with open('params.txt', 'w') as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")

print(f"Flag: {FLAG}")
print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
print(f"p = {p}")
print(f"q = {q}")

# Write factors for verification
with open('.secret', 'w') as f:
    f.write(f"p = {p}\nq = {q}\n")
