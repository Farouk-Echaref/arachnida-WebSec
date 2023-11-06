#!/usr/bin/python3

import time
import validators
import os
import click
import requests
from bs4 import BeautifulSoup

#set of unique URLs
uniqueURLs = set()

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

def validateURLs(URLs: set):
    for url in URLs:
        isValid = validateURLs.url(url)
        if isValid:
            continue
        else :
            URLs.remove(url)

def download_img(url, path, down_iter, extension):
    #check if directory exists, if not download it
    if not (os.path.exists(url) and os.path.isdir(path)):
        os.makedirs(path)
    full_path = path + 'img' + str(down_iter) + extension
    #get the body of the HTTP response
    response = requests.get(url, stream=True)
    #status_code 200 => successful response 
    if (response.status_code == 200):
        with open(full_path, 'wb') as output_file:
            for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        output_file.write(chunk)
        print('Complete File Download!')
    else:
        print("Request failed with status code:", response.status_code)
        exit(1)
    down_iter += 1
    

def combined_options(combined: str, url: str):
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

def loopURLs(URLs: set):
    finalURLSet = set()
    for url in URLs:
        finalURLSet.update(findURLS(url))
        #maybe sleep()
        time.sleep(0.1)
    return (finalURLSet)


#extract urls from one link
def findURLS(url: str):
    tempURLset = set()
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        # look for link tags in html (<a>)
        for item in soup.find_all('a'):
            tempURLset.add(item.get('href'))
    else:
        # maybe throw exception
        print("Request failed with status code:", response.status_code)
        exit(1)
    validateURLs(tempURLset)
    return (tempURLset)

def recursiveFindURL(url: str, depth: int, currentDepth: int):
    # add the first url for the first time
    newURLSet = set()
    newURLSet.add(url)

    if len(newURLSet) == 1:
        newURLSet.update(findURL(url))
    while currentDepth <= depth:
        newURLSet.update(loopURLs(newURLSet))
        validateURLs(newURLSet)
        currentDepth += 1
    return (newURLSet)


def starScraping(r: bool, l: int, p: str, url: str):
    """A program for downloading files."""
    # click.echo(f"URL: {url}.")
    if r and l is not None:
        # Both -r and -l were provided with their respective arguments.
        click.echo(f"r is true and l is set to user value {l}")
    elif r:
        # Only -r was provided without -l.
        click.echo(f"r is true but l is set to default value")
    elif r is False and l is True:
        # -r is false but -l is set.
        click.echo(f"Error")
    return (recursiveFindURL(url, l, 0))

@click.command()
@click.option('-r', '--recursive', is_flag=True, default=False, help='Enable Recursive Download')
@click.option('-l', '--depth', type=int, default=5, help='Set Depth Of Recursive Download')
@click.option('-p', '--path', type=str, default='./data/', help='Set Download Path')
@click.option('-c', '--combined', is_flag=True, default=False, help='Combined Options')
@click.argument('url', type=str)
def main(r: bool, l: int, p: str, combined: str, url: str):
    click.echo("Welcome to fechScraping:")
    # combined_options(combined, url)
    # parse Urls
    uniqueURLs = startScraping(r, l, p, url)

    # download each URL alone
    

if __name__ == '__main__':
    main()