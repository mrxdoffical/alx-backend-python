#!/usr/bin/env python3
"""
this module returns list of floats
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Function to return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the list of float numbers.
    """
    return sum(input_list)
