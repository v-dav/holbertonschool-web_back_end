#!/usr/bin/env python3
"""A module with a asynchronus routine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A coroutine awaiting and returning the delay"""
    the_delay = random.uniform(0, max_delay)
    await asyncio.sleep(the_delay)
    return the_delay
