#!/usr/bin/env python3
"""Module that provides a function to return tuples of elements and their lengths."""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples where each tuple contains an element and its length."""
    return [(i, len(i)) for i in lst]
