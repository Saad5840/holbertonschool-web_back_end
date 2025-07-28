#!/usr/bin/env python3
"""Module that provides a function to sum a list of floating-point numbers."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all elements in the list of floats input_list."""
    return sum(input_list)
