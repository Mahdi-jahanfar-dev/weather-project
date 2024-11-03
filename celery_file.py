import celery

app = celery.Celery('weather_project', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')