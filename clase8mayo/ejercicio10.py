'''
Ejercicio 10 - Akinator numérico¶
Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número. 
El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido. 
El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.
'''

import random

random_num = random.randint(1,100)
user_num = int(input("Introduce un número del 1 al 100: "))

while random_num != user_num:
    if user_num > random_num:
        print("Lo siento humano, es demasiado alto")
    else:
        print("🤏")
    
    user_num = int(input("Introduce un número del 1 al 100: "))

print("👌")

