#!/usr/bin/env python3
"""PHP MD5 magic hashes."""
# The answer is two strings whose MD5 hashes both start with "0e" followed by only digits
# In PHP, "0eNNNNN" == 0.0 in loose comparison (==), so any two such hashes compare equal

answer = "240610708 QNKCDZO"
print(f"Submit: {answer}")

# Verify
import hashlib
h1 = hashlib.md5(b"240610708").hexdigest()
h2 = hashlib.md5(b"QNKCDZO").hexdigest()
print(f"MD5('240610708') = {h1}")
print(f"MD5('QNKCDZO')   = {h2}")
print(f"Both start with '0e' and are all digits: {h1.startswith('0e') and h2.startswith('0e') and h1[2:].isdigit() and h2[2:].isdigit()}")
