# WP：01-view-source

## 题目信息

- 类型：查看源代码
- 难度：Easy
- 端口：13381

## 解题

浏览器打开题目页面，按 `Ctrl+U`（或右键→查看页面源代码），在 HTML 顶部找到注释：

```html
<!-- flag{...} -->
```

也可以用 curl：

```bash
curl http://172.16.173.140:13381/ | grep '<!--'
```

## Flag

`flag{view_source_is_the_first_step}`
