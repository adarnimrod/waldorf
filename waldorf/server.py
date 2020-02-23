"""Dummy web server using Flask."""
from flask import Flask

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route("/ping")
def ping():
    """Healthcheck."""
    return "pong"
