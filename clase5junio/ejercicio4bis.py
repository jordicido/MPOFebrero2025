"""
Ejercicio 4 - Verificar cuantos numeros primos hay¶
Escribe un programa que pida al usuario un número entero y 
verifique cuantos primos hay hasta ese número. El programa debe definir una función 
que reciba el número, realice la verificación y luego imprima 
el número de primos.
"""
import math

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero))+1):
        if numero%i == 0:
            return False
    
    return True

def cuantos_primos(numero):
    """un número es primo si solo es divisible entre 1 y si mismo"""
    resultado = 0
    
    for i in range(2, numero+1):
        if es_primo(i):
            resultado += 1
            print(i)

    return resultado

numero = int(input())
print(cuantos_primos(numero))