#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

from functools import wraps
import requests
import redis
from typing import Callable


def cache_results(method: Callable) -> Callable:
    """Decorator to cache the result of a function
    with an expiration time using Redis."""
    r = redis.Redis()

    @wraps(method)
    def wrapper(url: str) -> str:
        """ A wrapper method"""
        key = 'count:{}'.format(url)
        count = r.get(key)

        if count:
            r.incr(key)
        else:
            r.setex(key, 10, 1)

        return method(url)

    return wrapper


@cache_results
def get_page(url: str) -> str:
    """Obtain the HTML content
    of a particular URL and returns it."""

    response = requests.get(url)
    return response.text
