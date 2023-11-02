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


def start_scraping(r, p):
    """A program for downloading files."""
    click.echo(f"Recursive Download: {r}")
    click.echo(f"Download Path: {p}")

@click.command()
@click.option('-r', default=1, help='Recursive Download')
@click.option('-p', prompt='Download Path')
def main(r, p):
    click.echo("Welcome to fechScraping:")
    start_scraping(r, p)
    

if __name__ == '__main__':
    main()