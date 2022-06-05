import json

import requests

api_key2 = 'b75f4d920fc1a0e2ad9998a5e2bc6d3e'


city_name = 'almaty'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key2}'
req = requests.get(url)
data = req.json()

print(data)


with open('info.json', 'w') as file:
    json.dump(data, file, indent=4)