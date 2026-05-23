#!/bin/bash

# 启动 MySQL
mysqld_safe &

mysql_ready() {
	mysqladmin ping --socket=/run/mysqld/mysqld.sock --user=root --password=123456 > /dev/null 2>&1
}

while !(mysql_ready)
do
	echo "waiting for mysql ..."
	sleep 2
done

# 动态 FLAG 注入
INSERT_FLAG="${FLAG:-flag{TEST_Dynamic_FLAG}}"
mysql -u root -p123456 -e "
USE ctf;
UPDATE users SET flag='$INSERT_FLAG' WHERE username='admin';
"

# 启动 Apache（前台）
source /etc/apache2/envvars
exec apache2 -D FOREGROUND
