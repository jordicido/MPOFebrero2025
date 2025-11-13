# Conexión con las APIs (geocoding y meteorología)
import requests

API_GEO = "https://geocoding-api.open-meteo.com/v1/search"
API_FORE = "https://api.open-meteo.com/v1/forecast"

def get_geolocation(city):
    response = requests.get(API_GEO, {"name":city, "count":1})
    if response.status_code == 200:
        data = response.json()["results"]
        return data[0]["latitude"], data[0]["longitude"], data[0]["country"]
    else:
        raise requests.HTTPError("The API can't be accessed")

def get_forecast(latitude, longitude):
    response = requests.get(API_FORE, {"latitude":latitude, "longitude":longitude, "daily":"weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_probability_max", "timezone":"auto", "forecast_days":1})
    if response.status_code == 200:
        data = response.json()
        return data["daily"]["temperature_2m_max"][0], data["daily"]["temperature_2m_min"][0]
    else:
        raise requests.HTTPError("The API can't be accessed")