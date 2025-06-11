"""
Ejercicio 3 - Calcular el factorial de un número¶
Escribe un programa que pida al usuario un número entero 
y calcule su factorial. El programa debe definir una función 
que reciba el número, realice el cálculo del factorial y 
luego imprima el resultado.
"""

def calculo_factorial(numero):
    resultado = 1
    for i in range(numero,1,-1):
        resultado *= i
    return resultado

numero = int(input("Introduce un numero entero positivo: "))
print(calculo_factorial(numero))