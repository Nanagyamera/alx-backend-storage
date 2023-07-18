#!/usr/bin/env python3
"""
Task 14
"""


def top_students(mongo_collection):
    students = mongo_collection.aggregate([
        {"$addFields": {"averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
    return list(students)
