# weather/urls.py

from django.urls import path
from .views import weather_report

urlpatterns = [
    path('', weather_report, name='weather_report'),
]
