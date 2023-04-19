#!/usr/bin/env python3

"""get_hyper_index returns an advanced hyper pagination"""

import csv
import math
from typing import List, Dict, Any, Union, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return a tuple of size two containing a start index and an end
        index corresponding to the range of indexes to return in a list for
        those particular pagination parameters.
        """
        start = (page - 1) * page_size
        end = page * page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset (i.e. the correct list
        of rows).
        """
        assert isinstance(
            page, int) and page > 0, "page must be an integer greater than 0"
        assert isinstance(
            page_size, int) and page_size > 0,\
            "page_size must be an integer greater than 0"

        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
            Dict[str, Union[int, List[List[Any]], None]]:
        """Return a dictionary containing the following key-value pairs:
            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page (equivalent to return from previous task)
            - next_page: number of the next page, None if no next page
            - prev_page: number of the previous page, None if no previous page
            - total_pages: the total number of pages
            in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """"
          Returns a page of the dataset indexed by sorting position,
          starting at the specified index and
          including the specified page size.

          Args:
              index(int, optional): The starting index of the dataset page.
              Defaults to None, in which case index is set to 0.
              page_size(int, optional): The number of items to
              include in the dataset page.
              Defaults to 10.

          Returns:
              dict: A dictionary containing the following key-value pairs:
                  - index(int): The starting index of
                  the returned dataset page.
                  - next_index(int): The index of the first item after
                  the last item on the current page.
                  - page_size(int): The size of the returned dataset page.
                  - data(list): The actual dataset page.

        """
        dataset_len = len(self.dataset())
        if index is None:
            index = 0
        assert 0 <= index < dataset_len, f"Index {index} is out of range."

        data = []
        for i in range(index, min(index + page_size, dataset_len)):
            if i not in self.indexed_dataset():
                continue
            data.append(self.indexed_dataset()[i])

        next_index = min(index + page_size, dataset_len)
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
