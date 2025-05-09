#!/usr/bin/env python3
"""This is a coroutine module that takes no args. It loops
10 times each time asynchronously wait 1 second then yield
random number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields a random float numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
