#!/usr/bin/env python3
"""A module with two concurrent routines"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """A function executing multiple coroutines"""

    delays_list = []

    async def append_coroutine():
        """A basic coroutine"""
        task = task_wait_random(max_delay)
        await task
        delays_list.append(task.result())

    tasks = []
    for _ in range(n):
        # Appends coroutines objects but doesn't call the coroutine
        tasks.append(append_coroutine())

    # Runs all the coroutines concurrently
    await asyncio.gather(*tasks)
    return delays_list
