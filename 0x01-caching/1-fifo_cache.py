#!/usr/bin/env python3
""" FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - caching system following the FIFO algorithm
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.keys.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key) if key is not None\
            and key in self.cache_data else None
