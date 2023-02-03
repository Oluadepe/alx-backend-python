#!/usr/bin/env python3
""" Annotated function """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sums up a list of both float and int items. """
    return sum(mxd_lst)
