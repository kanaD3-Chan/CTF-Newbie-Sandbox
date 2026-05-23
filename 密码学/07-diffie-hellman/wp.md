# WP：密钥交换的漏洞

## Flag

```
flag{dh_small_subgroup_is_weak}
```

## 解题思路

g 的阶只有 8（g = 4096 = 2^12 mod 65537 的阶为 8），离散对数只需尝试 0-7。

```python
p = 65537
g = 4096

# 从 transcript.txt 读取参数
with open('transcript.txt') as f:
    exec(f.read())

for a_try in range(8):
    if pow(g, a_try, p) == A:
        shared = pow(B, a_try, p)
        shared_bytes = shared.to_bytes((shared.bit_length() + 7) // 8, 'big')
        flag = bytes(c ^ shared_bytes[i % len(shared_bytes)] for i, c in enumerate(bytes.fromhex(flag_enc)))
        print(f"Flag: {flag.decode()}")
        break
```
