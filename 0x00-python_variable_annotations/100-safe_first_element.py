#!/usr/bin/env python3
"""
Annotated python function

"""
from typing import Union, Sequence, Any


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first value of a given list """
    if lst:
        return lst[0]
    else:
        return None
