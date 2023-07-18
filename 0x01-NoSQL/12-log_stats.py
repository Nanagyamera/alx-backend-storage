#!/usr/bin/env python3
"""
Task12
"""
from pymongo import MongoClient


# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Select the database and collection
db = client['logs']
collection = db['nginx']

# Get the total number of documents in the collection
total_logs = collection.count_documents({})
print(f"first line: {total_logs} logs where {total_logs} is the number of documents in this collection")

# Get the number of documents with each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("second line: Methods:")
for method in http_methods:
    count = collection.count_documents({"method": method})
    print(f"\t{count} logs with method = {method}")

# Get the number of documents with specific method and path
specific_logs = collection.count_documents({"method": "GET", "path": "/status"})
print(f"method=GET, path=/status: {specific_logs} logs")

# Close the MongoDB connection
client.close()
