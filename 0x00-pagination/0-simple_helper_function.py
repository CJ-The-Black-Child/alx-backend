#!/usr/bin/env python3
"""
This module contains a function that calculates the range of indexes for
pagination.

The function takes two integer arguments: page and page_size. It returns
a tuple of size two containing a start index and an end index corresponding
to the range of indexes to return in a list for those particular pagination
parameters. Page numbers are 1-indexed, i.e., the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Parameters:
    page (int): The current page number.
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
