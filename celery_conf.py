from celery.schedules import crontab
from weather import getting_weather



beat_schedule = {
    'call_name_every_minutes':{
        'task':'weather.getting_weather',
        'schedule':crontab(minute='*/15'),
    }
}