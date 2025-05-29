'''
Ejercicio 4 - Tupla de números¶
Escribe un programa que pida al usuario una lista de números enteros separados 
por comas y almacene estos números en una tupla. Luego, el programa debe calcular
y mostrar la suma, el promedio, el número máximo y el número mínimo de la tupla.
'''

numeros = input("Introduce una lista de numeros separados por coma\n").split(",")
numeros = [int(num) for num in numeros]
tupla = tuple(numeros)

suma = 0
promedio = 0.0
maximo = float('-inf')
minimo = float('inf')

for numero in tupla:
    suma += numero
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

promedio = suma / len(tupla)

print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")