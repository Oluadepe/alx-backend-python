#!/usr/bin/env python3
"""
Annotated python function.
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """ Retrieve value with a given key from a dict """
    if key in dct:
        return dct[key]
    else:
        return default
