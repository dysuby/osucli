from pathlib import Path

from .error import NotDirectoryError


class Beatmap:

    def __init__(self, beatmap_dir: Path):
        if not beatmap_dir.is_dir():
            raise NotDirectoryError(f'Invalid beatmap dir: {beatmap_dir}')
        self.path = beatmap_dir

    @property
    def identifier(self) -> str:
        number = self.path.name.split()[0]
        if number.isdigit():
            return number
        else:
            return self.path.name
