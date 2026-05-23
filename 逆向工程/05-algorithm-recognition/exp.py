#!/usr/bin/env python3
import struct

def tea_decrypt(v, k):
    v0, v1 = v
    s = (32 * 0x9e3779b9) & 0xffffffff
    delta = 0x9e3779b9
    for _ in range(32):
        v1 = (v1 - (((v0 << 4) + k[2]) ^ (v0 + s) ^ ((v0 >> 5) + k[3]))) & 0xffffffff
        v0 = (v0 - (((v1 << 4) + k[0]) ^ (v1 + s) ^ ((v1 >> 5) + k[1]))) & 0xffffffff
        s = (s - delta) & 0xffffffff
    return (v0, v1)

key = [0xdeadbeef, 0xcafebabe, 0x12345678, 0x87654321]

expected = [
    0xf75e7798, 0x04c7c4b2,
    0x84d60457, 0x22677440,
    0xc2022040, 0xb51746e6,
    0x7adffb54, 0xe5d17296,
]

buf = expected[:]
for i in range(0, 8, 2):
    buf[i], buf[i+1] = tea_decrypt((buf[i], buf[i+1]), key)

flag = struct.pack('<8I', *buf).rstrip(b'\x00').decode()
print(flag)
