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
    gen_delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))

    for delay in asyncio.as_completed(delays):
        delay = await delay
        gen_delays.append(delay)

    return gen_delays
