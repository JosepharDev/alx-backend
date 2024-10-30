#!/usr/bin/env python3
""" defines FIFOCache Module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache FIFO concept on data storage in base class
    """

    def __init__(self):
        """ constructure method responsible
        of how object is created
        """
        super().__init()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ put defines
            add an item to cache storage if size of items in storage
            bigger than our constants we remove fist inserted one
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                key, _ = self.cache.data.popitem(last=False)
                print('DISCARD: ', key)
            self.cache_data[key] = item

    def get(self, key):
        """ put defines
            get the value from cache storage using key
            if not exist return None
        """
        return self.cache_data.get(key)
