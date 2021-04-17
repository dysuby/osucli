class OsuCliError(Exception):
    pass


class NotDirectoryError(OsuCliError, NotADirectoryError):
    pass


class NotAFileError(OsuCliError):
    pass
