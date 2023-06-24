import logging
import os

logger = logging.getLogger('sentiscope')
logger.setLevel(os.environ.get('LOG_LEVEL', logging.INFO))
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def get_logger():
    return logger
