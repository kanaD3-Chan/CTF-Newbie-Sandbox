# WP：奇怪的编码

## Flag

```
flag{base58_is_weird_too}
```

## 解题思路

字符集去掉了 0、O、I、l 等容易混淆的字符——这是 Base58 的特征。

```python
import base58

encoded = "iDMb6ZMnbVBAonRLhTEFayNjoN4xDm4sRE"
print(base58.b58decode(encoded).decode())
```
