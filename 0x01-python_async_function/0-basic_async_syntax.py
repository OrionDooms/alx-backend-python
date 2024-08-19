#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument,
that waits for a random delay between 0 and max_delay seconds,
and returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ max_delay with a default value of 10,
    wait_random that waits for a random delay integer
    """
    temp = await asyncio.sleep(random.uniform(
        0, max_delay), result=random.uniform(0, max_delay))
    return temp
