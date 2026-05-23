#!/usr/bin/env python3
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

FLAG = "flag{aes_ecb_byte_by_byte}"
key = os.urandom(16)

def oracle(plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext + FLAG.encode(), 16))

# Export oracle
oracle_code = f'''#!/usr/bin/env python3
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = {key}
flag = {FLAG.encode()}

def oracle(plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext + flag, 16))

if __name__ == "__main__":
    data = sys.argv[1].encode() if len(sys.argv) > 1 else b""
    result = oracle(data)
    print(result.hex())
'''

with open('aes_oracle.py', 'w') as f:
    f.write(oracle_code)
os.chmod('aes_oracle.py', 0o755)

c_empty = oracle(b"")

readme = f"""# AES 的弱点

**出题人：** KanaDE
**难度：** Medium
**方向：** Crypto

---

AES-ECB 模式加密。

相同的明文块，加密出相同的密文块。

这道题利用的就是这个性质——构造特定的输入，推断出 flag。

你有一个 `aes_oracle.py`，其中 `oracle(plaintext)` 函数会加密 `plaintext + flag`。

通过选择不同的 `plaintext`，你可以逐字节推断出 flag 的内容。

---

**附件：** `aes_oracle.py`
"""

with open('README.md', 'w') as f:
    f.write(readme)

print(f"Flag: {FLAG}")
print(f"Key: {key.hex()}")
print(f"oracle(b'') = {c_empty.hex()}")
