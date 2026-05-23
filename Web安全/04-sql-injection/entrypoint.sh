#!/bin/bash
set -e

# 初始化 MySQL 数据目录
if [ ! -d /var/lib/mysql/mysql ]; then
    mkdir -p /var/lib/mysql
    chown -R mysql:mysql /var/lib/mysql
    mysqld --initialize-insecure --user=mysql
fi

# 启动 MySQL
mysqld --user=mysql &
pid="$!"

# 等 MySQL 就绪
for i in {1..30}; do
    if mysqladmin ping --silent 2>/dev/null; then
        break
    fi
    sleep 1
done

# 替换 init.sql 中的占位符并导入
sed -i "s|FLAG_PLACEHOLDER|${FLAG}|" /tmp/init.sql
mysql -u root < /tmp/init.sql

# 启动 Apache（前台）
exec apachectl -D FOREGROUND
