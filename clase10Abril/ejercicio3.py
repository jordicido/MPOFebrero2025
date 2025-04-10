# Ejercicio 3 - Pacman
# nombre_usuario - snake_case --> Python
# nombreUsuario - camelCase --> java

pos_pacman = int(input("Cuál es la posición de pacman? "))
pos_fantasma = int(input("Cuál es la posición del fantasma? "))

# Comprobamos que la posición sea igual
if pos_pacman == pos_fantasma:
    # Caramelo -> Pacman come fantasma
    # Invisible -> pacman escapa
    # Normal -> pacman atrapado
    estado_pacman = input("Como está pacman? ")
    if estado_pacman == "caramelo":
        print("Pacman se ha comido al fantasma")
    elif estado_pacman == "invisible":
        print("Pacman ha escapado")
    else:
        print("Pacman ha sido atrapado")
else:
    print("Pacman ha escapado")