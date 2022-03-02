#!/usr/bin/env python3
import click
import synapseclient

from rdptoolkit.pusher import Pusher


@click.group(name="push", no_args_is_help=True)
def cli():
    """Push related commands"""


@cli.command(name="tools", no_args_is_help=True)
@click.option(
    "--tools_filepath",
    help="Tools filepath",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "--es_index",
    help="Elasticsearch Index",
    type=str,
    required=True,
)
def tools(tools_filepath, es_index):
    """Pushes the tools to ES."""
    pusher = Pusher()
    pusher.read_tools(tools_filepath)
    pusher.push_tools(es_index)


if __name__ == "__main__":
    cli()
