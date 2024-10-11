#!/usr/bin/env python3
"""
this module returns mixed lists
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function to return the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integer and float numbers.

    Returns:
        float: The sum of the list of numbers as a float.
    """
    return sum(mxd_lst)
