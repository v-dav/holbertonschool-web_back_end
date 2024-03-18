#!/usr/bin/env python3
"""Exercice module to learn to work with Redis"""

import redis
from typing import Union
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
