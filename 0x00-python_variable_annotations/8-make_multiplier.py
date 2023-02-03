#!/usr/bin/env python3
""" Annotated function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a function that multiplies a float with the multiplier """
    return (lambda x: x * multiplier)
