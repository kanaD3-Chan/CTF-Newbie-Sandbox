#!/usr/bin/env python3
"""
DH small subgroup attack.
g has order 8 mod p, so only 8 possible shared secrets.
Try all of them to decrypt flag_enc.
"""
p = 65537
g = 4096
A = 65536
B = 256
flag_enc_hex = "676d60667a65695e726c606d6d5e72746366736e74715e68725e7664606a7c"
flag_enc = bytes.fromhex(flag_enc_hex)

# Brute-force all possible private keys (0 to 7, since order of g is 8)
for a_try in range(8):
    if pow(g, a_try, p) == A:
        shared = pow(B, a_try, p)
        shared_bytes = shared.to_bytes((shared.bit_length() + 7) // 8, 'big')
        flag = bytes(c ^ shared_bytes[i % len(shared_bytes)] for i, c in enumerate(flag_enc))
        print(f"Found a = {a_try}, shared = {shared}, flag = {flag}")
        break
else:
    print("Could not find a via brute force — trying all shared secrets directly")
    for s_try in range(8):
        candidate_shared = pow(g, s_try, p)
        shared_bytes = candidate_shared.to_bytes((candidate_shared.bit_length() + 7) // 8, 'big')
        flag = bytes(c ^ shared_bytes[i % len(shared_bytes)] for i, c in enumerate(flag_enc))
        print(f"  shared={candidate_shared}: {flag}")
