#!/usr/bin/env python3
"""This module collect 10 random numbers using async
comprehension over async_generator, then return them.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return collected random numbers."""
    return [i async for i in async_generator()]
