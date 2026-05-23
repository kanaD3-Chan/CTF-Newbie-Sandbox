#!/usr/bin/env python3
# RC4 key reuse attack
# c1 encrypts known msg1 with keystream K
# c2 encrypts msg2 with SAME keystream K
# => c1 XOR c2 = msg1 XOR msg2  (same length)
# => msg2 = (c1 XOR c2) XOR msg1

c1_hex = "21eab1f54abc504b4dc7c3fd87e6143cf7889b19852473f1b8fc788a8a9d49c1698d458118e31267917b565c6457186214244baf94773180d0827f4e37fdb0ad3b6e3b91"
c2_hex = "21eab1f54abc504b4dc7c3fd87e6143cf7889b19852473f1b8fc788a8a9d49c157b97cbe3bc9290b96486b7d637d254f3f194c9ebf7005bdfcb2467a12fdb0ad3b6e3b91"
msg1  = b"This message contains the flag: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX in it."

c1 = bytes.fromhex(c1_hex)
c2 = bytes.fromhex(c2_hex)

# c1 XOR c2 = msg1 XOR msg2 (keystream cancels out)
xor_ct = bytes(a ^ b for a, b in zip(c1, c2))

# Recover msg2
msg2 = bytes(a ^ b for a, b in zip(xor_ct, msg1))

print(f"Recovered msg2: {msg2.decode()}")

# Extract flag
import re
m = re.search(rb'flag\{[^}]+\}', msg2)
if m:
    print(f"Flag: {m.group().decode()}")
