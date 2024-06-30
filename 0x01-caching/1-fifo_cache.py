#!/usr/bin/env python3
"""
The module contains
"""
from typing import Any

BaseCache = __import__('base_caching').BaseCache


class FIFOCache(BaseCache):
    """
    The fifo cache
    """

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key: str, item: Any) -> None:
        """
        Add an item in the cache
        """

        if key and item:
            if len(self.cache_data) >= BaseCache.MAX_ITEMS:
                discarded = self.queue.pop(0)
                self.cache_data.remove(discarded)
                print('DISCARD:', discarded)
            self.cache_data[key] = item
            self.queue.append(item)

    def get(self, key: str) -> Any:
        """Get an item by key"""

        return self.cache_data.get(key, None)
