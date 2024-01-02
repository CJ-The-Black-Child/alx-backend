#!/usr/bin/env python3
"""
This module contains a class LFUCache that inherits from BaseCaching.
This caching system uses a Least Frequently Used algorithm.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class. It is a caching system with a Least Frequently Used
    algorithm.
    It inherits from BaseCaching and overrides put and get methods.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = {}

    def put(self, key, item):
        """
        Assign the item value for the key in self.cache_data dictionary.
        If key or item is None or an empty string, this method should
        not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS,
        it must discard the least frequency used item (LFU algorithm).
        If there is more than 1 item to discard, use the LRU algorithm to
        discard only the least recently used.
        """
        if not key or not item:
            return
        if key in self.cache_data:
            del self.cache_data[key]
            self.keys_freq[key] += 1
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key = min(self.keys_freq, key=self.keys_freq.get)
            del self.cache_data[lfu_key]
            del self.keys_freq[lfu_key]
            print('DISCARD:', lfu_key)
        self.cache_data[key] = item
        self.keys_freq[key] = self.keys_freq.get(key, 0)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or an empty string, or if the key doesn't exist in
        self.cache_data, return None.
        """
        if key in self.cache_data:
            self.keys_freq[key] += 1
            return self.cache_data[key]
        return None
