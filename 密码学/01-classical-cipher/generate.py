#!/usr/bin/env python3
import random

FLAG = "flag{caesar_cipher_is_fun}"
shift = random.randint(1, 25)

def caesar_encrypt(text, shift):
    result = []
    for c in text:
        if c.islower():
            result.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
        elif c.isupper():
            result.append(chr((ord(c) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(c)
    return ''.join(result)

ciphertext = caesar_encrypt(FLAG, shift)

readme = f"""# 凯撒大帝的密信

**出题人：** KanaDE
**难度：** Easy
**方向：** Crypto

---

一段密文。看起来像英文，但每个字母都错位了。

凯撒大帝用的就是这个——他以为没人能破解。

**密文：** `{ciphertext}`

> Shift 未知，但一共只有 25 种可能。
"""

with open('README.md', 'w') as f:
    f.write(readme)

print(f"Flag: {FLAG}")
print(f"Shift: {shift}")
print(f"Ciphertext: {ciphertext}")
