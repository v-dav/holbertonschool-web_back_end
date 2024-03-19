#!/usr/bin/env python3
"""Exercice module to learn to work with Redis"""

import redis
from typing import Callable, Optional, Union
import uuid


class Cache():
    """The cache class"""

    def __init__(self) -> None:
        """The constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A method to store the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Reading from redis and reconering original key
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """From redis bytes to string"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: int) -> int:
        """
        From redis bytes to integer
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
