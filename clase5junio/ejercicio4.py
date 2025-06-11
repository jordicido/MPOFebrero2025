"""
Ejercicio 4 - Verificar si un número es primo¶
Escribe un programa que pida al usuario un número entero y 
verifique si es primo. El programa debe definir una función 
que reciba el número, realice la verificación y luego imprima 
si el número es primo o no.
"""
import math

def es_primo(numero):
    """un número es primo si solo es divisible entre 1 y si mismo"""
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero%i == 0:
            return  False
    return True

numero = int(input())
print(es_primo(numero))