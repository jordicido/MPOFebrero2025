'''
Ejercicio 3 - Mayor y menor elemento de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados 
por comas y encuentre el mayor y el menor elemento de la lista. 
El programa debe imprimir ambos resultados.
'''

lista_numero = input("Introduce una lista de números separadas por coma: ").split(",")
lista_numero = [int(num) for num in lista_numero]
print(f"menor: {min(lista_numero)} mayor: {max(lista_numero)}")
