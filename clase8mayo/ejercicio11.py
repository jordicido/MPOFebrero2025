'''
Ejercicio 11 - Media de notas
Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. 
Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y 
calcule la media de esas notas. El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1. 
Al final, imprime la media.

Introduce evaluaciones: 3
10 3 2.4 8 6 -1
Evaluación 1: 4.algo
7 7 7 7 -1
Evaluación 2: 7
10 9 8 -1
Evaluación 3: 9
'''

evaluaciones = int(input("Introduce las evaluaciones: "))

for i in range(evaluaciones):
    nota = float(input("Introduce la siguiente nota: "))
    num_notas = 0
    suma_notas = 0
    while nota != -1:
        num_notas += 1
        suma_notas += nota
        nota = float(input("Introduce la siguiente nota: "))
    print(f"Nota media evaluación {i+1}: {suma_notas/num_notas}")    