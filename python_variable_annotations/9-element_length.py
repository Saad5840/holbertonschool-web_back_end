#!/usr/bin/env python3
"""Module provides function to return tuples of elements and their lengths."""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples where each tuple contains element, its length."""
    return [(i, len(i)) for i in lst]
