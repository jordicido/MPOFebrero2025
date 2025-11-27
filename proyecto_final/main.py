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
                    location = get_location()
                    if location == None:
                        city = input_city()
                        location = get_geolocation(city).results[0]
                        set_location(location["name"], location["country"], location["latitude"], location["longitude"])
                    
                    fore_data = get_forecast(location["latitude"], location["longitude"])
                    print_forecast(print_today_weather(fore_data, location["name"], location["country"]))

                case 2:
                    location = get_location()
                    if location == None:
                        city = input_city()
                        location = get_geolocation(city).results[0]
                        
                    fore_data = get_forecast(location["latitude"], location["longitude"], 3)
                    print_forecast(print_daily_weather(fore_data, location["name"], location["country"], 3))

                case 0:
                    break
                case _:
                    print("Tienes que escoger una opción numérica válida")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()