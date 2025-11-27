# Programa principal: menú, flujo general y coordinación

from cli import *
from services import *
from formatter import *
from set_up import *

def main():
    while True:
        try: 
            print_menu()
            option = read_menu_option()
            match option:
                case 1:
                    '''
                        Mirar si existe ubicación en preferences.json -> get_location()
                        si no existe
                            pedimos city
                            guardamos ubicacion -> set_location(city, country, latitude, longitude)
                        
                        consultar datos
                            
                    '''
                    city = input_city()
                    result = get_geolocation(city)
                    print(result.results[0].name)
                    set_location(result.name, result.country, result.latitude, result.longitude)
                    fore_data = get_forecast(result.latitude, result.longitude)
                    print_forecast(print_today_weather(fore_data, result.name, result.country))

                case 2:
                    city = input_city()
                    lat, long, country = get_geolocation(city)
                    fore_data = get_forecast(lat, long, 3)
                    print_forecast(print_daily_weather(fore_data, city, country, 3))

                case 0:
                    break
                case _:
                    print("Tienes que escoger una opción numérica válida")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()