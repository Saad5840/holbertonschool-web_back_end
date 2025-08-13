#!/usr/bin/env python3
"""Function that updates the topics of all school documents with a given name"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all school documents with the given name.

    Args:
        mongo_collection: a PyMongo collection object.
        name (str): the name of the school to update.
        topics (list of str): the list of topics to set for the school.

    Returns:
        None
    """
    if mongo_collection is None or name is None or topics is None:
        return
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
