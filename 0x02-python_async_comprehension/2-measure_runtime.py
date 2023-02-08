#!/usr/bin/env python3
""" Task 2 module. """
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Executes async function 4 times and measures the execution time. """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    end = time.time()
    return end - start
