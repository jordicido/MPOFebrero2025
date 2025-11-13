# Programa principal: menú, flujo general y coordinación

from cli import *

def main():
    while True:
        try: 
            print_menu()
            option = read_menu_option()
            match option:
                case 1:
                    pass
                case 0:
                    break
                case _:
                    print("Tienes que escoger una opción numérica válida")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()