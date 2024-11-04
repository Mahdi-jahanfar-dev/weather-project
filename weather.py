from celery import shared_task
from redis_db import db
import requests



@shared_task
def getting_weather():
    cities = ['Tehran', 'Andimeshk', 'Karaj', 'Isfahan', 'Ahvaz']
    for city in cities:
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=abddd401438cb67d929f931f05f0c35b')
        if response.status_code == 200:
            info = response.json()
            lat = info[0]['lat']
            lon = info[0]['lon']
            temp_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=abddd401438cb67d929f931f05f0c35b&units=metric')
            if response.status_code == 200:
                data = temp_response.json()
                main = data['main']
                temp = main['temp']
                db.set(f'{city} temp', temp)
                print(f'{city} temp is : {db.get(f"{city} temp")}')
            else:
                print(temp_response.status_code)
        else:
            print(response.status_code)