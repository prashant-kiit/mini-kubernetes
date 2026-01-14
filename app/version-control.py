import os
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["repository"]
collection = db["app"]


with open("version-control.ignore", "r") as f:
    lines = f.readlines()

EXCLUDE = [line.strip() for line in lines]

for name in os.listdir("./"):
    path = os.path.join("./", name)

    if name in EXCLUDE:
        continue

    if os.path.isfile(path):
        with open(path, "r", errors="ignore") as f:
            data = f.read()
            collection.insert_one({"path": path, "data": data})
            print("Committed:", path)

print("Done")
