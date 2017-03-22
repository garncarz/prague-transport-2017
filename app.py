from flask import Flask

from task1.api import task1_api
from task2.api import task2_api


app = Flask(__name__)

app.register_blueprint(task1_api, url_prefix='/task1')
app.register_blueprint(task2_api, url_prefix='/task2')
