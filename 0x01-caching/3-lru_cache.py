#!/usr/bin/env python3
"""LRU Caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Implements cache algorithm using LRU
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Puts an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                l_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {l_key}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Returns the value for the key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data[key]
