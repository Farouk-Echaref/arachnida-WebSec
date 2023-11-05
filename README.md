# arachnida-WebSec
Introductory project on scraping but also on the discovery of metadatas. (Cybersecurity/Web)

## CLI Interface (Click)
- Using Click to handle options and arguments parsing

## Use Requests Library for HTTP requests

## Beautifulsoup (handle HTTP requests and File manipulation)
- retrieve page content using Get request
- store content -> pass it to BS for parsing using a parser
- find <img> tag ex: "<img alt="A Light in the Attic" class="thumbnail" src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/>"
- what we are interested in is the src part, we need to retrieve it: "'media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg'"
- combine URLs
    - url_base = "http://books.toscrape.com/" #Original website
    - url_ext = example.attrs['src'] #The extension you pulled earlier
    - full_url = url_base + url_ext #Combining first 2 variables to create a complete URL
- request the full_url (check return value == status code should be 200)
- store content and right it in a file

## download a file given by url and pathname
- check if directory exiss, if not create it 
- download the body of a response by chunk
- get the size of the body
- get filename
- write to disk

## recursive parsing of URLs
- Recursive finding of URLs: parse all URLs and store them in a list (check for duplications, check for invalid ones...)
    - 