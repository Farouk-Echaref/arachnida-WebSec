#!/usr/bin/python3

import os
import click
import random
import requests
from bs4 import BeautifulSoup, ResultSet
from typing import List, Union, Optional
from urllib.parse import urlparse, urljoin, ParseResult
from urllib import robotparser

USER_AGENT = "SpiderBot"
EXT = [".jpg", ".jpeg", ".bmp", ".png", ".gif"]
storeURLS: set[str] = set()

def mkdirSave(arg: List[Union[bool, int, str, str]]) -> None:
    if (os.path.exists(arg[2]) == False):
        print("Creating Directory ...")
        os.mkdir(arg[2])
    elif (os.path.isdir(arg[2]) == False):
        raise Exception("Invalid Diretory.")
    elif (os.access(arg[2], os.R_OK) == False or os.access(arg[2], os.W_OK) == False or os.access(arg[2], os.X_OK) == False):
        raise Exception("Permission Denied")
    return

def urlChecking(arg: List[Union[bool, int, str, str]]) -> None:
    result: ParseResult = urlparse(arg[3])
    if result.scheme == '':
        arg[3] = "http://" + arg[3]
        urlChecking(arg)
    elif result.netloc == '':
        raise Exception('No URL Netloc')
    elif (result.scheme != "http" and result.scheme != "https"):
        raise Exception('Invalid URL')

def getContentFromUrl(url: str) -> Optional[bytes]:
    user_agents = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
] 
    user_agent = random.choice(user_agents) 
    headers = {'User-Agent': user_agent} 
    pureUrl: str = urlparse(url).scheme + "://" + urlparse(url).netloc
    robotUrl: str = pureUrl + '/robots.txt'
    if(requests.get(robotUrl).status_code == 200):
        pathToCheck = urlparse(url).path
        # class to parse robot file
        parseRobot = robotparser.RobotFileParser()
        parseRobot.set_url(robotUrl)
        parseRobot.read()
        check: bool = parseRobot.can_fetch(USER_AGENT, pathToCheck)
        if (check == False):
            raise Exception("Robots.txt forbids path: ", pathToCheck)
        elif (check == True):
            print("Robots.txt allows path: ", pathToCheck)
        response: response = requests.get(url, headers=headers)
        response.raise_for_status()
        return (response.content)
    return (666)

def getFullUrl(url: str, path: str) -> str:
    parsedUrl = urlparse(path)

    # If the path doesn't have a netloc (network location), 
    # it is a relative path, and the full URL is resolved using urljoin.
    if parsedUrl.netloc == '':
        return urljoin(url, parsedUrl.path)
    #If the path has a netloc but no scheme, it is assumed to be an HTTP link.
    elif parsedUrl.scheme == '':
        return 'http://' + parsedUrl.netloc + parsedUrl.path
    #If the path has both a scheme and a netloc, it is considered a complete URL.
    return parsedUrl.scheme + '://' + parsedUrl.netloc + parsedUrl.path

def downloadOneImg(arg: List[Union[bool, int, str, str]], fullImgUrl: str) -> None:
    imgName: str = os.path.basename(fullImgUrl)
    saveFile: str = os.path.join(arg[2], imgName)
    try:
        if os.path.exists(saveFile):
            raise Exception ('Image Duplicate => Skip')
        imgContent: bytes = getContentFromUrl(fullImgUrl)
        with open(saveFile, 'wb') as image:
            image.write(imgContent)
    except Exception as e:
        print(f"Error while downloading image: {e}")
    return

def imagesDownloader(arg: List[Union[bool, int, str, str]], soup: BeautifulSoup, incomingUrl: str) -> None:
    imgTags: ResultSet = soup.find_all('img')
    for img in imgTags:
        imgPath:  str = img.get('src')
        if imgPath and os.path.splitext(imgPath)[1].lower() not in EXT:
            continue
        fullImgUrl: str = getFullUrl(incomingUrl, imgPath)
        print(fullImgUrl)
        downloadOneImg(arg, fullImgUrl)

def retrieveNewLinks(incomingUrl: str, soup: BeautifulSoup) -> set[str]:
    storeAnchor: set = set()
    anchorTags: ResultSet = soup.find_all('a')
    for tag in anchorTags:
        href: str = tag.get('href')
        if not href:
            continue
        newLink = getFullUrl(incomingUrl, href)
        if newLink in storeAnchor or newLink == incomingUrl:
            continue
        #Internal Links Filtering/domain restriction
        checkbase: ParseResult = urlparse(incomingUrl)
        checHref: ParseResult = urlparse(newLink)
        if checkbase.netloc != checHref.netloc:
            continue
        storeAnchor.add(newLink)
    return (storeAnchor)

def recursiveImageDownloader(arg: List[Union[bool, int, str, str]], current_level: int, incomingUrl: str) -> None:
    # recursive base condition
    if current_level >= arg[1]:
        return
    if incomingUrl in storeURLS:
        return
    #global set to store unique urls
    storeURLS.add(incomingUrl)
    try:
        content: bytes = getContentFromUrl(incomingUrl)
        if (content == 666):
            raise Exception("Bad URL")
        soup: BeautifulSoup = BeautifulSoup(content, 'lxml')
        # print(soup)
        imagesDownloader(arg, soup, incomingUrl)
        if current_level + 1 < arg[1]:
            newLinks: set[str] = retrieveNewLinks(incomingUrl, soup)
            for link in newLinks:
                recursiveImageDownloader(arg, current_level + 1, link)
    except Exception as e:
        print(f"{e}")

def startScraping(arg: List[Union[bool, int, str, str]]) -> None:
    try:
        urlChecking(arg)
        mkdirSave(arg)
        recursiveImageDownloader(arg, 0, arg[3])
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
