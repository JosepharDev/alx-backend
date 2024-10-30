#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ defines LIFOCache
     apply concept of LIFO on data cache in
     base class
    """
    def __init__(self):
        """ method to initialize the object """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ method put an item in cache_data using key
            and value if size of cache_data > MAX_ITEMS remove
            first one in cache_data
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                k_r, _ = self.cache_data.popitem()
                print("DISCARD:", k_r)
            self.cache_data[key] = item

    def get(self, key):
        """ get an item from cache_data if key
        is none or not found return None
        """
        return self.cache_data.get(key)
