#!/usr/bin/env python3
import requests

r = requests.get('http://127.0.0.1:13383/')
print('X-Flag:', r.headers.get('X-Flag'))
