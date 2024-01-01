#!/usr/bin/env python3
"""
This module contains a function that calculates the range of indexes for
pagination and a Server class that paginates a database of popular baby names.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Parameters:
    page (int): The current page number.
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end index.
    """
    assert (
        isinstance(page, int) and page > 0
    ), "page must be an integer greater than 0"
    assert (
        isinstance(page_size, int) and page_size > 0
    ), "page_size must be an integer greater than 0"

    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve the appropriate page of the dataset.

        Parameters:
        page (int): The current page number.
        page_size (int): The number of items per page.

        Returns:
        List[List]: A list of rows that represent the current page of
        the dataset.
        """
        assert (
            isinstance(page, int) and page > 0
        ), "page must be an integer greater than 0"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page_size must be an integer greater than 0"

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
