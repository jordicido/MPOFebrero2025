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

def print_today_weather(forecast_data: ForecastDaily, city, country):
    time = forecast_data.daily.time[0]
    t_max = forecast_data.daily.temperature_2m_max[0]
    t_min = forecast_data.daily.temperature_2m_min[0]
    sunrise = forecast_data.daily.sunrise[0].split("T")[1]
    sunset = forecast_data.daily.sunset[0].split("T")[1]
    prec = forecast_data.daily.precipitation_probability_max[0]
    weather = weather_code_icons.get(forecast_data.daily.weather_code[0])
    
    return fr"""
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

weather_code_icons = {
    # 00-03: CLEAR / PARTLY CLOUDY
    # Clear (00, 01)
    0: [
        fr"{f_r}    \___/    ",
        fr"{f_r}  __/   \__  ",
        fr"{f_r}    \   /    ",
        fr"{f_r}    /‾‾‾\    ",
        fr"{f_b}{s_n}      Despejado     "
    ],
    1: [
        fr"{f_r}    \___/    ",
        fr"{f_r}  __/   \__  ",
        fr"{f_r}    \   /    ",
        fr"{f_r}    /‾‾‾\    ",
        fr"{f_b}{s_n}      Despejado     "
    ],
    # Partly Cloudy (02, 03)
    2: [
        fr"{f_y}   \__/      ",
        fr"{f_y} --( _)--    ",
        fr"{f_y}   /{f_B}(    ).  ",
        fr"{f_B} (___.__)__) ",
        f"{f_b}{s_n}Parcialmente Nublado"
    ],
    3: [
        fr"{f_y}   \__/      ",
        fr"{f_y} --( _)--    ",
        fr"{f_y}   /{f_B}(    ).  ",
        fr"{f_B} (___.__)__) ",
        f"{f_b}{s_n}Parcialmente Nublado"
    ],
    # 04-09: CLOUDY / WINDY
    # Cloudy (04, 05, 06)
    4: [
        fr"{f_B}     .--.    ",
        fr"{f_B}  .-(    ).  ",
        fr"{f_B} (___.__)__) ",
        fr"{f_B}             ",
        f"{f_b}       Nublado      "
    ],
    5: [
        fr"{f_B}     .--.    ",
        fr"{f_B}  .-(    ).  ",
        fr"{f_B} (___.__)__) ",
        fr"{f_B}             ",
        f"{f_b}       Nublado      "
    ],
    6: [
        fr"{f_B}     .--.    ",
        fr"{f_B}  .-(    ).  ",
        fr"{f_B} (___.__)__) ",
        fr"{f_B}             ",
        f"{f_b}       Nublado      "
    ],
    # Windy (07, 08, 09)
    7: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    8: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    9: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    # 10-12: FOG
    10: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    11: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    12: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    # 13-19: STORM / LIGHT_RAIN / WINDY
    # Storm (13, 17, 18)
    13: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    14: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    15: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    16: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    17: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    18: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    19: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    # 20-29: LIGHT_RAIN / SNOW / STORM / FOG
    # Light Rain (20, 21, 23, 24, 25)
    20: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    21: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    # Snow (22, 26)
    22: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    23: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    24: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    25: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    26: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    # Storm (27, 29)
    27: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    # Fog (28)
    28: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    29: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    # 30-39: WINDY (Tormenta de Polvo/Arena)
    30: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    31: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    32: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    33: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    34: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    35: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    36: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    37: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    38: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    39: [
        fr"{f_B}    __       ",
        fr"{f_B}  .(  ).{f_b}~)~) ",
        fr"{f_B} (___)__)){f_b}~) ",
        fr"             ",
        f"{f_b}       Ventoso      "
    ],
    # 40-49: FOG
    40: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    41: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    42: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    43: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    44: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    45: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    46: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    47: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    48: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    49: [
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        fr"{f_B}  ~ ~ ~ ~ ~  ",
        fr"{f_B} ~ ~ ~ ~ ~ ~ ",
        f"{f_b}       Niebla       "
    ],
    # 50-59: LIGHT_RAIN (Llovizna)
    50: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    51: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    52: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    53: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    54: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    55: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    56: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    57: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    58: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    59: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    # 60-69: LIGHT_RAIN / HEAVY_RAIN (Lluvia)
    60: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    61: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    62: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    63: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    64: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    65: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    66: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    67: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    68: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    69: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    # 70-79: SNOW / HEAVY_RAIN (Nieve / Granizo)
    70: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    71: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    72: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    73: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    74: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    75: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    76: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    77: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    78: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    79: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    # 80-89: LIGHT_RAIN / HEAVY_RAIN / SNOW
    # Light Rain (80)
    80: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_c}   '  '  '   ",
        f"{f_b}    Lluvia ligera   "
    ],
    # Heavy Rain (81, 82, 83)
    81: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    82: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    83: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}  |{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|{f_c}'{f_B}|  ",
        f"{f_b}    Lluvia fuerte   "
    ],
    # Snow (84, 85, 86, 87, 88, 89)
    84: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    85: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    86: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    87: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    88: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    89: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_w}   *  *  *   ",
        f"{f_b}        Nieve       "
    ],
    # 90-99: STORM
    90: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    91: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    92: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    93: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    94: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    95: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    96: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    97: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    98: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ],
    99: [
        fr"{f_b}     .--.    ",
        fr"{f_b}  .-(    ).  ",
        fr"{f_b} (___.__)__) ",
        fr"{f_B}   / {f_y}Z {f_B}/ {f_y}Z   ",
        f"{f_b}      Tormenta      "
    ]
}