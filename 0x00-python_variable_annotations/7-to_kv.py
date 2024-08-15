#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """ Complex types """
    return (k, float(v ** 2))
