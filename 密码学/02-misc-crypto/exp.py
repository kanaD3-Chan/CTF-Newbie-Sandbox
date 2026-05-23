#!/usr/bin/env python3
"""Base58 decode."""
import base58

with open('encoded.txt') as f:
    encoded = f.read().strip()

decoded = base58.b58decode(encoded).decode()
print(f"Decoded: {decoded}")
# Extract flag
if decoded.startswith("flag{"):
    print(f"Flag: {decoded}")
