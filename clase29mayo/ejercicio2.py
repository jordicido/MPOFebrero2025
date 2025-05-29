'''
Ejercicio 2 - Contar palabras en un texto¶
Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece 
cada palabra en el texto. El programa debe imprimir un diccionario donde las claves
son las palabras y los valores son sus respectivas frecuencias. Considera las palabras
en minúsculas.

"Hola que tal que cuentas"
frecuencia = {
    "hola":1,
    "que":2,
    "tal":1,
    "cuentas":1
}

1. Definir las variables
2. Bucle que recorra las palabras y mire si:
    2.1 Si ya existian: sumo 1 a la frecuencia anterior
    2.2 Creo una entrada en el diccionario con frecuencia 1
3. Imprimir diccionario
'''
palabras = {}
texto = input("Introduce una frase\n").lower().split()

for palabra in texto:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

print(palabras)
