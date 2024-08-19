#!/usr/bin/env python3
'''Asyncronus python
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> List[float]:
    '''return a list of awaited response from previous function
    '''
    start = time.time()
    await wait_n(n, max_delay)
    return ((start - time.time()) / n)
