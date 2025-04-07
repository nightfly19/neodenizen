import logging
from logging import NullHandler

from .api import NeocitiesApi  # noqa: F401

__title__ = "neodenizen"
__description__ = "Python client library for Neocities API"
__url__ = "https://github.com/nightfly19/neodenizen"
__version__ = "1.0.0"
__author__ = "nightfly19"
__author_email__ = "sageimel@gmail.com"
__license__ = "Apache-2.0"
__copyright__ = "Copyright 2021 poyo46"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())
