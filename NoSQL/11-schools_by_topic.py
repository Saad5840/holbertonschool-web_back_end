#!/usr/bin/env python3
"""Function that returns the list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of all school documents that contain a specific topic.

    Args:
        mongo_collection: a PyMongo collection object.
        topic (str): the topic to search for in the 'topics' field.

    Returns:
        A list of school documents containing the given topic.
        Returns an empty list if no document matches.
    """
    if mongo_collection is None or topic is None:
        return []
    return list(mongo_collection.find({"topics": topic}))
