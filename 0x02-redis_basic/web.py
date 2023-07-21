#!/usr/bin/env python3
"""
Web Page Caching
"""
import redis
import requests
from functools import wraps
from typing import Callable


def cache_with_expiration(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(url: str) -> str:
        cache_key = f"count:{url}"
        html_content = redis_client.get(url)
        if html_content is None:
            html_content = method(url)
            # Cache the HTML content with an expiration of 10 seconds
            redis_client.set(url, html_content, ex=10)
        # Increment the cache count for the URL
        redis_client.incr(cache_key)
        return html_content

    return wrapper


@cache_with_expiration
def get_page(url: str) -> str:
    """
    Returns the content of a URL after caching the request's response,
    and tracking the request
    """
    response = requests.get(url)
    return response.text


# Set up Redis client
redis_client = redis.Redis()
