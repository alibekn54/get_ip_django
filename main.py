import requests

# Latitude: 43.245885 / N 43° 14' 45.188''
# Longitude: 76.814419 / E 76° 48' 51.906''
lat = '43.245885'
lon = '76.814419'

api_key = 'd60722d76693fe5719d84103c6d08d89'
url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={api_key}'

response = requests.get(url)
data = response.json()

print(data)