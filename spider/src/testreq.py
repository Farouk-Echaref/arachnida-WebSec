#!/usr/bin/python3

import requests

url = "http://commons.wikimedia.org/robots.txt"
res = requests.get(url)

print(res)