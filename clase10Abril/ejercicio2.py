# Ejercicio 2 - Portero de discoteca

edad = int(input("Cuantos años tienes? "))

if edad >= 18 and edad <= 60:
    print("Puedes entrar")
elif edad > 60:
    print("Vete a oldSkoolVeterans")
elif edad >= 16:
    print("Vete a KinderGarden")
else:
    print("Vete a tu casa")

