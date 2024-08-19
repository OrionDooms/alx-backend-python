#!/usr/bin/env python3
'''measure_time take in integers n and max_delay as arguments
that measures the total execution time'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    temp = time.time()
    asyncio.run(wait_n(n, max_delay))
    temp2 = time.time()
    return (temp2 - temp) / n
