import logging
import sys

logger = logging.getLogger("dpn")


def init_logging(verbose=False):
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
