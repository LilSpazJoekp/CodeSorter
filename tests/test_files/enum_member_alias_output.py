from enum import Enum, auto


class _Sentinel(Enum):
    CACHE_MISS = auto()


CACHE_MISS = _Sentinel.CACHE_MISS


def helper():
    return CACHE_MISS
