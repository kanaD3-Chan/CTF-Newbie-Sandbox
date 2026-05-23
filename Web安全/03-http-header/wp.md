# WP：03-http-header

## 题目信息

- 类型：HTTP 响应头信息泄露
- 难度：Easy
- 端口：13383

## 解题

打开开发者工具 `F12` → Network → 刷新 → 点击请求 → Response Headers，找到：

```
X-Flag: flag{...}
```

或用 curl：

```bash
curl -si http://172.16.173.140:13383/ | grep -i x-flag
```

## Flag

`flag{http_headers_tell_secrets}`
