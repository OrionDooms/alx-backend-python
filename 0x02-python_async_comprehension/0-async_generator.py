#!/usr/bin/env python3
"""Async Generator Task"""
import asyncio
import random

from typing import Generator
'''Return type of generator by the generic type yield_type'''


async def async_generator() -> Generator[int, None, None]:
    """loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for a in range(10):
        result = []
        await asyncio.sleep(1)
        result = random.uniform(0, 10)
        yield result
