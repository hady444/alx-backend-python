#!/usr/bin/env python
"""
Async Python
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random delay"""
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return (wait)
