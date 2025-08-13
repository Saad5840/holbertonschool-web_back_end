#!/usr/bin/env python3
"""12-log_stats.py: Provides stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    # Total logs
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # HTTP methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]
    agg_result = nginx.aggregate(pipeline)
    counts = {doc["_id"]: doc["count"] for doc in agg_result}
    for method in methods:
        print(f"\tmethod {method}: {counts.get(method, 0)}")

    # GET /status
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
