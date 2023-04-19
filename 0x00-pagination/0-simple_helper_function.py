#!/usr/bin/env python3
"""Index range"""


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
