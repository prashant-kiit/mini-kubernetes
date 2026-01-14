from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import redis
import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["repository"]
collection = db["app"]

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


# def on_modified(self):
#     payload = {
#         "type": "FILE_MODIFIED",
#         "path": path,
#     }

#     r.publish("repository.events", json.dumps(payload))
#     print("Published:", payload)


if __name__ == "__main__":
    print("Watching for insert changes...")

    pipeline = [{"$match": {"operationType": "insert"}}]

    with collection.watch(pipeline) as stream:
        for change in stream:
            print(change)
