import geocoder

# ip_adress = '95.82.121.233'
# city_ip = geocoder.ip(ip_adress)
#
# city = city_ip
# print(city.ip)

ip = geocoder.ip("95.82.121.233")
print(ip.country)