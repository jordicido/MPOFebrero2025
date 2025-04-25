# Recibo el número del usuario
numero = int(input("Introduce un número entero positivo:\n"))
# Inicializo una variable para ir contando los pares que hay en
# esa secuencia de números
pares = 0
# Para i en la secuencia [0,1,2,3,4,5...numero+1]
for i in range(0,numero+1):
    # Miro si i es par
    if i % 2 == 0:
        # Sumo uno al contador de pares
        pares = pares + 1

print(f"Número de pares: {pares}")    