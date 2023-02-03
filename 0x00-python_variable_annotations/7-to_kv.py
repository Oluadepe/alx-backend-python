#!/usr/bin/env python3
""" Annotated function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple of the 1st-arg and square of the 2nd-arg """
    return (k, v**2)
