#!/usr/bin/python3

from urllib.parse import urljoin

base_url = "https://example.com/subdirectory/"
relative_url = "../page.html"

full_url = urljoin(base_url, relative_url)
print(full_url)
