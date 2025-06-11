"""
Ejercicio 1 - Calcular el área de un círculo¶
Escribe un programa que pida al usuario el radio de un círculo y 
calcule su área. El programa debe definir una función que reciba 
el valor del radio, realice el cálculo del área y luego imprima 
el resultado.
"""
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = int(input("Introduce el radio: \n"))
print(f"El area de un círculo de radio {radio} es {calcular_area_circulo(radio):.2f}")

