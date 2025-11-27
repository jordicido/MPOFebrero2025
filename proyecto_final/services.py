# Conexión con las APIs (geocoding y meteorología)
import requests

from models.forecastDaily import ForecastDaily
from models.geocoding import Geocoding
from cache import *

API_GEO = "https://geocoding-api.open-meteo.com/v1/search"
API_FORE = "https://api.open-meteo.com/v1/forecast"


def get_geolocation(city, country_code="ES"):
    response = requests.get(API_GEO, {"name":city, "count":1, "countryCode": country_code, "language": "es"})
    if response.status_code == 200:
        data = response.json()
        result = Geocoding(**data)
        return result
    else:
        raise requests.HTTPError("The API can't be accessed")

def get_forecast(latitude, longitude, days=1):
    data = get_cache_data()
    if data == None:
        response = requests.get(API_FORE, {"latitude":latitude, "longitude":longitude, "daily":"weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_probability_max", "timezone":"auto", "forecast_days":days})
        if response.status_code == 200:
            data = response.json()
            set_data_to_cache(data)
        else:
            raise requests.HTTPError("The API can't be accessed")
        
    result = ForecastDaily(**data)
    return result