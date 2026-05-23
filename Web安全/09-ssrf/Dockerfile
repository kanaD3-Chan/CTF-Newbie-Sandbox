FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y apache2 php libapache2-mod-php && apt-get clean
RUN rm -f /var/www/html/index.html
RUN sed -i 's/allow_url_fopen = Off/allow_url_fopen = On/' /etc/php/*/apache2/php.ini 2>/dev/null; echo "allow_url_fopen = On" >> /etc/php/*/apache2/php.ini 2>/dev/null || true

COPY index.php /var/www/html/
COPY entrypoint.sh /

EXPOSE 80
CMD ["/bin/bash", "/entrypoint.sh"]