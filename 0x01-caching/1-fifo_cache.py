#!/usr/bin/env python3
"""
This module contains a class FIFOCache that inherits from BaseCaching.
This caching system uses a First-In, First-Out algorithm.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class. It is a caching system with a First-In, First-Out
    algorithm.
    It inherits from BaseCaching and overrides put and get methods.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data dictionary.
        If key or item is None or an empty string, this method should not
        do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS,
        it must discard the first item put in cache (FIFO algorithm).
        """
        if not key or not item:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print('DISCARD:', first_key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or an empty string, or if the key doesn't exist
        in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
