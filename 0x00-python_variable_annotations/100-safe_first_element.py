#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Union, Sequence, Any
# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Any can be used as a base class."""
    if not lst:
        return None
    return lst[0]
