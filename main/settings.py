import logging


TESTING = False

SENTRY_DSN = None


logging.basicConfig(level=logging.INFO)


try:
    from .settings_local import *
except ImportError:
    pass
