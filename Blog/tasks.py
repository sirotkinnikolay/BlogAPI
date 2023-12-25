# Create your tasks here
from celery import *


@shared_task
def test_celery():
    print('-------------test_celery_work----------------------->')
    pass

