#!/usr/bin/env python3
"""A python module that manitpulates mongo DB"""


def update_topics(mongo_collection, name, topics):
    """A function that changes all topics of a school document
    based on the name"""

    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
        )
