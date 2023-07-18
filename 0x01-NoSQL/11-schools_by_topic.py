#!/usr/bin/env python3
"""
Task 11
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns schools by topic
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
