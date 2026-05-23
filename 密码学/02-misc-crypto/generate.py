#!/usr/bin/env python3
import base58

FLAG = "flag{base58_is_weird_too}"
encoded = base58.b58encode(FLAG.encode()).decode()

with open('encoded.txt', 'w') as f:
    f.write(encoded + '\n')

readme = f"""# 奇怪的编码

**出题人：** KanaDE
**难度：** Easy
**方向：** Crypto

---

一段看起来乱七八糟的字符串。

不是 Base64，不是 Hex，不是 ASCII。

但它确实是某种编码。识别它，解码它，拿到 flag。

---

**附件：** `encoded.txt`
"""

with open('README.md', 'w') as f:
    f.write(readme)

print(f"Flag: {FLAG}")
print(f"Encoded: {encoded}")
