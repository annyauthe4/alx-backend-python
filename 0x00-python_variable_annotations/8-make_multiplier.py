#!/usr/bin/env python3
"""This module defines a function that takes a float as
arg and returns a function that multiplies a float by
multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function."""
    def multiply(x: float) -> float:
        """Multiplies args."""
        return x * multiplier
    return multiply
