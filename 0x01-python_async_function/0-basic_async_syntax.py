#!/usr/bin/env python3
"""This module contains an asynchronous coroutine that takes in
an int arg and returns the value.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns random delay moment."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
