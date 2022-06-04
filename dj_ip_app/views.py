from django.shortcuts import render

from ipware import get_client_ip

from ip2geotools.databases.noncommercial import DbIpCity
import datetime
import geocoder

# Create your views here.
import requests


def get_ip(request):
    # get api

    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')


    api_key = 'd60722d76693fe5719d84103c6d08d89'
    ip_city = geocoder.ip(ip)
    # print(ip.city)
    ip_city_2 = ip_city.city

    city_name = ip_city_2

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    req = requests.get(url)
    data = req.json()

    name = data['name']
    cur_weather = round(data['main']['temp'] - 273.15, 2)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    lon = data['coord']['lon']
    lat = data['coord']['lat']

    sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    dayLen = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
        data['sys']['sunrise'])

    feels = round(data['main']['feels_like'] - 273.15, 2)
    descr = data['weather'][0]['description']


    weather_info = {
        'Weather in': name,
        'current weather': cur_weather,
        'Feels like': feels,
        'Humidity': humidity,
        'Pressure': pressure,
        'Sunrise': str(sunrise_timestamp),
        'Sunset': str(sunset_timestamp),
        'Day length': dayLen,
        'Wind': wind,
        'Description': descr
    }


    context = {'main_ip': ip, 'info':weather_info, 'today': descr}
    return render(request, 'index.html', context=context)






def forecast(request):

        # get ip
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # find the city with ip geocoder

    ip_city = geocoder.ip(ip)

    ip_city_2 = ip_city.city
    ip_country = ip_city.country



    api_key2 = 'd60722d76693fe5719d84103c6d08d89'

    city_name = ip_city_2
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key2}'
    req = requests.get(url)
    data = req.json()


    name = data['name']
    lon = data['coord']['lon']
    lat = data['coord']['lat']

    exclude = "minute,hourly"

    url2 = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key2}'


    req2 = requests.get(url2)
    data2 = req2.json()

    days = []
    nights = []
    descr = []

    for i in data2['daily']:
        days.append(str(round(i['temp']['day'] - 273.15)) + ' °C' + '⠀')
        nights.append(str(round(i['temp']['night'] - 273.15)) + ' °C')
        descr.append(i['weather'][0]['main'] + ': ' + i['weather'][0]['description'])


    data_dict = {'morning': days, 'nights': nights, 'descr': descr}
    data_every = {}
    j = 1
    for i in range(0, 8):
        myStr = str(data_dict["morning"][i]) + " " + str(data_dict["nights"][i]) + " " + str(data_dict["descr"][i])
        data_every[j] = myStr
        j += 1

    main = {'city': name, 'country': ip_country}
    weather = {'weather': data_every}
    return render(request, 'forecast.html', context={'main': main, 'weather': weather})


#
# def test(request):
#     x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forw_for is not None:
#         ip = x_forw_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#
#
#     api_key = 'd60722d76693fe5719d84103c6d08d89'
#     ip_city = geocoder.ip(ip)
#     # print(ip.city)
#     ip_city_2 = ip_city.city
#
#     city_name = ip_city_2
#
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
#     req = requests.get(url)
#     data = req.json()
#
#     name = data['name']
#     cur_weather = round(data['main']['temp'] - 273.15, 2)
#     humidity = data['main']['humidity']
#     pressure = data['main']['pressure']
#     wind = data['wind']['speed']
#     lon = data['coord']['lon']
#     lat = data['coord']['lat']
#
#     sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
#     sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
#     dayLen = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
#         data['sys']['sunrise'])
#
#     feels = round(data['main']['feels_like'] - 273.15, 2)
#
#
#     weather_info = {
#         'Weather in': name,
#         'current weather': cur_weather,
#         'Feels like': feels,
#         'Humidity': humidity,
#         'Pressure': pressure,
#         'Sunrise': str(sunrise_timestamp),
#         'Sunset': str(sunset_timestamp),
#         'Day lenght': dayLen,
#         'Wind': wind
#     }
#
#
#     context = {'main_ip': ip, 'info':weather_info}
#
#     return render(request, 'ttml', context=context)