"""Celery worker."""
import logging
import os
from celery import Celery


BROKER_URL = os.getenv("BROKER_URL")
app = Celery("tasks", broker=BROKER_URL)  # pylint: disable=invalid-name


@app.task
def log(message):
    """Log message."""
    logging.info(f"Message: %s", message)
