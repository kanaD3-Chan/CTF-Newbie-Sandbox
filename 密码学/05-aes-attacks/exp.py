#!/usr/bin/env python3
"""Byte-at-a-time AES-ECB decryption (controlled prefix)."""
import sys
sys.path.insert(0, '.')
from aes_oracle import oracle

BS = 16

# Step 1: determine flag length
base_len = len(oracle(b""))
base_blocks = len(oracle(b"")) // BS
for i in range(1, BS * 2 + 1):
    if len(oracle(b"A" * i)) // BS > base_blocks:
        flag_len = len(oracle(b"")) - i
        break

print(f"[*] Detected flag length: {flag_len}")

# Step 2: detect ECB mode (duplicate blocks with 32+ same bytes)
ct = oracle(b"A" * 32)
if ct[0:16] == ct[16:32]:
    print("[*] ECB mode confirmed")
else:
    print("[!] Warning: may not be ECB")

# Step 3: recover byte by byte
known = b""
alphabet = [bytes([c]) for c in range(32, 127)]

for i in range(flag_len):
    block_idx = i // BS
    padding_len = BS - (i % BS) - 1
    prefix = b"A" * padding_len

    target = oracle(prefix)[block_idx * BS : (block_idx + 1) * BS]

    for ch in alphabet:
        test_input = prefix + known + ch
        test_ct = oracle(test_input)[block_idx * BS : (block_idx + 1) * BS]
        if test_ct == target:
            known += ch
            break

flag = known.decode()
print(f"[+] Recovered flag: {flag}")
assert flag.startswith("flag{") and flag.endswith("}"), "Flag check failed"
