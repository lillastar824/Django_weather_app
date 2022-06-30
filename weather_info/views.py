from django.shortcuts import render
import requests


def get_weather(request):
    """
    View to get weather information as per co-ordinates(latitude,longitude) given,
    Co-ordinates are fetched form UI, and API url is formatted as per given inputs.
    Data is fetched from API and rendered on the UI
    """
    latitude=request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}"
    weather = requests.get(url).json()
    weather_data = {
        "air_pressure_at_sea_level":weather['properties']["timeseries"][0]["data"]["instant"]["details"]["air_pressure_at_sea_level"],
        "air_temperature" : weather['properties']["timeseries"][0]["data"]["instant"]["details"]["air_temperature"],
        "wind_speed" : weather['properties']["timeseries"][0]["data"]["instant"]["details"]["wind_speed"]
    }

    context = {"data":weather_data}
    return render(request,'weather.html',context)
