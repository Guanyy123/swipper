## Broker settings.
broker_url = 'redis://127.0.0.1:6379/0'
broker_pool_limit = 1000 # broker pool, default 10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'
result_expires = 3600 # expire time


# List of modules to import when the Celery worker starts.
imports = ('myapp.tasks',)

## Using the database to store task state and results.
result_backend = 'redis://127.0.0.1:6379/0'
result_serializer = 'pickle'
result_cache_max = 10000 # Max cache of tasks

worker_redirect_stdouts_level = 'INFO'