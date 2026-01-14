import redis

r = redis.Redis(decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe("repository.events")

print("Subscribed to repository.events")

if __name__ == "__main__":
    for msg in pubsub.listen():
        if msg["type"] == "message":
            print("Received:", msg["data"])
