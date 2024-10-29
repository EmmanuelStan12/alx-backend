#!/usr/bin/env python3
"""FIFO Caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache caching algorithm
    """
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Puts a new item with key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.queue.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            f_key = self.queue.pop(0)
            del self.cache_data[f_key]
            print(f"DISCARD: {f_key}")

    def get(self, key):
        """Gets the item with the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
