import os
import socket
from flask import Flask
import redis

app = Flask(__name__)

REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def welcome():
    return "Welcome to the Flask + Redis application!"

@app.route("/count")
def count():
    visits = redis_client.incr("visit_count")
    hostname = socket.gethostname()
    return f"This page has been visited {visits} times (served by container: {hostname})"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)