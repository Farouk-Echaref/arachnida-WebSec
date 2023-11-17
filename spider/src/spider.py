#!/usr/bin/python3

import click
from typing import List, Union, Optional
from urllib.parse import urlparse, urljoin, ParseResult

def getContentFromUrl(arg: List[Union[bool, int, str, str]]) -> bytes:
    return b""  # Placeholder return value

def urlChecking(arg: List[Union[bool, int, str, str]]) -> None:
    result: ParseResult = urlparse(arg[3])
    print(result)

def downloadImagesRecursively(arg: List[Union[bool, int, str, str]]) -> None:
    return

def startScraping(arg: List[Union[bool, int, str, str]]) -> None:
    try:
        urlChecking(arg)
        content: bytes = getContentFromUrl(arg)
        downloadImagesRecursively(arg)
    except KeyboardInterrupt:
        # Some behavior for the signal
        # Exit status code for SIGINT
        exit(130)
    except Exception as e:
        print(f"Caught General Exception: {e}")

@click.command()
@click.option('-r', is_flag=True, default=False, help='Enable Recursive Download')
@click.option('-l', type=int, default=5, help='Set Depth Of Recursive Download')
@click.option('-p', type=str, default='./data/', help='Set Download Path')
@click.argument('url', type=str)
def main(r: bool, l: int, p: str, url: str) -> None:
    click.echo('Spider has started crawling: ')
    arg: List[bool, int, str, str] = [r, l, p, url]
    startScraping(arg)

if __name__ == '__main__':
    main()
