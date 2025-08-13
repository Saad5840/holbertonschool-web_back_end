#!/usr/bin/env python3
"""12-log_stats.py: Provides stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def main():
    """Fetch and display Nginx logs stats efficiently"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # List of HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Aggregation pipeline
    pipeline = [
        {
            "$facet": {
                "total_logs": [{"$count": "count"}],
                "methods_count": [
                    {"$match": {"method": {"$in": methods}}},
                    {"$group": {"_id": "$method", "count": {"$sum": 1}}}
                ],
                "status_check": [
                    {"$match": {"method": "GET", "path": "/status"}},
                    {"$count": "count"}
                ]
            }
        }
    ]

    result = list(nginx.aggregate(pipeline))[0]

    # Total logs
    total_logs = result["total_logs"][0]["count"] if result["total_logs"] else 0
    print(f"{total_logs} logs")

    # Methods counts
    counts = {doc["_id"]: doc["count"] for doc in result["methods_count"]}
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {counts.get(method, 0)}")

    # Status check count
    status_count = result["status_check"][0]["count"] if result["status_check"] else 0
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
