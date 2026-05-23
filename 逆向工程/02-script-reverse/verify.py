#!/usr/bin/env python3
import sys

def check(s):
    data = [
        0x33, 0x39, 0x34, 0x32, 0x2e, 0x25, 0x2c, 0x62,
        0x3d, 0x65, 0x3b, 0x0a, 0x37, 0x2c, 0x21, 0x66,
        0x36, 0x65, 0x31, 0x66, 0x0a, 0x27, 0x66, 0x23,
        0x66, 0x27, 0x26, 0x66, 0x28
    ]
    if len(s) != len(data):
        return False
    for i, c in enumerate(s):
        if (ord(c) ^ 0x55) != data[i]:
            return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 verify.py <flag>")
        return
    if check(sys.argv[1]):
        print("Correct!")
    else:
        print("Wrong!")

if __name__ == "__main__":
    main()
