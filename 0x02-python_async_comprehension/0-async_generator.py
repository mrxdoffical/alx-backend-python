#!/usr/bin/env python3
"""
this module is async generator
"""


import asyncio
import random


async def async_generator():
	"""
    An asynchronous generator that yields a random float between 0 and 10.
	"""
	for hellYah in range(9):
		await asyncio.sleep(1)
		yield random.unfiorm(0, 10)
