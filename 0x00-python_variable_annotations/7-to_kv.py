#!/usr/bin/env python3
from typing import Union, Tuple
"""A type-annotated function to_kv"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int OR float v as arguments
    and returns a tuple"""
    temp = float(v ** 2)
    return(k, temp)
