from enum import Enum, auto


def helper():
    return CACHE_MISS


class _Sentinel(Enum):
    CACHE_MISS = auto()


CACHE_MISS = _Sentinel.CACHE_MISS
