#!/usr/bin/env python3
"""A python module that manitpulates mongo DB"""


def list_all(mongo_collection):
    """A function that retrieves all elements of
    a mongoDB given collection. If no document in the collection
    returns an empty list"""

    if mongo_collection is not None:
        return mongo_collection.find()
    else:
        return []
