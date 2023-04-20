#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize MRUCache
        """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """
        Add an item in the cache with MRU algorithm
        """
        if key is None or item is None:
            return

        # If the key already exists in the cache,
        # move it to the front of the MRU list
        if key in self.cache_data:
            self.mru_keys.remove(key)
        # If the cache is at its limit, remove the most recently used item
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.mru_keys.pop()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        # Add the new item to the cache and the front of the MRU list
        self.cache_data[key] = item
        self.mru_keys.insert(0, key)

    def get(self, key):
        """
        Get an item by key from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the front of the MRU list
        self.mru_keys.remove(key)
        self.mru_keys.insert(0, key)

        return self.cache_data[key]
