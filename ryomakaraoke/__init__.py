from ryomakaraoke.karaoke import Karaoke
from ryomakaraoke.lib.get_platform import get_platform
from ryomakaraoke.version import __version__

PACKAGE = __package__
VERSION = __version__

__all__ = [
    "VERSION",
    "PACKAGE",
    Karaoke.__name__,
    get_platform.__name__,
]
