#!/usr/bin/env python3
"""A type annotated simple function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A type annotated sum function"""
    return float(sum(mxd_lst))
