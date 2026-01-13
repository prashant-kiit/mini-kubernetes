import redis

r = redis.Redis(decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe("repository.events")

for msg in pubsub.listen():
    if msg["type"] == "message":
        print("Received:", msg["data"])
