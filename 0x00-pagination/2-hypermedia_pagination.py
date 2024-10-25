#!/usr/bin/env python3
"""Simple helper function
"""
from typing import Tuple, List, Dict, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int]:
    """Return the start and end index
    """
    n = page * page_size
    return (n - page_size, n)


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data) or end > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns hypermedia from the api
        """
        data = self.get_page(page, page_size)

        total = len(self.__dataset)

        next_page = page + 1 if (page * page_size) < total else None
        prev_page = page - 1 if page > 1 else None

        t_pages = (total // page_size) + (1 if total % page_size > 0 else 0)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": t_pages
        }
