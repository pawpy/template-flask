import os

from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return {"message": "Hello from Flask!"}


@app.get("/health")
def health():
    return "ok\n", 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    # Local development only; production runs gunicorn (see README).
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
