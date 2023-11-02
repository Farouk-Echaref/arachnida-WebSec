#!/usr/bin/python3

import click

class Params:
    def __init__(self, url="", method="unoDepth", depth=5, path="./data/"):
        self.url = url
        self.method = method
        self.depth = depth
        self.path = path
    
    #Verify (test method)
    def __str__(self):
        return f"URL: {self.url}, Method: {self.method}, Depth: {self.depth}"


def combined_options(combined):
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
                click.echo("Unknown Option: {c}")
                

def start_scraping(r, l, p):
    """A program for downloading files."""
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
@click.option('-p', type=str, prompt='Download Path', help='Set Download Path')
@click.option('-c', '--combined', type=str, help='Combined Options')
def main(r, l, p, combined):
    click.echo("Welcome to fechScraping:")
    combined_options(combined)
    start_scraping(r, l, p)
    

if __name__ == '__main__':
    main()