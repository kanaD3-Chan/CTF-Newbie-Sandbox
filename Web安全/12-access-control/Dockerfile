FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y apache2 php libapache2-mod-php && apt-get clean
RUN rm -f /var/www/html/index.html

COPY index.php /var/www/html/
COPY entrypoint.sh /

EXPOSE 80
CMD ["/bin/bash", "/entrypoint.sh"]