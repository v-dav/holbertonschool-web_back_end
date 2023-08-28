#!/usr/bin/env python3
"""A type annotated simple function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """A function that returns a tuple"""
    return tuple([k, float(v * v)])
