#!/usr/bin/env python3
"""
This module contains a type-annotated function which
takes a float as an arg and returns the floor of
the float.
"""
import math


def floor(n: float) -> int:
    """Returns floor of a float."""
    return math.floor(n)
