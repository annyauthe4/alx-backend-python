#!/usr/bin/env python3
"""This module defines a type-annotated function which takes
a list of floats as arg and returns their sum as float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum in float."""
    return sum(input_list)
