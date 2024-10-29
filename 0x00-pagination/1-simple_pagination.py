#!/usr/bin/env python3
""" Simple pagination"""

from typing import List, Tuple
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function should return a tuple of size two containing
            a start and end index corresponding to the range """
    s = (page - 1) * page_size
    end = s + page_size
    return (s, end)


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
        """ check correct size and return a dataset """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        s, e = index_range(page, page_size)
        dataset = dataset()
        if s > len(dataset):
            return []
        return dataset[s, e]
