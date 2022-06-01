import requests
import datetime
api_key = 'd60722d76693fe5719d84103c6d08d89'

city_name = 'Almaty'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
req = requests.get(url)
data = req.json()


name = data['name']
cur_weather = round(data['main']['temp'] - 273.15, 2)
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
dayLen = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
feels = round(data['main']['feels_like'] - 273.15, 2)

print(f'Weather in {name}\n'
      f'Current weather {cur_weather}°C\n'
      f'Feels like {feels}°C\n'
      f'Humidity : {humidity}%\n'
      f'Sunrise : {sunrise_timestamp}\n'
      f'Sunset : {sunset_timestamp}\n'
      f'Day length : {dayLen}\n'
      f'Wind {wind} m/s'
)