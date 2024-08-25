#!/usr/bin/env python3
"""Annotate the below function’s parameters"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function return values with the appropriate types"""
    result: List[Tuple[Sequence, int]] = []
    result = [(element, len(element)) for element in lst]
    return result
