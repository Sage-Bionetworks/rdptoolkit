#!/usr/bin/env python3
import click

# from rdptoolkit import upload


@click.group(name='push', no_args_is_help=True)
def cli():
    """Push related commands"""


@cli.command(name="cckp-tools", no_args_is_help=True)
@click.option('--tools_filepath', help='Tools filepath',
              type=click.Path(exists=True), required=True)
def cckp_tools(tools_filepath):
    """Pushes the CCKP tools to ES."""
    print('Hello World')


if __name__ == '__main__':
    cli()