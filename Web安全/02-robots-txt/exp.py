#!/usr/bin/env python3
import requests

base = 'http://127.0.0.1:13382'

# 1. 读 robots.txt，找 Disallow 路径
r = requests.get(f'{base}/robots.txt')
print(r.text)

# 2. 访问 /flag.html
r = requests.get(f'{base}/flag.html')
import re
m = re.search(r'flag\{[^}]+\}', r.text)
if m:
    print('FLAG:', m.group())
