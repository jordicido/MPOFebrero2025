# Presentación y formato del resultado en texto

from models.forecastDaily import ForecastDaily
from colorama import Fore, Back, Style

b_w = Back.WHITE
f_r = Fore.RED
f_b = Fore.BLACK
f_y = Fore.YELLOW
f_c = Fore.CYAN
f_w = Fore.WHITE
f_B = Fore.BLUE
s_b = Style.BRIGHT
s_n = Style.NORMAL
reset = Style.RESET_ALL

def print_daily_weather(forecast_data: ForecastDaily, city, country, days): 
    result = ""
    for i in range(days):
        time = forecast_data.daily.time[i]
        t_max = forecast_data.daily.temperature_2m_max[i]
        t_min = forecast_data.daily.temperature_2m_min[i]
        sunrise = forecast_data.daily.sunrise[i].split("T")[1]
        sunset = forecast_data.daily.sunset[i].split("T")[1]
        prec = forecast_data.daily.precipitation_probability_max[i]
        weather = weather_code_icons.get(forecast_data.daily.weather_code[i])
        result += fr"""
{b_w}{f_r}{s_b}┌───────────────────────────────────────────────────┐{reset}
{b_w}{f_r}{s_b}│{f_b}{s_n} {city} - {country}{" "*(36 - len(country) - len(city))} {time}{f_r}{s_b}│{reset}
{b_w}{f_r}{s_b}├──────────────────────────────┬────────────────────┤{reset}
{b_w}{f_r}{s_b}│{f_b}{s_n} Temp. max: {t_max}ºC{" "*(16 - len(str(t_max)))}{f_r}{s_b}│    {weather[0]}   {f_r}{s_b}│{reset}
{b_w}{f_r}{s_b}│{f_b}{s_n} Temp. min: {t_min}ºC{" "*(16 - len(str(t_min)))}{f_r}{s_b}│    {weather[1]}   {f_r}{s_b}│{reset}
{b_w}{f_r}{s_b}│{f_b}{s_n} Sunrise: {sunrise}{" "*(20 - len(sunrise))}{f_r}{s_b}│    {weather[2]}   {f_r}{s_b}│{reset}
{b_w}{f_r}{s_b}│{f_b}{s_n} Sunset: {sunset}{" "*(21 - len(sunset))}{f_r}{s_b}│    {weather[3]}   {f_r}{s_b}│{reset}
{b_w}{f_r}{s_b}│{f_b}{s_n} % Precipitacion: {prec}%{" "*(11 - len(str(prec)))}{f_r}{s_b}│{weather[4]}{f_r}{s_b}│{reset}
{b_w}{f_r}{s_b}└──────────────────────────────┴────────────────────┘{reset}
"""
    return result