#!/usr/bin/env python3
"""
The module contains
"""
BaseCache = __import__('base_caching').BaseCache

class FIFOCache(BaseCache):
    """
    The fifo cache
    """

    def put(self, key: str, ):
        """
        
        """