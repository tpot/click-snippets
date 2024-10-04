import click

@click.command()
@click.option('-v', '--verbose', help='Display verbose output.')
@click.argument('input1', type=str, )
@click.argument('input2', type=str, )
def simple(verbose, input1, input2):
    """Funky command"""

    click.echo('Funky command')

    if verbose:
        click.echo('Displaying verbose output')

    click.echo(f'First input is {input1}')
    click.echo(f'Second input is {input2}')

if __name__ == '__main__':
   simple()
