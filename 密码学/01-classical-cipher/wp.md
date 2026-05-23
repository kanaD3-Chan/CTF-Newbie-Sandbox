# WP：凯撒大帝的密信

## Flag

```
flag{caesar_cipher_is_fun}
```

## 解题思路

凯撒密码只有 25 种可能的偏移量，遍历即可。

```python
ciphertext = "jpek{geiwev_gmtliv_mw_jyr}"

for shift in range(1, 26):
    plain = []
    for c in ciphertext:
        if c.islower():
            plain.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
        elif c.isupper():
            plain.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
        else:
            plain.append(c)
    result = ''.join(plain)
    if result.startswith("flag{"):
        print(f"Flag: {result}")
        break
```
