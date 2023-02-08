#!/usr/bin/env python3
""" Async comprehension. """
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ generates list of 10 numbers. """
    return [x async for x in async_generator()]
