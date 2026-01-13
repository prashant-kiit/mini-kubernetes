from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        payload = {
            "type": "FILE_MODIFIED",
            "path": event.src_path,
        }

        r.publish("repository.events", json.dumps(payload))
        print("Published:", payload)


if __name__ == "__main__":
    path = "../app"
    observer = Observer()
    observer.schedule(Handler(), path, recursive=True)
    observer.start()

    print(f"Observing {path} for changes")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
