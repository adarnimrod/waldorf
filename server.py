"""Dummy web server using Flask."""
from flask import Flask, request, jsonify
import tasks

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route("/ping")
def ping():
    """Healthcheck."""
    return "pong"


@app.route("/log", methods=["POST"])
def log():
    """Async log."""
    data = request.get_json()
    tasks.log.apply_async(args=(data,))
    return jsonify(data)
