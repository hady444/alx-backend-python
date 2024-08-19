#!/usr/bin/env python3
"""
Python Async
"""
import asyncio
from typing import List
import bisect
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 5, max_delay: int = 10) -> List[float]:
    li = []
    for _ in range(n):
        wait = await wait_random(max_delay)
        bisect.insort(li, wait)
    return li
