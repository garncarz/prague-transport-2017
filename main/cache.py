import json

from redis import StrictRedis
from . import settings


_redis = StrictRedis.from_url(settings.REDIS_URL)


def get(key):
    value = _redis.get(json.dumps(key))
    return json.loads(value) if value else None


def set(key, value):
    return _redis.set(json.dumps(key), json.dumps(value),
                      ex=settings.REDIS_EXPIRE_SECONDS)
