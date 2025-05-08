'''
Ejercicio 12 - Mayor y menor
Escribe un programa que pida al usuario una serie de números enteros y determine cuál 
es el mayor y cuál es el menor. 
El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. 
Al final, imprime el mayor y el menor.
'''
mayor = float('-inf')
menor = float('inf')
numero = int(input("Introduce un valor (0 para terminar): "))

while numero != 0:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
        
    numero = int(input("Introduce un valor (0 para terminar): "))

print(f"Mayor: {mayor} Menor: {menor}")