from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('weather/', views.weather, name='home_weather'),
]
