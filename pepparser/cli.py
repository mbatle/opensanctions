import click
import logging

from pepparser.emitter import Emitter
from pepparser.parsers.ofac import ofac_parse
from pepparser.parsers.sdfm_blacklist import sdfm_parse
from pepparser.parsers.cia_world_leaders import worldleaders_parse
from pepparser.parsers.every_politician import everypolitician_parse


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    fmt = '[%(levelname)-8s] %(name)-12s: %(message)s'
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format=fmt)
    logging.getLogger('requests').setLevel(logging.WARNING)


@cli.group()
def parse():
    pass


@parse.command()
@click.option('--sdn', default=False, is_flag=True)
@click.option('--consolidated', default=False, is_flag=True)
@click.argument('xmlfile')
def ofac(sdn, consolidated, xmlfile):
    emit = Emitter()
    ofac_parse(emit, sdn, consolidated, xmlfile)


@parse.command()
@click.argument('xmlfile')
def sdfm(xmlfile):
    emit = Emitter()
    sdfm_parse(emit, xmlfile)


@parse.command()
@click.argument('jsonfile')
def worldleaders(jsonfile):
    emit = Emitter()
    worldleaders_parse(emit, jsonfile)


@parse.command()
@click.argument('jsonfile')
def everypolitician(jsonfile):
    emit = Emitter()
    everypolitician_parse(emit, jsonfile)


if __name__ == '__main__':
    cli()