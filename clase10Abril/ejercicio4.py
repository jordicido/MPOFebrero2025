# Ejercicio 4 - Múltiplos de 3 y 5

numero = int(input("Introduce el número a comprobar: "))

if numero % 15 == 0:
    print("Es múltiplo de 3 y de 5")
elif numero % 3 == 0:
    print("Es múltiplo de 3")
elif numero % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 3 ni de 5")