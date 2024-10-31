#!/usr/bin/env python3
"""Basic dictionary module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class for basic caching
    """

    def put(self, key, item):
        """Assigns an item to a key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value of the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
