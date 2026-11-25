import openmeteo_requests
from variables import Systemvariables
from geopy.geocoders import Nominatim

openmeteo = openmeteo_requests.Client()
SysVars = Systemvariables()

geolocator = Nominatim(user_agent=SysVars.getUserAgent())


url = "https://api.open-meteo.com/v1/forecast"

def apiCall(location : str):

    located = geolocator.geocode(query=location)
    if located:
        params = {
            "latitude" : located.latitude,
            "longitude" : located.longitude,
            "current": ["temperature_2m", "relative_humidity_2m", "cloud_cover", "wind_speed_10m", "wind_direction_10m", "visibility"],
            "temperature_unit": "celsius",
            "wind_speed_unit": "kmh",
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]

        return response
    else: return False