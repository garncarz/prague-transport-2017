from celery import Celery


app = Celery(
    __name__,
    include=['task1.task', 'task2.task'],
)

app.config_from_object('main.settings')
