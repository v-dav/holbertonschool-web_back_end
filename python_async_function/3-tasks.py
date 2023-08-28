#!/usr/bin/env python3
"""A module with an asyncio task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that returns a task object"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
