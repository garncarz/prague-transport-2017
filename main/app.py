from flask import Flask
from raven.contrib.flask import Sentry

from task1.api import task1_api
from task2.api import task2_api

from . import settings


app = Flask(__name__)

if not settings.TESTING and getattr(settings, 'SENTRY_DSN', None):
    sentry = Sentry(app, dsn=settings.SENTRY_DSN, logging=True)

app.register_blueprint(task1_api, url_prefix='/task1')
app.register_blueprint(task2_api, url_prefix='/task2')
