#!/usr/bin/env python3
"""Function that inserts a new document in a PyMongo collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a PyMongo collection.

    Args:
        mongo_collection: a PyMongo collection object.
        **kwargs: key-value pairs representing the document fields.

    Returns:
        The _id of the newly inserted document.
    """
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
