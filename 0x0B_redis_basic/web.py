#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

from functools import wraps
import requests
import redis
from typing import Callable

r = redis.Redis()


def cache_results(method: Callable) -> Callable:
    """Decorator to cache the result of a function
    with an expiration time using Redis."""

    @wraps(method)
    def wrapper(url: str) -> str:
        """ A wrapper method"""
        key = 'count:{}'.format(url)

        r.incr(key)
        result = r.get(key)

        if result:
            return result.decode('utf-8')
        else:
            result = method(url)
            r.set(key, 0)
            r.setex(key, 10, result)
        return result

    return wrapper


@cache_results
def get_page(url: str) -> str:
    """Obtain the HTML content
    of a particular URL and returns it."""

    response = requests.get(url)
    return response.text
