from django.urls import path
from .views import *


urlpatterns = [
    path('', get_ip, name='main'),
    path('forecast/', forecast, name='forecast')
]