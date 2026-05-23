FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 安装 Apache + PHP + MySQL
RUN apt-get update && apt-get install -y \
    apache2 \
    php \
    libapache2-mod-php \
    php-mysql \
    mysql-server && \
    apt-get clean

RUN rm -f /var/www/html/index.html
COPY index.php /var/www/html/
COPY init.sql /tmp/init.sql
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80
CMD ["/entrypoint.sh"]
