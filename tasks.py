"""Celery worker."""
import logging
import os
from celery import Celery  # pylint: disable=import-error


BROKER_URL = os.getenv("BROKER_URL")
app = Celery("tasks", broker=BROKER_URL)  # pylint: disable=invalid-name


@app.task
def log(message):
    """Log message."""
    logging.info("Message: %s", message)
