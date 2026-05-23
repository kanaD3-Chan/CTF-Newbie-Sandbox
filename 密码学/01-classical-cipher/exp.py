#!/usr/bin/env python3
"""Caesar cipher: try all 25 shifts."""
ciphertext = "jpek{geiwev_gmtliv_mw_jyr}"

for shift in range(1, 26):
    plain = []
    for c in ciphertext:
        if c.islower():
            plain.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
        elif c.isupper():
            plain.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
        else:
            plain.append(c)
    result = ''.join(plain)
    if result.startswith("flag{"):
        print(f"Shift {shift}: {result}")
        break
