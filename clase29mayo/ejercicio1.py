'''
Ejercicio 1 - Capitales y países¶
Escribe un programa que almacene en un diccionario las capitales de varios países, 
se introducirán los datos con la forma PAIS-CAPITAL. Esto debe ejecutarse 
indefinidamente hasta que el usuario introduzca "FIN INSERCIONES". 
El programa debe permitir al usuario consultar la capital de un país introduciendo 
su nombre. Si el país no está en el diccionario, el programa debe informar al usuario.

paises = {
    "España":"Madrid",
    "Francia":"Paris
}

1. variables
2. bucle que lee y registra las entradas de pais-capital
3. pedir un pais y mirar si existe en el diccionario

'''
paises = {}
entrada = input("Indica un valor de la forma 'Pais-Capital' o escribe FIN INSERCIONES para finalizar\n").lower()

while entrada != "fin inserciones":
    # ["España","Madrid"]
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais] = capital
    entrada = input("Indica un valor de la forma 'Pais-Capital' o escribe FIN INSERCIONES para finalizar\n").lower()

pais_usuario = input("Introduce el nombre del país que quieres consultar").lower()
if pais_usuario in paises:
    print(f"La capital de {pais_usuario.capitalize()} es {paises[pais_usuario].capitalize()}")
else:
    print("No existe ese registro en el diccionario")
    