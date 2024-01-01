#!/usr/bin/env python3
"""
This module contains a function that calculates the range of indexes for
pagination, and a Server class that paginates a database of popular baby
names and provides deletion-resilient hypermedia pagination.
"""
import csv
import math
from typing import Dict, List, Tuple


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            self.__indexed_dataset = {
                i: data for i, data in enumerate(self.dataset())
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Retrieve a dictionary containing information about the page.

        Parameters:
        index (int): The current start index of the return page.
        page_size (int): The number of items per page.

        Returns:
        Dict: A dictionary containing the following key-value pairs:
        - index: the current start index of the return page
        - next_index: the next index to query with
        - page_size: the current page size
        - data: the actual page of the dataset
        """
        assert (
            isinstance(index, int) and index >= 0
        ), "index must be an integer greater than or equal to 0"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page_size must be an integer greater than 0"
        indexed_data = self.indexed_dataset()
        data = []
        next_index = index
        for _ in range(page_size):
            while indexed_data.get(next_index) is None and next_index < len(
                indexed_data
            ):
                next_index += 1
            if next_index >= len(indexed_data):
                break
            data.append(indexed_data[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }
