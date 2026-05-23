# WP：07-heap-basics

## 题目信息

- 类型：堆利用（UAF + fastbin attack → `__malloc_hook`）
- 保护：No PIE、No Canary、NX
- libc：glibc 2.23（ubuntu 16.04）
- 端口：13377

## 漏洞分析

程序提供 alloc/delete/edit/view 四个操作，存在两个漏洞：

1. **UAF（Use-After-Free）**：`delete` 调用 `free(chunks[idx])` 后没有将 `chunks[idx]` 置 NULL，导致 `view` 和 `edit` 仍可访问已释放的 chunk。

2. **edit 越界写**：`edit` 固定读入 0x60 字节，不受 alloc 时指定的 size 限制。

## 利用思路

### 第一步：泄漏 libc 基址

分配一个 small chunk（size >= 0x80，进入 unsorted bin 而非 fastbin），free 后其 `fd` 指针指向 `main_arena+88`（libc 内部地址）。利用 UAF 通过 `view` 读出这个指针，计算 libc 基址。

```python
libc_base = leaked_fd - 0x3c4b78  # main_arena+88 偏移
```

### 第二步：fastbin double free

分配两个 fastbin 大小的 chunk（alloc(0x60)，实际 chunk size 0x70），然后交叉 free：

```
free(2) -> free(3) -> free(2)
```

glibc 2.23 的 double free 检测只检查 `fastbin_head == chunk`，交叉 free 可绕过。此时 fastbin 链为 `2 -> 3 -> 2 -> ...`（循环）。

### 第三步：投毒 fd，指向 fake chunk

第一次 alloc 拿回 chunk2，同时将其 `fd` 改为 `__malloc_hook - 0x23`：

```python
alloc(0x60, p64(libc_base + __malloc_hook - 0x23))
```

**为什么是 `__malloc_hook - 0x23`？**

fastbin 分配时会检查 fake chunk 的 size 字段是否与当前 fastbin 大小匹配。`__malloc_hook - 0x23 - 8`（size 字段位置）在运行时值为 `0x7f`（来自 `__memalign_hook` 存储的 libc 地址的高字节），`0x7f & ~7 = 0x78`，对应 fastbin[5]，与 alloc(0x60) 一致。

### 第四步：分配 fake chunk，覆盖 `__malloc_hook`

连续 alloc 三次后，第四次 malloc 返回 `__malloc_hook - 0x13`（fake chunk 的 data 区域）。写入：

```python
b'\x00' * 0x13 + p64(one_gadget)
```

偏移 0x13 处正好是 `__malloc_hook`，将其覆盖为 one_gadget 地址。

### 第五步：触发

任意 malloc 调用都会跳转到 `__malloc_hook`，即 one_gadget，执行 `execve("/bin/sh")`。

## 为什么用 one_gadget 而不是 system

`system()` 内部调用 `fork()`，在 socat `EXEC` 模式下 fork 出的子进程 I/O 无法连接到 socket（与 06-ret2libc 同样的问题）。`one_gadget` 直接调用 `execve` 替换当前进程，I/O 保持不变。

## 关键偏移（glibc 2.23）

| 符号 | 偏移 |
|------|------|
| main_arena+88 | 0x3c4b78 |
| `__malloc_hook` | 0x3c4b10 |
| one_gadget | 0x4527a |
| fake chunk fd | `__malloc_hook - 0x23` |
| `__malloc_hook` 写入偏移 | 0x13 |
