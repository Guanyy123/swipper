import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swipper.settings')

# create Celery applications
celery_app = Celery('swipper')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()

def call_by_worker(func):
    '''Executing the tasks in async celery'''
    task = celery_app.task(func)
    return task.delay
