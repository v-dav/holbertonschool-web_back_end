#!/usr/bin/env python3
"""A type annotated simple function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type annotated function returning a function"""
    def the_multiplier(n: float) -> float:
        """The inner multiplier function"""
        return n * multiplier
    return the_multiplier
