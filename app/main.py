import os

from fastapi import FastAPI

app = FastAPI()

HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "8000"))


@app.get("/health")
def health():
    print(f"Health status on {HOST}:{PORT}")
    return {"status": "ok", "host": HOST, "port": PORT}
