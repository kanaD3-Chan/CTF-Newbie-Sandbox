#!/usr/bin/env python3
import os

FLAG = b"flag{rc4_key_reuse_is_lethal}"

msg1 = b"This message contains the flag: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX in it."
msg2 = b"This message contains the flag: " + FLAG + b" in it."

assert len(msg1) == len(msg2), f"len mismatch: {len(msg1)} != {len(msg2)}"

def rc4(key, data):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        out.append(byte ^ k)
    return bytes(out)

key = os.urandom(16)
c1 = rc4(key, msg1)
c2 = rc4(key, msg2)

# Verify
keystream = bytes(a ^ b for a, b in zip(c1, msg1))
recovered = bytes(a ^ b for a, b in zip(c2, keystream))
assert recovered == msg2, "RC4 recovery failed"

with open('ciphertexts.txt', 'w') as f:
    f.write(f"c1 = {c1.hex()}\n")
    f.write(f"c2 = {c2.hex()}\n")

readme = f"""# 流密码的秘密

**出题人：** KanaDE
**难度：** Medium
**方向：** Crypto

---

两段密文，用的是同一个密钥流加密的。

其中 c1 对应的明文是：

```
This message contains the flag: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX in it.
```

既然你知道 c1 的明文，能恢复出 c2 中的 flag 吗？

---

**附件：** `ciphertexts.txt`
"""

with open('README.md', 'w') as f:
    f.write(readme)

print(f"Flag: {FLAG.decode()}")
print(f"c1 = {c1.hex()}")
print(f"c2 = {c2.hex()}")
