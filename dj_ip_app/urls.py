from django.urls import path
from .views import *


urlpatterns = [
    path('', get_ip),
    path('forecast/', forecast)
]