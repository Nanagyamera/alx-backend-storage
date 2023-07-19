WEB CACHING WITH REDIS

This repository contains solutions to various caching-related tasks using Redis. Each task addresses a specific caching scenario and provides an implementation in Python using Redis as the caching mechanism. The solutions utilize the redis library for interacting with Redis and provide examples and explanations for each task.

Task 1: Cache Class

Description

The task involves creating a Cache class that uses Redis as a caching backend. The class includes methods to store data in Redis and retrieve it based on a generated key. The data can be of various types such as strings, bytes, integers, or floats.

Solution
The Cache class provides the following methods:

__init__: Initializes the Cache instance and sets up the Redis client. It also flushes the Redis database using flushdb() to clear any existing data.

store: Takes a data argument and stores it in Redis using a randomly generated key. The method returns the generated key.

get: Retrieves the value from Redis based on the provided key. It supports optional type conversion functions to convert the retrieved value back to the desired format.

get_str: Convenience method that retrieves a value as a string from Redis.

get_int: Convenience method that retrieves a value as an integer from Redis.


Task 2: Counting Method Calls

Description

This task involves implementing a decorator, count_calls, to track the number of times a method is called within the Cache class. The decorator increments a counter in Redis for each method call and stores it with a key based on the method's qualified name.

Solution

The count_calls decorator provides a wrapper function that tracks the method calls. The decorator is applied to the store method of the Cache class. Each time the store method is called, the decorator increments the counter for that method in Redis.


Task 3: Storing Call History

Description

This task focuses on implementing a decorator, call_history, to store the history of inputs and outputs for a particular function in Redis. The decorator appends the input parameters and the corresponding output to separate lists in Redis using keys based on the qualified name of the decorated function.

Solution

The call_history decorator provides a wrapper function that appends the input parameters and output to Redis lists. The decorator is applied to the store method of the Cache class. Each time the store method is called, the decorator stores the input parameters and the output in separate Redis lists.

Task 4: Replay Function

Description

This task involves implementing a replay function to display the history of calls for a particular function. The function retrieves the input parameters and output from Redis lists and displays them in a formatted manner.

Solution
The replay function retrieves the input parameters and output from Redis lists using the qualified name of the decorated function. It then iterates over the inputs and outputs, combining them to display the history of calls in a human-readable format.

Task 5: Web Page Caching

Description
This task focuses on implementing a get_page function that fetches the HTML content of a specified URL. The function tracks the number of times a URL is accessed and caches the result in Redis with an expiration time of 10 seconds.

Solution
The get_page function uses the requests library to fetch the HTML content of a URL. It is decorated with cache_with_expiration, which tracks the URL accesses and caches the result in Redis with the specified expiration time. If the result is already cached, it is retrieved from Redis; otherwise, the function fetches the content and caches it.

Setup and Dependencies
To run the provided solutions, you need to have the following dependencies installed:

redis: The Redis Python library for interacting with Redis.
requests: The requests library for making HTTP requests.
You can install the dependencies using pip:

Copy code
pip install redis requests
Ensure that you have a Redis server running locally or accessible via a network connection.

Feel free to explore each task's implementation in the provided code files. You can adapt the solutions to fit your specific caching requirements or integrate them into your own projects.
