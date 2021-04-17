import os
from typing import Dict
from pathlib import Path

from .error import NotAFileError
from .cfg_key import config_key


class UsrConfig:

    def __init__(self):
        self.__kv: Dict[str, str] = {}

    def dumps(self) -> str:
        result = ''
        for k, v in self.__kv.items():
            if k in config_key and k != 'Password':
                result += f'{k} = {v}\n'
        return result

    @staticmethod
    def gen_filename() -> str:
        return f'osu!.{os.getlogin()}.cfg'

    @staticmethod
    def parse_file(cfg_path: Path) -> 'UsrConfig':
        if not cfg_path.is_file():
            raise NotAFileError(f'Invalid config file: {cfg_path}')

        cfg = UsrConfig()

        content = cfg_path.read_text()
        for line in content.split('\n'):
            if not line or line.startswith('#'):
                continue

            ws = line.split('=')
            cfg_key = ws[0].strip()
            cfg.__kv[cfg_key] = ws[1].strip()

        return cfg
