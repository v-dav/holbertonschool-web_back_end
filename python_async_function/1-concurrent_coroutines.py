#!/usr/bin/env python3
"""A module with routines"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function executing multiple coroutines"""

    delays_list = []

    async def append_coroutine():
        """A basic coroutine"""
        delays_list.append(await wait_random(max_delay))

    tasks = []
    for _ in range(n):
        # Appends coroutines objects but doesn't call the coroutine
        tasks.append(append_coroutine())

    # Runs all the coroutines concurrently
    await asyncio.gather(*tasks)
    return delays_list
