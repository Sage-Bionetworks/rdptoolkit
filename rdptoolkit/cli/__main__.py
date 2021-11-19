#!/usr/bin/env python3
import click

from .. import __version__
from . import push

@click.group()
@click.version_option(__version__)
def cli():
    """Resource Discovery Portal toolkit"""

def main():
    cli.add_command(push.cli)
    cli()