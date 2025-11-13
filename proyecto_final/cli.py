# Interfaz de línea de comandos: menús e interacción con el usuario

def print_menu():
    print("""=== Weather CLI ===
1) Consultar ciudad (1 día)
2) Consultar ciudad (3 días)
3) Ver último resultado
4) Ver historial (últimas consultas)
0) Salir""")
    

def read_menu_option():
    option = input("Escoge una opción\n")
    if not option.isdigit():
        raise ValueError("Tienes que escoger una opción numérica válida")
    return int(option)

def input_city():
    return input("Qué ciudad quieres consultar?\n").strip()
