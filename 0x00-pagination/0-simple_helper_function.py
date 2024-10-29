#!/usr/bin/env python3
""" Simple pagination function helper"""

from Typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function should return a tuple of size two containing
            a start and end index corresponding to the range """
    s = (page - 1) * page_size
    end = s + page_size
    return (s, end)
