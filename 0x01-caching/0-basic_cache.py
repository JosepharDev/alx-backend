#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache defines:
        - methods to operate on base class data storage
    """

    def put(self, key, item):
        """ put defines:
            - add a data to data_cache in base class storage
            and do nothing if item or key is none
        """
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """ get defines:
            - get data from data_cache storage in base class
            if key exist and if not or key is none return none
        """
        return self.cache_data.get(key)
