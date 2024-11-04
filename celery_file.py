import celery
from celery.schedules import crontab



app = celery.Celery('weather', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

app.config_from_object('celery_conf')