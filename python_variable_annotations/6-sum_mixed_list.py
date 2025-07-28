#!/usr/bin/env python3
"""Module that provides a function to sum a list containing integers and floats."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all elements in the list mxd_lst as a float."""
    return sum(mxd_lst)
