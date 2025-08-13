#!/usr/bin/env python3
"""12-log_stats.py: Provides stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    # Total number of logs
    total = nginx.count_documents({})
    print(f"{total} logs")

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET /status count
    status = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
