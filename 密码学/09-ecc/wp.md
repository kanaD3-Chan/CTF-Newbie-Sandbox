# WP：椭圆曲线上的秘密

## Flag

```
flag{ecc_small_curve_is_weak}
```

## 解题思路

曲线参数太小（模数 p=97），G 的阶只有 5，暴力枚举离散对数即可。

```python
p = 97
a = 2
b = 3
G = (3, 6)
P = (80, 10)

def point_add(P1, P2):
    if P1 is None: return P2
    if P2 is None: return P1
    x1, y1 = P1; x2, y2 = P2
    if x1 == x2 and y1 != y2: return None
    if P1 == P2:
        lam = (3 * x1 * x1 + a) * pow(2 * y1, -1, p) % p
    else:
        lam = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

# 暴力求解离散对数
cur = G
for k in range(1, 10):
    if cur == P:
        print(f"secret = {k}")
        key = P[0] & 0xFF
        flag = bytes(c ^ key for c in bytes.fromhex("363c31372b3533330f233d313c3c0f33252226350f39230f2735313b2d"))
        print(f"Flag: {flag.decode()}")
        break
    cur = point_add(cur, G)
```
