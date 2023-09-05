#!/usr/bin/env python3
"""a Python script that provides some stats
about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print("{} logs".format(nginx_collection.count_documents({})))

    methods_count = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    for method, count in methods_count.items():
        methods_count[method] = nginx_collection.count_documents(
            {"method": method})

    print("Methods:")
    for method, count in methods_count.items():
        print("\tmethod {}: {}".format(method, count))

    print("{} status check".format(nginx_collection.count_documents(
        {"path": "/status"})))

    pipeline = [
        {
            "$group": {
                "_id": "$ip",  # group by field ip
                "count": {"$sum": 1}  # count number of occurencies of each IP
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]

    top_ips = list(nginx_collection.aggregate(pipeline))
    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))
