#!/usr/bin/env python3
"""12-log_stats.py: Provides stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Total number of logs
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # HTTP methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Number of GET requests to /status
    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
