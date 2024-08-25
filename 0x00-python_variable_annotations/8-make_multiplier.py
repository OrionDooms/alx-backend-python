#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Make_multiplier that takes a float multiplier as argument
    and returns a function that multiplies."""
    def multi_x(n: float) -> float:
        result = multiplier * n
        return result
    return multi_x
