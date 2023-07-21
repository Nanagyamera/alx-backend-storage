#!/usr/bin/env python3
"""
Redis NoSQL data storage.
"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union

redis_store = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times methods of the Cache 
    class are called.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        in_key = f"{method.__qualname__}:inputs"
        out_key = f"{method.__qualname__}:outputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    if fn is None or not hasattr(fn, "__self__"):
        return
    redis_client = getattr(fn.__self__, "_redis", None)
    if not isinstance(redis_client, redis.Redis):
        return
    fn_name = fn.__qualname__
    in_key = f"{fn_name}:inputs"
    out_key = f"{fn_name}:outputs"
    fn_call_count = int(redis_client.get(fn_name) or 0)
    print(f"{fn_name} was called {fn_call_count} times:")
    inputs = redis_client.lrange(in_key, 0, -1)
    outputs = redis_client.lrange(out_key, 0, -1)
    for inp, outp in zip(inputs, outputs):
        print(f"{fn_name}(*{inp.decode('utf-8')}) -> {outp}")


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, lambda x: int(x))
