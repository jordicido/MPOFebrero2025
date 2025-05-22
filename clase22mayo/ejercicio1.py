'''
Ejercicio 1 - Sumar elementos de una lista¶
Escribe un programa que pida al usuario una lista de números 
enteros separados por comas y calcule la suma de todos los 
elementos de la lista. El programa debe imprimir el resultado.
'''

lista_numeros = input("Escribe una lista de numeros separados por coma: ").split(",")
resultado = 0

# ['1', '2', '3', '4', '5', '6']
for numero in lista_numeros:
    resultado += int(numero)

print(f"Resultado: {resultado}")