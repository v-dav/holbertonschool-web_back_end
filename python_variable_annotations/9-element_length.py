#!/usr/bin/env python3
"""A type annotated simple function"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A type annotated function"""
    return [(i, len(i)) for i in lst]
