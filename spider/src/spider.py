#!/usr/bin/python3

import os
import click
import requests
from bs4 import BeautifulSoup

#in case i wanted to work with OOP, for now no need 
class Params:
    def __init__(self, url="", method="unoDepth", depth=5, path="./data/"):
        self.url = url
        self.method = method
        self.depth = depth
        self.path = path
    
    #Verify (test method)
    def __str__(self):
        return f"URL: {self.url}, Method: {self.method}, Depth: {self.depth}"

def download_img(url, path):
    #check if directory exists, if not download it
    if not (os.path.exists(url) and os.path.isdir(path)):
        os.makedirs(path)
    #get the body of the HTTP response
    response = requests.get(url, stream=True)
    #status_code 200 => successful response 
    if (response.status_code == 200):

    else:
        print("Request failed with status code:", response.status_code)
        exit(1)
    

def combined_options(combined, url):
    if combined:
        for c in combined:
            if c == 'r':
                #handle -r
                click.echo("Recursive Download")
            elif c == 'l':
                #handle -l
                click.echo("Recursive Download Depth")
            elif c == 'p':
                #handle -p
                click.echo("Setting Download Path")
            else:
                click.echo(f"Unknown Option: {c}")
                

def start_scraping(r, l, p, url):
    """A program for downloading files."""
    # click.echo(f"URL: {url}.")
    # if r and l is not None:
    #     # Both -r and -l were provided with their respective arguments.
    #     click.echo(f"Recursive download with depth {l} and download path {p}.")
    # elif r:
    #     # Only -r was provided without -l.
    #     click.echo(f"Recursive download with default depth and download path {p}.")
    # else:
    #     # No -r provided.
    #     click.echo(f"Downloading without recursion to path {p}.")
    
    r = requests.get(url)
    if r.status_code == 200:
        htmldata = r.text  
        soup = BeautifulSoup(htmldata, 'html.parser')  
        for item in soup.find_all('img'): 
            print(item['src'])
    else:
        print("Request failed with status code:", response.status_code)
        exit(1)

@click.command()
@click.option('-r', is_flag=True, help='Enable Recursive Download')
@click.option('-l', type=int, help='Set Depth Of Recursive Download')
@click.option('-p', type=str, help='Set Download Path')
@click.option('-c', '--combined', type=str, help='Combined Options')
@click.argument('url', type=str)
def main(r, l, p, combined, url):
    click.echo("Welcome to fechScraping:")
    combined_options(combined, url)
    start_scraping(r, l, p, url)
    

if __name__ == '__main__':
    main()