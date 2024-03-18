#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
from typing import Any
import uuid


class Cache():
    """The cache class"""

    def __init__(self) -> None:
        """The constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """A method to store the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
