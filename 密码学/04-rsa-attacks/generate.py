#!/usr/bin/env python3
from Crypto.Util.number import getPrime, bytes_to_long

FLAG = "flag{small_n_is_easy_to_factor}"

p = getPrime(160)
q = getPrime(160)
n = p * q
e = 65537
m = bytes_to_long(FLAG.encode())
c = pow(m, e, n)

readme = f"""# RSA 不是铁板一块

**出题人：** KanaDE
**难度：** Easy
**方向：** Crypto

---

给你 n、e、c。

n 很小，可以直接分解。

分解之后，求出 d，解密，拿到 flag。

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
