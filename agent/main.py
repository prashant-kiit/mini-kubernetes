from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Event: {event.src_path} was modified")

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