#!/usr/bin/env python3
"""A type annotated simple function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """A simple sum function with list parameter"""
    return sum(input_list)
