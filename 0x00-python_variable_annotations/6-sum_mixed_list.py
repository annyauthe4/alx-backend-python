#!/usr/bin/env python3
"""This module defines a type-annotated function which
takes a list of int and floats and returns their sum
as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of a mixed list as a float."""
    return sum(mxd_lst)
