#!/usr/bin/env python3
"""
something here
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Function to zoom into an array by repeating its elements.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int): The multiplication factor.

    Returns:
        List[int]: A list of integers
        with each element repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)


zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
