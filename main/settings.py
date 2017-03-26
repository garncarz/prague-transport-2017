import logging
import os


TESTING = False
TESTING_API = False

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

SENTRY_DSN = None


logging.basicConfig(level=logging.INFO)


# Celery

BROKER_URL = 'redis+socket://%s/redis.sock' % BASE_DIR
CELERY_RESULT_BACKEND = BROKER_URL
CELERY_IGNORE_RESULT = False


# Caching

REDIS_URL = 'unix://%s/redis.sock' % BASE_DIR
REDIS_EXPIRE_SECONDS = 60 * 60


try:
    from .settings_local import *
except ImportError:
    pass
