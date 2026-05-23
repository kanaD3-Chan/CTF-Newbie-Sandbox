FROM php:8.0-apache

LABEL auther="SLsec"

# Apache 初始化
RUN a2enmod rewrite

# 安装 MySQL 客户端和服务器
RUN apt update && \
    apt install -y default-mysql-client default-mysql-server

# 配置 mysql
RUN docker-php-source extract && \
    docker-php-ext-install pdo_mysql mysqli && \
    docker-php-source delete && \
    mysql_install_db --user=mysql --datadir=/var/lib/mysql

# 复制源码
COPY index.php /var/www/html/
COPY connect.php /var/www/html/
COPY init.sql /var/db.sql

# 配置数据库数据（构建时初始化，避免运行时等待）
RUN sh -c 'mysqld_safe &' \
    && sleep 5s \
    && mysqladmin -uroot password '123456' \
    && mysql -e "source /var/db.sql;" -uroot -p123456 \
    && mysqladmin -uroot -p123456 shutdown

# 入口点脚本（运行时注入动态 FLAG）
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /var/www/html
EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]
