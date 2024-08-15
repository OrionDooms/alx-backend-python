#!/usr/bin/env python3
"""a type-annotated function sum_mixed_list"""


from typing import Union, List
""" returns a sum of float"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    temp = sum(mxd_lst)
    return temp
