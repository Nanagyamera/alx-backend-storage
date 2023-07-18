#!/usr/bin/env python3
"""
Task 15
"""
from pymongo import MongoClient


# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Select the database and collection
db = client['logs']
collection = db['nginx']

# Get the total number of logs
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Get the number of logs for each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in http_methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Get the number of status check logs
status_checks_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_checks_count} status check")

# Get the top 10 most present IPs
top_ips = collection.aggregate([
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])
print("IPs:")
for ip in top_ips:
    print(f"\t{ip['_id']}: {ip['count']}")

# Close the MongoDB connection
client.close()
from pymongo import MongoClient
