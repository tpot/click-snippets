import click

@click.command()
def simple():
    """Funky command"""
    click.echo('Funky command')

if __name__ == '__main__':
   simple()
