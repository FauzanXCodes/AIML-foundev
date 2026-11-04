import time
import random
import logging

def simulate_network_delay():
    """
    Simulate network latency between 0.1 and 0.5 seconds.
    """
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)

def setup_logger(name):
    """
    Create and configure a logger with the given name.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def format_timestamp(ts):
    """
    Format a datetime timestamp into a readable string.
    """
    return ts.strftime("%Y-%m-%d %H:%M:%S")