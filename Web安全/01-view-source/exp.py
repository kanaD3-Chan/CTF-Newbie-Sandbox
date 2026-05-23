#!/usr/bin/env python3
import requests

url = 'http://127.0.0.1:13381/'
r = requests.get(url)
for line in r.text.splitlines():
    if '<!--' in line and 'flag' in line.lower():
        print(line.strip())
