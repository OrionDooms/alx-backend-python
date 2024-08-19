#!/usr/bin/env python3
import asyncio
from typing import List
"""Import wait_random from the previous python file"""
wait_random = __import__('0-basic_async_syntax').wait_random

""""wait_n takes 2 int arguments, n and max_delay,
wait_random n times with the specified max_delay"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    temp = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*temp))
