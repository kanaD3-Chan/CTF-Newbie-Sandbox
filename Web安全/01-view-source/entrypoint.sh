#!/bin/sh
# 用环境变量 FLAG 替换 HTML 注释占位符，然后启动 nginx
sed -i "s|<!-- FLAG_PLACEHOLDER -->|<!-- ${FLAG} -->|" /usr/share/nginx/html/index.html
exec nginx -g 'daemon off;'
