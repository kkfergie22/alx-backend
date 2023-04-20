#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
      - LIFO caching system
    """

    def __init__(self):
        """
        Initialize LIFOCache
        """
        super().__init__()
        self.keys_list = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item_key = self.keys_list.pop()
            del self.cache_data[last_item_key]
            print("DISCARD: {}".format(last_item_key))
        self.keys_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
