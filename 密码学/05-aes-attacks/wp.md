# WP：AES 的弱点

## Flag

```
flag{aes_ecb_byte_by_byte}
```

## 解题思路

AES-ECB 模式下相同明文块加密结果相同。利用 oracle 逐字节推断 flag。

```python
from aes_oracle import oracle

BS = 16

# 确定 flag 长度
base_blocks = len(oracle(b"")) // BS
for i in range(1, BS * 2 + 1):
    if len(oracle(b"A" * i)) // BS > base_blocks:
        flag_len = len(oracle(b"")) - i
        break

# 逐字节恢复
known = b""
alphabet = [bytes([c]) for c in range(32, 127)]

for i in range(flag_len):
    block_idx = i // BS
    padding_len = BS - (i % BS) - 1
    prefix = b"A" * padding_len
    
    target = oracle(prefix)[block_idx * BS : (block_idx + 1) * BS]
    for ch in alphabet:
        if oracle(prefix + known + ch)[block_idx * BS : (block_idx + 1) * BS] == target:
            known += ch
            break

print(f"Flag: {known.decode()}")
```
