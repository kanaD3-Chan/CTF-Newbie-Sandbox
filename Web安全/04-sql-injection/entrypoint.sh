#!/bin/bash

# 初始化 MySQL 数据目录
if [ ! -d /var/lib/mysql/mysql ]; then
    mkdir -p /var/lib/mysql
    chown -R mysql:mysql /var/lib/mysql
    mysqld --initialize-insecure --user=mysql || echo "[!] mysql init failed"
fi

# 启动 MySQL（后台）
mysqld --user=mysql &
pid="$!"

# 等 MySQL 就绪（最多等 15 秒）
for i in $(seq 1 15); do
    if mysqladmin ping --silent 2>/dev/null; then
        break
    fi
    sleep 1
done

# 导入数据（失败不阻塞 Apache 启动）
sed -i "s|FLAG_PLACEHOLDER|${FLAG}|" /tmp/init.sql
mysql -u root < /tmp/init.sql 2>/dev/null || echo "[!] mysql import failed"

# 前台启动 Apache
exec apache2ctl -D FOREGROUND
