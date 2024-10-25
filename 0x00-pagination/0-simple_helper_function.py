#!/usr/bin/env python3
"""Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """Return the start and end index
    """
    n = page * page_size
    return (n - page_size, n)
