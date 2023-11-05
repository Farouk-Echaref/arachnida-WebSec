#!/usr/bin/python3

import os
import click
import requests
from bs4 import BeautifulSoup

#avoiding duplications by using set()
unique_urls = set()

url = 'test.html'
def parseURL(url, depth):
    #un case of working on a website
    # r = requests.get(url)
    # if r.status_code == 200:
    #     html = r.text

    #in case of local HTML file
    with open(url, 'r') as html_file:
        html = html_file.read()
        soup = BeautifulSoup(html, 'lxml')
        for item in soup.find_all('img'):
            print(item['src'])
    # else:
    #     print("Request failed with status code:", response.status_code)
    #     exit(1)

parseURL(url,0)