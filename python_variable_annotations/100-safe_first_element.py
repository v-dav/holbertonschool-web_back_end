#!/usr/bin/env python3
"""A type annotated simple function"""

from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """A function that returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
