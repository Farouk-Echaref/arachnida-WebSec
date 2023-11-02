#!/usr/bin/python3

import click
import requests
from bs4 import BeautifulSoup

class Params:
    def __init__(self, url="", method="unoDepth", depth=5, path="./data/"):
        self.url = url
        self.method = method
        self.depth = depth
        self.path = path
    
    #Verify (test method)
    def __str__(self):
        return f"URL: {self.url}, Method: {self.method}, Depth: {self.depth}"


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
    click.echo(f"URL: {url}.")
    if r and l is not None:
        # Both -r and -l were provided with their respective arguments.
        click.echo(f"Recursive download with depth {l} and download path {p}.")
    elif r:
        # Only -r was provided without -l.
        click.echo(f"Recursive download with default depth and download path {p}.")
    else:
        # No -r provided.
        click.echo(f"Downloading without recursion to path {p}.")


@click.command()
@click.option('-r', is_flag=True, help='Enable Recursive Download')
@click.option('-l', type=int, help='Set Depth Of Recursive Download')
@click.option('-p', type=str, help='Set Download Path')
@click.option('-c', '--combined', type=str, help='Combined Options')
@click.argument('url', type=str)
def main(r, l, p, combined, url):
    click.echo("Welcome to fechScraping:")
    #already handled by click
    #if url is None:
    #        click.echo("Invalid! Provide a URL.")
    #        exit(1)
    combined_options(combined, url)
    start_scraping(r, l, p, url)
    

if __name__ == '__main__':
    main()