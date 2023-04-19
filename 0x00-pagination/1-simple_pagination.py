#!/usr/bin/env python3

"""Simple pagination"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing the start index and end index
    corresponding to the range of indexes to return in a list for the given
    pagination parameters.

    :param page: the 1-indexed page number.
    :param page_size: the number of items per page.
    :return: a tuple of (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the page of the dataset that corresponds to the given
        pagination parameters.

        :param page: the 1-indexed page number to retrieve (default 1).
        :param page_size: the number of items per page (default 10).
        :return: a list of rows from the dataset corresponding to the page.
        """
        assert isinstance(
            page, int) and page > 0, "Page must be an integer greater than 0"
        assert isinstance(
            page_size, int) and page_size > 0,\
            "Page size must be an integer greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
