import click
from typing import Tuple

def getContentFromUrl(argument: Tuple[bool, int, str, str]) -> None:
    return

def urlChecking(argument: Tuple[bool, int, str, str]) -> None:
    return

def downloadImagesRecursively(arguments: Tuple[bool,int,str,str]) -> None:
    return

def startScraping(arguments: Tuple[bool,int,str,str]) -> None:
    try:
        urlChecking(arguments)
        downloadImagesRecursively(arguments)
    except KeyboardInterrupt:
        #some behaviour for the signal

        #exi status code for SIGINT
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
    arguments: Tuple[bool, int, str, str] = (r, l, p, url)
    startScraping(arguments)

if __name__ == '__main__':
    main()
