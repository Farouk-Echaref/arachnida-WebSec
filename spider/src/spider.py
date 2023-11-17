import click
from typing import List,Union

def startScraping(arguments: List[Union[bool,int,str,str]]) -> None:


@click.command()
@click.option('-r', is_flag=True, default=False, help='Enable Recursive Download')
@click.option('-l', type=int, default=5, help='Set Depth Of Recursive Download')
@click.option('-p', type=str, default='./data/', help='Set Download Path')
@click.argument('url', type=str)
def main(r: bool, l: int, p: str, url: str) -> None:
    click.echo('Spider has started crawling: ')
    arguments: List[Union[bool, int, str, str]] = [r, l, p, url]
    startScraping(arguments)

if __name__ == '__main__':
    main()
