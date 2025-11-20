# Presentación y formato del resultado en texto

from datetime import datetime
from models.forecastDaily import ForecastDaily

def print_today_weather(forecast_data: ForecastDaily, city, country):
    return f"""
|==============================|
| {city} - {country}    |           |
|===================   {forecast_data.daily.weather_code[0]}    |
| Temp max: {forecast_data.daily.temperature_2m_max[0]}ºC         |           |
| Temp min:  {forecast_data.daily.temperature_2m_min[0]}ºC        ===========|
| Sunrise: {forecast_data.daily.sunrise[0].split("T")[1]}                      |
| Sunset: {forecast_data.daily.sunset[0].split("T")[1]}                       |
| % Precipitacion: {forecast_data.daily.precipitation_probability_max[0]}%              |
|==============================|
"""

def print_daily_weather(forecast_data: ForecastDaily, city, country, days):
    result = ""
    for i in range(days):
        result += f"""
|==============================|
| {city} - {country}   Day: {forecast_data.daily.time[i]} |           |
|===================   {forecast_data.daily.weather_code[i]}    |
| Temp max: {forecast_data.daily.temperature_2m_max[i]}ºC         |           |
| Temp min:  {forecast_data.daily.temperature_2m_min[i]}ºC        ===========|
| Sunrise: {forecast_data.daily.sunrise[i].split("T")[1]}                      |
| Sunset: {forecast_data.daily.sunset[i].split("T")[1]}                       |
| % Precipitacion: {forecast_data.daily.precipitation_probability_max[i]}%              |
|==============================|
"""
    return result