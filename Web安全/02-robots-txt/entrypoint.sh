#!/bin/sh
sed -i "s|FLAG_PLACEHOLDER|${FLAG}|" /usr/share/nginx/html/flag.html
exec nginx -g 'daemon off;'
