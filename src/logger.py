from vigilant import Logger
import os
from dotenv import load_dotenv

load_dotenv()
def setup_logger():
    logger = Logger(
        name="my-service",
        endpoint="ingress.vigilant.run",
        token=os.getenv('VIGILANT_METRIC_API'),
    )
    logger.autocapture_enable()
    return logger
