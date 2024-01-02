#!/usr/bin/env python3
"""
This module contains a class MRUCache that inherits from BaseCaching.
This caching system uses a Most Recently Used algorithm.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class. It is a caching system with a Most Recently Used algorithm.
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
        If key or item is None or an empty string, this method
        should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS,
        it must discard the most recently used item (MRU algorithm).
        """
        if not key or not item:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print('DISCARD:', last_key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or an empty string, or if the key doesn't exist in
        self.cache_data, return None.
        """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
