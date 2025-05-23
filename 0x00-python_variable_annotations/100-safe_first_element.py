#!/usr/bin/env python3
"""This module provides a duck-typed annotations."""
from typing import Sequence, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element of a sequence."""
    if lst:
        return lst[0]
    else:
        return None
