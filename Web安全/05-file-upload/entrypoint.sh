#!/bin/bash
set -e

# 写入 flag 并设置读取权限
echo "$FLAG" > /flag
chmod 644 /flag

# 确保上传目录存在
mkdir -p /var/www/html/uploads
chown -R www-data:www-data /var/www/html/uploads

exec apachectl -D FOREGROUND
