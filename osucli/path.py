from pathlib import Path


def get_default_osu_path() -> Path:
    return Path.home() / 'AppData/Local/osu!'
