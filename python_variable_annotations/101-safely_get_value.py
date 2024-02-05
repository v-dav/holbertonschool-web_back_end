#!/usr/bin/env python3
"""A type annotated simple function"""

from typing import Any, Mapping, TypeVar, Optional, Union

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any, default: Optional[T]) -> Union[Any, T]:
    """A type annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
