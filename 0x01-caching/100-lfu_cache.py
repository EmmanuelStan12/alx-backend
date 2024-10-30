#!/usr/bin/env python3
"""LFU Caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implements an LFU (Least Frequently Used) caching algorithm."""
    
    def __init__(self):
        super().__init__()
        self.freq_data = {}      # {key: frequency}
        self.freq_keys = {}      # {frequency: list of keys with that frequency}
        self.min_freq = 0        # Tracks the minimum frequency of any key in the cache

    def put(self, key, item):
        """Adds an item to the cache or updates it if it already exists."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item's frequency
            self._increment_frequency(key)
        else:
            # Check if the cache is at max capacity
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_least_frequent()

            # Insert the new item with frequency 1
            self.cache_data[key] = item
            self.freq_data[key] = 1
            self.min_freq = 1  # Reset minimum frequency for new items

            if 1 not in self.freq_keys:
                self.freq_keys[1] = []
            self.freq_keys[1].append(key)

    def get(self, key):
        """Retrieves an item by key, updating its frequency if it exists."""
        if key is None or key not in self.cache_data:
            return None

        # Increase the frequency of the item before returning it
        self._increment_frequency(key)
        return self.cache_data[key]

    def _increment_frequency(self, key):
        """Helper function to increase the frequency of a key in the cache."""
        current_freq = self.freq_data[key]
        new_freq = current_freq + 1
        self.freq_data[key] = new_freq

        # Move the key from the old frequency list to the new one
        self.freq_keys[current_freq].remove(key)
        if new_freq not in self.freq_keys:
            self.freq_keys[new_freq] = []
        self.freq_keys[new_freq].append(key)

        # Clean up if no keys remain at the old frequency
        if not self.freq_keys[current_freq]:
            del self.freq_keys[current_freq]
            if self.min_freq == current_freq:
                self.min_freq = new_freq

    def _evict_least_frequent(self):
        """Removes the least frequently used item from the cache."""
        # Evict the least frequently used key (min_freq bucket)
        keys_at_min_freq = self.freq_keys[self.min_freq]
        lfu_key = keys_at_min_freq.pop(0)  # Remove the oldest inserted key at min_freq

        if not keys_at_min_freq:
            del self.freq_keys[self.min_freq]

        # Remove from both cache and frequency data
        del self.cache_data[lfu_key]
        del self.freq_data[lfu_key]
        print(f"DISCARD: {lfu_key}")
