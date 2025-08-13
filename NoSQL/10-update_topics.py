#!/usr/bin/env python3
"""Function that updates the topics of a school document in a PyMongo collection"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document with the given name.

    Args:
        mongo_collection: a PyMongo collection object.
        name (str): the name of the school to update.
        topics (list of str): the list of topics to set for the school.

    Returns:
        None
    """
    if mongo_collection is None or name is None or topics is None:
        return
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
