#!/usr/bin/python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class"
            )

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class"
            )


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
            self.cache_data.append({key: item})

    def get(self, key):
        """ get defines:
            - get data from data_cache storage in base class
            if key exist and if not or key is none return none
        """
        return self.cache_data[key]
