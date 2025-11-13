# Programa principal: menú, flujo general y coordinación

from cli import *
from services import *

def main():
    while True:
        try: 
            print_menu()
            option = read_menu_option()
            match option:
                case 1:
                    # Primero pedir ciudad
                    # Llamar API geolocalización
                    # Llamar API forecast
                    # Formatear e imprimir salida
                    city = input_city()
                    lat, long, country = get_geolocation(city)
                    max_temp, min_temp = get_forecast(lat, long)
                    print(f"Tiempo de la ciudad: {city} País: {country}")
                    print(f"Temperatura máxima de hoy: {max_temp}")
                    print(f"Temperatura mínima de hoy: {min_temp}")

                case 0:
                    break
                case _:
                    print("Tienes que escoger una opción numérica válida")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()