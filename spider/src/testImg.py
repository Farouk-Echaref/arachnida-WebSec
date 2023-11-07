#!/usr/bin/python3

import os
import click
import requests
from bs4 import BeautifulSoup

#avoiding duplications by using set()
unique_urls = set()

url = 'https://images.unsplash.com/photo-1696075619078-6cb640d329ec?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw3fHx8ZW58MHx8fHx8'
def parseURL(url, depth):
    #un case of working on a website
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        print(soup)
        # for item in soup.find_all('img'):
        #     print(item['src'])
    # else:
    #     print("Request failed with status code:", response.status_code)
    #     exit(1)

parseURL(url,0)