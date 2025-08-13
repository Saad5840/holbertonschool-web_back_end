#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def main():
    """Fetch and display stats about nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Total number of logs
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Methods counts
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    pipeline = [
        {"$match": {"method": {"$in": methods}}},
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]
    results = {doc["_id"]: doc["count"] for doc in nginx.aggregate(pipeline)}
    for method in methods:
        print(f"\tmethod {method}: {results.get(method, 0)}")

    # Number of GET /status requests
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
