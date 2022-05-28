from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip

from ip2geotools.databases.noncommercial import DbIpCity

# Create your views here.


def index(request):
    client_ip, is_routable = get_client_ip(request)
    response = DbIpCity.get(client_ip, api_key='free')

    if client_ip is None:
        return HttpResponse("Unable to get the client's IP address")
    else:
        return HttpResponse(f'<h1>IP: {client_ip} {is_routable} city : {response.city} smthng : {response.country}</h1>')
    if is_routable:
        return HttpResponse("The client's IP address is publicly routable on the Internet")
    else:
        return HttpResponse("The client's IP address is private")


