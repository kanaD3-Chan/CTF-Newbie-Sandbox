#!/usr/bin/env python3
import hashlib

FLAG = "flag{php_md5_0e_is_magic}"

magic_pairs = [
    ("240610708", "QNKCDZO"),
    ("aabg7XSs", "aabC9RqS"),
    ("aaroZmOk", "aaK1STfY"),
    ("aaO8zKZF", "aa3OFF9m"),
]
a, b = magic_pairs[0]

readme = f"""# 哈希碰撞

**出题人：** KanaDE
**难度：** Easy
**方向：** Crypto

---

后端验证密码的 PHP 代码：

```php
<?php
$password = $_POST['password'];
$hash = md5($_POST['hash']);

if ($password == $hash) {{
    echo "flag: {FLAG}";
}} else {{
    echo "failed";
}}
?>
```

`md5()` 返回的是一个字符串。PHP 的 `==` 比较在某些情况下会把两个不同的字符串当成"相等"。

你能找出两个不同的字符串，使得它们的 MD5 值通过 PHP 的 `==` 比较为 true 吗？

> 提示：看看 `0e` 开头的 MD5 值在 PHP 中会被解析成什么。

---

**提交格式：** 两个字符串，空格隔开
"""

with open('README.md', 'w') as f:
    f.write(readme)

print(f"Flag: {FLAG}")
print(f"Answer: {a} {b}")
print(f"MD5({a}) = {hashlib.md5(a.encode()).hexdigest()}")
print(f"MD5({b}) = {hashlib.md5(b.encode()).hexdigest()}")
