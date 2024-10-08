#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the code from wait_n into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random
    is being called."""
    results = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in tasks:
        result = await task
        results.append(result)
    return sorted(results)
