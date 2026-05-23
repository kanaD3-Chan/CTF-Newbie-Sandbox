#!/usr/bin/env python3
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"\xf1\x07\x11\xdc\xed}U\xbb\x7f'\xdd#\xdc\xa0L\t"
flag = b'flag{aes_ecb_byte_by_byte}'

def oracle(plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext + flag, 16))

if __name__ == "__main__":
    data = sys.argv[1].encode() if len(sys.argv) > 1 else b""
    result = oracle(data)
    print(result.hex())
