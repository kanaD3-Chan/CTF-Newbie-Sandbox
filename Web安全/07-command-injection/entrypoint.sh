#!/bin/bash
echo "$FLAG" > /flag
chmod 644 /flag
apachectl start
tail -f /var/log/apache2/access.log