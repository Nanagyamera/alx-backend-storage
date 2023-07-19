#!/usr/bin/env python3
"""
A module for using the Redis NoSQL data storage
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Tracks the number of calls made to a method in a Cache class.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Invokes the given method after incrementing its call counter.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda d: d.decode("utf-8") if d is not None else None)

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=lambda d: int(d) if d is not None else None)


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def replay(method: Callable):
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    inputs = [eval(arg) for arg in redis.lrange(input_key, 0, -1)]
    outputs = [eval(output) for output in redis.lrange(output_key, 0, -1)]

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, outp in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp}) -> {outp}")


cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
