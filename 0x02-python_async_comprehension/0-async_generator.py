#!/usr/bin/env python3
"""Async Generator Task"""
import asyncio
import random


async def async_generator():
    """loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for a in range(10):
        result = []
        await asyncio.sleep(1)
        result = random.uniform(0, 10)
        yield result
