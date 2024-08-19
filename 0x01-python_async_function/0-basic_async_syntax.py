#!/usr/bin/env python
"""
Async Python
"""
import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random delay"""
    wait = random() * max_delay
    await asyncio.sleep(wait)
    return (wait)
