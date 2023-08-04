import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler


def setup_logger(name, logfile, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s-%(process)d-%(name)s-%(levelname)s-%(message)s')

    rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 512 * 1024, 5)
    rotateHandler.setFormatter(formatter)
    rotateHandler.setLevel(level)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(rotateHandler)

    return logger