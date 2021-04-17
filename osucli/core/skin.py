import io
from pathlib import Path

from .error import NotDirectoryError
from .zipper import Zip


class Skin:

    def __init__(self, skin_dir: Path):
        if not skin_dir.is_dir():
            raise NotDirectoryError(f'Invalid skin dir: {skin_dir}')
        self.path = skin_dir

    def archive(self) -> io.BytesIO:
        return Zip.zip_up(self.path.iterdir())

    @property
    def name(self) -> str:
        return f'{self.path.name}.osk'
