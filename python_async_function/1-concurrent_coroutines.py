#!/usr/bin/env python3
"""A module with two concurrent routines"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function executing multiple coroutines"""
    delays_list = []
    for _ in range(n):
        delays_list.append(wait_random(max_delay))
    results = await asyncio.gather(*delays_list)
    return sorted(results)
