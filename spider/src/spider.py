#!/usr/bin/python3

import os
import click
import requests
from typing import List, Union, Optional
from urllib.parse import urlparse, urljoin, ParseResult
from urllib import robotparser

USER_AGENT = "SpiderBot"

def urlChecking(arg: List[Union[bool, int, str, str]]) -> None:
    result: ParseResult = urlparse(arg[3])
    print(result)
    if result.scheme == '':
        arg[3] = "http://" + arg[3]
        print(arg[3])
        urlChecking(arg)
    elif result.netloc == '':
        raise Exception('No URL Netloc')
    elif (result.scheme != "http" and result.scheme != "https") :
        print(arg[3])
        raise Exception('Invalid URL')

def mkdirSave(arg: List[Union[bool, int, str, str]]) -> None:
    if (os.path.exists(arg[2]) == False):
        print("Creating Directory ...")
        os.mkdir(arg[2])
    elif (os.path.isdir(arg[2]) == False):
        raise Exception("Invalid Diretory.")
    elif (os.access(arg[2], os.R_OK) == False or os.access(arg[2], os.W_OK) == False or os.access(arg[2], os.X_OK) == False):
        raise Exception("Permission Denied")
    return

def getContentFromUrl(arg: List[Union[bool, int, str, str]]) -> bytes:
    pureUrl: str = urlparse(arg[3]).scheme + "://" + urlparse(arg[3]).netloc
    robotUrl = pureUrl + '/robots.txt'
    if(requests.get(robotUrl).status_code == 200):
        pathToCheck = urlparse(arg[3]).path
        # class to parse robot file
        parseRobot = robotparser.RobotFileParser()
        parseRobot.set_url(robotUrl)
        parseRobot.read()
        check = parseRobot.can_fetch(USER_AGENT, pathToCheck)
        if (check == False):
            raise Exception("Robots.txt forbids path: ", pathToCheck)
        elif (check == True):
            print("Robots.txt allows path: ", pathToCheck)
        response = requests.get(arg[3])
        response.raise_for_status()
        return (response.content)
    return (666)

def downloadImagesRecursively(arg: List[Union[bool, int, str, str]]) -> None:
    return

def startScraping(arg: List[Union[bool, int, str, str]]) -> None:
    try:
        urlChecking(arg)
        mkdirSave(arg)
        content: bytes = getContentFromUrl(arg)
        if (content == 666):
            print("Error requesting the URL")
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
    arg: List[Union[bool, int, str, str]] = [r, l, p, url]
    startScraping(arg)

if __name__ == '__main__':
    main()
