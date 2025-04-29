#!usr/bin/env python3
"""This module provides a function that execute multiple coroutines
at the same time using async.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns lists of float values."""
    delays = []

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
