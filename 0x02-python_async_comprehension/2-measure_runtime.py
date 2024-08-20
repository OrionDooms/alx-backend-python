#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''
import asyncio
import time
'''Import async_comprehension from the previous file'''
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.'''
    a = time.time()
    temp = [asyncio.create_task(async_comprehension()) for a in range(4)]
    await asyncio.gather(*temp)
    result = time.time() - a
    return result
