#!/usr/bin/env python3
"""A module with a async function inside sync function"""

import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n"""

    async def async_measure():
        """A asynchronous function"""
        start = time.time()
        await wait_n(n, max_delay)
        end = time.time()
        return (end - start) / n

    return asyncio.run(async_measure())
