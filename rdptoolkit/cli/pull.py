#!/usr/bin/env python3
import click

from rdptoolkit.puller import Puller


@click.group(name='pull', no_args_is_help=True)
def cli():
    """Pull related commands"""


@cli.command(name="nlpsandbox-tools")
def nlpsandbox_tools():
    """Collect, format and save NLP Sandbox tools data locally."""
    puller = Puller()
    puller.pull_from_nlpsandbox()


if __name__ == '__main__':
    cli()
