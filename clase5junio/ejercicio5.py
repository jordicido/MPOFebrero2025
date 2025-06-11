"""
Ejercicio 5 - Calcular la suma de dígitos de un número¶
Escribe un programa que pida al usuario un número entero y 
calcule la suma de sus dígitos. 
El programa debe definir una función que reciba el número, 
realice el cálculo de la suma de los dígitos y luego imprima el resultado.
"""

def suma_digitos(numero):
    resultado = 0
    while numero > 0:
        resultado += numero%10
        numero //= 10
    return resultado

numero = int(input("Introduce un numero entero positivo:\n"))
print(f"La suma de los digitos del numero {numero} es {suma_digitos(numero)}")