import platform
from pathlib import Path

import typer

from .path import get_default_osu_path

app = typer.Typer(name='osucli', help='Make osu! great again in terminal')

osu_path_option = typer.Option(get_default_osu_path(),
                               '--osu_path', '-P', show_default=False,
                               help='osu root path, use default path if not specified')


@app.callback()
def check_os():
    if platform.system() != 'Windows':
        typer.echo('osucli only support windows')
        raise typer.Exit()


@app.command('archive')
def archive_usr_data(osu_path: Path = osu_path_option,
                     output: Path = typer.Option(Path('.') / 'output.zip', '--output', '-o', help='output path')):
    """
    Archive your config, skins and songs
    """
    typer.echo(osu_path)
    pass

