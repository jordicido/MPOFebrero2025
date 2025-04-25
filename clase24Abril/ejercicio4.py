numero = int(input("Introduce un número entero positivo:\n"))
factorial = 1
for i in range(numero,1,-1):
    factorial = factorial * i

print(f"El factorial de {numero} es {factorial}")