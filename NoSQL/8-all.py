#!/usr/bin/env python3
"""Function that lists all documents in a PyMongo collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a PyMongo collection.

    Args:
        mongo_collection: a PyMongo collection object.

    Returns:
        A list of all documents in the collection.
        Returns an empty list if no documents are found.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
