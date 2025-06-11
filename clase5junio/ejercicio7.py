"""
Ejercicio 7 - Incrementar cada elemento de una lista¶
Escribe un programa que pida al usuario una lista de números 
enteros separados por comas y un número entero. El programa 
debe definir una función que reciba la lista y el número, incremente 
cada elemento de la lista por el número dado y luego imprima la lista 
resultante.
"""
"""
1,2,3,4,5,6,7,8,9,10
5
6,7,8,9,10,11,12,13,14,15
"""
def incrementa_lista(lista, numero):
    for i in range(len(lista)):
        lista[i] += numero
    numero += 5

numeros = input("Introduce una lista de numeros separados por coma\n").split(",")
lista = [int(num) for num in numeros]
numero = int(input("Introduce el incremento\n"))
incrementa_lista(lista, numero)
print(lista)
print(numero)