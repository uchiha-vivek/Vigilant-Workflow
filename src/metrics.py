from vigilant import init_metrics_handler, shutdown_metrics_handler, emit_metric
import os
from dotenv import load_dotenv

load_dotenv()


def setup_metrics():
    init_metrics_handler(
        name="python-app",
        token=os.getenv('VIGILANT_API'),
    )

def log_metric(name: str, value: int, attrs: dict = None):
    emit_metric(name=name, value=value, attrs=attrs)

def shutdown_metrics():
    shutdown_metrics_handler()

