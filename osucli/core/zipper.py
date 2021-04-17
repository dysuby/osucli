import io
import zipfile
from typing import Iterable, Union, List, Tuple

from pathlib import Path


FileName = Path
FileData = bytes
FilePair = Tuple[FileName, FileData]


class Zip:

    @staticmethod
    def zip_up(elements: Iterable[Union[FileName, List[FilePair]]]) -> io.BytesIO:
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a") as f:
            for e in elements:
                if isinstance(e, Path):
                    f.write(e)
                elif isinstance(e, List):
                    for filename, data in e:
                        f.writestr(filename, data)

        return zip_buffer
