numero = int(input("Introduce un número entero positivo:\n"))

for i in range(numero+1):
    if i%3 == 0 and i%5 == 0:
        continue
    elif i%3 == 0:
        print(f"{i} es múltiplo de 3")
    elif i%5 == 0:
        print(f"{i} es múltiplo de 5")