import celery
from celery.schedules import crontab
app = celery.Celery('weather_project', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.config_from_object('celery_conf')