#!/usr/bin/env python3
""" Annotated function """
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns a list with tuple items """
    return [(i, len(i)) for i in lst]
