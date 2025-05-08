'''
Ejercicio 13 - Número de cifras¶
Escribe un programa que pida al usuario una serie de números enteros positivos hasta 
la introducción de un valor -1 para cada número debe contar cuántas cifras tiene. 
El programa debe imprimir la longitud de cada número. 
No podéis usar la función len() para contar las cifras ni convertir el número a cadena.
'''

numero = int(input("Introduce un número (-1 para acabar): "))

while numero != -1:
    cifras = 1
    copia_num = numero
    while numero > 9:
        cifras += 1
        numero //= 10
    print(f"El número de dígitos de {copia_num} es {cifras}")
    numero = int(input("Introduce un número (-1 para acabar): "))
    