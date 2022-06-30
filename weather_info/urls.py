from django.urls import path
from weather_info import views

urlpatterns = [
    path('',views.get_weather)
]