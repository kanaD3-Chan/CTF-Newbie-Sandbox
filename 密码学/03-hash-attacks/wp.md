# WP：哈希碰撞

## Flag

```
flag{php_md5_0e_is_magic}
```

## 提交答案

```
240610708 QNKCDZO
```

## 解题思路

PHP 的 `==` 是弱类型比较。当 MD5 值为 `0eXXXXX...` 格式（全是数字）时，PHP 将其解析为 `0 × 10^XXXXX = 0`。两个不同的 `0e` 哈希值用 `==` 比较都会为 `true`。

```python
import hashlib

a = "240610708"
b = "QNKCDZO"

h1 = hashlib.md5(a.encode()).hexdigest()
h2 = hashlib.md5(b.encode()).hexdigest()

# h1 = 0e462097431906509019562988736854
# h2 = 0e830400451993494058024219903391
# 两个不同的值，但在 PHP 中 == 比较为 true
```
