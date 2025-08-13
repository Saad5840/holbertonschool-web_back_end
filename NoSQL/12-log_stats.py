#!/usr/bin/env python3
"""12-log_stats.py: Provides stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Total number of documents
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Count per HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET /status
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
