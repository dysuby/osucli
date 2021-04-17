from pathlib import Path
from typing import Iterable

from .skin import Skin
from .beatmap import Beatmap
from .cfg import UsrConfig


class OsuFileManager:

    def __init__(self, osu_path: Path):
        self.root_path: Path = osu_path

    def skins(self) -> Iterable[Skin]:
        skins_dir = self.root_path / 'Skins'
        if not skins_dir.is_dir():
            raise NotADirectoryError('Invalid Skins dir')

        for skin in skins_dir.iterdir():
            yield Skin(skin)

    def beatmaps(self):
        # there is a non-changeable config `BeatmapDirectory`
        beatmaps_dir = self.root_path / 'Songs'
        if not beatmaps_dir.is_dir():
            raise NotADirectoryError('Invalid Songs dir')
        for beatmap in beatmaps_dir.iterdir():
            yield Beatmap(beatmap)

    def usr_cfg(self) -> UsrConfig:
        return UsrConfig.parse_file(self.root_path / UsrConfig.gen_filename())
