# Programa principal: menú, flujo general y coordinación

from cli import *
from services import *
from models.forecastDaily import ForecastDaily

def main():
    while True:
        try: 
            print_menu()
            option = read_menu_option()
            match option:
                case 1:
                    city = input_city()
                    lat, long, country = get_geolocation(city)
                    fore_data = get_forecast(lat, long)
                    print(f"Tiempo de la ciudad: {city} País: {country}")
                    print(f"Temperatura máxima de hoy: {fore_data.daily.temperature_2m_max}")
                    print(f"Temperatura mínima de hoy: {fore_data.daily.temperature_2m_min}")
                    print(f"Hora del amanecer: {fore_data.daily.sunrise}")
                    print(f"Hora del anochecer: {fore_data.daily.sunset}")
                    print(f"Probabilidad de lluvia: {fore_data.daily.precipitation_probability_max}%")


                case 0:
                    break
                case _:
                    print("Tienes que escoger una opción numérica válida")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()