#!/usr/bin/env python3
"""This module defines a type-annotated function that takes a
str and an int/float as args and returns a tuple. The first
element of the tuple is the str. The 2nd is the square of the
int or float but annotated as float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple."""
    return (k, v ** 2)
