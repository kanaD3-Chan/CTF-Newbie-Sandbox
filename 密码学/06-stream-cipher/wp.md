# WP：流密码的秘密

## Flag

```
flag{rc4_key_reuse_is_lethal}
```

## 解题思路

两段密文使用相同的 RC4 密钥流。相同密钥流下，c1 XOR c2 = m1 XOR m2。

```python
c1_hex = "ee5af7e49b26fdb89de760f767086e454ed1124d126073c60988491a801818470ecfd61be423022e90b1acb09baefbb033a466c9c587cc40be63abe88a8d74017cac41fd"
c2_hex = "ee5af7e49b26fdb89de760f767086e454ed1124d126073c60988491a8018184730fbef24c7093942978291919c84c69d189961f8ee80f87d925392dcaf8d74017cac41fd"
msg1  = b"This message contains the flag: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX in it."

c1 = bytes.fromhex(c1_hex)
c2 = bytes.fromhex(c2_hex)

xor_ct = bytes(a ^ b for a, b in zip(c1, c2))
msg2 = bytes(a ^ b for a, b in zip(xor_ct, msg1))

import re
m = re.search(rb'flag\{[^}]+\}', msg2)
if m:
    print(f"Flag: {m.group().decode()}")
```
