from django.shortcuts import render
from django.template import Template, Context
from ipware import get_client_ip

from ip2geotools.databases.noncommercial import DbIpCity

# Create your views here.
import requests


def get_ip(request):
    client_ip, is_routable = get_client_ip(request)
    response = DbIpCity.get(client_ip, api_key='free')

    if client_ip is None:
        unable = "Unable to get the client's IP address"
    else:
        ip = client_ip
        is_rout = is_routable
        city = response.city
        country = response.country
    if is_routable:
        publicly = "The client's IP address is publicly routable on the Internet"
    else:
        private = "The client's IP address is private"



    api_key2 = 'd60722d76693fe5719d84103c6d08d89'

    city_name = city
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key2}'
    req = requests.get(url)
    data = req.json()


    name = data['name']
    lon = data['coord']['lon']
    lat = data['coord']['lat']

    exclude = "minute,hourly"

    url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key2}'

    print(url2)

    req2 = requests.get(url2)
    data2 = req2.json()

    days = []
    nights = []
    descr = []

    for i in data2['daily']:
        days.append(round(i['temp']['day'] - 273.15, 2))
        nights.append(round(i['temp']['night'] - 273.15, 2))
        descr.append(i['weather'][0]['main'] + ': ' + i['weather'][0]['description'])


    data_dict = {'morning': days, 'nights': nights, 'descr': descr}
    data_every = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: ''
    }
    for i in range(0, 8):
        myStr = str(data_dict["morning"][i]) + " " + str(data_dict["nights"][i]) + " " + str(data_dict["descr"][i])
        data_every[i] = myStr

    main = {'city': city, 'country': country}
    weather = {'weather': data_every}

    return render(request, 'index.html', context={'main': main, 'weather': weather})


