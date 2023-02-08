#!/usr/bin/env python3
""" Task 4. """
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns list of all delays """
    wait_list = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_list)
