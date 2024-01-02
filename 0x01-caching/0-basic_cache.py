#!/usr/bin/env python3
"""
This module contains a class BasicCache that inherits from BaseCaching.
This caching system doesn't have a limit.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class. It is a caching system without limit.
    It inherits from BaseCaching and overrides put and get methods.
    """

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data dictionary.
        If key or item is None or an empty string, this method should
        not do anything.
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or an empty string, or if the key doesn't exist
        in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
