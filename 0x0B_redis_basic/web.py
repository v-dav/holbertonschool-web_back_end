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
    def wrapper(url):
        """ Wrapper method
        """
        r.incr(f"count:{url}")
        cached_response = r.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = method(url)
        r.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@cache_results
def get_page(url: str) -> str:
    """Obtain the HTML content
    of a particular URL and returns it."""

    response = requests.get(url)
    return response.text
