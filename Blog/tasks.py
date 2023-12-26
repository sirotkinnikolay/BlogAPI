# Create your tasks here
from celery import *
from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0')


@app.task
def test_celery():
    print('-------------test_celery_work----------------------->')
    pass
