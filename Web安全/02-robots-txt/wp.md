# WP：02-robots-txt

## 题目信息

- 类型：robots.txt 信息泄露
- 难度：Easy
- 端口：13382

## 解题

访问 `/robots.txt`，看到：

```
User-agent: *
Disallow: /secret/
Disallow: /admin/
Disallow: /flag.html
```

直接访问 `/flag.html` 即可拿到 flag。

```bash
curl http://172.16.173.140:13382/robots.txt
curl http://172.16.173.140:13382/flag.html
```

## Flag

`flag{robots_txt_is_not_a_secret}`
